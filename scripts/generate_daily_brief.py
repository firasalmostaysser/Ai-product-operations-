#!/usr/bin/env python3
"""Generate a daily AI career update brief in markdown.

The script is dependency-free and attempts to pull live headlines from
selected AI and automation RSS/Atom feeds. It also keeps an up-to-date
"latest.md" pointer in the daily-updates folder.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from html import unescape
from pathlib import Path
from typing import Iterable
from urllib.error import URLError
from urllib.request import Request, urlopen
import xml.etree.ElementTree as ET


@dataclass(frozen=True)
class BriefItem:
    category: str
    title: str
    why_it_matters: str
    action_today: str


@dataclass(frozen=True)
class FeedSource:
    name: str
    url: str


@dataclass(frozen=True)
class Headline:
    source: str
    title: str
    link: str


def current_date_utc() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def clean_text(value: str | None) -> str:
    if not value:
        return ""
    return " ".join(unescape(value).split())


def local_name(tag: str) -> str:
    if "}" in tag:
        return tag.split("}", 1)[1]
    return tag


def child_text(element: ET.Element, accepted_names: Iterable[str]) -> str:
    names = set(accepted_names)
    for child in list(element):
        if local_name(child.tag) in names and child.text:
            return clean_text(child.text)
    return ""


def child_link(element: ET.Element) -> str:
    # RSS: <link>https://...</link>
    rss_link = child_text(element, {"link"})
    if rss_link.startswith("http"):
        return rss_link

    # Atom: <link href="https://..." rel="alternate" />
    for child in list(element):
        if local_name(child.tag) != "link":
            continue
        href = clean_text(child.attrib.get("href"))
        rel = clean_text(child.attrib.get("rel"))
        if href and (not rel or rel == "alternate"):
            return href
    return ""


def fetch_xml(url: str, timeout_seconds: int = 12) -> bytes:
    request = Request(
        url=url,
        headers={
            "User-Agent": (
                "Mozilla/5.0 (X11; Linux x86_64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/125.0 Safari/537.36"
            )
        },
    )
    with urlopen(request, timeout=timeout_seconds) as response:
        return response.read()


def parse_headlines(source_name: str, payload: bytes, limit: int = 2) -> list[Headline]:
    try:
        root = ET.fromstring(payload)
    except ET.ParseError:
        return []

    headlines: list[Headline] = []
    seen_links: set[str] = set()
    for element in root.iter():
        name = local_name(element.tag)
        if name not in {"item", "entry"}:
            continue

        title = child_text(element, {"title"})
        link = child_link(element)
        if not title or not link:
            continue
        if link in seen_links:
            continue

        seen_links.add(link)
        headlines.append(Headline(source=source_name, title=title, link=link))
        if len(headlines) >= limit:
            break

    return headlines


def get_live_market_headlines(per_source_limit: int = 2) -> list[Headline]:
    sources = [
        FeedSource("OpenAI News", "https://openai.com/news/rss.xml"),
        FeedSource("Anthropic News", "https://www.anthropic.com/news/rss.xml"),
        FeedSource("Hugging Face Blog", "https://huggingface.co/blog/feed.xml"),
        FeedSource("LangChain Blog", "https://blog.langchain.dev/rss/"),
        FeedSource("n8n Blog", "https://blog.n8n.io/rss/"),
    ]

    headlines: list[Headline] = []
    for source in sources:
        try:
            xml_payload = fetch_xml(source.url)
            headlines.extend(
                parse_headlines(
                    source_name=source.name,
                    payload=xml_payload,
                    limit=per_source_limit,
                )
            )
        except (TimeoutError, URLError):
            # Feed fetch failures should never break the daily brief.
            continue
    return headlines


def day_theme() -> tuple[str, str]:
    weekday = datetime.now(timezone.utc).strftime("%A")
    mapping: dict[str, tuple[str, str]] = {
        "Monday": (
            "AI Product Operations",
            "Focus on triage quality, incident routing, and handoff documentation.",
        ),
        "Tuesday": (
            "GTM Automation",
            "Focus on account research, prospect scoring, and outreach personalization.",
        ),
        "Wednesday": (
            "Agent Building",
            "Focus on tool schemas, planner-executor flow, and fallback logic.",
        ),
        "Thursday": (
            "MCP and Integrations",
            "Focus on tool/resource contracts and secure system boundaries.",
        ),
        "Friday": (
            "Portfolio and Publishing",
            "Focus on case-study quality, metrics narrative, and public visibility.",
        ),
        "Saturday": (
            "Interview and Communication",
            "Focus on recorded answers and concise storytelling with STAR format.",
        ),
        "Sunday": (
            "Review and Planning",
            "Focus on weekly scoreboard, gaps, and next week's execution plan.",
        ),
    }
    return mapping.get(
        weekday,
        (
            "Execution",
            "Focus on shipping one visible artifact and one tailored application.",
        ),
    )


def build_brief_content(run_date: str) -> str:
    # Keep items practical and execution-oriented.
    items = [
        BriefItem(
            category="AI Product Ops",
            title="Incident triage with LLM + routing rules",
            why_it_matters=(
                "Teams hiring AI Product Ops value people who reduce time-to-resolution "
                "and improve cross-team handoffs."
            ),
            action_today=(
                "Build or improve one triage workflow step and log before/after handling time."
            ),
        ),
        BriefItem(
            category="GTM / RevOps",
            title="AI-assisted account research and personalization",
            why_it_matters=(
                "GTM teams care about faster prep, better targeting, and measurable pipeline quality."
            ),
            action_today=(
                "Generate 10 personalized opening lines from your pipeline and rate quality."
            ),
        ),
        BriefItem(
            category="AI Automation",
            title="Human-in-the-loop approval for risky automations",
            why_it_matters=(
                "Reliable systems with review checkpoints are more production-ready than pure demos."
            ),
            action_today=(
                "Add one approval gate to your workflow and document where human review is mandatory."
            ),
        ),
        BriefItem(
            category="AI Agents / MCP",
            title="Tool contracts and structured outputs",
            why_it_matters=(
                "Clear tool input/output contracts make agent behavior more debuggable and safer."
            ),
            action_today=(
                "Define one tool schema in JSON and validate agent outputs against it."
            ),
        ),
        BriefItem(
            category="Career / Interviews",
            title="Clarity-first communication practice",
            why_it_matters=(
                "Interview outcomes improve when answers are concise, structured, and metric-backed."
            ),
            action_today=(
                "Record one 90-second answer: problem -> action -> result -> reflection."
            ),
        ),
    ]
    live_headlines = get_live_market_headlines(per_source_limit=2)
    theme_title, theme_detail = day_theme()

    checklist = [
        "Ship one visible artifact (commit, demo clip, or documented workflow).",
        "Send 3 tailored applications and 1 direct outreach.",
        "Update data/job_pipeline.csv after every application.",
        "Practice 15 minutes of spoken interview answers.",
        "Write 5 lines of reflection in your daily log.",
    ]

    lines: list[str] = []
    lines.append(f"# Daily AI Career Brief - {run_date}")
    lines.append("")
    lines.append(
        "Use this brief to decide what to build, apply for, and publish today."
    )
    lines.append("")
    lines.append("## Theme of the Day")
    lines.append("")
    lines.append(f"- **{theme_title}**: {theme_detail}")
    lines.append("")
    lines.append("## Priority Themes")
    lines.append("")

    for idx, item in enumerate(items, start=1):
        lines.append(f"### {idx}. [{item.category}] {item.title}")
        lines.append(f"- Why it matters: {item.why_it_matters}")
        lines.append(f"- Action today: {item.action_today}")
        lines.append("")

    lines.append("## Live Market Signals")
    lines.append("")
    if live_headlines:
        for item in live_headlines:
            lines.append(f"- [{item.source}] {item.title} ({item.link})")
    else:
        lines.append(
            "- Live feeds unavailable right now. Retry later and add 3 manual notes from your own searches."
        )
    lines.append("")

    lines.append("## Non-Negotiable Daily Checklist")
    lines.append("")
    for point in checklist:
        lines.append(f"- [ ] {point}")
    lines.append("")

    lines.append("## End-of-Day Reflection")
    lines.append("")
    lines.append("- What did I ship today?")
    lines.append("- What metric or signal improved?")
    lines.append("- What will I do first tomorrow?")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append(
        "Tip: Add at least 3 personalized notes from interviews, application feedback, or customer conversations."
    )
    lines.append("")

    return "\n".join(lines)


def write_brief_files(content: str, run_date: str, output_dir: Path) -> None:
    ensure_dir(output_dir)
    dated_file = output_dir / f"{run_date}.md"
    latest_file = output_dir / "latest.md"

    dated_file.write_text(content, encoding="utf-8")
    latest_file.write_text(content, encoding="utf-8")


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    updates_dir = root / "daily-updates"
    run_date = current_date_utc()
    content = build_brief_content(run_date)
    write_brief_files(content, run_date, updates_dir)
    print(f"Generated daily brief: {updates_dir / f'{run_date}.md'}")
    print(f"Updated latest brief: {updates_dir / 'latest.md'}")


if __name__ == "__main__":
    main()
