# Mock Interview Questions & Model Answers

## How to Use This

1. Read a question
2. Close this file
3. Answer out loud (record yourself)
4. Come back and read the model answer
5. Compare — what did you miss? What was different?
6. Practice until your answer is as good or better

Do 3-5 questions per day.

---

## Section 1: The Introduction

### "Tell me about yourself"

**Model Answer (adapt with your actual details):**

> "I'm Firas, based in Tunis, Tunisia. My background combines software engineering and product management — I started as a backend engineer building real-time systems, then transitioned to Product Owner where I led delivery of an enterprise SaaS for 18 months. 
>
> About a year ago I became deeply focused on AI automation. I've been building workflows using n8n and Claude that automate operational work — things like document processing, client onboarding, and reporting. My most concrete example: I automated a legal document workflow that reduced processing time from 2 hours to 10 minutes.
>
> I'm looking for a remote AI Product Operations role where I can combine my product background and AI skills to build real operational leverage. The combination of technical depth and product thinking seems to be what companies need most right now."

**Length:** 2-3 minutes. Practice until it takes exactly that long.

---

## Section 2: AI & Technical Questions

### "What AI tools do you use in your work?"

**Model Answer:**

> "Day-to-day, I primarily use three things. First, Cursor IDE for development — it has deep AI integration that speeds up building considerably. Second, n8n for workflow automation — I build most of my automation projects visually there and extend with code where needed. Third, the Claude and OpenAI APIs directly for building custom AI logic.
>
> For specific projects, I've used Claude's tool calling API to build agents, pgvector in Supabase for RAG pipelines, and I'm currently learning LangChain for more complex agent workflows.
>
> I also try to stay current — I read The Rundown AI newsletter daily and follow what's being built in the n8n and AI agent communities."

---

### "Explain what a RAG system is to a non-technical person"

**Model Answer:**

> "Great question. Imagine you have a very smart assistant, but they only know what they learned in school years ago — nothing current, nothing specific to your company.
>
> RAG — Retrieval-Augmented Generation — solves that. Before answering your question, the assistant first searches through a library of documents you've given them — your company's manuals, your meeting notes, your product documentation. They find the relevant parts, read them, and then answer your question using both their training AND your current documents.
>
> So it's like giving your AI assistant a search engine over your specific knowledge. The result is an AI that knows your business, your products, and your current state — not just general knowledge."

---

### "How would you evaluate if an AI feature is working well?"

**Model Answer:**

> "I think about three dimensions. First: quality — are the outputs actually correct and useful? I'd build a test set of representative inputs with known good outputs, then score each version of the model or prompt against it. Maybe 50-100 test cases.
>
> Second: reliability — how often does it fail or produce garbage? I'd track error rates over time, especially edge cases.
>
> Third: cost and performance — how much does each API call cost and how long does it take? These constrain what's feasible at scale.
>
> Then there's user satisfaction, which I'd measure through qualitative feedback and, if possible, behavioral metrics — like, are users actually acting on the AI's suggestions or ignoring them?
>
> I'd set up something like Langfuse to trace every AI call so I can see the full picture of inputs, outputs, latency, and cost. That observability is essential for iterating intelligently."

---

### "What's the difference between an AI chatbot and an AI agent?"

**Model Answer:**

> "A chatbot is reactive — it responds to what you say. You ask, it answers. The conversation is the extent of its capabilities.
>
> An agent is proactive and goal-oriented. You give it a goal, and it figures out the steps to achieve it — autonomously. It can use tools: search the web, read files, call APIs, write code, run it. It loops: 'reason, act, observe the result, reason again' until the goal is achieved.
>
> For example: if you asked a chatbot 'What are the top AI tools this week?' it would give you training data from months ago. If you asked an agent the same question, it would search Google, visit the relevant pages, synthesize the information, and give you a current answer — all automatically.
>
> The agent can take actions in the world. The chatbot can only talk."

---

## Section 3: Product Operations Questions

### "Describe a workflow you've owned end-to-end"

**Model Answer (using your real experience):**

> "A good example is the notary document processing workflow I built. The problem was this: legal secretaries were manually transcribing information from handwritten contracts into digital templates. It took about 2 hours per contract and was error-prone.
>
> I owned this from discovery to deployment. First I spent time with the secretaries understanding the exact steps — what information they extracted, where they put it, what edge cases existed. Then I designed a three-step automation: OCR to extract text from the scanned document, Claude to parse the legal structure and map fields to the template, and n8n to format and save the final document.
>
> The hard part was the prompt engineering — handwriting is inconsistent, so I needed Claude to handle variations gracefully. I tested with 20 sample contracts, iterated on the prompt until accuracy was consistently above 95%, then rolled it out.
>
> Result: 2 hours reduced to 10 minutes per contract. 11x improvement. The secretaries now use it for every contract."

---

### "How do you handle a situation where an AI system is producing wrong outputs and affecting clients?"

**Model Answer:**

> "First, containment: stop the bleeding. If it's critical, disable the AI output and fall back to the manual process — even if it's slower, accuracy matters more.
>
> Then investigation: look at the logs. What specific inputs caused the bad outputs? Was it a certain type of input, a model update, a prompt change? I'd use something like Langfuse to trace the exact calls.
>
> Then root cause: is it a prompt issue — the instructions weren't clear enough for this edge case? A model issue — did the underlying model change? An input issue — is the data coming in differently than expected?
>
> Then fix: update the prompt, add input validation, or escalate to the model provider if it's their issue.
>
> Then communication: be honest with the affected clients. Tell them what happened, what you found, what you fixed, and what safeguards you added. Don't hide it — the trust damage from hiding is worse than the original issue.
>
> Finally, process improvement: add the failing inputs to your test suite so it never breaks the same way again."

---

### "What would you do in your first 30 days in this role?"

**Model Answer:**

> "I'd break it into three tracks running in parallel.
>
> First: learn the product deeply. I'd use it as a power user, read every piece of documentation, talk to the people who built it, and ideally talk to 2-3 clients to understand what they actually care about.
>
> Second: understand the operations. What are the recurring workflows? What's manual that could be automated? Where do things break? I'd shadow the team for the first two weeks rather than trying to immediately improve things.
>
> Third: deliver something concrete. Even if small. I'd identify one operational bottleneck I can automate within two weeks and build it. Not to be impressive — to learn the actual system, to prove I can execute, and to start building trust with the team.
>
> By day 30, I want to have a clear answer to: 'Where are the biggest leverage points for AI automation in this operation?'"

---

## Section 4: Behavioral Questions

### "Why do you want to work in AI specifically?"

**Model Answer:**

> "Honestly — I've been using AI tools to build things for the past year, and the productivity difference is not incremental, it's categorical. I built tools in 3-5 days that would have taken months before. The notary automation, for example — two years ago that was a multi-month project. I built it in a week.
>
> That experience made me want to go deeper. I want to understand how these systems really work, how to build them reliably, how to use them to create real operational leverage for organizations. And I think the next 5 years are a defining period for this technology — I want to be building fluency now, not catching up later.
>
> It's not about chasing a trend. I've already been using these tools to solve real problems. This is me going all-in on the thing that I've seen work."

---

### "You're in Tunisia — how does remote work with a team in the UK/Europe?"

**Model Answer:**

> "Honestly, Tunisia is ideal for UK-aligned companies. My timezone is UTC+1, which means I have full overlap with UK business hours and significant overlap with Central European time.
>
> In practice, I've worked with international clients and remote teams for years — at Softylines we had clients across North Africa and Europe, and I coordinated with them entirely remotely. I've gotten very good at async communication: clear documentation, proactive updates, being explicit about what I've done and what I need.
>
> The infrastructure side is solid — I have fiber internet, a professional home setup, and reliable backup options. And there's a benefit you might not have considered: being in North Africa means I can also serve MENA-region clients who speak Arabic or French, which expands your reach if that's ever useful."

---

### "Tell me about a time you had to learn something completely new very quickly"

**Model Answer:**

> "When I transitioned from backend engineer to Product Owner at Softylines, I had essentially no formal product management training. I'd been writing code for almost 2 years and suddenly I was responsible for stakeholder management, sprint planning, backlog prioritization, and client relationships simultaneously.
>
> My approach: I didn't pretend to know what I didn't know. I told my manager in my first week: 'I know what good software looks like, but I'm learning the product side.' Then I immersed myself — read Marty Cagan's 'Inspired' in a week, sat in on every client call for the first month even if I wasn't needed, asked a lot of questions.
>
> Within 2 months I was running client onboarding independently. Within 6 months I was consistently delivering features on time and had built a reputation with clients as someone who understood their needs.
>
> The lesson was: admitting what you don't know actually accelerates learning, because you stop performing competence and start actually building it."

---

## Section 5: Questions to Ask Them

Always prepare 3-4 questions to ask. Use these as a base:

### For AI Product Operations roles:
- "What does success look like at the end of the first 90 days?"
- "What's the biggest operational bottleneck the team is facing right now?"
- "How autonomous is this role — do you have strong opinions on process, or is the person expected to define how things run?"
- "What AI tools is the team currently using or experimenting with?"
- "What's the ratio of 'building new things' vs. 'maintaining existing processes' in this role?"

### For any role:
- "What's the team culture like around failure and experimentation?"
- "How does this role grow over 12-24 months?"
- "What would you change about the team or product if you could?"

**Why questions matter:**
- Shows genuine curiosity
- Helps you evaluate if it's a good fit
- Makes the conversation more natural and two-directional
- Interviewers often remember candidates who asked great questions

---

*Practice these until the answers come naturally. The goal is not to memorize — the goal is to be so familiar with the material that you can speak about it comfortably under pressure.*
