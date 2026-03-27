# AI Career Operating System (Firas)

This repository is your **full training and execution system** to become job-ready for:

- AI Product Operations
- GTM / Revenue Operations with AI
- AI Automation Builder / Agent Builder

You are not starting from zero.  
You already have strong product, technical, and automation foundations.  
Now we turn them into a clear, repeatable system that gets interviews, projects, and income.

---

## Start Here (in order)

1. `docs/01_Mindset_And_Positioning.md`
2. `docs/02_180_Day_Roadmap.md`
3. `docs/03_Daily_System.md`
4. `docs/04_AI_Agents_MCP_Bootcamp.md`
5. `docs/05_Portfolio_Blueprints.md`
6. `docs/06_Job_Search_OS_Tunisia_and_Remote.md`
7. `docs/07_Interview_and_English_Accent_Playbook.md`
8. `docs/08_Codex_Claude_Usage_Playbook.md`
9. `docs/09_Global_Demand_and_Compensation.md`
10. `docs/10_Automation_Agent_System_LinkedIn_Safe.md`

Then use:

- `templates/daily_log_template.md` every day
- `templates/weekly_review_template.md` every week
- `templates/project_case_study_template.md` for each project
- `templates/interview_answer_bank_template.md` for interview prep
- `data/job_pipeline.csv` for job applications and follow-ups
- `data/skills_matrix.csv` to track technical growth
- `data/jobs_leads_example.csv` for lead scoring script input
- `data/application_packet_template.md` for CV/intro generation
- `scripts/generate_daily_brief.py` for daily market updates
- `scripts/score_job_leads.py` to rank leads by fit and expected pay
- `scripts/generate_application_packets.py` to draft tailored application packets

---

## Quick Daily Command

Generate a fresh AI tools and market brief:

```bash
python3 scripts/generate_daily_brief.py
```

This creates:

- `daily-updates/YYYY-MM-DD.md`
- `daily-updates/latest.md`

---

## Application Automation Commands (LinkedIn-safe)

1) Score leads (from your CSV):

```bash
python3 scripts/score_job_leads.py --input data/jobs_leads_example.csv --output data/jobs_scored.csv
```

2) Generate tailored application packets:

```bash
python3 scripts/generate_application_packets.py --input data/jobs_scored.csv --output-dir applications --top-n 10
```

Each packet includes:

- Custom intro paragraph
- Role-fit bullet points
- Interview talking points
- Tailored follow-up message

Use these drafts to apply manually (or with official APIs/tools). This keeps your account safe.

---

## What "Winning" Looks Like

By following this system, your target outcomes are:

- 3 strong portfolio projects that prove business impact
- 100+ high-quality applications with custom positioning
- 40+ targeted networking messages
- 15+ interviews
- 1+ paid role or freelance retainer in AI Ops / GTM / Automation

---

## Your Career Narrative (Core Positioning)

Use this identity everywhere (CV, LinkedIn, interviews):

> "I am a technical product operator who builds AI-powered workflows that reduce manual work, improve execution speed, and help teams ship and sell faster."

---

## Tooling Stack You Will Master

- Codex + Claude Code (build fast with quality)
- n8n / Make / Zapier (automation orchestration)
- Python + APIs + webhooks
- Prompt engineering and evaluation
- AI agent frameworks + MCP fundamentals
- Product metrics, GTM metrics, and operational dashboards

---

## Automation Included

This repo includes a GitHub Action:

- `.github/workflows/daily-ai-brief.yml`

It can generate and commit daily brief updates automatically.

---

## Important

You are not late.  
You are in the exact phase where focused execution compounds fast.

Use this repo daily for 90+ days without breaks.  
Consistency will beat talent + luck.