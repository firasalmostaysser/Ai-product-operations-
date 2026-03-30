# Phase 4: AI Automation Builders (Days 43-56)

**Goal**: Master automation platforms, build real workflows that solve business problems, and start making money as an AI automation consultant.

---

## Why Automation = Money

Businesses waste thousands of hours on manual tasks that AI + automation can handle. If you can:
- Identify these tasks
- Build automated solutions
- Show the ROI (time saved, errors reduced, cost cut)

...you can charge $500-5000 per workflow. This is a **real, immediate income opportunity**.

---

## The Automation Stack

```
┌─────────────────────────────────────────────────────┐
│                 YOUR AUTOMATION STACK                │
│                                                     │
│  ┌──────────┐  ┌──────────┐  ┌──────────────────┐  │
│  │   n8n    │  │   Make   │  │   Custom Python  │  │
│  │(primary) │  │(secondary)│  │  (advanced)      │  │
│  └──────────┘  └──────────┘  └──────────────────┘  │
│                                                     │
│  ┌──────────┐  ┌──────────┐  ┌──────────────────┐  │
│  │  Zapier  │  │ Activepieces│  │   AI APIs      │  │
│  │ (know it)│  │ (open src)│  │  (OpenAI,Claude) │  │
│  └──────────┘  └──────────┘  └──────────────────┘  │
└─────────────────────────────────────────────────────┘
```

---

## Tool 1: n8n (Your Primary Weapon) -- Days 43-49

### Why n8n

- **Open source** (self-host for free)
- **700+ integrations** (every tool you'd need)
- **AI nodes built in** (OpenAI, Anthropic, etc.)
- **Code when needed** (JavaScript/Python nodes)
- **Visual workflow builder** (easy to show clients)
- **Growing fast** -- one of the most popular automation tools in AI

### Setup

**Cloud (quick start):**
- Go to n8n.io, create account
- Free tier: 5 active workflows

**Self-hosted (recommended for learning):**
```bash
# Using Docker
docker run -d --name n8n \
  -p 5678:5678 \
  -v n8n_data:/home/node/.n8n \
  n8nio/n8n

# Or using npm
npm install -g n8n
n8n start
```

Access at `http://localhost:5678`

### Core Concepts

| Concept | What It Is |
|---------|-----------|
| **Workflow** | A series of connected nodes that automate a process |
| **Node** | A single step (trigger, action, or logic) |
| **Trigger** | What starts the workflow (webhook, schedule, event) |
| **Connection** | Data flow between nodes |
| **Execution** | One run of the workflow |
| **Credentials** | API keys and auth stored securely |

### 10 Workflows to Build (Build All of These)

#### Workflow 1: AI Email Classifier
**What it does**: Incoming emails get classified by AI and routed to the right person.

```
Email Trigger → AI Node (classify) → Switch → Route to Slack channels
```

- Trigger: Gmail/IMAP new email
- AI: Claude classifies as Support/Sales/Partnership/Spam
- Switch: Route based on classification
- Action: Post to appropriate Slack channel with summary

#### Workflow 2: Content Generator Pipeline
**What it does**: Generate social media content from a blog post URL.

```
Webhook → Scrape URL → AI Generate Posts → Post to Buffer/LinkedIn
```

- Input: Blog post URL via webhook
- Scrape the content
- AI generates: 1 LinkedIn post, 3 tweets, 1 summary
- Schedule posts via Buffer or post directly

#### Workflow 3: Lead Enrichment
**What it does**: When a new lead comes in, automatically research them.

```
New Lead (CRM) → Scrape LinkedIn → AI Research → Enrich CRM Record
```

- Trigger: New contact in CRM (HubSpot, Airtable)
- Research: Scrape company website, LinkedIn
- AI: Generate summary, identify pain points, suggest talking points
- Update: Enrich CRM record with research

#### Workflow 4: Customer Support Auto-Responder
**What it does**: AI drafts responses to support tickets.

```
New Ticket → AI Classify → AI Draft Response → Human Review → Send
```

- Trigger: New ticket (Zendesk, email, form)
- AI classifies urgency and topic
- AI drafts response using knowledge base
- Sends to human for approval
- Sends approved response

#### Workflow 5: Meeting Notes Processor
**What it does**: Process meeting recordings into action items.

```
New Recording → Transcribe → AI Extract Actions → Create Tasks → Send Summary
```

- Trigger: New file in Google Drive or webhook
- Transcribe using Whisper API
- AI extracts: action items, decisions, key points
- Create tasks in Notion/Linear/Asana
- Email summary to attendees

#### Workflow 6: Competitive Intelligence Monitor
**What it does**: Monitor competitors and generate weekly reports.

```
Schedule (weekly) → Scrape Competitor Sites → AI Analyze Changes → Generate Report → Email
```

- Cron trigger: Every Monday
- Scrape competitor websites, Product Hunt, G2 reviews
- AI: Compare changes, identify new features, pricing updates
- Generate markdown report
- Email to team

#### Workflow 7: Invoice/Document Processor
**What it does**: Extract data from invoices/documents using AI.

```
New Document → OCR/Parse → AI Extract Fields → Update Spreadsheet → Notify
```

- Trigger: New file uploaded (email attachment, Google Drive)
- OCR if needed (image → text)
- AI extracts: vendor, amount, date, line items
- Updates Google Sheets or accounting software
- Notifies finance team

#### Workflow 8: Social Listening Agent
**What it does**: Monitor social media for brand mentions and respond.

```
Schedule → Search Mentions → AI Sentiment Analysis → Alert if Negative → Draft Response
```

#### Workflow 9: Job Application Tracker
**What it does**: Track job applications and automate follow-ups.

```
New Application (Airtable) → Schedule Follow-ups → AI Draft Follow-up → Send → Update Status
```

**Build this for yourself immediately.**

#### Workflow 10: AI Content Calendar
**What it does**: Generate a week's worth of content ideas with drafts.

```
Schedule (Sunday) → AI Research Trends → AI Generate Topics → AI Draft Content → Create Calendar Events
```

### n8n AI Nodes Deep Dive

n8n has dedicated AI nodes:

- **AI Agent** node: Build agents directly in n8n
- **Chat Model** node: Connect to Claude, GPT, etc.
- **Memory** node: Give agents conversation memory
- **Tool** nodes: Give agents tools (calculator, code, web search)
- **Vector Store** nodes: RAG with Pinecone, Qdrant, etc.
- **Text Splitter** nodes: Chunk documents for processing
- **Embeddings** nodes: Generate embeddings

This means you can build complete AI agents visually in n8n without writing code.

---

## Tool 2: Make (Integromat) -- Days 50-52

### When to Use Make vs n8n

| Criteria | Use Make | Use n8n |
|----------|---------|---------|
| Client prefers no-code | Yes | Yes (but Make is slightly easier) |
| Need self-hosting | No | Yes |
| Complex logic | Good | Better (code nodes) |
| AI workflows | Good | Better (AI nodes) |
| Enterprise clients | Yes | Yes |
| Budget conscious | Paid only | Free (self-host) |
| Integrations needed | 1000+ | 700+ |

### Key Make Concepts

- **Scenarios** (= n8n Workflows)
- **Modules** (= n8n Nodes)
- **Routers** (= n8n Switch nodes)
- **Aggregators** (combine multiple items into one)
- **Iterators** (process arrays one by one)

### Build 3 Workflows in Make

1. **AI Blog Writer**: RSS feed → AI generates blog draft → save to Google Docs
2. **CRM Automation**: New deal → AI research company → update deal notes → notify sales
3. **Report Generator**: Schedule → pull data from APIs → AI analyze → generate PDF → email

---

## Tool 3: Custom Python Automation -- Days 53-54

Sometimes you need more control than visual tools provide.

### FastAPI + Background Tasks

```python
# automation_server.py
from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel
import anthropic
import httpx

app = FastAPI()
client = anthropic.Anthropic()

class AutomationRequest(BaseModel):
    task: str
    data: dict

@app.post("/automate/classify-email")
async def classify_email(email_body: str, background_tasks: BackgroundTasks):
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=200,
        messages=[{
            "role": "user",
            "content": f"Classify this email into one category (support/sales/partnership/spam) and extract key info. Email: {email_body}"
        }]
    )
    
    classification = response.content[0].text
    
    background_tasks.add_task(route_email, classification, email_body)
    
    return {"classification": classification}

async def route_email(classification: str, email_body: str):
    # Route to Slack, update CRM, etc.
    pass
```

### Scheduled Tasks with APScheduler

```python
from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()

@scheduler.scheduled_job('cron', hour=8, minute=0)
def daily_ai_news_digest():
    """Run every day at 8 AM -- gather AI news and send digest."""
    # 1. Scrape news sources
    # 2. AI summarize
    # 3. Send email/Slack
    pass

scheduler.start()
```

---

## Tool 4: Zapier -- Day 55

### Know It, Don't Master It

Zapier is the most well-known automation tool. You should:
- Know how it works
- Be able to discuss it with clients
- Know its limitations vs n8n/Make
- Build 1-2 simple Zaps

**Key difference**: Zapier is simpler but more expensive and less flexible than n8n.

---

## Day 56: The Automation Business Model

### How to Make Money with Automation

**Service Pricing:**
| Complexity | Price Range | Example |
|-----------|------------|---------|
| Simple (2-3 steps) | $200-500 | Email forwarding + AI classification |
| Medium (5-10 steps) | $500-2000 | Lead enrichment pipeline |
| Complex (10+ steps) | $2000-5000 | Full customer onboarding automation |
| Enterprise | $5000-20000+ | Multi-system integration suite |

**Monthly Maintenance**: $100-500/month per workflow

### Where to Find Clients

1. **Upwork** -- Search for "automation" or "n8n" or "AI workflow" projects
2. **LinkedIn** -- Post about automations you've built, results you've achieved
3. **Local businesses** -- Walk in, ask "What manual tasks take the most time?"
4. **AI communities** -- People are looking for automation builders
5. **Cold outreach** -- Target businesses that clearly need automation (still using spreadsheets for operations)

### Your Automation Consulting Pitch

"I help businesses eliminate manual work using AI-powered automation. My average client saves 20+ hours per week by automating repetitive tasks like email processing, document handling, lead management, and reporting. I build the automation, train your team, and provide ongoing support."

---

## Phase 4 Checklist

- [ ] Built 10 n8n workflows (all listed above)
- [ ] Built 3 Make workflows
- [ ] Built 1 custom Python automation
- [ ] Understand pricing for automation services
- [ ] Created a portfolio page showcasing your automations
- [ ] Applied to 3+ automation gig on Upwork/freelance platform
- [ ] Can explain n8n vs Make vs Zapier vs custom code tradeoffs

---

**Next: `05-portfolio-and-income.md` -- Build the portfolio and start earning.**
