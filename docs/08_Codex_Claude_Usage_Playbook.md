# 08 - Codex + Claude Usage Playbook (How to Use AI Daily)

This guide helps you use coding agents effectively for career acceleration.

---

## 1) When to use Codex/Claude

Use AI coding agents for:

- Building portfolio project scaffolds quickly
- Generating first drafts of automation scripts
- Refactoring and improving reliability
- Writing docs, README files, and case studies
- Creating test cases and debugging flows

Do **not** use them blindly for:

- Security-sensitive code without review
- Production deployment decisions without validation
- Metrics claims without real measurements

---

## 2) Prompt framework for high-quality output

Use this structure:

1. **Role**: "Act as AI Product Ops engineer"
2. **Context**: tools, constraints, business goal
3. **Task**: exact deliverable
4. **Output format**: files, sections, checklist
5. **Quality bar**: tests, logging, edge cases

Example:

```text
Act as a senior AI automation engineer.
Context: I am building an n8n workflow for support triage.
Task: Produce a Python webhook handler that classifies issue type and urgency.
Output: One file with clear functions, plus README section and sample input/output.
Quality: Include retries, error handling, and structured logs.
```

---

## 3) Daily AI collaboration loop

For each work session:

1. Define one small objective.
2. Ask agent for plan + first version.
3. Run/test locally.
4. Ask agent to improve based on concrete errors.
5. Document result in case-study format.

This loop beats long prompts with vague goals.

---

## 4) Pairing model strengths

Practical approach:

- Use one agent for fast scaffolding and bulk edits.
- Use another agent for stricter review and critique.
- Use yourself as final decision-maker.

Rule:

> AI drafts. You verify. Reality decides.

---

## 5) Prompt templates for your job goals

### Template A - Build feature

```text
Build [feature] for [project].
Business objective: [metric/outcome].
Tech stack: [stack].
Constraints: [time, dependencies, environment].
Return:
1) Implementation
2) Test plan
3) README update
4) Risks and mitigations
```

### Template B - Debug workflow

```text
Here is my error log and expected behavior.
Identify root cause, propose minimal fix, and provide patch.
Then provide one preventive guardrail and one test case.
```

### Template C - Case study writer

```text
Turn these raw notes into a concise case study:
- Problem
- Solution architecture
- Implementation
- KPI impact
- Failures and fixes
- Next iteration
```

---

## 6) Quality checklist before accepting AI output

- [ ] Does the code run?
- [ ] Are failure modes handled?
- [ ] Are metrics measurable?
- [ ] Is the README understandable to non-engineers?
- [ ] Can I explain every design choice in an interview?

If any answer is "no", iterate.

---

## 7) Build speed without losing trust

Use this sequence:

1. Fast draft
2. Functional validation
3. Reliability hardening
4. Documentation
5. Demo recording

Most candidates stop at step 1 or 2.
You win by finishing all 5.

---

## 8) Weekly Codex/Claude objectives

- Ship at least 3 AI-assisted commits
- Produce one polished case-study update
- Generate one interview story from real project work
- Save top prompts in a `prompts/` folder per project

Prompt assets are reusable career capital.
