# Project 2: Job Alert Automation (n8n)

## What It Is

An n8n workflow that runs every morning at 8am and:
1. Searches for new AI Product Operations, AI Ops, and GTM Engineer job postings
2. Uses Claude to filter and score them for relevance
3. Enriches each posting with company info
4. Emails you a curated list with match scores

## Why Build This

- Directly solves YOUR problem (you need to find the right jobs)
- Teaches n8n fundamentals (scheduling, HTTP requests, AI nodes, email)
- Shows real business automation skills
- Works while you sleep

## What You'll Learn

- n8n scheduler trigger
- n8n HTTP Request node (calling external APIs)
- n8n AI/LLM node
- n8n Send Email node
- Data transformation in n8n

## Tech Stack

- **n8n** (self-hosted locally with Docker)
- **Serper.dev API** (Google search API — free 2,500 queries/month)
- **Claude API** (via n8n AI node)
- **Gmail** (for sending alerts)

## Step-by-Step Build

### Step 1: Set Up n8n

```bash
docker run -it --rm \
  --name n8n \
  -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n \
  -e N8N_BASIC_AUTH_ACTIVE=true \
  -e N8N_BASIC_AUTH_USER=admin \
  -e N8N_BASIC_AUTH_PASSWORD=yourpassword \
  n8nio/n8n
```

Open `http://localhost:5678`

### Step 2: Set Up API Credentials in n8n

1. **Anthropic API**: 
   - Go to Settings → Credentials → New
   - Search "Anthropic"
   - Enter your API key

2. **Serper.dev** (free Google search API):
   - Go to [serper.dev](https://serper.dev) → create free account
   - Get your API key
   - In n8n: Settings → Credentials → New → "HTTP Request Auth" → API Key

3. **Gmail**:
   - Settings → Credentials → New → Gmail OAuth2
   - Follow the OAuth setup

### Step 3: Build the Workflow

Create a new workflow in n8n. Add these nodes:

#### Node 1: Schedule Trigger
- **Type**: Schedule Trigger
- **Trigger interval**: Every day at 8:00 AM

#### Node 2: Set Search Queries
- **Type**: Set node
- **Operation**: Add multiple items
- Set a field called `queries` with value:
```json
[
  "AI Product Operations remote job 2026",
  "AI Ops engineer remote Tunisia EMEA",
  "n8n automation engineer remote job",
  "GTM engineer AI remote job",
  "Technical Product Manager AI remote"
]
```

#### Node 3: Split in Batches
- **Type**: Split in Batches
- **Batch Size**: 1
- This loops through each search query

#### Node 4: Search Jobs (HTTP Request)
- **Type**: HTTP Request
- **Method**: POST
- **URL**: `https://google.serper.dev/search`
- **Headers**: `X-API-KEY: {{your_serper_key}}`
- **Body** (JSON):
```json
{
  "q": "{{$json.queries[0]}} site:linkedin.com OR site:wellfound.com",
  "num": 10,
  "tbs": "qdr:d"
}
```
(the `tbs: qdr:d` means "last 24 hours")

#### Node 5: Extract Job Data (Code Node)
- **Type**: Code
- **Language**: JavaScript
- **Code**:
```javascript
// Extract relevant job data from search results
const searchResults = $input.first().json;
const jobs = [];

if (searchResults.organic) {
  for (const result of searchResults.organic.slice(0, 5)) {
    jobs.push({
      title: result.title,
      url: result.link,
      snippet: result.snippet,
      source: new URL(result.link).hostname
    });
  }
}

return jobs.map(job => ({ json: job }));
```

#### Node 6: AI Filter & Score (Basic LLM Chain)
- **Type**: Basic LLM Chain (under AI nodes)
- **Chat Model**: Claude 3.5 Sonnet (or Haiku for cost savings)
- **Prompt**:
```
You are evaluating whether a job posting is relevant for Firas Al Mostaysser, a Tunisian AI automation specialist.

Firas's profile:
- Based in Tunisia (remote-only jobs OK, EMEA jobs preferred)
- Skills: n8n, Claude API, Product Owner experience, Backend engineering (Node.js, Supabase)
- Looking for: AI Product Operations, AI Ops, GTM Engineer, Technical PM with AI focus
- Salary: targeting $2,000-$5,000/month remote

Job info:
Title: {{$json.title}}
URL: {{$json.url}}  
Description: {{$json.snippet}}

Return JSON:
{
  "relevant": true/false,
  "score": 1-10,
  "reason": "one sentence why this is or isn't relevant",
  "location_ok": true/false
}

Return ONLY JSON.
```

#### Node 7: Filter Relevant Jobs (IF Node)
- **Type**: If
- **Condition**: `{{$json.output.relevant}}` is equal to `true`
- Also filter: `{{$json.output.score}}` is greater than or equal to `6`

Only jobs that pass continue.

#### Node 8: Aggregate Results (Wait + Merge)
After the batch loop completes, merge all results.
- **Type**: Merge
- **Mode**: Append all items

#### Node 9: Build Email (Code Node)
```javascript
const jobs = $input.all();

let emailBody = `<h2>🤖 Daily AI Job Alerts - ${new Date().toLocaleDateString()}</h2>`;
emailBody += `<p>Found ${jobs.length} relevant opportunities:</p>`;

// Sort by score
jobs.sort((a, b) => b.json.output.score - a.json.output.score);

for (const job of jobs) {
  const data = job.json;
  const score = data.output?.score || '?';
  const reason = data.output?.reason || '';
  
  emailBody += `
    <hr>
    <h3>${data.title} (Score: ${score}/10)</h3>
    <p>${reason}</p>
    <p>${data.snippet}</p>
    <a href="${data.url}">View Job →</a>
  `;
}

emailBody += '<br><br><p><em>Sent by your AI Job Alert system</em></p>';

return [{ json: { emailBody, jobCount: jobs.length } }];
```

#### Node 10: Send Email (Gmail)
- **Type**: Gmail
- **To**: `firas.almostaysser@gmail.com`
- **Subject**: `🎯 {{$json.jobCount}} AI Job Opportunities - {{$now.format('MMMM DD')}}`
- **Body**: `{{$json.emailBody}}`
- **Body Content Type**: HTML

### Step 4: Test the Workflow

1. Click the "Test workflow" button
2. Watch each node execute
3. Check the email

**Common issues:**
- Serper API not returning results → check your API key and query format
- Claude returning invalid JSON → check your prompt, make sure you said "Return ONLY JSON"
- Email not sending → check Gmail OAuth credentials

### Step 5: Activate the Workflow

Toggle "Active" in n8n. The workflow will now run every morning at 8am automatically.

## What the Workflow Actually Looks Like

```
[Schedule: 8am daily]
       ↓
[Set: 5 search queries]
       ↓
[Split in Batches: process 1 query at a time]
       ↓
[HTTP: Search via Serper.dev API]
       ↓
[Code: Extract job data from results]
       ↓
[AI: Score and filter with Claude]
       ↓
[IF: relevant=true AND score>=6]
       ↓
[Merge all passing jobs]
       ↓
[Code: Format email HTML]
       ↓
[Gmail: Send daily digest]
```

## Extensions

1. **LinkedIn-specific scraping**: Use LinkedIn search RSS feeds
2. **Apply directly**: Add a node that auto-drafts your application email
3. **Track applications**: Log jobs to a Supabase table with status tracking
4. **Telegram alert**: Send a Telegram message instead of/in addition to email (faster)
5. **Company research**: For high-scoring jobs, automatically research the company

## Portfolio Framing

> "Built a fully automated job discovery and scoring system using n8n + Claude. The system searches multiple job sources daily, uses Claude to score relevance against my profile, and delivers a personalized digest every morning. This runs 100% automatically — I just read the email."

---

*Time to complete: 2-3 hours | Next: [Project 3: AI Meeting Notes](./03-ai-meeting-notes.md)*
