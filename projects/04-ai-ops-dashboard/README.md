# Project 4: AI Operations Dashboard

## Overview
A real-time dashboard for monitoring AI product operations. Shows the metrics that matter for running AI products in production.

## What You'll Learn
- Building dashboards with Next.js + shadcn/ui
- Real-time data with Supabase Realtime
- Data visualization with Recharts
- Thinking about AI product metrics
- Full-stack deployment

## Features

### Dashboard Panels

1. **Model Performance**
   - Accuracy/quality score over time
   - Latency (p50, p95, p99)
   - Error rate
   - Token usage

2. **Usage Analytics**
   - Queries per hour/day/week
   - Active users
   - Feature usage breakdown
   - Geographic distribution

3. **Cost Monitor**
   - Daily/weekly/monthly AI API costs
   - Cost per query trend
   - Budget alerts
   - Cost projections

4. **Customer Health**
   - Health scores per customer
   - Usage trends per customer
   - Churn risk indicators
   - Escalation tracker

5. **Incident Tracker**
   - Active incidents
   - Mean time to resolution
   - Incident history
   - Status page

6. **Feature Adoption**
   - New feature rollout progress
   - Adoption rate by feature
   - User feedback summary

## Tech Stack
- **Frontend**: Next.js 14, TypeScript, Tailwind CSS, shadcn/ui
- **Charts**: Recharts or Tremor
- **Backend**: Next.js API routes or FastAPI
- **Database**: Supabase
- **Real-time**: Supabase Realtime subscriptions
- **Deployment**: Vercel

## Step-by-Step Build Guide

### Step 1: Generate the UI with v0
Go to v0.dev and describe each dashboard panel. Get the components.

### Step 2: Set up the Next.js project
```bash
npx create-next-app@latest ai-ops-dashboard --typescript --tailwind --app
cd ai-ops-dashboard
npx shadcn-ui@latest init
npm install recharts @supabase/supabase-js
```

### Step 3: Create the database schema
Set up tables for metrics, incidents, customers in Supabase.

### Step 4: Build seed data generator
Create a script that generates realistic mock data.

### Step 5: Connect frontend to data
Fetch data from Supabase, display in charts.

### Step 6: Add real-time updates
Subscribe to Supabase Realtime for live metric updates.

### Step 7: Deploy
Push to GitHub, connect to Vercel, deploy.

## What to Show in Your Portfolio
- Live dashboard with realistic data
- Screenshot of each panel
- Explanation of which metrics matter and why
- "This is the dashboard I'd build for your AI product" -- killer interview line
