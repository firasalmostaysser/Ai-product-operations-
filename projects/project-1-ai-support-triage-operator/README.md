# Project 1 - AI Support Triage Operator

## Objective

Reduce manual support triage effort and route issues to the correct owner faster.

Target outcomes:

- Decrease triage time per ticket
- Improve first-response speed
- Reduce misrouting errors

---

## Suggested Architecture

1. Inbound source (email/form/Slack)
2. Classification step (issue type + urgency)
3. Routing logic (owner/team mapping)
4. Draft response summary
5. Logging and QA table

---

## Folder Structure

```text
project-1-ai-support-triage-operator/
  README.md
  prompts/
  sample-data/
  results/
  assets/
```

---

## Build Plan (7 days)

### Day 1

- Define ticket categories and urgency levels
- Create sample ticket dataset

### Day 2

- Build first classifier prompt/template
- Test on 20 sample tickets

### Day 3

- Add routing rules (team/owner mapping)
- Add fallback for uncertain cases

### Day 4

- Add summary generation for handoff
- Add structured JSON output schema

### Day 5

- Create evaluation table (accuracy + speed)
- Fix biggest failure cases

### Day 6

- Record demo and clean README
- Add architecture diagram

### Day 7

- Publish case study + LinkedIn post
- Add project to CV and applications

---

## Minimum Demo Requirements

- Input: raw ticket text
- Output:
  - issue_type
  - urgency
  - owner/team
  - summary
  - confidence

---

## KPI Table (fill with your data)

| Metric | Before | After | Delta |
|---|---:|---:|---:|
| Avg triage time per ticket |  |  |  |
| Misroute rate |  |  |  |
| First response time |  |  |  |

---

## Next Steps

1. Create `sample-data/tickets.csv`.
2. Build classifier prompt in `prompts/classifier_prompt.md`.
3. Generate first results in `results/`.
