# 05 - Portfolio Blueprints (What to Build)

Your portfolio should prove one thing:

> You can use AI to create measurable business outcomes.

Each project must include:

1. Problem statement
2. Workflow architecture diagram
3. Tools used
4. Demo (video/GIF/screenshots)
5. Metrics (before vs after)
6. Lessons + next version

---

## Project 1: AI Support Triage Operator (Product Ops)

### Goal

Auto-triage inbound support or bug reports and route to the right team.

### Stack

- n8n (or Make)
- OpenAI/Anthropic API
- Slack/Email/Notion integration
- Google Sheets/Postgres log table

### Workflow

1. Inbound ticket arrives (email/form/Slack)
2. LLM classifies issue type + urgency
3. Extracts required fields
4. Routes to correct channel/owner
5. Creates summary and suggested next action
6. Logs every run for QA

### Business metrics

- Triage time reduction (%)
- First-response speed improvement
- Misroute rate before/after

### Deliverables

- README with architecture and KPI table
- 3-minute Loom walkthrough
- Example prompt + evaluation notes

---

## Project 2: AI GTM Prospect Research Assistant

### Goal

Reduce manual pre-call research time for outbound sales motions.

### Stack

- Python script + API calls
- Clay/Apollo/LinkedIn data (or synthetic data if needed)
- LLM summarization
- Notion/HubSpot export format

### Workflow

1. Input company + contact list
2. Gather website + public data
3. Generate account brief:
   - likely pain points
   - relevant use cases
   - suggested outreach angles
4. Draft first-touch personalized messages
5. Push structured output to sheet/CRM format

### Business metrics

- Research time per account
- Message personalization quality
- Response rate lift (if tested live)

### Deliverables

- Sample input/output files
- Prompt templates for SDR/BDR use
- 1-page case study with KPI assumptions

---

## Project 3: AI Agent + MCP Mini Ops Console (Flagship)

### Goal

Build a simple agent that can use tools via MCP-style interfaces to run small operational tasks.

### Scope (practical)

- Agent receives operator request in plain language
- Agent calls specific tools (calendar/task/doc/search)
- Agent returns action summary and confidence note

### Example use cases

1. "Summarize today's priority tickets and prepare handoff notes."
2. "Create follow-up tasks for stalled opportunities."
3. "Draft weekly product ops report from data snippets."

### Technical expectations

- Clear tool contracts (input/output)
- Error handling and fallback behavior
- Execution logs for transparency

### Business metrics

- Minutes saved per workflow
- Number of tasks automated
- Error/failure rate over test runs

### Deliverables

- Architecture README
- Demo script and sample runs
- "What I would improve for production" section

---

## Presentation Format for Each Project

Use this repo structure:

```text
projects/
  project-name/
    README.md
    assets/
    prompts/
    sample-data/
    results/
```

README template:

1. Overview
2. Business problem
3. Solution architecture
4. Setup and run steps
5. Sample output
6. KPI impact
7. Limitations and next iteration

---

## Quality Checklist Before Publishing

- [ ] Demo works end-to-end
- [ ] README can be understood by non-engineers
- [ ] Includes quantified value
- [ ] Includes one "failure case" and fix
- [ ] Includes one short video
- [ ] Pushed to GitHub with clean commit history

---

## Portfolio Publishing Cadence

- Week 2: Publish Project 1
- Week 5: Publish Project 2
- Week 9: Publish Project 3

After each publish:

1. Post on LinkedIn with "problem -> build -> impact"
2. Send to 5 target people (recruiters/founders/operators)
3. Add to CV and job applications immediately
