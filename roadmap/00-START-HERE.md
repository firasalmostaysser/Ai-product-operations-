# Day 1: Start Here

**Read this entire file. Then do everything in it. Today.**

---

## Step 1: Set Up Your AI Arsenal (1 hour)

You need these accounts and tools installed before anything else.

### Must-Have (Free or Free Tier)

| Tool | What It Is | Action |
|------|-----------|--------|
| [Cursor](https://cursor.com) | AI-powered code editor | You have this. Make sure you're on latest version. |
| [Claude](https://claude.ai) | Anthropic's AI assistant | Create account. Use Pro if you can ($20/mo -- worth it). |
| [Claude Code](https://docs.anthropic.com/en/docs/claude-code) | CLI coding agent | Install: `npm install -g @anthropic-ai/claude-code` |
| [ChatGPT](https://chat.openai.com) | OpenAI's assistant | Create account. Free tier works. Plus ($20/mo) is better. |
| [GitHub](https://github.com) | Code hosting | You have this. Make your profile look professional today. |
| [Codex](https://openai.com/codex) | OpenAI's coding agent | Access through OpenAI platform |
| [v0](https://v0.dev) | Vercel's UI generator | Create account. Free tier available. |
| [Bolt.new](https://bolt.new) | Full-stack app builder | Create account. You already know this one. |
| [n8n](https://n8n.io) | Automation platform | Create cloud account OR self-host (we'll do both). |
| [Replit](https://replit.com) | Online IDE with AI agent | Create account. |

### Set Up API Keys (You'll Need These)

1. **OpenAI API Key**: https://platform.openai.com/api-keys
2. **Anthropic API Key**: https://console.anthropic.com/
3. **Google AI (Gemini) API Key**: https://aistudio.google.com/apikey

Store these securely. You'll use them for building agents and tools.

### Install on Your Machine

```bash
# Node.js (if not installed)
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt-get install -y nodejs

# Python 3.11+ (if not installed)
sudo apt install python3 python3-pip python3-venv

# Claude Code
npm install -g @anthropic-ai/claude-code

# Essential Python packages
pip install openai anthropic langchain crewai fastapi uvicorn

# n8n (self-hosted)
npm install -g n8n
```

---

## Step 2: Understand the Landscape (30 minutes)

Read these definitions until you can explain each one to a non-technical person:

### What is an AI Agent?

An AI agent is a program that uses a large language model (like GPT-4 or Claude) to **think**, **plan**, and **take actions** to accomplish a goal. Unlike a simple chatbot that just responds to messages, an agent can:

- Break a task into steps
- Use tools (search the web, run code, read files, call APIs)
- Remember context from previous steps
- Make decisions based on results
- Loop until the job is done

**Example**: You tell an agent "Find the top 10 AI startups hiring in EMEA and draft outreach emails for each." The agent would: search the web, filter results, extract company info, research each company, draft personalized emails, and present them to you.

### What is MCP (Model Context Protocol)?

MCP is a standard created by Anthropic that lets AI models connect to external tools and data sources in a standardized way. Think of it like USB for AI:

- **Before MCP**: Every AI tool had its own custom way to connect to databases, APIs, file systems. Messy.
- **After MCP**: One standard protocol. Any AI model can connect to any MCP-compatible tool.

**MCP has 3 parts**:
1. **MCP Servers** -- Programs that expose tools/data (e.g., a server that lets AI read your database)
2. **MCP Clients** -- AI applications that connect to servers (e.g., Cursor, Claude Desktop)
3. **The Protocol** -- The standard communication format between them

**Why it matters for your career**: Companies are building MCP servers for everything. Knowing how to build and configure them is a high-demand skill.

### What is AI Product Operations?

AI Product Ops sits between product, engineering, and customers. You:

- Own day-to-day workflows for AI products
- Use AI to investigate issues and generate solutions
- Build scalable internal processes
- Coordinate delivery across teams
- Make sure AI products actually work for users

**This is NOT a coding-heavy role**. It's about **using AI tools intelligently**, **managing workflows**, and **shipping outcomes**.

### What is GTM (Go-To-Market)?

GTM is the strategy for launching a product to market. In AI, this means:

- **Positioning**: How do you describe your AI product vs competitors?
- **Target audience**: Who buys this? What's their pain?
- **Channels**: Where do you reach them? (LinkedIn, communities, events, outbound)
- **Sales motion**: Self-serve? Enterprise sales? PLG (product-led growth)?
- **Pricing**: Usage-based? Seat-based? Free tier?

### What is AI Automation?

Using AI + automation tools to eliminate manual work. Examples:

- Auto-categorize support tickets using AI
- Generate weekly reports from data using LLMs
- Auto-respond to common customer questions
- Process documents and extract key information
- Route leads to the right sales rep based on AI analysis

---

## Step 3: Your First Build (2 hours)

You're going to build something today. Not tomorrow. Today.

### Build a Simple AI Chatbot with Claude

Create a new folder and build this:

```python
# simple_agent.py
import anthropic

client = anthropic.Anthropic()  # Uses ANTHROPIC_API_KEY env variable

def chat(user_message: str, conversation_history: list) -> str:
    conversation_history.append({
        "role": "user",
        "content": user_message
    })
    
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1024,
        system="You are a helpful AI career advisor specializing in AI product operations and automation roles. You help users navigate the AI job market.",
        messages=conversation_history
    )
    
    assistant_message = response.content[0].text
    conversation_history.append({
        "role": "assistant",
        "content": assistant_message
    })
    
    return assistant_message

def main():
    print("AI Career Advisor - Type 'quit' to exit")
    print("-" * 50)
    history = []
    
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() == 'quit':
            break
        
        response = chat(user_input, history)
        print(f"\nAdvisor: {response}")

if __name__ == "__main__":
    main()
```

**Run it**: `ANTHROPIC_API_KEY=your-key python simple_agent.py`

You just built your first AI application. That's more than 90% of people who talk about AI.

---

## Step 4: Join Communities (30 minutes)

Do this TODAY. These communities are where jobs get posted, knowledge gets shared, and connections get made.

1. **Discord - Cursor** (https://discord.gg/cursor) -- Active community, tips, jobs
2. **Discord - Anthropic** -- Claude tips, MCP discussions
3. **Discord - n8n** -- Automation workflows, templates
4. **Discord - LangChain** -- Agent building community
5. **Twitter/X** -- Follow: @AnthropicAI, @OpenAI, @cursor_ai, @naborsky, @swyx, @lataborsky
6. **LinkedIn** -- Start posting about your AI learning journey TODAY
7. **Reddit** -- r/LocalLLaMA, r/artificial, r/MachineLearning

---

## Step 5: Plan Your Week

| Day | Focus | Output |
|-----|-------|--------|
| Day 1 (Today) | Setup + First Build | Working chatbot + all accounts created |
| Day 2 | Cursor AI Deep Dive | Complete Cursor mastery (see Phase 1) |
| Day 3 | Claude Code + Codex | Build something with each tool |
| Day 4 | AI Agents Theory | Understand agents, tools, memory |
| Day 5 | Build First Real Agent | Agent with tool use (web search + file ops) |
| Day 6 | MCP Introduction | Understand protocol, set up first MCP server |
| Day 7 | Review + LinkedIn Post | Write about what you learned, share publicly |

---

## Step 6: Set Your Daily Routine

Every single day:

```
08:00 - 08:30  Check AI news (see daily-log/how-to-stay-updated.md)
08:30 - 10:30  Study (follow current roadmap phase)
10:30 - 11:00  Break + LinkedIn engagement (comment on 5 posts)
11:00 - 14:00  Build (work on current project)
14:00 - 15:00  Lunch + AI podcast/YouTube
15:00 - 16:30  Apply to jobs / Network / Freelance outreach
16:30 - 17:00  Daily log + plan tomorrow
```

---

## What Success Looks Like

By end of Week 1, you should be able to:
- [ ] Explain AI agents, MCP, and AI Product Ops to anyone
- [ ] Have built 2-3 small AI tools
- [ ] Have joined 5+ communities
- [ ] Have posted on LinkedIn about your journey
- [ ] Have applied to at least 3 jobs

By end of Month 1:
- [ ] Built 3 portfolio projects
- [ ] Can build AI agents from scratch
- [ ] Understand MCP and can build/configure MCP servers
- [ ] Have a polished GitHub profile with AI projects
- [ ] Have had at least 5 interview conversations

By end of Month 3:
- [ ] 5+ portfolio projects deployed and live
- [ ] Making money (freelance, consulting, or employed)
- [ ] Active in AI communities with a growing reputation
- [ ] Can confidently discuss any AI tool, agent framework, or automation platform

---

**Now go to `roadmap/01-ai-tools-mastery.md` and start Phase 1.**
