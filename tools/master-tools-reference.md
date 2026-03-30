# AI Tools Master Reference

> Updated: 2026-03-27. Review and update monthly.

---

## Tier 1: Must Master (Use Daily)

### Cursor IDE
**What it is:** A code editor built on VSCode with deep AI integration. The best AI coding tool available.

**Why it's different from VSCode + Copilot:**
- Chat with Claude/GPT-4o about your entire codebase, not just the current file
- "Apply" suggestions directly — no copy-paste
- Composer: write a description, get a full multi-file implementation
- Cursor Rules: define coding standards that apply to every AI suggestion

**Key shortcuts:**
- `Ctrl+K` — inline edit (select code, press, describe what to change)
- `Ctrl+L` — open chat panel
- `Ctrl+I` — open Composer (big changes across files)
- `@filename` — reference a file in chat
- `@codebase` — search your entire codebase in chat

**Power tips:**
1. Use Composer to scaffold entire features: "Add a RAG pipeline using Supabase pgvector and Anthropic embeddings"
2. Use `@` to reference your docs: "@README.md add a section about the new feature"
3. Set up Cursor Rules (.cursorrules file) with your stack and preferences

**Getting started:**
1. Download at [cursor.com](https://cursor.com)
2. Sign in and get free 2-week Pro trial
3. Switch model to claude-opus-4-5 or GPT-4o in settings

---

### Claude Code (CLI)
**What it is:** Anthropic's official command-line AI coding agent. You run it in your terminal and it writes code, runs commands, edits files — fully autonomous.

**Why it matters:** Claude Code can take a high-level goal and execute it end-to-end: create files, write code, install dependencies, run tests, iterate. It's like having a senior engineer who types for you.

**Installation:**
```bash
npm install -g @anthropic-ai/claude-code
```

**Usage:**
```bash
# Navigate to your project
cd my-project

# Start Claude Code
claude

# Then type your goal, for example:
# "Build a REST API endpoint that accepts a job description and returns CV match analysis"
# "Fix the failing tests in test_agent.py"
# "Refactor the authentication module to use JWT"
```

**What makes it special:**
- It reads ALL your files before starting (full project context)
- It runs commands (npm install, pytest, git) and sees the output
- It iterates automatically: if a test fails, it reads the error and fixes it
- It can generate a full project from a single sentence description

**Best practices:**
- Give it clear, specific goals with context
- Tell it your tech stack upfront
- Review changes with `git diff` before accepting
- Use it for scaffolding and repetitive tasks, review carefully for complex logic

**Cost:** Uses Anthropic API directly. Each coding session typically costs $0.50–$3.00 in API credits depending on project size.

---

### n8n
**What it is:** Open-source automation platform with AI superpowers. Visual workflow builder. Your core tool for automation projects.

**See the full guide:** [`/courses/ai-automation.md`](../courses/ai-automation.md)

**Quick reference:**
```bash
# Start locally with Docker
docker run -it --rm -p 5678:5678 -v ~/.n8n:/home/node/.n8n n8nio/n8n

# Open in browser
http://localhost:5678
```

---

### Anthropic Claude API
**What it is:** Direct access to Claude models via API. The foundation of your AI building work.

**Models (as of March 2026):**

| Model | Best For | Cost (approx) |
|-------|---------|---------------|
| claude-opus-4-5 | Complex reasoning, best quality | $15/M input tokens |
| claude-sonnet-4-5 | Balance of quality and speed | $3/M input tokens |
| claude-haiku-3-5 | Fast, cheap, simple tasks | $0.25/M input tokens |

**1 million tokens ≈ 750,000 words. For most projects, costs are pennies per run.**

**Quick start:**
```python
import anthropic

client = anthropic.Anthropic(api_key="your_key")
response = client.messages.create(
    model="claude-opus-4-5",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello!"}]
)
print(response.content[0].text)
```

**API Key:** [console.anthropic.com](https://console.anthropic.com) → API Keys → Create key
New accounts get $5 free credit.

---

## Tier 2: Learn This Month

### OpenAI API (GPT-4o)
**Why:** Some clients prefer GPT-4o. Also needed for embeddings (cheaper than Claude embeddings).

**Key models:**
- `gpt-4o` — best quality, multimodal (images + text)
- `gpt-4o-mini` — cheap, fast (use for embeddings and simple tasks)
- `text-embedding-3-small` — embeddings (1536 dimensions, very cheap)

**Quick start:**
```python
from openai import OpenAI
client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "Hello!"}]
)
print(response.choices[0].message.content)
```

---

### Bolt.new
**What it is:** AI that builds full web apps from a text description. You already use this!

**Best use cases:**
- Build a front-end for your AI tools in 10 minutes
- Rapid prototype a SaaS idea
- Build demo apps to show clients

**Tips:**
- Be very specific: "Build a web app with a text input and a button. When clicked, POST to http://localhost:5678/webhook/summarize with the text. Display the response."
- Use for UI, not for complex backend logic
- Always review the code it generates

---

### Windsurf (by Codeium)
**What it is:** An AI IDE similar to Cursor. Good free tier.

**When to use over Cursor:** When you want a free alternative. Cursor has a better model selection; Windsurf has a more generous free tier.

---

### LangChain
**What it is:** Python/JavaScript library for building AI agents and RAG systems.

**When to use:** When you need more control than n8n's AI nodes offer, but don't want to implement everything from scratch.

**Installation:**
```bash
pip install langchain langchain-anthropic langchain-openai
```

**Quick start with Claude:**
```python
from langchain_anthropic import ChatAnthropic

llm = ChatAnthropic(model="claude-opus-4-5")
response = llm.invoke("What is an AI agent?")
print(response.content)
```

---

### Supabase (You Already Know This!)
**What it is:** Open-source Firebase alternative. PostgreSQL + Auth + Storage + Edge Functions.

**New things to learn (beyond what you know):**
- **pgvector**: Vector extension for RAG systems (see Project 5)
- **Edge Functions**: Run serverless functions close to users
- **Realtime**: Subscribe to database changes (you built this before with Socket.io — Supabase has it built-in now)

---

## Tier 3: Know What They Are (Learn When Needed)

### CrewAI
**What it is:** Framework for building teams of AI agents that collaborate on complex tasks.

**When to use:** When one agent isn't enough. Example: "Research assistant" agent + "Writer" agent + "Editor" agent all working together.

```python
from crewai import Agent, Task, Crew

researcher = Agent(role="Researcher", goal="Find relevant information", backstory="...")
writer = Agent(role="Writer", goal="Write compelling content", backstory="...")

research_task = Task(description="Research AI trends in 2026", agent=researcher)
writing_task = Task(description="Write a blog post", agent=writer, context=[research_task])

crew = Crew(agents=[researcher, writer], tasks=[research_task, writing_task])
result = crew.kickoff()
```

---

### LangGraph
**What it is:** LangChain's framework for building stateful, multi-step agents with loops and branches.

**When to use:** When your agent needs to loop, branch, or have human checkpoints.

---

### Pinecone
**What it is:** Managed vector database. Alternative to Supabase pgvector.

**When to use:** When you need a dedicated vector database with more features than pgvector. For most projects, Supabase pgvector is fine.

---

### Helicone / LangSmith / Langfuse
**What they are:** LLM observability tools — log every AI API call with inputs, outputs, latency, and cost.

**Why you need one:** You can't improve what you can't measure. These tools let you see exactly what your agents are doing.

**Recommendation:** Start with **Langfuse** (open-source, self-hostable) or **LangSmith** (if using LangChain).

---

### Perplexity API
**What it is:** Search API that returns cited, current information. Better than basic web search for research agents.

**When to use:** When your agents need to search the web and you want high-quality, cited results.

---

## Daily AI News Sources

Stay updated without spending hours. Check these every morning (5 minutes total):

| Source | Format | What It Covers |
|--------|--------|---------------|
| [The Rundown AI](https://www.therundown.ai/) | Email newsletter | Daily AI news, tools, launches |
| [TLDR AI](https://tldr.tech/ai) | Email newsletter | Quick AI news digest |
| [r/AIAgents](https://reddit.com/r/AIAgents) | Reddit | AI agent tutorials and discussions |
| [r/n8n](https://reddit.com/r/n8n) | Reddit | n8n workflows and tips |
| [Andrej Karpathy on X/Twitter](https://twitter.com/karpathy) | Twitter/X | Deep AI insights from former OpenAI/Tesla |
| [Simon Willison's blog](https://simonwillison.net/) | Blog | Technical AI exploration |
| [Latent Space Podcast](https://www.latent.space/) | Podcast | In-depth AI engineering discussions |

**Note for daily log:** Every day, write down ONE new thing you learned from these sources.

---

## Tool Setup Checklist

Use this when setting up a new machine:

- [ ] Cursor IDE installed and logged in
- [ ] Anthropic API key in environment variables
- [ ] OpenAI API key in environment variables
- [ ] n8n running locally (Docker)
- [ ] Claude Code CLI installed (`npm install -g @anthropic-ai/claude-code`)
- [ ] Python 3.10+ with pip
- [ ] Node.js 18+ with npm
- [ ] Git configured with your email/name
- [ ] Supabase project created
- [ ] Serper.dev account for search API
- [ ] GitHub account with SSH key configured

---

## Environment Variables Template

Create a `.env` file in each project (never commit this):

```bash
# AI APIs
ANTHROPIC_API_KEY=sk-ant-...
OPENAI_API_KEY=sk-...

# Database
SUPABASE_URL=https://xxxx.supabase.co
SUPABASE_SERVICE_KEY=eyJ...
SUPABASE_ANON_KEY=eyJ...

# Search
SERPER_API_KEY=...

# Automation
N8N_URL=http://localhost:5678
N8N_API_KEY=...

# Email (optional)
GMAIL_USER=firas.almostaysser@gmail.com
SMTP_PASSWORD=...
```

---

*Last updated: 2026-03-27 | Review and update tools list monthly*
