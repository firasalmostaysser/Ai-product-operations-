# Project 1: CV Tailor Agent

## What It Is

An AI agent that takes a job description and your CV, then:
1. Extracts the key requirements from the job posting
2. Analyzes your CV for relevant experience
3. Rewrites your CV summary and skills section to match the job
4. Highlights what to emphasize in a cover letter
5. Gives you a match score and gap analysis

## Why Build This First

- Uses just the Claude API (no complex setup)
- Directly solves YOUR real problem (tailoring CVs for each application)
- Easy to demo to someone else (they can use it too)
- Shows prompt engineering skills
- Shows you can build real AI-powered tools, not just wrappers

## What You'll Learn

- Claude Messages API (the foundation of everything)
- System prompts vs. user prompts
- Structured output from Claude (JSON responses)
- Basic Python or Node.js for AI API calls

## Tech Stack

- **Python 3.10+** or **Node.js 18+**
- **Anthropic Python SDK** (`pip install anthropic`)
- **dotenv** for API key management

## Step-by-Step Build Instructions

### Step 1: Set Up the Environment

```bash
mkdir cv-tailor-agent
cd cv-tailor-agent
pip install anthropic python-dotenv
touch .env main.py README.md .gitignore
```

Create `.env`:
```
ANTHROPIC_API_KEY=your_key_here
```

Create `.gitignore`:
```
.env
__pycache__/
*.pyc
```

Get your API key: [console.anthropic.com](https://console.anthropic.com) → API Keys → Create key. Free $5 credit to start.

### Step 2: Write the Core Script

Create `main.py`:

```python
import os
import json
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client = Anthropic()

# Your actual CV content (update with your real info)
YOUR_CV = """
Name: Firas Al Mostaysser
Location: Tunis, Tunisia
Email: firas.almostaysser@gmail.com

SUMMARY:
Software engineer turned Product Owner with 3+ years of technical experience and 
18 months in product/operations. Built real-time systems for 80,000+ concurrent users.
Now specializing in AI automation, building n8n + Claude workflows that automate 
operational bottlenecks for growing SaaS companies.

EXPERIENCE:
Founder & AI Automation Builder | Reefq | Jan 2025 - Present
- Built n8n automation workflows for client onboarding and operations
- Used Claude API to build intelligent document processing (notary tool: 2hr → 10min)
- Conducted 40+ customer discovery calls across multiple industries

Product Owner | Softylines | Nov 2023 - Jul 2025
- Led delivery of enterprise HR SaaS platform, coordinating team of 8
- Shipped 15+ features on schedule
- Onboarded 50+ startup clients to the platform
- Managed cross-functional teams (engineering, design, QA)

Backend Engineer | Softylines | Mar 2022 - Nov 2023
- Built real-time notification system: Socket.io, Redis, Kafka, PostgreSQL
- Served 80,000+ concurrent users

SKILLS:
Technical: Node.js, PostgreSQL, Redis, Supabase, n8n, React, Python, Docker, APIs
AI Tools: Claude API, n8n AI nodes, Cursor IDE, LangChain (learning)
Languages: Arabic (native), French (fluent), English (fluent)

EDUCATION:
National Engineering Degree, Software Engineering | Polytechnic School of Sousse | 2021-2025
"""

SYSTEM_PROMPT = """You are a professional career coach and technical recruiter with 10 years of experience. 
You specialize in helping software engineers and AI professionals land roles at top tech companies.

When given a job description and a CV, you:
1. Extract the key requirements from the job description
2. Analyze the CV for relevant experience and gaps
3. Provide specific, actionable advice

You always return structured, helpful analysis. You are honest about gaps but always frame them constructively."""

def analyze_cv_match(job_description: str, cv: str) -> dict:
    """Analyze how well a CV matches a job description."""
    
    response = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=2000,
        system=SYSTEM_PROMPT,
        messages=[
            {
                "role": "user",
                "content": f"""Please analyze how well this CV matches the job description.

JOB DESCRIPTION:
{job_description}

MY CV:
{cv}

Return a JSON response with exactly these fields:
{{
  "match_score": <number 0-100>,
  "strengths": ["list of 3-5 specific strengths that match the job"],
  "gaps": ["list of 2-4 gaps or missing skills"],
  "rewritten_summary": "a 3-sentence professional summary rewritten to target THIS specific job",
  "skills_to_highlight": ["list of 5-8 skills from CV most relevant to this job"],
  "cover_letter_angle": "one paragraph about the most compelling angle to take in a cover letter",
  "recommended_actions": ["2-3 specific things to do before applying"]
}}

Return ONLY valid JSON. No other text or formatting."""
            }
        ]
    )
    
    # Parse the JSON response
    result = json.loads(response.content[0].text)
    return result

def generate_tailored_cv_section(job_description: str, cv: str, section: str) -> str:
    """Generate a tailored version of a specific CV section."""
    
    response = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=1000,
        system=SYSTEM_PROMPT,
        messages=[
            {
                "role": "user",
                "content": f"""Rewrite the {section} section of this CV to better match the job description.

JOB DESCRIPTION:
{job_description}

CURRENT CV:
{cv}

Rewrite only the {section} section. Make it:
- Specific and relevant to this job
- Quantified where possible (use numbers from the original CV)
- Action-verb first for each bullet
- No more than 3-5 bullet points or 2-3 sentences if a summary

Return only the rewritten section text, nothing else."""
            }
        ]
    )
    
    return response.content[0].text

def main():
    print("=== CV Tailor Agent ===\n")
    
    # Example job description (paste any job description here)
    job_description = """
    AI Product Operations - Remote (Tunisia)
    
    We're looking for someone to join our AI Product Operations team.
    
    Responsibilities:
    - Own day-to-day product workflows and operational processes
    - Use AI tools to investigate product issues and generate solutions  
    - Build automated workflows to scale the team's operations
    - Coordinate between engineering, product, and client teams
    - Think like a product owner: balance user needs with technical constraints
    
    Requirements:
    - Experience with AI tools (ChatGPT, Claude, Cursor, n8n, or similar)
    - Product or operations experience
    - Technical background preferred (can read code, understand APIs)
    - Strong written communication in English
    - Based in Tunisia with reliable internet
    - High ownership mindset
    
    Nice to have:
    - Experience with automation tools (n8n, Make, Zapier)
    - Background in SaaS or tech
    """
    
    print("Analyzing your CV against the job description...\n")
    
    # Analyze the match
    analysis = analyze_cv_match(job_description, YOUR_CV)
    
    print(f"MATCH SCORE: {analysis['match_score']}/100\n")
    
    print("STRENGTHS (emphasize these):")
    for s in analysis['strengths']:
        print(f"  ✅ {s}")
    
    print("\nGAPS (address these):")
    for g in analysis['gaps']:
        print(f"  ⚠️  {g}")
    
    print("\nREWRITTEN SUMMARY:")
    print(f"  {analysis['rewritten_summary']}")
    
    print("\nSKILLS TO HIGHLIGHT:")
    for skill in analysis['skills_to_highlight']:
        print(f"  • {skill}")
    
    print("\nCOVER LETTER ANGLE:")
    print(f"  {analysis['cover_letter_angle']}")
    
    print("\nRECOMMENDED ACTIONS:")
    for action in analysis['recommended_actions']:
        print(f"  → {action}")
    
    print("\n" + "="*50)
    print("Generating tailored experience section...\n")
    tailored_experience = generate_tailored_cv_section(job_description, YOUR_CV, "experience")
    print(tailored_experience)

if __name__ == "__main__":
    main()
```

### Step 3: Test and Iterate

```bash
python main.py
```

Expected output: Analysis with score, strengths, gaps, rewritten summary, and recommendations.

**If you get an error:**
- `AuthenticationError` → Check your API key in `.env`
- `JSONDecodeError` → Claude returned non-JSON. Add `print(response.content[0].text)` to see what it returned. Usually means you need to adjust the prompt.

### Step 4: Make It Interactive

Add an interactive CLI so you can paste any job description:

```python
def main():
    print("=== CV Tailor Agent ===")
    print("Paste a job description (press Enter twice when done):\n")
    
    lines = []
    while True:
        line = input()
        if line == "" and lines and lines[-1] == "":
            break
        lines.append(line)
    
    job_description = "\n".join(lines[:-1])  # Remove trailing empty line
    
    print("\nAnalyzing...\n")
    analysis = analyze_cv_match(job_description, YOUR_CV)
    # ... rest of output
```

### Step 5: Create a Proper README

```markdown
# CV Tailor Agent

An AI agent that analyzes job descriptions and tailors your CV to match.

## What It Does
- Extracts key requirements from any job description
- Scores how well your CV matches (0-100)
- Identifies strengths to emphasize and gaps to address
- Rewrites your CV summary for the specific role
- Provides a cover letter angle

## Tech Stack
- Python 3.10+
- Anthropic Claude API (claude-opus-4-5)

## Setup
1. `pip install anthropic python-dotenv`
2. Get an API key at console.anthropic.com
3. Create `.env` with `ANTHROPIC_API_KEY=your_key`
4. Update `YOUR_CV` in `main.py` with your CV
5. Run: `python main.py`

## Example Output
[Screenshot here]

## What I Learned
- Claude Messages API and system prompts
- Structured JSON output from LLMs
- Iterative prompt engineering to get reliable outputs
```

### Step 6: Push to GitHub

```bash
git init
git add .
git commit -m "feat: CV tailor agent using Claude API"
git branch -M main
git remote add origin https://github.com/yourusername/cv-tailor-agent.git
git push -u origin main
```

## Extensions (Do After You Have the Basic Version Working)

1. **Web scraper**: Auto-scrape job URLs instead of pasting text
2. **PDF CV reader**: Upload your CV as a PDF instead of hardcoding it
3. **Multiple job comparison**: Rank 10 jobs by match score
4. **Streamlit UI**: Build a web interface so others can use it
5. **Save history**: Log all analyses to Supabase to track your applications

## Portfolio Value

When sharing this project:
- "I built an AI agent using Claude's API that analyzes job postings and tailors CVs automatically"
- "Demonstrates: prompt engineering, structured output, real-world utility"
- Share the GitHub link + a screenshot of the output

---

*Time to complete basic version: 3-4 hours | Next: [Project 2: Job Alert Automation](./02-job-alert-automation.md)*
