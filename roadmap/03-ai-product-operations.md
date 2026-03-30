# Phase 3: AI Product Operations (Days 29-42)

**Goal**: Learn exactly what AI Product Ops roles require and build the frameworks, vocabulary, and instincts to excel in them.

---

## What AI Product Operations Actually Looks Like

### A Day in the Life

```
09:00  Check overnight alerts -- any AI model degradation? Customer issues?
09:30  Standup with engineering -- what shipped, what's blocked?
10:00  Review customer feedback queue -- categorize, prioritize, route
10:30  Investigate a production issue: model quality dropped for a specific use case
11:30  Build a workflow to automate the feedback categorization (AI + n8n)
12:00  Lunch
13:00  Client onboarding call -- configure AI product for new customer
14:00  Create internal documentation for new feature rollout
15:00  Analyze usage metrics -- which features are adopted, which aren't?
15:30  Write a brief for engineering: "Users are requesting X, here's the data"
16:00  Update project tracker, sync with PM on priorities
16:30  Test new AI model version against current benchmarks
17:00  End-of-day sync, plan tomorrow
```

### Core Responsibilities

1. **Workflow Management**: Own and improve the processes that keep AI products running
2. **Issue Investigation**: When something breaks, figure out why and fix it
3. **Client Configuration**: Set up AI products for specific customer needs
4. **Cross-Functional Coordination**: Bridge engineering, product, sales, and support
5. **AI-Powered Automation**: Use AI to make internal operations more efficient
6. **Quality Monitoring**: Track AI model performance and flag regressions
7. **Documentation**: Keep everything documented so the team can scale

---

## The Skills You Need

### Skill 1: Product Thinking

**What it is**: Ability to think about user needs, business goals, and technical constraints simultaneously.

**Framework: The Product Ops Triangle**

```
           USER NEEDS
              /\
             /  \
            /    \
           /      \
          /  SHIP  \
         /   IT    \
        /____________\
  TECHNICAL        BUSINESS
  CONSTRAINTS      GOALS
```

Every decision you make balances these three forces.

**Practice exercises:**

1. Pick any AI product (Claude, Cursor, n8n). Write a 1-page analysis:
   - Who are the users? What do they need?
   - What are the technical constraints?
   - What are the business goals?
   - What would you ship next and why?

2. Take a customer complaint and turn it into a product brief:
   - What's the actual problem?
   - Who's affected?
   - What's the impact?
   - Proposed solution?
   - How do we validate it worked?

### Skill 2: Metrics & Analytics

**Key metrics for AI products:**

| Metric | What It Measures | Why It Matters |
|--------|-----------------|----------------|
| Task Success Rate | % of tasks AI completes correctly | Core quality metric |
| Response Latency | Time to generate response | User experience |
| Token Usage | Tokens consumed per request | Cost control |
| User Retention | % of users who come back | Product-market fit |
| Feature Adoption | % of users using new features | Launch effectiveness |
| Error Rate | % of requests that fail | Reliability |
| CSAT/NPS | Customer satisfaction | Overall happiness |
| Cost per Query | $ per AI interaction | Unit economics |
| Time to Value | Time from signup to first success | Onboarding quality |

**Practice:**

1. Set up a simple dashboard (use v0 or Cursor) that tracks these metrics with mock data
2. Write a weekly ops report analyzing trends
3. Create alerts for when metrics go out of bounds

### Skill 3: Incident Management

When an AI product breaks, you need a systematic approach:

**DIARI Framework (memorize this):**

1. **D**etect: Notice the problem (monitoring, alerts, customer reports)
2. **I**nvestigate: What changed? What's the scope? Who's affected?
3. **A**ct: Fix it or mitigate it
4. **R**eport: Communicate to stakeholders (internal + external)
5. **I**mprove: Post-mortem, prevent recurrence

**Common AI product issues:**

- Model quality degradation after update
- Increased latency due to load
- Incorrect outputs for specific input patterns
- Integration failures with customer systems
- Cost spikes from unexpected usage patterns

### Skill 4: Process Design

AI Product Ops is about building processes that scale. Learn these:

**Customer Onboarding Process:**
```
1. Discovery call → Understand needs
2. Configuration plan → Document what to set up
3. Environment setup → Create account, configure AI
4. Integration → Connect to customer systems
5. Testing → Validate everything works
6. Training → Show customer how to use it
7. Go-live → Launch with monitoring
8. Follow-up → Check in after 1 week, 1 month
```

**Feature Rollout Process:**
```
1. Internal testing → Team uses it first
2. Beta group → Select customers test it
3. Feedback collection → Gather and categorize feedback
4. Fix critical issues → Address blockers
5. Documentation → Create user guides
6. General availability → Roll out to all customers
7. Adoption tracking → Monitor usage
8. Iteration → Improve based on data
```

**Bug/Issue Triage Process:**
```
Priority 1 (P1): Product down, revenue impact → Fix immediately
Priority 2 (P2): Major feature broken, workaround exists → Fix today
Priority 3 (P3): Minor issue, no workaround → Fix this week
Priority 4 (P4): Cosmetic/nice-to-have → Backlog
```

### Skill 5: Stakeholder Communication

**The 4-Audience Framework** (different messages for different people):

| Audience | They Care About | Communication Style |
|----------|----------------|-------------------|
| Engineering | Technical details, root cause, fix | Specific, data-driven, async |
| Product | User impact, roadmap implications | Strategic, user-centric |
| Sales/CS | Customer impact, timeline to fix | Empathetic, action-oriented |
| Leadership | Business impact, risk, resources | Executive summary, metrics |

**Example: Model quality dropped**

To Engineering: "Claude-based classification is returning incorrect categories for 15% of inputs since the v2.1 model update at 14:00 UTC. Error pattern: misclassifying sports content as entertainment. I've isolated test cases in ticket #1234."

To Product: "Our content classification accuracy dropped from 95% to 80% after today's model update. ~200 customers are affected. This impacts the auto-tagging feature. Engineering is investigating; I recommend we roll back while we fix."

To Sales: "Some customers may notice incorrect content categories today. We're aware and fixing it. ETA: 4 hours. If any customer escalates, loop me in directly."

To Leadership: "Production issue: 15% accuracy drop in content classification affecting ~200 customers. Root cause: model update. Rollback in progress, full fix ETA 4 hours. No revenue impact expected if resolved on time."

---

## AI Product Ops Frameworks to Study

### 1. RICE Prioritization

For deciding what to work on:
- **R**each: How many users does this affect?
- **I**mpact: How much does it improve things? (3=massive, 2=high, 1=medium, 0.5=low)
- **C**onfidence: How sure are you about the estimates? (100%, 80%, 50%)
- **E**ffort: Person-months to complete

**Score = (Reach x Impact x Confidence) / Effort**

### 2. Jobs To Be Done (JTBD)

Understanding what users actually need:
"When [situation], I want to [motivation], so I can [expected outcome]."

Example: "When I receive a customer complaint about AI quality, I want to quickly identify what went wrong, so I can fix it before more customers are affected."

### 3. OKRs (Objectives and Key Results)

How AI Product Ops teams set goals:

**Objective**: Improve AI product reliability
- KR1: Reduce P1 incidents from 4/month to 1/month
- KR2: Decrease mean time to resolution from 4 hours to 1 hour  
- KR3: Achieve 99.5% model uptime (currently 98.2%)

**Objective**: Accelerate client onboarding
- KR1: Reduce time-to-value from 14 days to 5 days
- KR2: Achieve 90% client satisfaction score at 30-day check-in
- KR3: Automate 60% of configuration steps (currently 20%)

---

## Practical Exercises

### Exercise 1: Mock Incident Response (2 hours)

**Scenario**: Your AI chatbot product started giving inaccurate answers about pricing to customers 2 hours ago. Customer support has received 15 tickets.

Write:
1. An investigation plan (what you'd check first)
2. A stakeholder update for each audience
3. A post-mortem document with root cause analysis and prevention measures

### Exercise 2: Onboarding Process Design (3 hours)

Design a complete customer onboarding process for an AI content generation tool:
1. Map out every step from first contact to fully active
2. Identify which steps can be automated with AI
3. Create templates for each communication touchpoint
4. Design a success metric dashboard

### Exercise 3: Weekly Ops Report (1 hour)

Write a weekly operations report using this template:
```
# Week of [Date] - AI Product Operations Report

## Key Metrics
- Task Success Rate: X% (▲▼ from last week)
- Response Latency: Xms (▲▼)
- Active Users: X (▲▼)
- Customer Issues: X new, X resolved, X open

## Highlights
- [What went well]

## Issues & Actions
- [What broke and what we did about it]

## Next Week Focus
- [Priorities]
```

### Exercise 4: Product Brief (2 hours)

Write a product brief for a feature you'd add to any AI product you use. Include:
1. Problem statement (with data if possible)
2. Proposed solution
3. Success metrics
4. Risks and mitigations
5. Timeline and effort estimate

---

## Books & Resources for AI Product Ops

1. **"Inspired" by Marty Cagan** -- Product management bible
2. **"The Lean Product Playbook" by Dan Olsen** -- Systematic product development
3. **"Continuous Discovery Habits" by Teresa Torres** -- Customer research
4. **"Measure What Matters" by John Doerr** -- OKRs
5. **"The AI Product Manager's Handbook"** -- Specific to AI products

### Online Resources
- Lenny's Newsletter (lennysnewsletter.com) -- Product management insights
- Reforge -- Growth and product courses
- ProductHunt -- See what AI products are launching daily
- AI Product Institute -- AI-specific product management

---

## Phase 3 Checklist

- [ ] Can explain what AI Product Ops does in 30 seconds
- [ ] Know the key metrics for AI products
- [ ] Can write stakeholder communications for 4 different audiences
- [ ] Have designed at least 2 operational processes
- [ ] Have written a mock incident post-mortem
- [ ] Understand RICE, JTBD, and OKR frameworks
- [ ] Have a portfolio of written exercises (brief, report, post-mortem)

---

**Next: `04-ai-automation-builders.md` -- Where you start making money.**
