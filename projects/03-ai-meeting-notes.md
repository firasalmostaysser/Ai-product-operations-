# Project 3: AI Meeting Notes Generator

## What It Is

A simple tool that:
1. Takes a meeting transcript (copied from Zoom/Google Meet/Otter.ai)
2. Uses Claude to generate structured meeting notes
3. Outputs: summary, decisions made, action items with owners, open questions

## Why This Project Matters

This is one of the highest-ROI AI tools for any organization. Every company has meetings. Most meetings are poorly documented. This solves a universal problem and demonstrates:
- Practical AI application
- Understanding of structured output
- Real business value

You can sell this as a freelance project to any company for $300–$800.

## Tech Stack

- **Python** or **Node.js** — your choice
- **Anthropic Claude API**
- Optional: Simple **Streamlit** or **HTML** front-end

## The Core Prompt (This Is The Key Part)

```python
MEETING_NOTES_PROMPT = """You are an expert meeting facilitator and note-taker. 
You create structured, clear, and actionable meeting notes that busy professionals 
actually read and use.

From the transcript provided, generate meeting notes with these EXACT sections:

## Meeting Summary
(2-3 sentences: who was there, what was discussed, what was decided)

## Key Decisions
(Bullet list of final decisions made. Phrased as "We decided to..." or "It was agreed that...")

## Action Items
(Table format with: | Task | Owner | Deadline | Priority |)
(If deadline not mentioned, write "No deadline set")
(If owner not mentioned, write "To be assigned")

## Open Questions  
(Bullet list of unresolved questions that need follow-up)

## Key Insights / Context
(2-4 bullets of important background info or context that came up)

Rules:
- Be specific and precise — no vague summaries
- If something is unclear from the transcript, note it as [unclear]
- Keep action items actionable (start with a verb: "Create", "Review", "Schedule", etc.)
- Do not invent information not in the transcript
"""
```

## Full Code

```python
import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()
client = Anthropic()

def generate_meeting_notes(transcript: str, meeting_title: str = "Meeting") -> str:
    """Generate structured meeting notes from a transcript."""
    
    response = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=2000,
        system=MEETING_NOTES_PROMPT,
        messages=[
            {
                "role": "user",
                "content": f"""Meeting: {meeting_title}
                
Transcript:
{transcript}

Generate the meeting notes."""
            }
        ]
    )
    
    return response.content[0].text

def main():
    # Example transcript (paste a real one for testing)
    sample_transcript = """
    Ahmed: OK so let's get started. We have 30 minutes.
    Firas: Great. So the main issue is the client onboarding is taking too long.
    Ahmed: How long is it taking now?
    Firas: About 3 days per client. We want to get it to same day.
    Sarah: I think we need to automate the setup process. The manual configuration is the bottleneck.
    Firas: Exactly. I was thinking we build an n8n workflow that handles the initial config.
    Ahmed: How long would that take to build?
    Firas: Probably 2-3 days of work. But then we never have to do it manually again.
    Ahmed: OK let's do it. Firas, can you scope it out by Friday?
    Firas: Yes, I'll have a proper spec ready.
    Sarah: I'll review the current onboarding process doc and identify what can be automated.
    Ahmed: Perfect. What about the API limits issue we had last week?
    Firas: Still investigating. I think it's related to the batch size. I'll fix it by EOD today.
    Ahmed: Great. Any other blockers?
    Sarah: I need access to the production database to investigate the performance issue.
    Ahmed: I'll ask IT to grant access. Anything else?
    Firas: One thing - should we document the new workflow once it's built?
    Ahmed: Yes, definitely. Add it to Notion.
    Ahmed: OK, I think we're done. Good meeting everyone.
    """
    
    print("Generating meeting notes...\n")
    notes = generate_meeting_notes(sample_transcript, "Onboarding Process Review")
    print(notes)
    
    # Save to file
    with open("meeting_notes.md", "w") as f:
        f.write(f"# {meeting_title}\n\n")
        f.write(notes)
    print("\n✅ Notes saved to meeting_notes.md")

if __name__ == "__main__":
    main()
```

## Expected Output

```markdown
## Meeting Summary
The team reviewed the client onboarding process, identifying a 3-day setup time 
as the main bottleneck. Firas proposed building an n8n automation to reduce this 
to same-day onboarding. A database access issue was also discussed.

## Key Decisions
- We decided to build an n8n workflow to automate client configuration
- It was agreed that Firas will scope the automation project
- Documentation will be added to Notion once the workflow is built

## Action Items
| Task | Owner | Deadline | Priority |
|------|-------|----------|----------|
| Scope n8n onboarding automation | Firas | Friday | High |
| Review current onboarding process doc | Sarah | No deadline set | Medium |
| Investigate and fix API batch size issue | Firas | EOD today | High |
| Grant Sarah access to production database | Ahmed | No deadline set | Medium |

## Open Questions
- What exactly is causing the API limits issue with batch processing?
- Are there other parts of onboarding beyond config that can be automated?

## Key Insights / Context
- Current onboarding time: ~3 days per client
- Target onboarding time: same day
- The manual configuration step is the main bottleneck
- Production database access is needed to investigate the performance issue
```

## Adding a Simple Web UI with Streamlit

```bash
pip install streamlit
```

Create `app.py`:
```python
import streamlit as st
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()
client = Anthropic()

st.title("🎙️ AI Meeting Notes Generator")
st.markdown("Paste your meeting transcript below to generate structured notes.")

meeting_title = st.text_input("Meeting Title", "Team Meeting")
transcript = st.text_area("Meeting Transcript", height=300, 
                          placeholder="Paste your transcript here...")

if st.button("Generate Notes", type="primary") and transcript:
    with st.spinner("Generating meeting notes..."):
        notes = generate_meeting_notes(transcript, meeting_title)
    
    st.markdown("---")
    st.markdown("## Generated Meeting Notes")
    st.markdown(notes)
    
    # Download button
    st.download_button(
        "Download Notes (.md)",
        notes,
        f"{meeting_title.lower().replace(' ', '_')}_notes.md",
        "text/markdown"
    )
```

Run it:
```bash
streamlit run app.py
```

Now you have a web app at `localhost:8501`. Take a screenshot — this is your demo.

## Deploy for Free

**Option 1: Streamlit Community Cloud** (easiest)
1. Push to GitHub
2. Go to share.streamlit.io
3. Connect your repo
4. Done — free public URL

**Option 2: Hugging Face Spaces** (also free)
1. Create account on huggingface.co
2. New Space → Streamlit
3. Upload your app

## Portfolio Framing

> "Built a meeting notes generator that uses Claude to turn any transcript into structured notes with action items, decisions, and open questions. Has a Streamlit web interface and is deployed publicly. Used by my own team for weekly meetings."

---

*Time to complete: 2-3 hours (4-5 with Streamlit UI) | Next: [Project 4: Outreach Personalizer](./04-outreach-personalizer.md)*
