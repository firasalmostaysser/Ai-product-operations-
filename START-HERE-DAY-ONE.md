# Start Here: Day One Action Plan

You just got this repository. You feel overwhelmed. Here's exactly what to do today.

**Do NOT read everything at once. Do this, in this order.**

---

## Next 2 Hours: Get Your Tools Working

### Step 1: Get Your Anthropic API Key (10 min)
1. Go to [console.anthropic.com](https://console.anthropic.com)
2. Sign up (free $5 credit on signup — enough for 100+ experiments)
3. Go to API Keys → Create Key
4. Copy and save it somewhere safe

### Step 2: Install Cursor IDE (10 min)
1. Go to [cursor.com](https://cursor.com)
2. Download and install
3. Sign up for free (includes 2-week Pro trial)
4. Open it, go to Settings → Models → make sure "claude-opus-4-5" is available

### Step 3: Run Your First Claude API Call (15 min)

Create a folder, open it in Cursor, and create these files:

`requirements.txt`:
```
anthropic
python-dotenv
```

`.env`:
```
ANTHROPIC_API_KEY=paste_your_key_here
```

`hello.py`:
```python
import anthropic
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-opus-4-5",
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": "I am Firas, a software engineer from Tunisia learning AI. In 3 sentences, tell me the most important thing I should know to get started building AI agents."
        }
    ]
)

print(response.content[0].text)
```

In terminal:
```bash
pip install -r requirements.txt
python hello.py
```

If you see Claude's answer in your terminal — **you just called the most powerful AI model in the world from your own code.** That's the foundation of everything.

### Step 4: Install n8n (15 min)

```bash
# Make sure Docker is installed first (docker.com/get-started)
docker run -it --rm -p 5678:5678 -v ~/.n8n:/home/node/.n8n n8nio/n8n
```

Open `http://localhost:5678` in your browser. Create your account.

You now have n8n running locally.

---

## Next 3 Hours: Build Something Real

### Build Project 1: CV Tailor Agent

Open [`/projects/01-cv-tailor-agent.md`](./projects/01-cv-tailor-agent.md) and follow the instructions.

**By the end of this:** You have a working AI agent that takes job descriptions and rewrites your CV sections. You can put it on GitHub. You have your first portfolio project.

---

## End of Day Actions (30 min)

1. **Push your first project to GitHub**
   ```bash
   git init
   git add .
   git commit -m "feat: first AI project - CV tailor agent"
   # Create a repo on github.com, then:
   git remote add origin https://github.com/yourusername/cv-tailor-agent.git
   git push -u origin main
   ```

2. **Write your first daily log**
   - Open `/daily-log/2026-03-27.md` (already created for you as a template)
   - Duplicate it for today's date if different
   - Fill it in honestly

3. **Practice your 2-minute introduction out loud**
   - Use the template in `/interview-prep/accent-and-communication.md`
   - Record yourself once on your phone
   - Don't listen back yet (do that tomorrow)

---

## This Week's Goals (7 Days)

| Day | Goal |
|-----|------|
| Day 1 (today) | Tools set up + Project 1 complete |
| Day 2 | Set up n8n fully + first n8n workflow (webhook → Claude → print response) |
| Day 3 | Build Project 2 (Job Alert Automation in n8n) |
| Day 4 | Build Project 3 (AI Meeting Notes) |
| Day 5 | Polish all 3 projects + write READMEs |
| Day 6 | Push everything to GitHub + update LinkedIn profile |
| Day 7 | Write your first LinkedIn post about what you built |

---

## The One Rule

**Every day: build something AND write a log entry.**

Not every day will be a breakthrough. Some days you'll spend 3 hours debugging one node in n8n. That's normal. Log it. The compound effect of consistent daily action is the entire strategy.

In 30 days: you'll have 10+ projects and a completely different sense of yourself.
In 60 days: you'll be applying to jobs from a position of strength.
In 90 days: you'll likely have income from this.

---

## If You Get Stuck

1. **Check the relevant course file** in `/courses/`
2. **Ask Claude Code** — `claude` in your terminal, describe your problem
3. **Search n8n community** — [community.n8n.io](https://community.n8n.io) has answers to almost everything
4. **Ask on Reddit** — r/n8n, r/LangChain, r/AIAgents are all active and helpful
5. **Google the error message** — almost every error has been seen before

Getting unstuck is a skill. The fact that you got stuck on something technical and figured it out is itself a story to tell in interviews.

---

## When You Feel Like Giving Up

Read this:

You got to an interview at Storyteller — a company that hires selectively and pays market rates. They liked your CV. They saw your potential. You made it further than most applicants.

One thing held you back: a skill you hadn't yet invested in (spoken English clarity). 

You are not hopeless. You are someone who got close and now has a specific, solvable problem to fix.

Every expert was once a beginner. Every person doing AI automation for a living had a day where they didn't know what n8n was. That's not the difference between you and them — the only difference is how many hours of deliberate practice they've accumulated.

You're starting that accumulation today.

Let's go.

---

*Next read: [Roadmap Overview →](./roadmap/00-overview.md)*
