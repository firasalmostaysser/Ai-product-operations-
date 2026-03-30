# Project 5: GTM Intelligence Tool

## Overview
A competitive intelligence tool that tracks AI companies, monitors product launches, analyzes pricing, and generates weekly market briefs.

## What You'll Learn
- Web scraping and data collection
- AI-powered analysis and report generation
- Scheduled automation
- Market research skills
- Full-stack app development

## Features

1. **Competitor Tracker**
   - Monitor specific companies for website changes
   - Track product launches and feature updates
   - Alert on pricing changes

2. **Market Map**
   - Visual map of AI tools by category
   - Filterable and searchable
   - Regularly updated

3. **Weekly Digest**
   - AI-generated competitive intelligence report
   - Key launches, trends, and insights
   - Delivered via email or shown in dashboard

4. **Pricing Database**
   - Track pricing across AI products
   - Historical pricing data
   - Trend analysis

5. **Launch Tracker**
   - Product Hunt launches
   - Y Combinator launches
   - Major product announcements

## Tech Stack
- **Backend**: Python, FastAPI
- **Scraping**: httpx, BeautifulSoup (or Playwright for JS sites)
- **AI**: Claude API for analysis and report generation
- **Database**: Supabase
- **Frontend**: Next.js dashboard
- **Automation**: n8n or APScheduler for scheduled collection
- **Deployment**: Railway (backend) + Vercel (frontend)

## Step-by-Step Build Guide

### Step 1: Build the scraper
Start with scraping 5 AI company websites for basic info.

### Step 2: Store and compare data
Save snapshots in Supabase. Detect changes between snapshots.

### Step 3: AI analysis
Send changes to Claude for analysis and insight generation.

### Step 4: Build the report generator
Generate markdown reports from the analyzed data.

### Step 5: Build the dashboard
Display tracked companies, market map, and reports.

### Step 6: Add scheduling
Run data collection daily, reports weekly.

### Step 7: Deploy
Full deployment with automated data collection running.

## What to Show in Your Portfolio
- Live dashboard showing real market data
- Sample weekly intelligence report
- Market map visualization
- "Here's my competitive analysis of [industry segment]" -- great for GTM interviews
