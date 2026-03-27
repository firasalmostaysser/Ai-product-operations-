# Project 5: Personal Knowledge RAG System

## What It Is

A RAG (Retrieval-Augmented Generation) system that:
1. Indexes your documents, notes, and files into a vector database
2. Lets you ask questions about them in natural language
3. Claude retrieves the relevant context and answers your question

**Example uses:**
- "What were all the client pain points I found during my Reefq discovery calls?"
- "What did I learn about n8n in Week 2 of my learning log?"
- "Find everything I've written about Supabase"
- "What are all the action items from my past meetings?"

## Why This Project Is Important

RAG is the most common AI pattern in production. Almost every AI product uses it:
- Customer support bots (search the knowledge base)
- Enterprise search (search internal documents)
- Personal assistants (search your notes/emails)
- Legal AI (search case law and documents)

Building this from scratch means you truly understand how AI products work.

## How RAG Works (Conceptual)

```
INDEXING (done once, or when documents change):
Document → Split into chunks → Embed each chunk → Store in vector DB

QUERYING (done every time user asks a question):
User question → Embed the question → Find similar chunks in vector DB
                → Feed chunks + question to Claude → Claude answers
```

**Key concept: Embeddings**
An embedding is a list of numbers (e.g., [0.23, -0.41, 0.87, ...]) that represents the *meaning* of a piece of text. Similar meanings → similar numbers → close together in vector space.

When you search, you convert your question to an embedding and find the chunks with the closest embeddings. This is "semantic search" — it finds relevant content even if the exact words don't match.

## Tech Stack

- **Python 3.10+**
- **Anthropic Claude API** (for answering questions)
- **OpenAI API** (for embeddings — cheaper than Claude embeddings)
- **Supabase** with pgvector extension (you already know Supabase!)
- **LangChain** (to manage the RAG pipeline)

## Set Up Supabase Vector Database

### Step 1: Create a Supabase project
Go to [supabase.com](https://supabase.com) → New Project

### Step 2: Enable pgvector and create the documents table

In your Supabase SQL editor, run:

```sql
-- Enable the pgvector extension
create extension if not exists vector;

-- Create the documents table
create table documents (
  id bigserial primary key,
  content text not null,
  metadata jsonb,
  embedding vector(1536)  -- 1536 dimensions for OpenAI text-embedding-3-small
);

-- Create an index for fast similarity search
create index on documents using ivfflat (embedding vector_cosine_ops)
  with (lists = 100);

-- Create a function for similarity search
create or replace function match_documents(
  query_embedding vector(1536),
  match_count int default 5,
  filter jsonb default '{}'
)
returns table (
  id bigint,
  content text,
  metadata jsonb,
  similarity float
)
language plpgsql
as $$
begin
  return query
  select
    documents.id,
    documents.content,
    documents.metadata,
    1 - (documents.embedding <=> query_embedding) as similarity
  from documents
  where metadata @> filter
  order by documents.embedding <=> query_embedding
  limit match_count;
end;
$$;
```

### Step 3: Install Python dependencies

```bash
pip install anthropic openai supabase langchain langchain-openai python-dotenv
```

### Step 4: Set up environment variables

```bash
ANTHROPIC_API_KEY=your_anthropic_key
OPENAI_API_KEY=your_openai_key
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_SERVICE_KEY=your_service_role_key
```

## Build the RAG System

### File 1: `ingest.py` — Index Your Documents

```python
import os
import json
from pathlib import Path
from supabase import create_client
from openai import OpenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter
from dotenv import load_dotenv

load_dotenv()

supabase = create_client(os.environ["SUPABASE_URL"], os.environ["SUPABASE_SERVICE_KEY"])
openai_client = OpenAI()

def get_embedding(text: str) -> list[float]:
    """Get embedding for a piece of text."""
    response = openai_client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    return response.data[0].embedding

def chunk_text(text: str, chunk_size: int = 500, chunk_overlap: int = 50) -> list[str]:
    """Split text into overlapping chunks."""
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", ". ", " ", ""]
    )
    return splitter.split_text(text)

def ingest_document(content: str, metadata: dict):
    """Ingest a document into the vector database."""
    chunks = chunk_text(content)
    print(f"  Splitting into {len(chunks)} chunks...")
    
    for i, chunk in enumerate(chunks):
        embedding = get_embedding(chunk)
        
        supabase.table("documents").insert({
            "content": chunk,
            "metadata": {**metadata, "chunk_index": i, "total_chunks": len(chunks)},
            "embedding": embedding
        }).execute()
    
    print(f"  ✅ Indexed {len(chunks)} chunks")

def ingest_folder(folder_path: str, doc_type: str = "notes"):
    """Ingest all .md and .txt files in a folder."""
    folder = Path(folder_path)
    
    for file_path in folder.glob("**/*.md"):
        print(f"Indexing: {file_path.name}")
        content = file_path.read_text(encoding="utf-8")
        ingest_document(content, {
            "source": str(file_path),
            "filename": file_path.name,
            "doc_type": doc_type
        })
    
    for file_path in folder.glob("**/*.txt"):
        print(f"Indexing: {file_path.name}")
        content = file_path.read_text(encoding="utf-8")
        ingest_document(content, {
            "source": str(file_path),
            "filename": file_path.name,
            "doc_type": doc_type
        })

if __name__ == "__main__":
    # Index your learning logs and notes
    print("Indexing learning logs...")
    ingest_folder("./daily-log", doc_type="learning_log")
    
    print("\nIndexing course notes...")
    ingest_folder("./courses", doc_type="course")
    
    print("\n✅ Indexing complete!")
```

### File 2: `query.py` — Ask Questions

```python
import os
from openai import OpenAI
from anthropic import Anthropic
from supabase import create_client
from dotenv import load_dotenv

load_dotenv()

supabase = create_client(os.environ["SUPABASE_URL"], os.environ["SUPABASE_SERVICE_KEY"])
openai_client = OpenAI()
anthropic_client = Anthropic()

def get_embedding(text: str) -> list[float]:
    response = openai_client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    return response.data[0].embedding

def search_documents(query: str, n_results: int = 5) -> list[dict]:
    """Search for relevant document chunks."""
    query_embedding = get_embedding(query)
    
    result = supabase.rpc("match_documents", {
        "query_embedding": query_embedding,
        "match_count": n_results
    }).execute()
    
    return result.data

def answer_question(question: str) -> str:
    """RAG pipeline: retrieve context, then answer."""
    
    # Step 1: Retrieve relevant chunks
    print("🔍 Searching knowledge base...")
    chunks = search_documents(question)
    
    if not chunks:
        return "No relevant information found in your knowledge base."
    
    # Step 2: Format context
    context = "\n\n---\n\n".join([
        f"Source: {chunk['metadata'].get('filename', 'unknown')}\n{chunk['content']}"
        for chunk in chunks
    ])
    
    print(f"📚 Found {len(chunks)} relevant chunks. Asking Claude...")
    
    # Step 3: Ask Claude with context
    response = anthropic_client.messages.create(
        model="claude-opus-4-5",
        max_tokens=1500,
        system="""You are a personal knowledge assistant for Firas Al Mostaysser.
        
You have access to Firas's learning logs, course notes, and project documentation.
Answer questions based ONLY on the provided context. If the context doesn't contain 
the answer, say so clearly.

When answering:
- Be specific and reference the source documents
- Quote relevant passages when helpful
- If multiple sources have relevant info, synthesize them""",
        messages=[
            {
                "role": "user",
                "content": f"""Context from Firas's knowledge base:

{context}

---

Question: {question}"""
            }
        ]
    )
    
    return response.content[0].text

def main():
    print("🤖 Personal Knowledge Assistant")
    print("Type 'quit' to exit\n")
    
    while True:
        question = input("Ask anything about your notes: ").strip()
        
        if question.lower() == 'quit':
            break
        
        if not question:
            continue
        
        answer = answer_question(question)
        print(f"\n💬 Answer:\n{answer}\n")
        print("-" * 50)

if __name__ == "__main__":
    main()
```

### Run It

```bash
# First, index your documents
python ingest.py

# Then, ask questions
python query.py
```

**Example questions to test:**
- "What did I learn about n8n AI nodes?"
- "What are the key concepts in AI Product Operations?"
- "What projects am I supposed to build in Month 1?"
- "What is the ReAct pattern?"

## Adding a Streamlit Chat Interface

```python
import streamlit as st
from query import answer_question

st.title("🧠 Firas's Knowledge Assistant")
st.caption("Ask anything about your learning logs, notes, and projects")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
if question := st.chat_input("Ask about your notes..."):
    # Show user message
    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.markdown(question)
    
    # Generate answer
    with st.chat_message("assistant"):
        with st.spinner("Searching knowledge base..."):
            answer = answer_question(question)
        st.markdown(answer)
    
    st.session_state.messages.append({"role": "assistant", "content": answer})
```

```bash
streamlit run chat.py
```

## Portfolio Framing

> "Built a personal RAG system that indexes all my learning notes and lets me query them with natural language. Uses OpenAI embeddings, Supabase pgvector, and Claude for answering. This is the same architecture used in enterprise knowledge management products."

The real power: **this repo itself is your knowledge base**. Index all the files in this repo and you have an AI assistant that knows your entire career roadmap and can answer questions about it.

---

*Time to complete: 4-6 hours | Next: [Project 6: Client Onboarding Agent](./06-client-onboarding-agent.md)*
