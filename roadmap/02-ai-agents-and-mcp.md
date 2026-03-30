# Phase 2: AI Agents & MCP (Days 15-28)

**Goal**: Understand how AI agents work at a deep level, build several from scratch, and master MCP (Model Context Protocol). This is the most valuable skill gap to close.

---

## Part 1: AI Agents -- From Theory to Practice

### What is an AI Agent? (Deep Dive)

An AI agent is a system with these components:

```
┌──────────────────────────────────────────────────┐
│                   AI AGENT                       │
│                                                  │
│  ┌─────────┐  ┌──────────┐  ┌─────────────────┐ │
│  │  BRAIN   │  │  TOOLS   │  │    MEMORY       │ │
│  │ (LLM)   │  │          │  │                 │ │
│  │ Claude   │  │ Search   │  │ Short-term      │ │
│  │ GPT-4   │  │ Code     │  │ (conversation)  │ │
│  │ Gemini  │  │ Database │  │                 │ │
│  │         │  │ API calls│  │ Long-term       │ │
│  │         │  │ Files    │  │ (vector store)  │ │
│  └────┬────┘  └────┬─────┘  └────────┬────────┘ │
│       │            │                 │           │
│       └────────────┼─────────────────┘           │
│                    │                             │
│            ┌───────┴───────┐                     │
│            │  ORCHESTRATOR │                     │
│            │  (Agent Loop) │                     │
│            └───────────────┘                     │
└──────────────────────────────────────────────────┘
```

**The Agent Loop** (This is the key concept):

```
1. User gives a goal
2. Agent THINKS about what to do (uses LLM)
3. Agent PLANS steps
4. Agent EXECUTES a step (uses a tool)
5. Agent OBSERVES the result
6. Agent REFLECTS -- did it work? What next?
7. If not done, go back to step 2
8. If done, return result to user
```

This is called the **ReAct (Reasoning + Acting) pattern**.

### The 5 Levels of AI Agent Complexity

**Level 1: Simple Chatbot**
- Just LLM + conversation history
- No tools, no memory beyond conversation
- Example: Basic ChatGPT conversation

**Level 2: Tool-Using Agent**
- LLM + ability to call tools (search, code execution, APIs)
- Can take actions, not just talk
- Example: ChatGPT with web search, Cursor AI

**Level 3: Autonomous Agent**
- LLM + tools + planning + memory
- Can break complex tasks into steps and execute them
- Example: Claude Code, Codex, Devin

**Level 4: Multi-Agent System**
- Multiple agents working together
- Each agent has a specialty
- They coordinate to solve complex problems
- Example: CrewAI, AutoGen multi-agent setups

**Level 5: Self-Improving Agent**
- Agents that learn from their mistakes
- Can modify their own behavior
- Create new tools as needed
- This is the frontier

### Key Concepts You Must Know

**Function Calling / Tool Use**
```python
# This is how you give an AI model tools to use
tools = [
    {
        "name": "search_web",
        "description": "Search the web for current information",
        "input_schema": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "The search query"
                }
            },
            "required": ["query"]
        }
    }
]

# The model decides WHEN to use a tool and WHAT arguments to pass
response = client.messages.create(
    model="claude-sonnet-4-20250514",
    tools=tools,
    messages=[{"role": "user", "content": "What's the latest AI news today?"}]
)
# If response wants to use a tool, you execute it and send the result back
```

**RAG (Retrieval-Augmented Generation)**
- Store documents in a vector database
- When user asks a question, find relevant documents
- Send those documents + question to the LLM
- LLM answers based on YOUR data, not just training data

**Embeddings**
- Turn text into numbers (vectors)
- Similar text = similar numbers
- Used for search, recommendations, clustering

**Structured Output**
- Make LLMs return data in specific formats (JSON, etc.)
- Critical for agents that need to process results programmatically

---

## Part 2: Build Your First Real Agent (Days 15-18)

### Project: AI Research Agent

Build an agent that can research any topic, gather information from multiple sources, and produce a structured report.

```python
# research_agent.py
import anthropic
import json

client = anthropic.Anthropic()

# Define the tools this agent can use
tools = [
    {
        "name": "search_web",
        "description": "Search the web for information about a topic. Returns relevant results.",
        "input_schema": {
            "type": "object",
            "properties": {
                "query": {"type": "string", "description": "Search query"}
            },
            "required": ["query"]
        }
    },
    {
        "name": "read_url",
        "description": "Read the content of a webpage",
        "input_schema": {
            "type": "object",
            "properties": {
                "url": {"type": "string", "description": "URL to read"}
            },
            "required": ["url"]
        }
    },
    {
        "name": "save_report",
        "description": "Save the research report to a file",
        "input_schema": {
            "type": "object",
            "properties": {
                "filename": {"type": "string", "description": "Filename for the report"},
                "content": {"type": "string", "description": "Report content in markdown"}
            },
            "required": ["filename", "content"]
        }
    }
]

def execute_tool(tool_name: str, tool_input: dict) -> str:
    """Execute a tool and return the result."""
    if tool_name == "search_web":
        # In a real implementation, use a search API
        return f"[Search results for: {tool_input['query']}]\n- Result 1: ...\n- Result 2: ..."
    elif tool_name == "read_url":
        # In a real implementation, fetch the URL
        return f"[Content from {tool_input['url']}]: ..."
    elif tool_name == "save_report":
        with open(tool_input["filename"], "w") as f:
            f.write(tool_input["content"])
        return f"Report saved to {tool_input['filename']}"
    return "Unknown tool"

def run_agent(task: str):
    """Run the agent loop until the task is complete."""
    messages = [{"role": "user", "content": task}]
    
    print(f"\n{'='*60}")
    print(f"AGENT TASK: {task}")
    print(f"{'='*60}\n")
    
    while True:
        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=4096,
            system="You are a thorough research agent. Break down research tasks into steps, use tools to gather information, and produce comprehensive reports.",
            tools=tools,
            messages=messages
        )
        
        # Check if the agent wants to use tools
        if response.stop_reason == "tool_use":
            # Process each content block
            assistant_content = response.content
            messages.append({"role": "assistant", "content": assistant_content})
            
            tool_results = []
            for block in assistant_content:
                if block.type == "tool_use":
                    print(f"  TOOL: {block.name}({json.dumps(block.input)})")
                    result = execute_tool(block.name, block.input)
                    print(f"  RESULT: {result[:100]}...")
                    tool_results.append({
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": result
                    })
            
            messages.append({"role": "user", "content": tool_results})
        
        elif response.stop_reason == "end_turn":
            # Agent is done
            final_text = ""
            for block in response.content:
                if hasattr(block, "text"):
                    final_text += block.text
            print(f"\nAGENT COMPLETE:\n{final_text}")
            return final_text

# Run it
if __name__ == "__main__":
    run_agent("Research the top 5 AI agent frameworks in 2026. Compare their features, pricing, and best use cases. Save a report.")
```

### What You Just Learned

1. **Tool definition**: How to describe tools for the AI model
2. **Agent loop**: The think → act → observe cycle
3. **Tool execution**: How to run tools and feed results back
4. **Autonomous completion**: The agent decides when it's done

---

## Part 3: MCP Deep Dive (Days 19-23)

### MCP Architecture

```
┌─────────────┐     ┌──────────────┐     ┌─────────────┐
│  MCP CLIENT  │────│  MCP PROTOCOL │────│  MCP SERVER  │
│  (Cursor,    │     │  (JSON-RPC   │     │  (Your      │
│   Claude     │     │   over       │     │   custom    │
│   Desktop)   │     │   stdio/SSE) │     │   server)   │
└─────────────┘     └──────────────┘     └─────────────┘
```

### MCP Server Capabilities

An MCP server can expose:

1. **Tools**: Functions the AI can call (like our agent tools above)
2. **Resources**: Data the AI can read (files, database records, API data)
3. **Prompts**: Pre-built prompt templates

### Build Your First MCP Server

```typescript
// mcp-server/src/index.ts
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

const server = new McpServer({
  name: "career-tools",
  version: "1.0.0",
});

// Tool 1: Search for AI job listings
server.tool(
  "search_ai_jobs",
  "Search for AI-related job listings in a specific region",
  {
    role: z.string().describe("Job role to search for (e.g., 'AI Product Operations')"),
    region: z.string().describe("Region to search in (e.g., 'EMEA', 'Remote')"),
  },
  async ({ role, region }) => {
    // In production: call a job search API
    return {
      content: [
        {
          type: "text" as const,
          text: JSON.stringify({
            results: [
              { title: role, company: "Example Corp", location: region, url: "https://..." },
            ],
            total: 1,
          }),
        },
      ],
    };
  }
);

// Tool 2: Analyze a job description
server.tool(
  "analyze_job_description",
  "Analyze a job description and extract key requirements, skills, and match score",
  {
    job_description: z.string().describe("The full job description text"),
  },
  async ({ job_description }) => {
    return {
      content: [
        {
          type: "text" as const,
          text: JSON.stringify({
            required_skills: ["extracted from description"],
            nice_to_have: ["extracted from description"],
            experience_level: "mid-level",
            ai_tools_mentioned: ["extracted from description"],
          }),
        },
      ],
    };
  }
);

// Tool 3: Generate a tailored CV section
server.tool(
  "tailor_cv_section",
  "Generate a tailored CV section based on job requirements and your experience",
  {
    job_requirements: z.string().describe("Key requirements from the job"),
    your_experience: z.string().describe("Your relevant experience"),
    section_type: z.string().describe("CV section type: summary, experience, or skills"),
  },
  async ({ job_requirements, your_experience, section_type }) => {
    return {
      content: [
        {
          type: "text" as const,
          text: `Tailored ${section_type} section based on matching ${your_experience} to ${job_requirements}`,
        },
      ],
    };
  }
);

// Resource: Your career profile
server.resource(
  "career-profile",
  "career://profile",
  async (uri) => ({
    contents: [
      {
        uri: uri.href,
        mimeType: "application/json",
        text: JSON.stringify({
          name: "Firas Al Mostaysser",
          location: "Tunis, Tunisia",
          languages: ["Arabic", "French", "English"],
          experience_years: 4,
          key_skills: [
            "Product Management",
            "Backend Engineering",
            "AI Automation",
            "Client Discovery",
          ],
          target_roles: [
            "AI Product Operations",
            "AI Solutions Engineer",
            "GTM Operations",
          ],
        }),
      },
    ],
  })
);

async function main() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
  console.error("Career Tools MCP Server running on stdio");
}

main().catch(console.error);
```

### Setting Up MCP in Cursor

Add to your Cursor settings (`.cursor/mcp.json` in your project):

```json
{
  "mcpServers": {
    "career-tools": {
      "command": "npx",
      "args": ["tsx", "mcp-server/src/index.ts"]
    }
  }
}
```

Now Cursor's AI can use your custom tools when you chat with it.

### Useful Pre-Built MCP Servers to Know

| MCP Server | What It Does | Use Case |
|-----------|-------------|----------|
| `@modelcontextprotocol/server-filesystem` | Read/write files | Let AI access local files |
| `@modelcontextprotocol/server-github` | GitHub API access | Manage repos, issues, PRs |
| `@modelcontextprotocol/server-postgres` | PostgreSQL queries | Let AI query your database |
| `@modelcontextprotocol/server-slack` | Slack integration | AI-powered Slack automation |
| `@modelcontextprotocol/server-brave-search` | Web search | Give AI web search ability |
| `@modelcontextprotocol/server-puppeteer` | Browser automation | Web scraping, testing |

---

## Part 4: Agent Frameworks (Days 24-26)

### LangChain / LangGraph

The most popular framework for building AI agents.

**When to use**: Complex agents with multiple steps, chains of operations, or when you need structured workflows.

```python
# Simple LangChain agent example
from langchain_anthropic import ChatAnthropic
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.tools import DuckDuckGoSearchRun

model = ChatAnthropic(model="claude-sonnet-4-20250514")
search = DuckDuckGoSearchRun()
tools = [search]

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI career advisor. Use search to find current information."),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}"),
])

agent = create_tool_calling_agent(model, tools, prompt)
executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

result = executor.invoke({"input": "Find AI Product Operations jobs hiring in EMEA right now"})
print(result)
```

### CrewAI

Multi-agent framework -- multiple AI agents working together.

```python
from crewai import Agent, Task, Crew

researcher = Agent(
    role="AI Market Researcher",
    goal="Find the latest AI job market trends and opportunities",
    backstory="Expert in AI industry analysis and job market trends",
    verbose=True,
)

writer = Agent(
    role="Career Content Writer",
    goal="Create compelling career materials based on research",
    backstory="Expert in writing CVs, cover letters, and LinkedIn content for tech professionals",
    verbose=True,
)

research_task = Task(
    description="Research the top 10 companies hiring for AI Product Operations roles in EMEA. Include company name, role title, key requirements, and salary range.",
    agent=researcher,
    expected_output="A detailed report of 10 companies with AI Product Ops roles",
)

writing_task = Task(
    description="Based on the research, create a tailored LinkedIn post announcing expertise in AI Product Operations, highlighting relevant experience.",
    agent=writer,
    expected_output="A LinkedIn post ready to publish",
)

crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, writing_task],
    verbose=True,
)

result = crew.kickoff()
print(result)
```

### OpenAI Assistants API

OpenAI's managed agent platform.

**When to use**: When you want hosted agents with built-in file search, code execution, and function calling without managing infrastructure.

---

## Part 5: Advanced Agent Patterns (Days 27-28)

### Pattern 1: Planning Agent
Agent that creates a plan before executing. Better for complex tasks.

### Pattern 2: Reflection Agent
Agent that reviews its own output and improves it. Higher quality results.

### Pattern 3: Tool-Making Agent
Agent that can create new tools when existing ones aren't sufficient.

### Pattern 4: Human-in-the-Loop
Agent that pauses for human approval at critical steps. Important for production.

### Pattern 5: Multi-Agent Orchestration
Multiple specialized agents coordinated by a manager agent.

---

## Phase 2 Checklist

By end of Phase 2, you should be able to:

- [ ] Explain the AI agent loop (ReAct pattern) clearly
- [ ] Build a tool-using agent from scratch with Anthropic or OpenAI APIs
- [ ] Explain MCP to a non-technical person
- [ ] Build a custom MCP server with at least 3 tools
- [ ] Configure MCP servers in Cursor
- [ ] Use at least one agent framework (LangChain or CrewAI)
- [ ] Know when to use each framework
- [ ] Have built at least 2 agent projects

---

## Portfolio Pieces from This Phase

1. **Research Agent**: Autonomous research agent that gathers and summarizes info
2. **MCP Server**: Custom MCP server with useful tools
3. **Multi-Agent System**: CrewAI crew that solves a real problem

Each of these should be in a GitHub repo with a clear README, demo, and explanation.

---

**Next: `03-ai-product-operations.md` -- The role-specific knowledge.**
