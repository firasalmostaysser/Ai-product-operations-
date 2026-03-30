# 10 - Automation Agent System (LinkedIn-Safe)

Goal: automate 70-80% of your job search pipeline while keeping account safety and application quality.

---

## Important first: do NOT fully auto-apply on LinkedIn

LinkedIn explicitly restricts unauthorized automation and bot-like behavior.

Risky actions:

- Automated clicks/submits through unofficial bots
- Mass auto-DMs with repetitive patterns
- Scraping through unauthorized tools

Possible consequences:

- Temporary restrictions
- Permanent account bans
- Loss of network/data access

So the smart strategy is:

> **Semi-automation**: AI does targeting, scoring, drafting, and prep.  
> You do final review + final submit.

This gives speed + quality + account safety.

---

## Architecture (practical)

### Stage 1: Lead ingestion

Sources:

- LinkedIn search (manual export/logging)
- Wellfound, Otta, RemoteOK, WeWorkRemotely, company career pages
- Referral opportunities from your network

Output:

- Rows appended to `data/job_pipeline.csv`

---

### Stage 2: AI scoring and prioritization

Script:

- `scripts/score_job_leads.py`

What it does:

- Scores each lead by role fit, remote fit, compensation clarity, and growth potential
- Adds a priority score and recommended next action

Output:

- `data/jobs_scored.csv`

---

### Stage 3: Application packet generation

Script:

- `scripts/generate_application_packets.py`

What it does:

- Takes one selected lead
- Generates:
  - tailored intro paragraph
  - evidence bullets from your profile
  - 3 custom talking points for interview

Output:

- `applications/<company>__<role>.md`

---

### Stage 4: Human review and submit

You do:

1. Edit final language for authenticity
2. Submit application manually
3. Send personalized outreach message
4. Update status in `data/job_pipeline.csv`

This is where trust is built.

---

## Why this wins

- Faster than manual process
- Higher quality than mass applications
- Safer than full bot automation
- Easier to explain in interviews ("I built a disciplined AI-assisted career ops system")

---

## Daily command sequence

```bash
python3 scripts/score_job_leads.py
python3 scripts/generate_application_packets.py --input data/jobs_scored.csv --output-dir applications --top-n 10
python3 scripts/generate_daily_brief.py
```

---

## Optional: LinkedIn profile integration

You cannot directly "link me" to your private LinkedIn account in this environment.

But you can still automate safely:

1. Export profile content manually (headline, about, experience bullets) into a markdown file.
2. Keep a local `profile/linkedin_profile_source.md` file.
3. Use AI scripts to generate optimized profile variants and outreach text.
4. Paste final updates manually into LinkedIn.

This keeps control in your hands and avoids policy violations.

---

## "Do this now" checklist

- [ ] Add 20 target roles to `data/job_pipeline.csv`
- [ ] Run lead scoring script
- [ ] Generate 5 tailored application packets
- [ ] Manually submit top 3
- [ ] Send 3 human, personalized messages
- [ ] Track response rate weekly

---

## Non-obvious thing most candidates miss

Most candidates apply and wait.

You should run a **3-layer conversion system**:

1. Application
2. Direct outreach
3. Referral path

Same job, 3 paths -> much higher interview probability.
