# 04 - AI Agents + MCP Bootcamp (From Zero)

This module takes you from beginner to practical builder.

---

## Part A: Core concepts (simple language)

### What is an AI agent?

An agent is an LLM-based system that can:

1. Understand a goal
2. Decide next actions
3. Use tools (APIs, browser, code, DB)
4. Check results and iterate

Basic loop:

1. Receive objective
2. Plan
3. Execute tool call
4. Observe output
5. Repeat until done or blocked

---

### What is MCP?

MCP (Model Context Protocol) is a standard way for AI models to connect to external tools and data sources.

Think of MCP as "USB-C for AI tools":

- One standard interface
- Many tools/resources connected consistently
- Easier portability between model environments

Why it matters for jobs:

- Companies need safe, structured access to internal systems
- MCP-like patterns are becoming standard in AI operations

---

## Part B: Skill ladder (6 levels)

### Level 1 - Prompt and task design

You should be able to:

- Write role/task/context/output prompts
- Define constraints and success criteria
- Ask model for structured JSON output

Practice task:

- Turn messy support tickets into priority + owner + ETA using prompt templates

---

### Level 2 - Single workflow automation

You should be able to:

- Trigger workflows from form/webhook
- Call LLM once
- Save result to sheet/DB/Notion

Tools:

- n8n or Make
- OpenAI/Anthropic API
- Google Sheets/Notion

Practice task:

- "Meeting notes -> action items -> assigned owners"

---

### Level 3 - Multi-step workflow with guardrails

You should be able to:

- Chain multiple steps
- Add validation and fallback logic
- Handle API errors and retries

Practice task:

- Lead enrichment pipeline:
  - Input lead list
  - Enrich from sources
  - LLM writes personalized first line
  - Quality filter and score

---

### Level 4 - Retrieval + tools

You should be able to:

- Use docs/knowledge base for grounding
- Choose relevant context
- Avoid hallucination with citations/links

Practice task:

- Internal policy assistant for onboarding questions

---

### Level 5 - Agentic orchestration

You should be able to:

- Build planner/executor/reflection pattern
- Use tool selection based on task type
- Log decisions for auditability

Practice task:

- Agent that triages product incidents and proposes first response draft

---

### Level 6 - MCP-style integration mindset

You should be able to:

- Understand resource/tool abstractions
- Design safe access boundaries
- Document capabilities and limits

Practice task:

- Simulate a mini MCP server design doc for CRM + ticketing integration

---

## Part C: 30-day agents learning sprint

### Week 1

- Learn agent fundamentals and prompt structure
- Build 2 single-step automations
- Document with screenshots and metrics

### Week 2

- Build one multi-step workflow with retries
- Add human-in-the-loop approval step
- Publish mini case study

### Week 3

- Build retrieval assistant from your own docs
- Add evaluation sheet (accuracy/helpfulness)
- Improve prompts based on failures

### Week 4

- Build one "mini agent" end-to-end
- Write architecture README
- Record 3-minute demo

---

## Part D: Must-know design patterns

1. Planner -> Executor -> Critic
2. Human approval on high-risk actions
3. Confidence scoring before final answer
4. Retry with backoff on unstable APIs
5. Caching repeated expensive calls
6. Structured logs for debugging

---

## Part E: Common mistakes to avoid

- Building demos with no business use case
- No metrics before/after
- No fallback when model output fails
- Over-complex architecture too early
- Ignoring data privacy and credentials hygiene

---

## Part F: "job-ready" proof checklist

You are job-ready when you can show:

- 3 automation projects with measurable impact
- 1 agent-style workflow with architecture diagram
- 1 write-up on handling failure cases
- 1 explanation of MCP integration approach

If you can explain these clearly in interviews, you stand out.
