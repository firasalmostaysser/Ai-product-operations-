# AI Agents & MCP: Complete Beginner Guide

## Start Here: What Is an AI Agent?

An **AI agent** is a program that can:
1. **Understand** a goal in natural language
2. **Plan** steps to achieve it
3. **Use tools** to take actions (search the web, read files, write code, call APIs)
4. **Remember** context and results
5. **Loop** until the goal is achieved

**Simple example:** "Find me the 5 best n8n courses published in 2026 and summarize them."

A regular LLM (like ChatGPT) would try to answer from its training data (and be wrong/outdated). An agent would:
1. Search Google for "best n8n courses 2026"
2. Visit each URL
3. Extract the relevant content
4. Synthesize a summary
5. Return the result

The **agent** is what bridges "asking a question" to "getting real, current, accurate information."

---

## The Three Building Blocks of Any Agent

### 1. The Brain (LLM)
This is Claude, GPT-4o, Gemini, etc. It does the reasoning. It decides what to do next.

### 2. The Tools
Tools are functions the LLM can call. Examples:
- `search_web(query)` — searches Google and returns results
- `read_file(path)` — reads a file from the filesystem
- `execute_sql(query)` — runs a database query
- `send_email(to, subject, body)` — sends an email
- `call_api(url, method, body)` — makes an HTTP request

The LLM doesn't run these tools directly — it **requests** that a tool be called, and your code actually runs it.

### 3. The Loop (Agent Runtime)
The agent runtime manages the conversation between the LLM and the tools:
```
1. User says: "What are the top 5 AI tools launched this week?"
2. LLM says: "I should search the web for this." → calls search_web("AI tools launched this week")
3. Runtime runs the tool, gets results
4. LLM reads the results, says: "Let me look at these URLs more closely." → calls read_url(url1), read_url(url2)
5. Runtime runs those tools
6. LLM synthesizes all the information → returns final answer
```

This loop of "reason → act → observe → reason again" is called the **ReAct pattern**.

---

## ReAct Pattern: How Agents Think

**ReAct = Reasoning + Acting**

Every turn, the agent does:
```
Thought: I need to find the current price of Bitcoin
Action: search_web("Bitcoin price today")
Observation: Bitcoin is $85,000 as of March 27, 2026
Thought: I have the answer
Final Answer: Bitcoin is trading at $85,000 today.
```

This is literally what happens inside an agent. The "Thought" is Claude reasoning. The "Action" is a tool call. The "Observation" is the result.

**Why this matters for you:** When you're debugging an agent that's not working, you look at the Thought → Action → Observation chain to find where it went wrong.

---

## Types of Memory in AI Agents

### In-Context Memory (Short-term)
The conversation history. Everything in the current chat window. This is lost when the conversation ends. Limited by context window size.

### External Memory (Long-term)
Stored outside the LLM — in a database, vector store, or file. The agent retrieves relevant memories when needed. This is how RAG works.

### Procedural Memory (Skills)
The system prompt. This contains the agent's "personality," instructions, and capabilities. It persists across all conversations.

**Practical example for you:**
- If you build a customer support agent for a company, the system prompt contains the company's policies (procedural memory), the agent retrieves relevant knowledge base articles (external memory), and remembers the current customer's conversation (in-context memory).

---

## Tool Calling: How It Actually Works

Here's the actual code flow for tool calling with Claude:

```python
import anthropic

client = anthropic.Anthropic()

# Define the tools (what tools the agent can use)
tools = [
    {
        "name": "search_web",
        "description": "Search the internet for current information",
        "input_schema": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "The search query"
                }
            },
            "required": ["query"]
        }
    }
]

# First call: Claude decides whether to use a tool
response = client.messages.create(
    model="claude-opus-4-5",
    max_tokens=1024,
    tools=tools,
    messages=[
        {"role": "user", "content": "What are the top AI tools launched this week?"}
    ]
)

# Check if Claude wants to use a tool
if response.stop_reason == "tool_use":
    tool_call = response.content[0]  # The tool Claude wants to call
    tool_name = tool_call.name       # "search_web"
    tool_input = tool_call.input     # {"query": "AI tools launched this week"}
    
    # You run the tool (your code, not Claude's)
    tool_result = actual_search_function(tool_input["query"])
    
    # Send the result back to Claude
    response2 = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=1024,
        tools=tools,
        messages=[
            {"role": "user", "content": "What are the top AI tools launched this week?"},
            {"role": "assistant", "content": response.content},
            {"role": "user", "content": [
                {
                    "type": "tool_result",
                    "tool_use_id": tool_call.id,
                    "content": tool_result
                }
            ]}
        ]
    )
    
    # Now Claude gives you the final answer
    print(response2.content[0].text)
```

**This is it.** Everything more complex is built on top of this pattern.

---

## What Is MCP (Model Context Protocol)?

**MCP (Model Context Protocol)** is a standard created by Anthropic that lets AI models connect to external tools and data sources in a consistent, safe, and composable way.

**Before MCP:** Every AI tool had its own custom way of connecting to databases, file systems, APIs, etc. It was messy, inconsistent, and hard to reuse.

**After MCP:** You write an MCP server once (following the standard), and any MCP-compatible AI client (Claude Desktop, Cursor, Windsurf, etc.) can automatically use it.

### The MCP Architecture

```
┌─────────────────────┐
│   AI Application    │  ← Claude Desktop, Cursor, your app
│   (MCP Client)      │
└────────┬────────────┘
         │ MCP Protocol (JSON-RPC)
         ↓
┌─────────────────────┐
│   MCP Server        │  ← You build this (or use existing ones)
│                     │
│  - Tools            │  ← Functions the AI can call
│  - Resources        │  ← Data the AI can read
│  - Prompts          │  ← Pre-built prompts
└────────┬────────────┘
         │
         ↓
┌─────────────────────┐
│   External Service  │  ← Database, API, filesystem, etc.
└─────────────────────┘
```

### MCP Concepts

**Hosts** — Applications that connect to MCP servers (Claude Desktop, Cursor, your app)

**Clients** — The MCP client inside a host application that manages connections

**Servers** — Programs that expose tools/resources/prompts via MCP protocol

**Tools** — Functions the AI can call (like `read_file`, `query_database`, `send_email`)

**Resources** — Data sources the AI can read (like a file, a database table, a webpage)

**Prompts** — Pre-written prompt templates the AI can use

### Why MCP Is Important for You

1. **It's the new standard** — More and more AI tools are adopting MCP. Knowing it = future-proof
2. **You can build MCP servers** — Connect any API/database to any AI tool without custom integration
3. **It multiplies your capabilities** — One MCP server works with Claude, Cursor, Windsurf, and any other MCP-compatible tool
4. **The ecosystem is growing fast** — There are already 1000+ community MCP servers

### Existing MCP Servers You Can Use Right Now

These are pre-built MCP servers you can connect Claude Desktop or Cursor to:

| MCP Server | What It Does | Use Case |
|-----------|-------------|---------|
| `@modelcontextprotocol/server-filesystem` | Read/write local files | Ask Claude to read your project files |
| `@modelcontextprotocol/server-github` | GitHub repos, issues, PRs | Ask Claude to review code, create issues |
| `@modelcontextprotocol/server-postgres` | PostgreSQL queries | Ask Claude to query your database |
| `@modelcontextprotocol/server-brave-search` | Web search | Let Claude search the internet |
| `@modelcontextprotocol/server-slack` | Slack channels | Ask Claude to read Slack messages |
| `supabase-mcp` | Supabase operations | You already know Supabase! |
| `@modelcontextprotocol/server-puppeteer` | Web scraping | Let Claude browse websites |

---

## How to Set Up Your First MCP Server

### Step 1: Install Claude Desktop

Download from [claude.ai/download](https://claude.ai/download)

### Step 2: Configure MCP in Claude Desktop

Create/edit `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac) or `%APPDATA%\Claude\claude_desktop_config.json` (Windows):

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "/Users/firas/projects"
      ]
    },
    "postgres": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-postgres",
        "postgresql://localhost/mydb"
      ]
    }
  }
}
```

### Step 3: Restart Claude Desktop

Now when you ask Claude "what files are in my projects folder?" — it will actually look.

### Step 4: Build Your Own MCP Server

Here's a minimal MCP server in Python (using the official SDK):

```python
from mcp.server import Server
from mcp.server.models import InitializationOptions
import mcp.types as types

# Create the server
app = Server("my-custom-server")

# Define a tool
@app.list_tools()
async def handle_list_tools() -> list[types.Tool]:
    return [
        types.Tool(
            name="get_job_listings",
            description="Search for AI jobs matching the given criteria",
            inputSchema={
                "type": "object",
                "properties": {
                    "keywords": {"type": "string"},
                    "location": {"type": "string"}
                },
                "required": ["keywords"]
            }
        )
    ]

# Handle tool calls
@app.call_tool()
async def handle_call_tool(name: str, arguments: dict) -> list[types.TextContent]:
    if name == "get_job_listings":
        # Your actual logic here
        results = search_jobs(arguments["keywords"], arguments.get("location", "remote"))
        return [types.TextContent(type="text", text=str(results))]

# Run the server
if __name__ == "__main__":
    import asyncio
    from mcp.server.stdio import stdio_server
    
    async def main():
        async with stdio_server() as (read_stream, write_stream):
            await app.run(read_stream, write_stream, InitializationOptions())
    
    asyncio.run(main())
```

---

## LangChain: The Agent Framework

**LangChain** is a Python/JavaScript library that makes it easier to build agents. Instead of manually managing the tool-calling loop, LangChain handles it for you.

### Key LangChain Concepts

**LLM** — the AI model (Claude, GPT-4o)
**Chain** — a sequence of LLM calls (input → LLM → output → next LLM → final output)
**Agent** — an LLM + tools + a loop
**Memory** — storage for conversation history
**Retriever** — a component that fetches relevant documents from a vector store
**Vectorstore** — a database optimized for similarity search (Supabase pgvector, Pinecone, Chroma)

### A Simple LangChain Agent

```python
from langchain_anthropic import ChatAnthropic
from langchain.agents import create_react_agent, AgentExecutor
from langchain.tools import Tool
from langchain import hub

# Initialize the LLM
llm = ChatAnthropic(model="claude-opus-4-5")

# Define tools
def search_web(query: str) -> str:
    """Search the web and return results"""
    # Your search implementation
    return f"Search results for: {query}"

tools = [
    Tool(
        name="search_web",
        description="Search the internet for current information",
        func=search_web
    )
]

# Get a pre-built ReAct prompt
prompt = hub.pull("hwchase17/react")

# Create the agent
agent = create_react_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# Run the agent
result = agent_executor.invoke({"input": "What are the top 5 AI tools this week?"})
print(result["output"])
```

### LangGraph: Agents with Loops and Branches

**LangGraph** is the newer part of LangChain that lets you build more complex agents with:
- Conditional routing ("if the answer is unclear, search again")
- Parallel tool execution
- Human-in-the-loop (pause and wait for human approval)
- Persistent state (remember across sessions)

```python
from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolExecutor

# Define the state your agent carries
from typing import TypedDict, Annotated
import operator

class AgentState(TypedDict):
    messages: Annotated[list, operator.add]

# Build the graph
workflow = StateGraph(AgentState)

# Add nodes (steps in the workflow)
workflow.add_node("agent", call_llm)      # LLM reasoning
workflow.add_node("tools", execute_tools) # Tool execution

# Add edges (what happens after each step)
workflow.set_entry_point("agent")
workflow.add_conditional_edges(
    "agent",
    should_continue,  # function that decides: "done" or "use tools"
    {"continue": "tools", "end": END}
)
workflow.add_edge("tools", "agent")  # After tools, go back to agent

# Compile and run
app = workflow.compile()
result = app.invoke({"messages": [("user", "Research the top AI tools this week")]})
```

---

## Practical Exercise: Build Your First Agent

**Goal:** Build an agent that takes a job URL, visits it, extracts the key requirements, and scores how well your CV matches.

### Step 1: Set up the environment
```bash
pip install anthropic requests beautifulsoup4
```

### Step 2: Build the tools

```python
import anthropic
import requests
from bs4 import BeautifulSoup

client = anthropic.Anthropic(api_key="your-api-key")

def scrape_url(url: str) -> str:
    """Scrapes text content from a URL"""
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(response.text, "html.parser")
    # Remove scripts, styles
    for tag in soup(["script", "style"]):
        tag.decompose()
    return soup.get_text(separator="\n", strip=True)[:5000]  # Limit to 5000 chars

tools = [
    {
        "name": "scrape_url",
        "description": "Visit a URL and extract its text content",
        "input_schema": {
            "type": "object",
            "properties": {
                "url": {"type": "string", "description": "The URL to scrape"}
            },
            "required": ["url"]
        }
    }
]

YOUR_CV = """
Name: Firas Al Mostaysser
Experience: Backend Engineer → Product Owner → Founder
Skills: Node.js, PostgreSQL, Redis, Supabase, n8n, React, AI automation
Languages: Arabic, French, English
"""

def run_agent(job_url: str):
    messages = [
        {
            "role": "user",
            "content": f"""
I have a job listing at this URL: {job_url}

Please:
1. Visit the URL and read the job description
2. Extract the key requirements and responsibilities
3. Compare them to my CV below
4. Give me a match score (0-100) and explain what I'm missing

My CV:
{YOUR_CV}
"""
        }
    ]
    
    system_prompt = "You are a career coach. Help the user understand how well they match a job listing."
    
    while True:
        response = client.messages.create(
            model="claude-opus-4-5",
            max_tokens=2048,
            system=system_prompt,
            tools=tools,
            messages=messages
        )
        
        if response.stop_reason == "end_turn":
            print("Agent's answer:")
            print(response.content[0].text)
            break
        
        if response.stop_reason == "tool_use":
            messages.append({"role": "assistant", "content": response.content})
            
            for block in response.content:
                if block.type == "tool_use":
                    if block.name == "scrape_url":
                        result = scrape_url(block.input["url"])
                        messages.append({
                            "role": "user",
                            "content": [{"type": "tool_result", "tool_use_id": block.id, "content": result}]
                        })

# Run it
run_agent("https://example.com/job-posting")
```

This is a real, working AI agent you can build in 30 minutes. It demonstrates:
- Tool definition
- Tool calling loop
- Agent reasoning
- Real-world utility

---

## MCP vs. LangChain vs. n8n — Which to Use When?

| Scenario | Best Tool |
|---------|-----------|
| You want Claude to have access to your local files/database while chatting | MCP (Claude Desktop) |
| You want to build a production AI API/service | LangChain / custom Python |
| You want to automate a business workflow with AI | n8n |
| You want to give a specific Claude instance specific tools | Tool calling (direct API) |
| You're building a complex multi-step agent | LangGraph |
| You want to build fast without much code | n8n AI nodes |

**For your career:** Master n8n first (fastest to production, most job demand), then learn Claude tool calling (most flexible), then LangChain (deepest capability).

---

## What to Learn Next

1. **Claude tool calling** — the foundation of everything. Practice until you can do it without looking at docs.
2. **n8n AI Agent node** — build agents without writing much code
3. **MCP setup** — install 3 MCP servers on your Claude Desktop
4. **LangChain basics** — build your first chain and agent
5. **LangGraph** — build an agent that loops and branches

---

## Resources

- [Anthropic Tool Use Documentation](https://docs.anthropic.com/en/docs/build-with-claude/tool-use/overview)
- [MCP Official Docs](https://modelcontextprotocol.io/introduction)
- [MCP Servers Directory](https://github.com/modelcontextprotocol/servers)
- [LangChain Python Docs](https://python.langchain.com/docs/introduction/)
- [LangGraph Docs](https://langchain-ai.github.io/langgraph/)
- [LangChain Academy (free courses)](https://academy.langchain.com/)
- [n8n AI Agent Node Docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/)

---

*Back: [`ai-product-operations.md`](./ai-product-operations.md) | Next: [`ai-automation.md`](./ai-automation.md)*
