# AI Product Operations: Complete Guide

## What Is This Role?

**AI Product Operations** (sometimes called "AI Ops," "AI Product Ops," or "Technical Product Operations") is one of the fastest-growing roles in the tech industry. It sits at the intersection of:

- **Product Management** — understanding what users need, prioritizing features
- **Operations** — running workflows, ensuring quality, managing delivery
- **AI Engineering** — using and configuring AI tools to accelerate everything

You are NOT writing deep ML algorithms. You ARE:
- Running the day-to-day operational flows of an AI product
- Using AI to investigate issues, generate solutions, improve quality
- Building workflows that scale the team's output
- Being the bridge between technical AI capabilities and business/client needs

---

## Why This Role Exists Now

Three years ago, this job didn't exist. It exists now because:

1. **AI products need a different kind of operations** — traditional ops is about process; AI ops is about prompts, models, evaluation, quality
2. **Speed of AI is outpacing traditional PM workflows** — you need someone who can ship and iterate using AI tools, not just manage Jira tickets
3. **Non-engineers need to work with AI** — AI Product Ops is the translator between "what the model can do" and "what the client needs"
4. **Cost and quality management** — running LLMs at scale is expensive and unpredictable; someone needs to own this

---

## The Storyteller Example

Here's what an AI Product Ops role at Storyteller actually means:

**Storyteller** makes a "Stories" format SDK (like Instagram/Snapchat Stories) that sports organizations (NBA, NFL clubs, etc.) embed in their apps. Their AI Product Ops person would:

1. **Onboard new clients** — configure their Storyteller setup, test that Stories render correctly
2. **Investigate issues** — "NBA team says Stories aren't loading for Android users" → dig into logs, reproduce, escalate
3. **Build workflows** — "can we automate the weekly content performance report?" → build it with n8n + Claude
4. **Use AI to accelerate** — write a Claude prompt that auto-generates sports content suggestions, or builds an analysis of which story types perform best
5. **Coordinate with engineering** — translate client needs into bug reports or feature requests
6. **Iterate on AI features** — test new prompts, evaluate output quality, ship improvements

You did almost ALL of this as Product Owner at Softylines. The difference is the AI tooling.

---

## Core Competencies You Need

### 1. AI Workflow Design

**What it means:** You can design a process end-to-end that uses AI to accomplish a goal.

**Example workflow:** Client needs weekly engagement report
```
1. Pull data from Storyteller analytics API (HTTP Request node in n8n)
2. Process and structure the data (Code node)
3. Feed to Claude with a prompt: "Analyze this data and write a 1-page exec summary"
4. Format the output (Claude structured output)
5. Send via email/Slack (n8n notification node)
Schedule: every Monday 8am
```

**How to practice:**
- Map out 5 manual workflows you know and redesign them with AI
- Build 2 real n8n workflows that use Claude or GPT

### 2. Prompt Engineering for Operations

**What it means:** Writing system prompts that produce reliable, consistent, high-quality outputs for operational use cases.

**Key difference from casual prompting:** Operational prompts must work consistently across many inputs, not just one. They need:
- Clear role definition ("You are a sports content analyst...")
- Output format specification ("Return JSON with keys: summary, highlights, action_items")
- Edge case handling ("If data is missing, say 'N/A' in that field")
- Error handling ("If you cannot analyze, explain why in the 'error' field")

**Example operational prompt:**
```
You are a product operations analyst for a sports Stories platform.
You will receive weekly engagement data for a sports organization's Stories feed.

Analyze the data and return a JSON response with exactly these fields:
{
  "headline_metric": "one sentence on the most important number",
  "top_performing_stories": ["list of 3 story titles"],
  "declining_metrics": ["list of any metrics that decreased week-over-week"],
  "recommended_actions": ["list of 2-3 specific, actionable recommendations"],
  "executive_summary": "3 sentences max, for a non-technical sports executive"
}

Rules:
- Never make up data. If a field cannot be determined, use null.
- Use plain language. No jargon.
- Be specific. "Engagement dropped 15%" not "engagement could be improved."
```

**How to practice:**
- Write 10 operational prompts for real business use cases
- Test each prompt with 5 different inputs and measure consistency
- Iterate until the output is 90%+ reliable

### 3. AI Product Quality & Evaluation

**What it means:** Knowing how to tell if an AI product is working well or not.

**Key metrics in AI products:**
- **Accuracy/Quality** — is the output correct and useful?
- **Latency** — how long does it take to respond?
- **Cost per request** — how much does each API call cost?
- **Error rate** — how often does it fail or produce garbage?
- **User satisfaction** — are users happy with the outputs?

**Evaluation approaches:**
1. **Human evaluation** — you (or testers) grade outputs 1–5
2. **LLM-as-judge** — use Claude to grade Claude's outputs (powerful but tricky)
3. **Golden set testing** — maintain 50 test inputs with known good outputs; run after every change
4. **A/B testing** — run two versions simultaneously, compare metrics

**Tools for this:**
- LangSmith (LangChain's tracing + eval platform)
- Langfuse (open-source alternative)
- Ragas (RAG evaluation)
- Custom eval scripts (you can build these with Python)

### 4. Client/Stakeholder Communication for AI Products

**What it means:** Explaining AI behavior to non-technical clients without losing their trust.

**Common situations you'll face:**
- "Why did the AI say this wrong thing?" → Explain model limitations, how you're fixing it
- "Can AI do X for us?" → Scope assessment (yes/no/maybe + timeline)
- "We don't trust AI" → Explain the human-in-the-loop components
- "AI was working last week but now it's different" → Explain model updates, versioning

**Key communication principles:**
1. Never overpromise. AI has limitations. Be honest.
2. Show don't tell. Demo > explanation.
3. Use the client's business language, not AI jargon.
4. Always have a fallback plan ("if AI fails, here's the manual process").

### 5. AI Product Ops Tooling

**Tools you need to know:**

| Tool | Purpose | Priority |
|------|---------|----------|
| n8n | Workflow automation | P0 |
| Claude API / OpenAI API | LLM calls | P0 |
| Supabase | Database + vector search | P0 (you know this) |
| LangSmith or Langfuse | Tracing + evaluation | P1 |
| PromptLayer | Prompt versioning | P1 |
| Retool or Appsmith | Internal admin tools | P1 |
| Linear or Jira | Issue tracking (you know this) | P0 |
| Notion or Confluence | Documentation | P0 |
| Slack | Async communication | P0 |
| Loom | Async video communication | P0 |

---

## A Day in the Life: AI Product Operations

Here's what a typical day looks like in this role:

**9:00am** — Check Slack for overnight issues from clients. One sports team reports their automated highlights aren't generating. Open LangSmith, check the logs.

**9:30am** — Find the issue: the content input was too long and exceeded context window. Write a fix prompt that truncates input gracefully. Test in staging.

**10:00am** — Weekly sync with engineering. Share 3 client requests from this week. Prioritize with the product manager. Estimate effort using AI (ask Claude to estimate given the current architecture).

**11:00am** — Build a new automation: when a client sends a Slack message with a content brief, auto-generate 5 story ideas using Claude + post them back in Slack. Build it in n8n in 45 minutes.

**12:00pm** — Lunch.

**1:00pm** — Client call with a Premier League football club. Walk them through their weekly Stories analytics report. They ask about adding AI-generated match highlights. Scope it live: "3-4 days for a prototype."

**2:30pm** — Work on the highlight generator prototype. Write the prompt, test it with last week's match data.

**4:00pm** — Review the output quality. The first 10 results are good, 2 are weird. Update the prompt to handle edge cases. Re-test.

**5:00pm** — Update Notion docs with the new workflow and prompt. Commit prompt to the prompt management system.

**5:30pm** — Done.

---

## AI Product Operations vs. Traditional Product Operations

| Traditional Ops | AI Product Ops |
|----------------|----------------|
| Fix bugs manually | Use AI to diagnose and suggest fixes |
| Document processes in Notion | Use AI to auto-generate and maintain docs |
| Write weekly reports manually | Build AI that writes reports automatically |
| Handle client questions one by one | Build AI that answers common questions |
| Write test cases manually | Use AI to generate test cases |
| Analyze user feedback | Use AI to categorize and summarize feedback |

**The upgrade is:** every manual, repeatable task gets automated. Your job becomes designing those automations and handling the exceptions AI can't handle.

---

## Key AI Product Ops Frameworks

### The AI Operations Stack

```
Layer 4: Business Logic (what the product does)
    ↕
Layer 3: AI Workflows (n8n, LangChain, custom agents)
    ↕
Layer 2: LLM APIs (Claude, GPT-4o, Gemini)
    ↕
Layer 1: Data (Supabase, APIs, documents, databases)
```

Your job touches all 4 layers but primarily lives in Layer 3.

### The ARISE Framework for AI Workflow Design

- **A — Automate**: What manual process can be fully automated?
- **R — Replace**: What manual process can AI replace with supervision?
- **I — Improve**: What AI process already exists but needs better quality?
- **S — Scale**: What works at small scale but needs to work at 10x volume?
- **E — Eliminate**: What process is no longer needed because AI handles upstream?

### The 3 Modes of AI Product Operations

1. **Build mode** — creating new AI workflows, prompts, automations
2. **Monitor mode** — checking quality, catching failures, reviewing metrics
3. **Fix mode** — investigating issues, debugging prompts, handling incidents

In a given week, you'll typically spend: 40% build, 40% monitor, 20% fix.

---

## How to Talk About AI Product Ops in an Interview

**Question: "What is AI Product Operations?"**

Good answer:
> "It's the operational layer that makes AI products work reliably in production. It's not about building the AI itself — it's about designing the workflows, prompts, and processes that turn AI capabilities into consistent, scalable business value. My job is to make sure the AI is doing the right thing, doing it consistently, and doing it efficiently — and when it's not, figuring out why and fixing it."

**Question: "How do you evaluate an AI feature?"**

Good answer:
> "I think about three dimensions: quality, reliability, and cost. For quality, I'd build a golden test set — maybe 50 representative inputs with expected outputs — and score each new version against it. For reliability, I'd track error rate and edge case failures. For cost, I'd monitor token usage and optimize prompts to reduce waste without sacrificing quality. I'd also set up tracing with something like Langfuse so I can see exactly what's happening in every call."

**Question: "Can you give an example of a workflow you've automated?"**

Your answer (use your real experience):
> "At my previous role, I built a notary automation tool. The workflow was: secretary uploads a handwritten contract → OCR extracts the text → Claude parses the legal structure and fills a structured template → the formatted document is auto-saved in the system. What used to take 2 hours now takes 10 minutes. That's an 11x improvement. The key was writing a reliable parsing prompt that could handle the inconsistencies in handwritten documents — I spent about 3 hours iterating on that prompt with 20 test cases until the accuracy was consistently above 95%."

---

## The Best Companies Hiring for This Role Right Now

Search for these job titles (March 2026):
- "AI Product Operations"
- "AI Ops"
- "Technical Product Manager - AI"
- "AI Implementation Manager"
- "AI Solutions Engineer"
- "Conversational AI Specialist"
- "LLM Product Specialist"
- "AI Product Specialist"
- "Prompt Engineer" (often ops-focused)

**Best companies to target:**
- AI-first SaaS companies (Storyteller, Synthesia, ElevenLabs, Perplexity, etc.)
- Enterprise software companies adding AI (Salesforce, HubSpot, Notion, Linear)
- AI workflow companies (Zapier, Make, n8n — yes, they hire ops people)
- Consulting firms with AI practices (Accenture, McKinsey — but these are harder)
- AI startups in fintech, legaltech, healthtech

**Where to find them:**
- LinkedIn (set alerts for job titles above)
- [wellfound.com](https://wellfound.com) (AngelList — startup jobs)
- [remote.co](https://remote.co)
- [workatastartup.com](https://workatastartup.com) (YC companies)
- [remoteok.com](https://remoteok.com)
- [himalayas.app](https://himalayas.app) (remote-only)

---

## Resources to Go Deeper

- [Anthropic's guide to building with Claude](https://docs.anthropic.com/en/docs/build-with-claude/overview)
- [OpenAI Cookbook](https://cookbook.openai.com/) — practical examples
- [LangChain Academy](https://academy.langchain.com/) — free courses on agents, RAG
- [Langfuse docs](https://langfuse.com/docs) — LLM observability
- [Lenny's Newsletter](https://www.lennysnewsletter.com/) — best PM newsletter, covers AI a lot

---

*Next: [`ai-agents-and-mcp.md`](./ai-agents-and-mcp.md)*
