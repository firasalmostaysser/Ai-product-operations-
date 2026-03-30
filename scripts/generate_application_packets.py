#!/usr/bin/env python3
"""Generate draft application packets from scored job leads.

This script automates preparation work while keeping final submission human-controlled.
It creates one markdown packet per selected company with:
  - role-fit snapshot
  - customized intro paragraph draft
  - evidence bullets mapped to role keywords
  - interview talking points
  - personalized follow-up message draft

Usage:
  python3 scripts/generate_application_packets.py \
      --input data/jobs_scored.csv \
      --output-dir applications \
      --top-n 10
"""

from __future__ import annotations

import argparse
import csv
from pathlib import Path


def normalize(text: str) -> str:
    return " ".join((text or "").lower().split())


def split_keywords(value: str) -> set[str]:
    if not value:
        return set()
    normalized = value.replace(";", ",").replace("/", ",")
    parts = [p.strip().lower() for p in normalized.split(",")]
    return {p for p in parts if p}


def slugify(name: str) -> str:
    chars: list[str] = []
    for ch in (name or "").strip().lower():
        if ch.isalnum():
            chars.append(ch)
        elif ch in {" ", "-", "_"}:
            chars.append("-")
    slug = "".join(chars).strip("-")
    while "--" in slug:
        slug = slug.replace("--", "-")
    return slug or "item"


def parse_int(value: str, default: int = 0) -> int:
    text = normalize(value)
    if not text:
        return default
    digits = "".join(ch for ch in text if ch.isdigit())
    return int(digits) if digits else default


def load_rows(input_path: Path) -> list[dict[str, str]]:
    with input_path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        return list(reader)


def default_evidence() -> list[str]:
    return [
        "Backend engineering foundation with API/data systems experience.",
        "Product Owner track record coordinating cross-functional execution.",
        "AI automation mindset focused on reducing manual work and cycle time.",
        "Strong communication across technical and non-technical stakeholders.",
        "Multilingual execution across Arabic, French, and English contexts.",
    ]


def map_evidence(requirement_keywords: set[str]) -> list[str]:
    evidence_map = {
        "product ops": "I have owned operational workflows and improved handoffs across teams.",
        "product operations": "I have owned operational workflows and improved handoffs across teams.",
        "ai": "I use AI tools and structured prompting to accelerate operational tasks with quality controls.",
        "automation": "I build automation with guardrails, logs, and clear escalation paths.",
        "gtm": "I can support GTM execution with structured research, segmentation, and process design.",
        "revops": "I can improve RevOps hygiene, reporting consistency, and pipeline visibility.",
        "api": "I can integrate APIs/webhooks and bridge business goals to technical implementation.",
        "stakeholder": "I translate business priorities into executable technical and operational actions.",
        "communication": "I communicate in concise context -> action -> result format.",
        "english": "I optimize for clear, structured English communication in async and interviews.",
        "n8n": "I can orchestrate practical workflow automation with n8n and external tools.",
        "python": "I can build lightweight Python automations and data-processing utilities.",
    }
    selected: list[str] = []
    for keyword, sentence in evidence_map.items():
        if keyword in requirement_keywords and sentence not in selected:
            selected.append(sentence)
    if not selected:
        selected = default_evidence()[:4]
    return selected


def build_intro(company: str, role: str, source: str) -> str:
    source_hint = f" after finding the opportunity via {source}" if source else ""
    return (
        f"I am applying for the {role} role at {company}{source_hint}. "
        "My strength is combining technical implementation, product/operations execution, "
        "and AI-driven workflow improvement. I focus on reducing manual workload, improving "
        "handoff quality, and helping teams execute faster with measurable outcomes."
    )


def follow_up_message(company: str, role: str) -> str:
    return (
        f"Hi [Name], I just applied for the {role} role at {company}. "
        "I combine engineering + product ops + AI automation and would be happy to share "
        "a short case study relevant to your team workflows."
    )


def choose_link(row: dict[str, str]) -> str:
    return (row.get("url") or row.get("job_link") or "N/A").strip() or "N/A"


def choose_requirements(row: dict[str, str]) -> str:
    return (row.get("must_have_skills") or row.get("must_have_keywords") or "").strip()


def build_packet(row: dict[str, str]) -> str:
    company = (row.get("company") or "Company").strip()
    role = (row.get("role") or "Role").strip()
    source = (row.get("source") or "").strip()
    location = (row.get("location") or "N/A").strip()
    remote_policy = (row.get("remote_policy") or row.get("work_mode") or "N/A").strip()
    link = choose_link(row)
    fit_score = (row.get("fit_score") or row.get("score") or "N/A").strip()
    priority = (row.get("priority") or "N/A").strip()
    decision = (row.get("decision") or "review").strip()
    score_reason = (row.get("score_reason") or row.get("reason") or "N/A").strip()
    next_action = (row.get("next_action") or "Review and decide.").strip()
    salary_min = (row.get("salary_min") or "").strip()
    salary_max = (row.get("salary_max") or "").strip()
    currency = (row.get("currency") or "").strip()
    requirements = choose_requirements(row)
    requirement_keywords = split_keywords(requirements)

    evidence_lines = map_evidence(requirement_keywords)
    intro = build_intro(company, role, source)
    followup = follow_up_message(company, role)

    salary_label = "N/A"
    if salary_min and salary_max and currency:
        salary_label = f"{currency} {salary_min}-{salary_max}"
    elif salary_min and currency:
        salary_label = f"{currency} {salary_min}+"

    lines: list[str] = []
    lines.append(f"# Application Packet - {company} - {role}")
    lines.append("")
    lines.append("## Lead Snapshot")
    lines.append("")
    lines.append(f"- Source: {source or 'N/A'}")
    lines.append(f"- Company: {company}")
    lines.append(f"- Role: {role}")
    lines.append(f"- Location: {location}")
    lines.append(f"- Remote Policy: {remote_policy}")
    lines.append(f"- Salary Band: {salary_label}")
    lines.append(f"- Job Link: {link}")
    lines.append(f"- Fit Score: {fit_score}")
    lines.append(f"- Priority: {priority}")
    lines.append(f"- Decision: {decision}")
    lines.append(f"- Scoring Reason: {score_reason}")
    lines.append(f"- Next Action: {next_action}")
    lines.append("")
    lines.append("## Custom Intro Paragraph (Draft)")
    lines.append("")
    lines.append(intro)
    lines.append("")
    lines.append("## Requirement Fit Mapping")
    lines.append("")
    if requirements:
        lines.append(f"- Job keywords: {requirements}")
    else:
        lines.append("- Job keywords: (add manually from JD)")
    for item in evidence_lines:
        lines.append(f"- Evidence: {item}")
    lines.append("")
    lines.append("## CV Bullet Suggestions")
    lines.append("")
    lines.append("- Built and improved operational workflows by combining AI assistance with process controls.")
    lines.append("- Coordinated cross-functional delivery and translated priorities into execution.")
    lines.append("- Applied technical problem-solving to reduce turnaround time and improve reliability.")
    lines.append("")
    lines.append("## Interview Talking Points")
    lines.append("")
    lines.append("- Present one automation project with before/after metrics.")
    lines.append("- Explain how you balance execution speed with reliability and ownership.")
    lines.append("- Demonstrate concise communication style with structured answers.")
    lines.append("")
    lines.append("## Follow-up Message Draft")
    lines.append("")
    lines.append(followup)
    lines.append("")
    lines.append("## Final Human Checklist")
    lines.append("")
    lines.append("- [ ] Verify job requirements against real JD.")
    lines.append("- [ ] Add one company-specific product or team reference.")
    lines.append("- [ ] Adjust CV bullets with role language.")
    lines.append("- [ ] Submit manually on official site/LinkedIn.")
    lines.append("- [ ] Log submission in data/job_pipeline.csv.")
    lines.append("")
    return "\n".join(lines)


def filter_rows(rows: list[dict[str, str]], allowed_decisions: set[str]) -> list[dict[str, str]]:
    selected: list[dict[str, str]] = []
    for row in rows:
        decision = normalize(row.get("decision", "review"))
        if decision in allowed_decisions:
            selected.append(row)
    selected.sort(key=lambda r: parse_int(r.get("fit_score", "0")), reverse=True)
    return selected


def write_packets(rows: list[dict[str, str]], output_dir: Path, top_n: int) -> int:
    output_dir.mkdir(parents=True, exist_ok=True)
    count = 0
    for row in rows[:top_n]:
        company = row.get("company", "")
        role = row.get("role", "")
        path = output_dir / f"{slugify(company)}__{slugify(role)}.md"
        path.write_text(build_packet(row), encoding="utf-8")
        count += 1
    return count


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate draft application packets.")
    parser.add_argument(
        "--input",
        default="data/jobs_scored.csv",
        help="Input scored CSV path (default: data/jobs_scored.csv)",
    )
    parser.add_argument(
        "--output-dir",
        default="applications",
        help="Output directory for markdown packets (default: applications)",
    )
    parser.add_argument(
        "--top-n",
        type=int,
        default=10,
        help="Maximum number of packets to generate (default: 10)",
    )
    parser.add_argument(
        "--decisions",
        default="apply_now,apply",
        help="Comma-separated decision values to include (default: apply_now,apply)",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    root = Path(__file__).resolve().parents[1]
    input_path = root / args.input
    output_dir = root / args.output_dir

    if not input_path.exists():
        raise FileNotFoundError(
            f"Input file not found: {input_path}. Run score_job_leads.py first."
        )

    rows = load_rows(input_path)
    allowed_decisions = {normalize(x) for x in args.decisions.split(",") if normalize(x)}
    selected = filter_rows(rows, allowed_decisions=allowed_decisions)
    created = write_packets(selected, output_dir=output_dir, top_n=max(1, args.top_n))

    print(f"Read rows: {len(rows)}")
    print(f"Eligible rows: {len(selected)} (decisions={sorted(allowed_decisions)})")
    print(f"Generated packets: {created}")
    print(f"Output directory: {output_dir.resolve()}")


if __name__ == "__main__":
    main()
