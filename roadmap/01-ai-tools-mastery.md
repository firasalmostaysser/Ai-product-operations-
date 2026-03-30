# Phase 1: AI Tools Mastery (Days 1-14)

**Goal**: Become dangerous with every major AI coding and building tool. Not just "I've tried it" -- "I can ship production work with it."

---

## Why This Phase First

Every role you're targeting (AI Product Ops, GTM, AI Automation) requires you to **use AI tools at an expert level**. You need to:

1. Know what each tool is best at
2. Build real things with each one
3. Have opinions about when to use what
4. Talk about them credibly in interviews

---

## Tool 1: Cursor AI (Days 1-3)

**You already use Cursor. Now master it.**

### What Most People Don't Know About Cursor

1. **Agent Mode vs Ask Mode**: Agent mode lets Cursor autonomously make changes across multiple files. Ask mode is for questions. Most people only use Ask mode.

2. **Rules Files**: Create `.cursor/rules` files to give Cursor context about your project. This dramatically improves code quality.

```
# Example .cursor/rules file
You are working on an AI automation platform built with:
- Backend: FastAPI (Python 3.11)
- Frontend: Next.js 14 with TypeScript
- Database: Supabase (PostgreSQL)
- AI: Anthropic Claude API
- Automation: n8n for workflow orchestration

Follow these conventions:
- Use async/await for all API calls
- Type everything in TypeScript (no `any`)
- Use Pydantic models for all API request/response schemas
- Write docstrings for all functions
```

3. **Multi-file Editing**: Use `@` to reference files. Cursor can edit multiple files in one operation.

4. **Terminal Integration**: Cursor can run commands in the terminal. Use this for testing, deploying, and debugging.

5. **Image Input**: You can paste screenshots and Cursor will generate code to match the design.

### Exercises

- [ ] Build a complete REST API with FastAPI using only Cursor prompts
- [ ] Create a React dashboard by pasting a screenshot and letting Cursor generate it
- [ ] Use Agent mode to refactor a multi-file project
- [ ] Create a `.cursor/rules` file for an AI automation project
- [ ] Use Cursor to debug a complex issue (give it error logs and let it fix)

---

## Tool 2: Claude Code (Days 4-5)

**Claude Code is a CLI-based coding agent. It runs in your terminal and can autonomously build entire projects.**

### Setup

```bash
npm install -g @anthropic-ai/claude-code
export ANTHROPIC_API_KEY=your-key-here
```

### How It Works

1. Open terminal in any project directory
2. Run `claude` to start
3. Describe what you want to build
4. Claude Code reads your files, understands context, and makes changes
5. It can run tests, fix errors, and iterate

### Key Features

- **Autonomous file editing**: Reads and writes files directly
- **Command execution**: Can run shell commands
- **Git integration**: Can commit, create PRs
- **Multi-file understanding**: Reads entire codebases
- **Tool use**: Can use MCP servers for additional capabilities

### When to Use Claude Code vs Cursor

| Scenario | Use Claude Code | Use Cursor |
|----------|----------------|------------|
| Building from scratch | Yes | Yes |
| Refactoring large codebase | Yes (better context) | Yes |
| Quick UI changes | No | Yes (visual) |
| Debugging with logs | Either | Either |
| Writing documentation | Yes | Yes |
| Complex multi-step tasks | Yes (autonomous) | Yes (agent mode) |
| When you want visual diff | No | Yes |

### Exercises

- [ ] Build a complete Python CLI tool using only Claude Code
- [ ] Use Claude Code to add tests to an existing project
- [ ] Create a full API + database schema with Claude Code
- [ ] Use Claude Code to write documentation for a project
- [ ] Build an n8n custom node using Claude Code

---

## Tool 3: OpenAI Codex (Days 6-7)

**Codex is OpenAI's autonomous coding agent, accessible in ChatGPT.**

### What Codex Does

- Runs in a cloud sandbox
- Can read/write files, run code, install packages
- Works asynchronously -- you can give it a task and come back later
- Good for isolated tasks that need a clean environment

### When to Use Codex

- When you need a clean, isolated environment
- For tasks that take time (it runs in background)
- When you want to experiment without affecting your local setup
- For generating boilerplate or starter code

### Exercises

- [ ] Use Codex to build a data processing pipeline
- [ ] Have Codex create a complete project with tests
- [ ] Use Codex for code review (paste code, ask for improvements)

---

## Tool 4: v0 by Vercel (Days 8-9)

**v0 generates production-ready UI components from text descriptions.**

### Why v0 Matters for You

AI Product Ops and AI Automation roles often need you to **quickly prototype dashboards, admin panels, and internal tools**. v0 lets you do this in minutes.

### How to Use v0

1. Go to v0.dev
2. Describe what you want: "A dashboard showing AI agent performance metrics with charts for success rate, response time, and token usage"
3. v0 generates React + Tailwind code
4. Iterate with follow-up prompts
5. Export to your project

### Exercises

- [ ] Generate an AI operations dashboard with v0
- [ ] Create a client onboarding wizard for an AI product
- [ ] Build a workflow builder UI
- [ ] Create an analytics dashboard for automation workflows
- [ ] Generate a landing page for an AI automation service

---

## Tool 5: Bolt.new & Lovable (Days 10-11)

**Full-stack app builders that generate complete applications.**

### Bolt.new (You Already Know This)

**Go deeper:**
- Use it to build complete SaaS tools
- Learn to iterate effectively (prompt engineering for Bolt)
- Deploy directly to production

### Lovable

Similar to Bolt.new but with different strengths:
- Better at complex multi-page apps
- Supabase integration built-in
- Good for MVP prototyping

### Exercises

- [ ] Build a complete AI tool tracker app with Bolt.new (track which AI tools you use, their cost, and ROI)
- [ ] Create a client CRM for AI consulting with Lovable
- [ ] Build an automation workflow visualizer
- [ ] Ship a micro-SaaS in one day using either tool

---

## Tool 6: AI-Powered Research & Writing (Days 12-13)

**Not just coding tools -- you need AI for research, writing, and analysis.**

### Perplexity AI
- Deep research on any topic
- Use for competitive analysis, market research
- Cite sources (important for GTM roles)

### Claude for Analysis
- Upload documents (PDFs, CSVs) for analysis
- Use Projects feature to maintain context
- Create analysis reports

### NotebookLM (Google)
- Upload multiple sources
- Generate summaries and insights
- Create audio overviews (podcasts from your docs)

### Exercises

- [ ] Use Perplexity to research the top 20 AI Product Ops roles and what they require
- [ ] Upload 5 job descriptions to Claude and ask it to identify common skills and requirements
- [ ] Use NotebookLM to create a study guide from AI agent documentation

---

## Day 14: Integration & Review

### Build an "AI Tool Comparison" Project

Create a simple web app (use Cursor + v0) that compares AI coding tools:

**Features:**
- List of tools with descriptions
- Your personal rating and notes for each
- "Best for" recommendations
- Cost comparison

**This becomes a portfolio piece AND proves you know the tools.**

### Self-Assessment

Answer these honestly:

1. Can you build a complete API using Cursor in under 30 minutes?
2. Can you use Claude Code to autonomously add features to an existing project?
3. Can you prototype a dashboard with v0 in under 10 minutes?
4. Can you ship a complete MVP with Bolt.new in a day?
5. Do you know when to use which tool?

If any answer is "no," spend more time on that tool before moving to Phase 2.

---

## Key Principle: Ship, Don't Study

For every hour studying a tool, spend 2 hours building with it. Reading documentation without building is a waste of time. Build ugly things. Build broken things. Build things nobody will use. Just build.

---

**Next: `02-ai-agents-and-mcp.md` -- This is where it gets exciting.**
