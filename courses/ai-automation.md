# AI Automation: Complete Guide (n8n, Make, Workflows)

## What Is AI Automation?

**AI Automation** = connecting AI models to real business systems to automate workflows that used to require humans.

**Traditional automation** (Zapier, old n8n): "When X happens, do Y" — purely rule-based.

**AI Automation** (modern n8n, Make + AI): "When X happens, understand it intelligently, then decide Y" — AI-powered decision making in the middle.

**Example of the difference:**
- Old: Email arrives → save attachment to Dropbox (simple rule)
- AI: Email arrives → Claude reads it, classifies urgency, drafts a response, routes to right team member, saves relevant data to CRM, and creates a Notion task if follow-up needed

---

## Why n8n Is Your Primary Tool

**n8n** is the best automation platform for AI workflows in 2026. Here's why:

| Feature | n8n | Make (Integromat) | Zapier |
|---------|-----|-------------------|--------|
| Open-source | ✅ | ❌ | ❌ |
| Self-hostable | ✅ | ❌ | ❌ |
| AI/LLM nodes | ✅ Native | ✅ Limited | ✅ Limited |
| Agent node | ✅ | ❌ | ❌ |
| Code node (JS/Python) | ✅ | ✅ Limited | ❌ |
| Free tier | ✅ (self-hosted) | Limited | Limited |
| MCP support | Coming | ❌ | ❌ |
| Developer-friendly | ✅ Very | ✅ | ❌ |

**For you specifically:** n8n is free when self-hosted, has the best AI integration, and you can code in it (your background = big advantage over non-technical n8n users).

---

## Setting Up n8n Locally

### Option 1: Docker (Recommended — Most Control)

```bash
# Install Docker first if you don't have it
# Then run n8n:
docker run -it --rm \
  --name n8n \
  -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n \
  n8nio/n8n
```

Open `http://localhost:5678` — you have n8n running.

### Option 2: npm (Simpler)
```bash
npm install n8n -g
n8n start
```

### Option 3: n8n Cloud (Easiest for Testing)
Go to [n8n.io](https://n8n.io) and create a free cloud account. Limited executions but zero setup.

---

## n8n Core Concepts

### Nodes
Every action in n8n is a "node." There are 3 types:

1. **Trigger nodes** — start the workflow (webhook, schedule, email received, etc.)
2. **Action nodes** — do something (send email, write to database, call API)
3. **Logic nodes** — control flow (if/else, loop, merge, switch)

### The Canvas
n8n has a visual canvas where you drag nodes and connect them with arrows. It looks like this:

```
[Trigger: Webhook] → [AI Node: Claude] → [If: Good Response?]
                                               ↓ Yes          ↓ No
                                    [Send Email]    [Slack Alert]
```

### Credentials
n8n stores your API keys securely as "credentials." Set up once, use everywhere.

### Executions
Every time a workflow runs, it creates an "execution" with full logs of what happened at each node. This is your debugger.

---

## The 10 Most Important n8n Nodes

### 1. Webhook Trigger
Listens for incoming HTTP POST requests. Use this to trigger workflows from external services.

```
URL: https://your-n8n.com/webhook/abc123
Method: POST
Body: {"event": "new_customer", "email": "user@example.com"}
```

### 2. HTTP Request
Makes HTTP calls to any API. This is how you connect to services that don't have an n8n integration.

```
Method: POST
URL: https://api.anthropic.com/v1/messages
Headers: x-api-key = {{$credentials.anthropicApi.apiKey}}
Body: {
  "model": "claude-opus-4-5",
  "messages": [{"role": "user", "content": "{{$json.text}}"}]
}
```

### 3. AI Agent Node (n8n's best feature)
Run a full ReAct agent inside n8n. Give it tools, a goal, and let it run.

```
Chat Model: Claude 3.5 Sonnet
Memory: Window Buffer Memory (last 10 messages)
Tools: [Calculator, HTTP Request, Code Executor]
System Message: "You are an operations assistant..."
```

### 4. Basic LLM Chain
Simpler than the agent — just one LLM call. Use when you don't need tool calling.

```
Chat Model: Claude
Prompt: "Summarize the following email in 3 bullet points: {{$json.emailBody}}"
```

### 5. Code Node
Run custom JavaScript or Python. You have an unfair advantage here — use it.

```javascript
// Take the incoming data and transform it
const items = $input.all();
return items.map(item => ({
  json: {
    name: item.json.firstName + ' ' + item.json.lastName,
    email: item.json.email.toLowerCase(),
    score: calculateScore(item.json)
  }
}));
```

### 6. IF Node
Branch your workflow based on conditions.
```
Condition: {{$json.sentiment}} is equal to "positive"
True path → send thank you email
False path → flag for human review
```

### 7. Schedule Trigger
Run a workflow on a schedule (cron).
```
Every Monday at 9am → generate weekly report
Every day at 7pm → summarize today's news
Every hour → check for new job postings
```

### 8. Email Trigger (IMAP) + Send Email (SMTP)
Receive emails → process them with AI → send responses.

### 9. Slack Node
Send messages to Slack channels, receive messages from Slack.

### 10. Supabase Node (YOU KNOW THIS!)
Read and write to your Supabase database. Perfect for storing AI outputs, client data, logs.

---

## 5 Real AI Automation Workflows to Build

### Workflow 1: AI Email Triage System

**What it does:** Receives emails → classifies them (urgent/normal/spam) → routes them → drafts a response for urgent ones.

```
[Email Trigger: IMAP] 
  → [Basic LLM Chain: "Classify this email: urgent/normal/spam/inquiry. Return JSON: {category, summary, suggested_action}"]
  → [Switch Node: based on category]
      → urgent: [Claude: Draft response] → [Send Email] + [Slack: Alert team]
      → normal: [Supabase: Log to inbox table]
      → spam: [Email: Move to spam folder]
      → inquiry: [Supabase: Save as lead] + [Claude: Draft FAQ response]
```

**Time to build:** 45 minutes  
**Business value:** Never miss an urgent email. Eliminate email triage time.

---

### Workflow 2: Job Opportunity Monitor

**What it does:** Every morning, searches LinkedIn/job sites for AI Product Operations roles and emails you a curated list with match scores.

```
[Schedule Trigger: 8am daily]
  → [HTTP Request: Search LinkedIn API / Serper.dev for "AI Product Operations" jobs]
  → [Code Node: Extract job titles, companies, URLs]
  → [Loop Node: For each job]
      → [HTTP Request: Scrape job posting]
      → [AI Agent: Score match to Firas's CV (1-100) + 3-sentence reason]
  → [Code Node: Sort by score, keep top 10]
  → [Gmail Node: Send formatted email with top 10 opportunities]
```

**Time to build:** 1.5 hours  
**Business value:** Never miss a job opportunity. Automated, personalized job search.

---

### Workflow 3: AI-Powered Client Onboarding

**What it does:** Client fills out a form → AI generates a personalized onboarding plan → creates tasks in Linear/Notion → sends welcome email.

```
[Webhook Trigger: Form submission]
  → [Code Node: Parse form data]
  → [Claude: Generate personalized onboarding plan based on company size, use case, tech stack]
  → [Notion Node: Create onboarding project with generated tasks]
  → [Linear Node: Create tickets for each onboarding step]
  → [Email Node: Send personalized welcome email with next steps]
  → [Slack Node: Notify customer success team]
  → [Supabase: Log client data]
```

**Time to build:** 2 hours  
**Business value:** Onboarding 10 clients manually → onboarding 100 clients with the same effort.

---

### Workflow 4: Content Performance Analysis

**What it does:** Every Monday, pulls social media/analytics data, Claude analyzes it, generates an executive report, sends to stakeholders.

```
[Schedule Trigger: Monday 9am]
  → [HTTP Request: LinkedIn Analytics API]
  → [HTTP Request: Twitter/X API]
  → [HTTP Request: Google Analytics API (if website)]
  → [Code Node: Combine all data]
  → [Claude: Analyze performance, identify trends, generate recommendations]
  → [Claude: Write executive summary (2 paragraphs, non-technical language)]
  → [Email Node: Send formatted HTML report to stakeholders]
  → [Supabase: Store report for historical tracking]
```

**Time to build:** 2 hours  
**Business value:** 3-hour weekly report → 5 minutes to review.

---

### Workflow 5: AI Lead Research Agent

**What it does:** You get a company name → AI researches them → produces a complete briefing doc.

```
[Webhook Trigger: Slack slash command "/research CompanyName"]
  → [AI Agent with tools:]
      - Tool: search_web(query)
      - Tool: scrape_url(url)
      - Tool: check_linkedin(company)
  → [Agent runs for 3-5 steps researching the company]
  → [Claude: Structure output as: company overview, recent news, key people, tech stack, potential pain points, personalized outreach angle]
  → [Notion: Create research note]
  → [Slack: Reply with formatted briefing]
```

**Time to build:** 2-3 hours  
**Business value:** 1 hour of research → 30 seconds. Perfect for sales and BD work.

---

## n8n Prompting Patterns

### Pattern 1: Structured Output
Always ask for JSON when you need to route or process the output:

```
System: You are a data extraction assistant. Always return valid JSON.

User: Extract the following from this email:
- sender_name
- urgency (low/medium/high)  
- main_request (one sentence)
- action_required (yes/no)
- suggested_response (2-3 sentences if yes)

Email: {{$json.emailBody}}

Return ONLY valid JSON. No other text.
```

### Pattern 2: Context Injection
Pass dynamic data into your prompts using n8n expressions:

```
System: You are a customer success manager for {{$json.companyName}}.

User: The client {{$json.clientName}} has this issue: {{$json.issueDescription}}

Their plan is: {{$json.plan}}
Their account age: {{$json.accountAgeDays}} days

Draft a helpful, empathetic response.
```

### Pattern 3: Few-Shot Examples in Prompts
Give Claude examples of what good output looks like:

```
Classify the following message as: urgent / question / complaint / praise / other

Examples:
"Our entire system is down!" → urgent
"How do I reset my password?" → question
"This product is terrible" → complaint
"Your support team was amazing!" → praise

Message to classify: {{$json.message}}
Return ONLY the category word.
```

### Pattern 4: Chain Prompts
Break complex tasks into steps, passing output between them:

```
Step 1: Extract → "Extract the key requirements from this job posting"
Step 2: Compare → "Compare these requirements to Firas's skills: [Step 1 output] vs [CV]"  
Step 3: Strategize → "Write a cover letter paragraph addressing the gaps: [Step 2 output]"
```

---

## Debugging n8n Workflows

### The n8n Execution Log
Every execution shows you exactly what each node received and produced. Use it to find bugs.

**Most common issues:**
1. **Wrong JSON path** — use `{{$json.field.subfield}}` not `{{$json["field"]["subfield"]}}`
2. **API rate limit** — add a "Wait" node between API calls
3. **AI returned unexpected format** — improve your prompt, add schema validation
4. **Authentication failed** — re-check your API credentials
5. **Empty data** — add an "IF" node to handle empty/null cases

### Debugging Tips
- Use the "Execute Node" button to test single nodes with sample data
- Use "Pinned data" to freeze test data and iterate on later nodes
- Always test with edge cases: empty strings, special characters, very long text

---

## Make (Integromat) — When to Use It

Make is n8n's main competitor. It's cloud-only but has some advantages:

**Use Make when:**
- Client already uses Make and you need to maintain their workflows
- You need a specific integration that n8n doesn't have
- Client doesn't want to self-host anything

**Key Make concepts:**
- **Scenarios** = n8n workflows
- **Modules** = n8n nodes
- **Bundles** = n8n items (data packets flowing through the workflow)
- **Filters** = n8n IF nodes

The logic is the same as n8n. If you know n8n, you can learn Make in 2 hours.

---

## Zapier — For Clients Who Need Simplicity

Zapier is the most user-friendly but also the most limited. Good for:
- Non-technical clients who want simple "if this then that" automations
- When you need fast setup and don't care about code
- Integration with 7,000+ apps (more than n8n/Make)

**As a consultant:** Know Zapier basics to serve clients who are already on it. Build your real work on n8n.

---

## Building Your Automation Portfolio

Your goal: 5–10 publicly documented automation projects. Here's how to structure each:

### For Each Project:
1. **Problem statement** — what manual work does this replace?
2. **Workflow diagram** — screenshot of n8n canvas
3. **Tools used** — n8n, Claude, Supabase, etc.
4. **Code snippets** — any custom code nodes you wrote
5. **Prompts used** — the actual prompts (anonymized if sensitive)
6. **Results** — time saved, quality improvement, scale achieved
7. **How to deploy** — instructions so others can use it

### Where to Share:
- GitHub repo with README for each workflow
- LinkedIn posts showing the workflow in action (video screen recording)
- n8n community templates (they feature interesting templates)
- Dev.to article walkthrough

---

## Automation Pricing Guide

When you start freelancing, price automation projects like this:

| Project Type | Complexity | Price Range |
|-------------|-----------|-------------|
| Simple zap (2-3 nodes) | Low | $150–$300 |
| Multi-step workflow with AI | Medium | $400–$800 |
| Complex agent workflow | High | $800–$2,000 |
| Full automation system (5+ workflows) | Very High | $2,000–$5,000 |
| Monthly retainer (maintain + improve) | Ongoing | $300–$800/month |

**Tip:** Always quote a retainer. One-time projects are fine but retainers = predictable income.

---

## Resources

- [n8n Official Docs](https://docs.n8n.io)
- [n8n AI Nodes Documentation](https://docs.n8n.io/integrations/builtin/cluster-nodes/)
- [n8n Community](https://community.n8n.io) — where you'll find answers and help others
- [n8n Templates](https://n8n.io/workflows/) — 1000+ free workflow templates
- [Make Academy](https://www.make.com/en/help/learning-resources) — free Make tutorials
- [Zapier University](https://zapier.com/university) — free Zapier tutorials
- [Cole Medin on YouTube](https://www.youtube.com/@ColeMedin) — best n8n + AI agent tutorials

---

*Back: [`ai-agents-and-mcp.md`](./ai-agents-and-mcp.md) | Next: [`gtm-and-market.md`](./gtm-and-market.md)*
