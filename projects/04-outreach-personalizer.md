# Project 4: AI Outreach Personalizer

## What It Is

An n8n + Claude workflow that:
1. Takes a company URL (or LinkedIn URL)
2. Scrapes the company's website and/or LinkedIn
3. Researches recent news about the company
4. Generates a personalized cold email from you to the decision-maker

## Why This Project Is Powerful

This directly demonstrates GTM + AI skills — one of the hottest skill combinations in 2026.
Companies pay $500–$2,000 to have this built for their sales teams.
It also generates real leads for your own consulting business.

## Architecture

```
[Input: Company URL + Your message goal]
           ↓
[HTTP: Scrape company website]
           ↓
[HTTP: Search for recent company news via Serper]
           ↓
[HTTP: (Optional) LinkedIn company data]
           ↓
[Code: Combine all research]
           ↓
[Claude: Generate personalized email]
           ↓
[Output: Personalized email + research summary]
```

## n8n Workflow Build

### Node 1: Webhook Trigger
```json
{
  "trigger": "webhook",
  "path": "/outreach",
  "method": "POST",
  "expectedBody": {
    "company_url": "string",
    "decision_maker_name": "string",
    "decision_maker_title": "string", 
    "your_goal": "string"
  }
}
```

Test trigger: Send this POST request:
```json
{
  "company_url": "https://www.storyteller.io",
  "decision_maker_name": "Ryan",
  "decision_maker_title": "Head of Operations",
  "your_goal": "offer AI automation consulting services"
}
```

### Node 2: Scrape Company Website (HTTP Request)
```
Method: GET
URL: {{$json.company_url}}
Add header: User-Agent: Mozilla/5.0 (compatible; researchbot/1.0)
```

### Node 3: Extract Key Info from Website (Claude)
```
Prompt:
Extract key business information from this website content.

Website content: {{$json.data}}

Return JSON:
{
  "company_description": "2-3 sentence description of what they do",
  "target_customers": "who they sell to",
  "key_value_props": ["list of their main value propositions"],
  "company_size_hint": "startup/SMB/enterprise/unknown",
  "tech_mentioned": ["any technologies mentioned"]
}
```

### Node 4: Search Recent News (HTTP Request to Serper)
```
Method: POST
URL: https://google.serper.dev/news
Headers: X-API-KEY: your_key
Body: {
  "q": "{{$json.company_url.replace('https://', '').replace('www.', '').split('/')[0]}}",
  "num": 5,
  "tbs": "qdr:m"
}
```

### Node 5: Combine Research (Code Node)
```javascript
const websiteData = $('Extract Key Info').first().json;
const newsData = $('Search Recent News').first().json;

const companyInfo = {
  ...websiteData,
  recent_news: newsData.news?.slice(0, 3).map(n => ({
    title: n.title,
    snippet: n.snippet,
    date: n.date
  })) || []
};

return [{ json: companyInfo }];
```

### Node 6: Generate Personalized Email (Claude)

System prompt:
```
You are Firas Al Mostaysser, an AI automation consultant based in Tunisia.

Your background:
- 3+ years as backend engineer (Node.js, PostgreSQL, Redis, Supabase)
- 18 months as Product Owner (delivered enterprise SaaS to 50+ clients)
- Now specializing in n8n + Claude AI automations that save 80%+ of manual work
- Recent wins: notary firm 2hr→10min, built real-time systems for 80K+ users

Your email style:
- Short (4 sentences max)
- Specific and personalized (reference real details about them)
- Leads with value, not features
- No corporate jargon
- No "I hope this finds you well" or "I wanted to reach out"
```

User prompt:
```
Write a personalized cold email to {{$json.decision_maker_name}}, 
{{$json.decision_maker_title}} at {{company description}}.

My goal: {{$json.your_goal}}

Company research:
- What they do: {{$json.company_description}}
- Their customers: {{$json.target_customers}}
- Key value props: {{$json.key_value_props}}
- Recent news: {{$json.recent_news}}

Write an email that:
1. Opens with something SPECIFIC to them (a detail from the research)
2. States a likely pain point they have given their stage and business
3. Shows a relevant win I've had ("I did X for a similar company, result was Y")
4. Ends with a soft ask ("Worth a quick chat?" or "Happy to share more details if useful")

Return JSON:
{
  "subject_line": "compelling subject line (not generic)",
  "email_body": "the full email text",
  "personalization_note": "what specific detail did you use to personalize?"
}
```

### Node 7: Format Response (Code Node)
```javascript
const result = JSON.parse($input.first().json.output);
const research = $('Combine Research').first().json;

return [{
  json: {
    subject: result.subject_line,
    email: result.email_body,
    personalization: result.personalization_note,
    company_research: research,
    generated_at: new Date().toISOString()
  }
}];
```

### Node 8: Respond to Webhook
Return the result back to whoever called the webhook.

## Example Output

**Input:**
```json
{
  "company_url": "https://www.storyteller.io",
  "decision_maker_name": "Alex",
  "decision_maker_title": "Head of Product",
  "your_goal": "offer AI automation consulting for their client onboarding"
}
```

**Output:**
```json
{
  "subject": "Your Stories SDK + 5x faster client onboarding",
  "email": "Hi Alex,\n\nSaw Storyteller recently landed the NBA partnership — congrats, that's a big one for sports engagement.\n\nI'm guessing onboarding new league clients at that scale is a lot of manual configuration work. I just automated onboarding for a SaaS company that cut setup from 3 days to 4 hours using n8n + Claude — same pattern would apply to your SDK configuration process.\n\nHappy to share the workflow doc if that's useful — no call needed.\n\nFiras",
  "personalization": "Used the NBA partnership as the opening hook"
}
```

## Build the Front-End (Bonus)

Create a simple HTML page that calls your n8n webhook:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Outreach Personalizer</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 600px; margin: 40px auto; padding: 20px; }
        input, textarea { width: 100%; padding: 8px; margin: 5px 0 15px 0; border: 1px solid #ddd; border-radius: 4px; }
        button { background: #5865F2; color: white; padding: 10px 20px; border: none; border-radius: 4px; cursor: pointer; }
        #output { background: #f5f5f5; padding: 15px; border-radius: 4px; margin-top: 20px; white-space: pre-wrap; }
    </style>
</head>
<body>
    <h1>🤖 AI Outreach Personalizer</h1>
    
    <label>Company URL:</label>
    <input type="url" id="url" placeholder="https://company.com">
    
    <label>Decision Maker Name:</label>
    <input type="text" id="name" placeholder="Alex">
    
    <label>Their Title:</label>
    <input type="text" id="title" placeholder="Head of Product">
    
    <label>Your Goal:</label>
    <textarea id="goal" rows="2" placeholder="offer AI automation consulting for their onboarding process"></textarea>
    
    <button onclick="generate()">Generate Email</button>
    
    <div id="output" style="display:none"></div>
    
    <script>
    async function generate() {
        const btn = document.querySelector('button');
        btn.textContent = 'Generating...';
        btn.disabled = true;
        
        const res = await fetch('http://localhost:5678/webhook/outreach', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({
                company_url: document.getElementById('url').value,
                decision_maker_name: document.getElementById('name').value,
                decision_maker_title: document.getElementById('title').value,
                your_goal: document.getElementById('goal').value
            })
        });
        
        const data = await res.json();
        const output = document.getElementById('output');
        output.style.display = 'block';
        output.innerHTML = `<strong>Subject:</strong> ${data.subject}\n\n<strong>Email:</strong>\n${data.email}\n\n<em>Personalization: ${data.personalization}</em>`;
        
        btn.textContent = 'Generate Email';
        btn.disabled = false;
    }
    </script>
</body>
</html>
```

## Portfolio Framing

> "Built an AI-powered outreach personalization system. It takes a company URL, automatically researches the company (website scraping + news search), and generates a personalized cold email using Claude. Reduced my outreach research + writing time from 20 minutes per email to 2 minutes."

---

*Time to complete: 3-4 hours | Next: [Project 5: Personal Knowledge RAG](./05-personal-knowledge-rag.md)*
