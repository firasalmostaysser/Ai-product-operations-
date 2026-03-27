# Interview Playbook

**This is your complete guide to nailing interviews for AI Product Ops, GTM, and AI Automation roles -- including handling accent challenges.**

---

## Dealing With the Accent Barrier

You lost the Storyteller opportunity due to accent concerns. Let's fix that permanently.

### Understanding the Problem

The issue isn't your accent. It's a combination of:
1. **Clarity** -- Can they understand every word?
2. **Pacing** -- Are you speaking too fast when nervous?
3. **Vocabulary precision** -- Using the exact right words
4. **Confidence** -- Sounding certain vs uncertain

### Action Plan: Spoken English Improvement

#### Daily Practice (30 minutes minimum)

**Technique 1: Shadow Speaking**
1. Find a YouTube video of someone in your target role (AI Product Ops, GTM)
2. Play 10 seconds, pause, repeat exactly what they said
3. Match their speed, tone, and emphasis
4. Record yourself and compare
5. Do this for 15 minutes daily

**Recommended speakers to shadow:**
- Lenny Rachitsky (Product Management interviews)
- Product Hunt launch videos (AI companies)
- Y Combinator Demo Day presentations
- TED talks on AI/technology

**Technique 2: Record & Review**
1. Record yourself answering interview questions (use your phone)
2. Listen back. Identify:
   - Words that aren't clear
   - Sentences that are too fast
   - Filler words (um, uh, like, you know)
3. Re-record until clean
4. Do 3 questions per day

**Technique 3: Pronunciation Drills**
Common words you'll say in interviews that need to be crystal clear:
- "Automation" (aw-toh-MAY-shun)
- "Scalable" (SKAY-luh-bul)
- "Implementation" (im-pleh-men-TAY-shun)
- "Architecture" (AR-kih-tek-chur)
- "Infrastructure" (IN-fruh-struk-chur)
- "Analytics" (an-uh-LIT-iks)
- "Stakeholder" (STAYK-hol-der)
- "Prioritize" (pry-OR-ih-tyze)
- "Orchestration" (or-kess-TRAY-shun)
- "Pipeline" (PIPE-lyne)

**Technique 4: AI-Powered Practice**
Use ChatGPT or Claude with voice mode:
1. "Act as an interviewer for an AI Product Operations role. Ask me questions one at a time. After each answer, rate my clarity and suggest improvements."
2. Practice 20 minutes daily with voice
3. This is free and available 24/7

**Technique 5: Speaking Pace Control**
- Normal conversation: 120-150 words per minute
- Interview optimal: 110-130 words per minute (slightly slower)
- When nervous, you speed up. Consciously slow down.
- Pause between sentences. Pauses show confidence, not uncertainty.

#### Weekly Practice

- **Language exchange**: Find an English speaker learning Arabic/French (HelloTalk, Tandem apps)
- **Mock interviews**: Practice with AI, then with real people
- **Read aloud**: Read AI articles out loud for 10 minutes (improves fluency)

#### Tools

| Tool | Purpose | Cost |
|------|---------|------|
| Elsa Speak | Pronunciation coaching AI | Free / $12/mo |
| Speeko | Public speaking coaching | Free / $8/mo |
| ChatGPT Voice | Conversation practice | Free with Plus |
| Otter.ai | Record and transcribe your calls | Free tier |
| HelloTalk | Language exchange partners | Free |

---

## The Interview Framework

### Before the Interview

**Research checklist (do ALL of these):**
- [ ] Company website -- understand the product deeply
- [ ] Recent blog posts -- know what they're working on
- [ ] LinkedIn profiles of interviewers -- find common ground
- [ ] Glassdoor reviews -- know the culture
- [ ] Product Hunt -- read user reviews
- [ ] Twitter -- what are employees posting about?
- [ ] Competitors -- know the competitive landscape

**Technical setup:**
- [ ] Good internet connection (test before)
- [ ] Quiet room, clean background
- [ ] Good lighting (face a window, not away from it)
- [ ] Headset with clear microphone
- [ ] Backup plan if internet fails (phone hotspot)
- [ ] Water nearby
- [ ] Notes (but don't read from them)

### The Interview Itself

**Opening (first 2 minutes) -- CRITICAL**

The first impression sets the tone. Prepare this:

"Hi [Name], great to meet you. I'm Firas, based in Tunis. Quick context -- I spent three years as a backend engineer building real-time systems, then moved to Product Owner where I fell in love with the intersection of product and operations. Now I'm focused on AI automation and product operations. I'm excited about [Company] because [specific reason related to their product]."

**Practice this until it's smooth and natural.**

**Framework for Answering Questions: STAR-AI**

A modified STAR method for AI roles:

- **S**ituation: Set the context briefly
- **T**ask: What was the challenge?
- **A**ction: What did you do? (Emphasize AI tools used)
- **R**esult: What was the outcome? (Use numbers)
- **AI**: How would you do it better/faster with AI today?

**Example:**

Q: "Tell me about a time you improved a process."

A: "At Softylines, our client onboarding took 3 weeks because everything was manual -- data entry, configuration, documentation. **(Situation)**

I was tasked with reducing onboarding time while maintaining quality. **(Task)**

I mapped the entire process, identified repetitive steps, and automated document generation and basic configuration. I also created templates for the custom parts. **(Action)**

We reduced onboarding from 3 weeks to 8 days, and client satisfaction improved because they got value faster. **(Result)**

If I were doing this today, I'd use AI to auto-generate configurations based on client requirements, use n8n to automate the entire workflow, and use Claude to generate personalized onboarding documentation. I could probably get it down to 2-3 days. **(AI)**"

---

## Common Interview Questions & Answers

### For AI Product Operations Roles

**Q1: "What does AI Product Operations mean to you?"**

"AI Product Ops is the bridge between product vision and daily execution. It's about owning the workflows that keep an AI product running smoothly -- monitoring quality, investigating issues, coordinating between engineering and customers, and constantly automating processes to scale operations. The 'AI' part means I use AI tools not just in the product but in how I do my job -- automating reporting, using AI for issue investigation, building workflows that would be impossible manually."

**Q2: "How would you handle a situation where the AI model quality drops?"**

"First, detect and scope the issue. What percentage of outputs are affected? Which input types? Since when? Then investigate -- was there a model update, data change, or load issue? Communicate immediately: engineering gets the technical details, product gets the user impact, and customer-facing teams get what to tell customers. Then either roll back or fix, depending on severity. After resolution, I'd do a post-mortem to prevent recurrence and set up monitoring to catch similar issues faster next time."

**Q3: "Tell us about your experience with AI tools."**

"I use AI tools every day, both for building and for operations. Cursor AI is my primary development environment -- I use agent mode for complex refactoring and multi-file changes. I build automation workflows with n8n that integrate AI for classification, summarization, and content generation. I've built AI-powered tools like a notary automation system that reduced contract processing from 2 hours to 10 minutes using OCR and Claude. I also use Claude Code for autonomous code generation and Bolt.new for rapid prototyping. I'm not just a user -- I understand how these tools work under the hood, including concepts like RAG, embeddings, and tool-use."

**Q4: "How do you prioritize when everything is urgent?"**

"I use a combination of impact and effort analysis. First, classify by actual urgency -- is this causing revenue loss right now, or does it feel urgent? I use a modified RICE framework: reach (how many users affected), impact (severity), confidence (how sure am I about the fix), and effort. P1 issues (product down, revenue impact) get dropped everything. For everything else, I communicate realistic timelines and negotiate scope. The key is being transparent about tradeoffs -- 'I can ship A today or A+B by Thursday. Which do you prefer?'"

**Q5: "Why are you interested in this role specifically?"**

**Template (customize for each company):**
"Three reasons. First, your product is solving [specific problem] which I've personally experienced as a [relevant context]. Second, the role combines product thinking with AI tools, which is exactly where my skills intersect -- I've been a Product Owner and I'm deeply into AI automation. Third, [something specific about the company culture, team, or mission]. I'm not applying to dozens of jobs. I'm selective about where my combination of technical background, product experience, and AI obsession can create the most value."

### For GTM / BDR / Solutions Engineer Roles

**Q6: "How would you explain [AI product] to a non-technical buyer?"**

"I'd start with their problem, not our technology. Something like: 'You know how your team spends X hours every week doing [manual task]? Our product automates that using AI, so your team can focus on [high-value work] instead. Companies like [customer example] saw [specific result] after implementing it. The setup takes [timeframe], and you'd start seeing results in [timeframe].' I never lead with technology. I lead with pain and outcomes."

**Q7: "What's your approach to outbound outreach?"**

"Research first, always. I spend 10 minutes understanding each prospect before I reach out. I look at their company, their role, recent activity, and identify a specific pain point I can address. My outreach is always: [specific observation about them] + [how our product helps with that specific thing] + [low-commitment ask]. I learned this approach doing 40+ discovery calls for my jewelry platform -- the best conversations happened when I showed I understood their world before asking for anything."

---

## Questions to Ask THEM

Always ask questions. It shows you're evaluating them too.

### High-Impact Questions

1. "What does the first 30 days look like for this role? What's the first thing I'd work on?"
2. "What's the biggest operational challenge the team faces right now?"
3. "How does this role interact with engineering and product teams?"
4. "What tools does the team currently use for [automation/monitoring/communication]?"
5. "What would make someone wildly successful in this role?"
6. "How does the team stay current with new AI developments?"
7. "What's the team culture around trying new AI tools and approaches?"

### Questions That Show Depth

1. "How do you measure AI model quality in production?"
2. "What's your current incident response process?"
3. "How do you handle the tradeoff between model accuracy and latency?"
4. "What's the biggest gap in your current automation stack?"

---

## Take-Home Task Strategy

Many AI roles include a take-home task. Here's how to crush it:

### Process

1. **Read the brief 3 times.** Highlight every requirement.
2. **Plan before you build.** Write a 5-line plan. Don't start coding immediately.
3. **Use AI strategically.** Cursor for code, Claude for thinking, v0 for UI.
4. **Over-communicate.** Add a document explaining your approach, tradeoffs, and what you'd do with more time.
5. **Ship quality.** Clean code, clear README, deployed demo.
6. **Show AI usage.** They want to see you leveraging AI tools. Don't hide it.

### Common Task Types

| Task Type | What They're Evaluating | How to Excel |
|-----------|------------------------|-------------|
| Build a workflow | Can you ship? Tool proficiency | Working demo + documentation |
| Write a product brief | Product thinking, communication | Structure, data, clear recommendations |
| Analyze data | Analytical skills, AI usage | Insights, not just charts. Use AI to analyze. |
| Debug a system | Investigation skills | Systematic approach, root cause analysis |
| Design a process | Operational thinking | Scalability, automation opportunities |

---

## Post-Interview Follow-Up

Send within 2 hours:

```
Subject: Thank you - [Role Name] interview

Hi [Name],

Thank you for the conversation today. I enjoyed learning about 
[specific thing discussed].

[1-2 sentences referencing something specific from the interview 
that shows you were listening and engaged]

I'm excited about the opportunity to [specific contribution you'd make].
Looking forward to next steps.

Best,
Firas
```

---

## Mindset

### On Rejection

Every rejection is data. Ask:
- "Thank you for letting me know. Could you share what the deciding factor was? I'm actively working on becoming the strongest candidate for roles like this, and your feedback would be incredibly valuable."

Most companies won't answer. Some will. Even one piece of feedback is gold.

### On the Accent

Your accent is part of your identity. You're trilingual. Most people interviewing you speak one language. The goal isn't to eliminate your accent -- it's to be clear and confident. Many successful leaders in tech have accents. Focus on **clarity**, not **perfection**.

### On Comparing Yourself

The job market is tough everywhere. You have an engineering degree, product experience, AI skills, and you're hustling. That combination is rare. It might take 20 applications to get 5 interviews to get 1 offer. That's normal. Keep building, keep applying, keep improving.
