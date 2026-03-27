# AI Glossary -- Terms You Need to Know Cold

**In interviews, conversations, and work, you must use these terms correctly and confidently.**

---

## Core AI Terms

### LLM (Large Language Model)
A neural network trained on massive text data that can generate, understand, and reason about text. Examples: Claude, GPT-4, Gemini, Llama.

### Token
The basic unit that LLMs process. Roughly 1 token = 0.75 words. "Hello, how are you?" = ~6 tokens. Pricing is usually per 1M tokens.

### Context Window
How much text an LLM can "see" at once. Claude Sonnet: 200K tokens (~150K words). Bigger = can process more data at once.

### Prompt
The input you give an LLM. Can be simple ("Summarize this") or complex (multi-page instructions with examples).

### System Prompt
Hidden instructions that set the AI's behavior. Users don't see it. It defines personality, rules, and capabilities.

### Temperature
Controls randomness. 0 = deterministic (same answer every time). 1 = creative/random. For operations work, use 0-0.3. For creative work, 0.7-1.0.

### Fine-Tuning
Training an existing model on your specific data to improve its performance on your tasks. Expensive and complex. Usually not needed -- RAG is often better.

### Inference
Running a trained model to get predictions/outputs. When you send a message to Claude, the process of generating a response is inference.

---

## Agent Terms

### AI Agent
A system that uses an LLM to think, plan, and take actions autonomously to achieve a goal. Goes beyond chat -- it actually does things.

### Tool Use / Function Calling
The ability of an LLM to decide it needs to use an external tool (search, database, calculator) and generate the correct parameters to call it.

### ReAct (Reasoning + Acting)
A pattern where agents alternate between thinking ("I need to search for X") and acting (executing a search). The dominant agent architecture.

### Agent Loop
The cycle: observe → think → plan → act → observe result → repeat until done. This is the core of how agents work.

### Orchestration
Coordinating multiple agents or steps in a workflow. The "manager" that decides which agent does what and in what order.

### Multi-Agent System
Multiple specialized agents working together, each handling different aspects of a task. One might research, another writes, another reviews.

### Human-in-the-Loop (HITL)
An agent pattern where the system pauses at critical points and asks a human for approval before continuing.

---

## RAG & Data Terms

### RAG (Retrieval-Augmented Generation)
Instead of relying on the LLM's training data, you retrieve relevant documents from YOUR data and include them in the prompt. This way, the AI answers based on your specific information.

### Embedding
Converting text into a vector (list of numbers) that captures its meaning. Similar texts have similar vectors. Used for search and RAG.

### Vector Database
A database optimized for storing and searching embeddings. You store your documents as vectors and find similar ones efficiently. Examples: Pinecone, pgvector, Qdrant.

### Chunking
Splitting large documents into smaller pieces before embedding them. A 100-page PDF might be split into 500 chunks. Chunk size affects quality.

### Semantic Search
Finding documents by meaning, not just keywords. "Car breakdown" would match "vehicle malfunction" because the embeddings are similar.

### Knowledge Base
A collection of documents that an AI system can search to answer questions. The "data" in RAG.

---

## MCP Terms

### MCP (Model Context Protocol)
An open standard by Anthropic that provides a universal way for AI models to connect to external tools and data. Think "USB for AI."

### MCP Server
A program that exposes tools, resources, or prompts to AI models via the MCP protocol. You build these.

### MCP Client
An application that connects to MCP servers and uses them. Examples: Cursor, Claude Desktop.

### MCP Tool
A function exposed by an MCP server that the AI can call. Like "search_database" or "send_email."

### MCP Resource
Data exposed by an MCP server that the AI can read. Like a file, database record, or API response.

### stdio Transport
MCP communication over standard input/output. The server runs as a subprocess of the client.

### SSE Transport
MCP communication over HTTP Server-Sent Events. For remote MCP servers.

---

## Product Operations Terms

### OKR (Objectives and Key Results)
Goal-setting framework. Objective = qualitative goal. Key Results = measurable outcomes. "Improve reliability (O)" → "99.5% uptime, <1 P1 incident/month (KRs)."

### KPI (Key Performance Indicator)
A metric that indicates performance. For AI products: accuracy, latency, error rate, customer satisfaction.

### SLA (Service Level Agreement)
A commitment to customers about performance levels. "99.9% uptime" or "Response within 200ms."

### P1/P2/P3/P4 (Priority Levels)
Incident severity classification. P1 = critical (product down). P4 = cosmetic issue.

### Post-Mortem
After-incident analysis: what happened, why, and how to prevent it. Blameless by convention.

### Runbook
Step-by-step guide for handling specific operational scenarios. "If X happens, do Y."

### Feature Flag
A way to enable/disable features for specific users without deploying new code. Essential for gradual rollouts.

### A/B Test
Showing different versions of something to different users and measuring which performs better.

### Time to Value (TTV)
How long it takes a new customer to get value from the product. Lower = better onboarding.

### CSAT / NPS
Customer satisfaction metrics. CSAT = "How satisfied are you?" NPS = "Would you recommend us?"

---

## GTM Terms

### GTM (Go-To-Market)
The strategy for bringing a product to customers. Includes positioning, pricing, channels, and sales motion.

### ICP (Ideal Customer Profile)
A description of the perfect customer: industry, size, pain points, budget, decision process.

### Persona
A fictional representation of a target user. "Sarah, the VP of Ops at a 200-person SaaS company who's frustrated with manual reporting."

### TAM / SAM / SOM
Total Addressable Market / Serviceable Addressable Market / Serviceable Obtainable Market. Concentric circles of market opportunity.

### PLG (Product-Led Growth)
Growth strategy where the product itself drives acquisition, conversion, and expansion. Users try before they buy.

### ARR / MRR
Annual Recurring Revenue / Monthly Recurring Revenue. Key SaaS metrics.

### CAC (Customer Acquisition Cost)
How much it costs to acquire one customer. Includes marketing, sales, and onboarding costs.

### LTV (Lifetime Value)
Total revenue expected from a customer over their entire relationship. LTV > 3x CAC is healthy.

### Churn
The rate at which customers leave. 5% monthly churn = losing half your customers yearly.

### Pipeline
The total value of potential deals in your sales process. "We have $500K in pipeline."

### Lead Scoring
Assigning a numerical score to leads based on how likely they are to buy. Higher score = prioritize.

### Outbound vs Inbound
Outbound = you reach out to prospects. Inbound = they come to you (through content, SEO, word of mouth).

---

## Automation Terms

### Workflow
A series of automated steps triggered by an event. "New email → classify → route → respond."

### Trigger
What starts a workflow. Webhook, schedule, new record, file upload, etc.

### Webhook
An HTTP endpoint that receives data when something happens. "When a form is submitted, POST data to this URL."

### API (Application Programming Interface)
A way for two systems to communicate. You send a request, it sends a response.

### Integration
Connecting two systems so they can share data. "Integrate Slack with your CRM."

### ETL (Extract, Transform, Load)
Pulling data from sources, transforming it into the right format, and loading it into a destination.

### Cron Job
A scheduled task that runs at specific times. "Every Monday at 8 AM, generate the weekly report."

### Idempotent
An operation that produces the same result whether you run it once or many times. Important for reliable automation.

---

## How to Use This Glossary

1. Read through it once to familiarize yourself
2. When you encounter a term you don't know, look it up here first
3. Practice using these terms in your LinkedIn posts and conversations
4. During interviews, use these terms naturally -- it shows fluency
5. If an interviewer uses a term you don't know, ask them to clarify (this shows curiosity, not ignorance)
