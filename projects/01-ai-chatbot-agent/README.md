# Project 1: AI Customer Support Agent

## Overview
Build a complete AI-powered customer support system with RAG (Retrieval-Augmented Generation), automatic escalation, and analytics.

## What You'll Learn
- How RAG works (embeddings, vector search, context injection)
- Building APIs with FastAPI
- Using Anthropic Claude API with tool use
- Vector databases with Supabase pgvector
- Building chat interfaces

## Architecture

```
User Question
     │
     ▼
Chat Interface (Next.js)
     │
     ▼
FastAPI Backend
     │
     ├──► Embed question (OpenAI embeddings)
     │
     ├──► Search knowledge base (Supabase pgvector)
     │
     ├──► Send question + context to Claude
     │
     ├──► Check confidence → Escalate if low
     │
     └──► Return answer + log analytics
```

## Tech Stack
- **Backend**: Python 3.11, FastAPI, uvicorn
- **AI**: Anthropic Claude API, OpenAI Embeddings API
- **Database**: Supabase (PostgreSQL + pgvector)
- **Frontend**: Next.js 14, TypeScript, Tailwind CSS
- **Deployment**: Vercel (frontend) + Railway (backend)

## Setup Instructions

### Prerequisites
```bash
python3 -m venv venv
source venv/bin/activate
pip install fastapi uvicorn anthropic openai supabase python-dotenv
```

### Environment Variables
```
ANTHROPIC_API_KEY=your-key
OPENAI_API_KEY=your-key
SUPABASE_URL=your-supabase-url
SUPABASE_KEY=your-supabase-key
```

### Database Setup (Supabase)
```sql
-- Enable pgvector extension
CREATE EXTENSION IF NOT EXISTS vector;

-- Knowledge base documents
CREATE TABLE documents (
  id uuid DEFAULT gen_random_uuid() PRIMARY KEY,
  content text NOT NULL,
  embedding vector(1536),
  metadata jsonb DEFAULT '{}',
  created_at timestamptz DEFAULT now()
);

-- Conversations
CREATE TABLE conversations (
  id uuid DEFAULT gen_random_uuid() PRIMARY KEY,
  messages jsonb[] DEFAULT '{}',
  status text DEFAULT 'active',
  escalated boolean DEFAULT false,
  created_at timestamptz DEFAULT now()
);

-- Analytics
CREATE TABLE analytics (
  id uuid DEFAULT gen_random_uuid() PRIMARY KEY,
  question text,
  answer text,
  confidence float,
  response_time_ms int,
  escalated boolean DEFAULT false,
  created_at timestamptz DEFAULT now()
);

-- Vector similarity search function
CREATE OR REPLACE FUNCTION match_documents(
  query_embedding vector(1536),
  match_count int DEFAULT 5,
  match_threshold float DEFAULT 0.7
)
RETURNS TABLE (
  id uuid,
  content text,
  similarity float
)
LANGUAGE sql STABLE
AS $$
  SELECT
    documents.id,
    documents.content,
    1 - (documents.embedding <=> query_embedding) AS similarity
  FROM documents
  WHERE 1 - (documents.embedding <=> query_embedding) > match_threshold
  ORDER BY documents.embedding <=> query_embedding
  LIMIT match_count;
$$;
```

## Step-by-Step Build Guide

### Step 1: Start with the basic chatbot (no RAG)
Just Claude answering questions directly.

### Step 2: Add knowledge base upload
Upload documents → chunk them → embed them → store in Supabase.

### Step 3: Add RAG
When user asks a question → embed it → find similar docs → send to Claude with context.

### Step 4: Add escalation logic
If Claude's response includes low-confidence indicators, route to human.

### Step 5: Add analytics
Log every interaction with timing, confidence, and escalation status.

### Step 6: Build the dashboard
Show analytics: common questions, resolution rate, response time charts.

### Step 7: Deploy
Frontend on Vercel, backend on Railway, database on Supabase.

## What to Show in Your Portfolio
- Live demo link
- Architecture diagram
- Key metrics from the analytics dashboard
- Code snippets showing RAG implementation
- Explanation of design decisions
