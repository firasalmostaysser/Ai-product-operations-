# Project 3: n8n Automation Suite

## Overview
A collection of 5 production-ready n8n workflows that solve real business problems using AI. Each workflow is exported as JSON and documented for easy import.

## What You'll Learn
- n8n workflow building (visual + code nodes)
- AI integration in automation (Claude, OpenAI nodes)
- Webhook APIs
- Error handling in automation
- Real-world automation patterns

## The 5 Workflows

### Workflow 1: AI Lead Scorer
**Trigger**: New lead added to CRM (webhook or Airtable)
**Process**: AI analyzes lead data (company, role, industry) and scores 1-100
**Output**: Updated CRM record with score + recommended actions

### Workflow 2: Content Pipeline
**Trigger**: New blog post URL submitted via webhook
**Process**: Scrape content → AI generates LinkedIn post + 3 tweets + email newsletter blurb
**Output**: Drafts saved to Google Docs, notification sent to Slack

### Workflow 3: Invoice Processor
**Trigger**: New PDF uploaded to Google Drive
**Process**: Extract text → AI identifies vendor, amount, date, line items
**Output**: Data added to Google Sheets, notification if amount > threshold

### Workflow 4: Weekly Report Generator
**Trigger**: Cron (every Monday at 8 AM)
**Process**: Pull data from APIs → AI analyzes trends → Generate markdown report
**Output**: Report saved to Notion/Google Docs, emailed to team

### Workflow 5: Customer Onboarding Automator
**Trigger**: New signup (webhook from app)
**Process**: Send welcome email → Create Slack channel → Schedule check-in → Set up tasks
**Output**: Complete onboarding sequence triggered automatically

## How to Use

### Import a Workflow
1. Open n8n (cloud or self-hosted)
2. Go to Workflows → Import from File
3. Select the JSON file from `workflows/` folder
4. Configure credentials (API keys, etc.)
5. Activate

### Folder Structure
```
workflows/
├── 01-ai-lead-scorer.json
├── 02-content-pipeline.json
├── 03-invoice-processor.json
├── 04-weekly-report-generator.json
└── 05-customer-onboarding.json
docs/
├── 01-lead-scorer-guide.md
├── 02-content-pipeline-guide.md
├── 03-invoice-processor-guide.md
├── 04-weekly-report-guide.md
└── 05-onboarding-guide.md
```

## Setup Requirements

### n8n Instance
- Cloud: n8n.io (free tier: 5 active workflows)
- Self-hosted: `docker run -d -p 5678:5678 n8nio/n8n`

### API Keys Needed
- Anthropic API key (for AI nodes)
- Google Workspace credentials (for Sheets, Drive, Gmail)
- Slack webhook URL
- Airtable API key (optional)

## What to Show in Your Portfolio
- Screenshots of each workflow in n8n
- Demo videos showing workflows in action
- Documentation explaining the business value of each
- Metrics: "This workflow saves X hours/week"
- Landing page for the suite
