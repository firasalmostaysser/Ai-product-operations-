#!/usr/bin/env python3
"""Score job leads for AI Product Ops / GTM Ops / Automation roles.

Reads lead rows from CSV, assigns fit scores, and writes a ranked output CSV.
No external dependencies required.
"""

from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Weights:
    title: int = 30
    remote: int = 20
    timezone: int = 15
    seniority: int = 15
    salary: int = 10
    industry: int = 10


TARGET_TITLE_KEYWORDS = [
    "ai product operations",
    "product operations",
    "gtm operations",
    "revenue operations",
    "revops",
    "automation",
    "solutions engineer",
    "implementation",
    "technical account",
]

BONUS_TITLE_KEYWORDS = [
    "ai",
    "agent",
    "workflow",
    "operations",
]

INDUSTRY_PRIORITY = {
    "ai": 10,
    "saas": 8,
    "developer tools": 8,
    "b2b software": 7,
    "fintech": 6,
    "other": 3,
}

SENIORITY_SCORES = {
    "entry": 15,
    "junior": 14,
    "associate": 14,
    "junior-mid": 13,
    "mid": 12,
    "manager": 10,
    "senior": 8,
    "lead": 6,
    "director": 3,
}

REMOTE_SCORES = {
    "remote": 20,
    "hybrid": 10,
    "onsite": 2,
}

TIMEZONE_SCORES = {
    "emea-friendly": 15,
    "europe": 12,
    "global": 10,
    "unknown": 6,
    "us-only": 2,
}

EUROPE_KEYWORDS = {
    "europe",
    "emea",
    "uk",
    "ireland",
    "france",
    "germany",
    "netherlands",
    "belgium",
    "spain",
    "portugal",
    "italy",
}

US_ONLY_KEYWORDS = {"us-only", "united states only", "usa only", "north america only"}


def normalize(value: str) -> str:
    return " ".join((value or "").strip().lower().split())


def parse_k_value(raw_value: str) -> int:
    text = normalize(raw_value).replace(",", "")
    digits: list[str] = []
    current = ""
    for char in text:
        if char.isdigit():
            current += char
        elif current:
            digits.append(current)
            current = ""
    if current:
        digits.append(current)
    if not digits:
        return 0
    first = int(digits[0])
    return first // 1000 if first >= 1000 else first


def score_title(role_title: str) -> int:
    title = normalize(role_title)
    score = 0
    if any(keyword in title for keyword in TARGET_TITLE_KEYWORDS):
        score += 20
    score += min(10, sum(1 for kw in BONUS_TITLE_KEYWORDS if kw in title) * 3)
    return min(score, Weights().title)


def score_remote(row: dict[str, str]) -> int:
    mode = normalize(row.get("remote_policy", "")) or normalize(row.get("work_mode", ""))
    if not mode:
        mode = normalize(row.get("location", ""))
    for key, points in REMOTE_SCORES.items():
        if key in mode:
            return points
    return 5


def infer_timezone_fit(row: dict[str, str]) -> str:
    explicit = normalize(row.get("timezone_fit", ""))
    if explicit:
        return explicit

    location = normalize(row.get("location", ""))
    if any(token in location for token in US_ONLY_KEYWORDS):
        return "us-only"
    if "global" in location:
        return "global"
    if any(token in location for token in EUROPE_KEYWORDS):
        return "emea-friendly"
    return "unknown"


def score_timezone(row: dict[str, str]) -> int:
    tz = infer_timezone_fit(row)
    for key, points in TIMEZONE_SCORES.items():
        if key in tz:
            return points
    return TIMEZONE_SCORES["unknown"]


def score_seniority(level: str) -> int:
    lv = normalize(level)
    for key, points in SENIORITY_SCORES.items():
        if key in lv:
            return points
    return 8


def score_salary(row: dict[str, str]) -> int:
    salary_min = parse_k_value(row.get("salary_min", ""))
    salary_range = row.get("salary_range", "")
    if salary_min == 0 and salary_range:
        salary_min = parse_k_value(salary_range)

    if salary_min >= 100:
        return 10
    if salary_min >= 80:
        return 8
    if salary_min >= 60:
        return 6
    if salary_min >= 45:
        return 4
    if salary_min > 0:
        return 2
    return 3


def score_industry(row: dict[str, str]) -> int:
    text = normalize(row.get("industry", "")) or normalize(row.get("notes", ""))
    best = INDUSTRY_PRIORITY["other"]
    for key, points in INDUSTRY_PRIORITY.items():
        if key in text:
            best = max(best, points)
    return best


def compute_total_score(row: dict[str, str]) -> tuple[int, str]:
    title_score = score_title(row.get("role", ""))
    remote_score = score_remote(row)
    timezone_score = score_timezone(row)
    seniority_score = score_seniority(row.get("seniority", ""))
    salary_score = score_salary(row)
    industry_score = score_industry(row)

    total = min(
        title_score + remote_score + timezone_score + seniority_score + salary_score + industry_score,
        100,
    )

    reasons: list[str] = []
    if title_score >= 24:
        reasons.append("strong title fit")
    if remote_score >= 20:
        reasons.append("remote-friendly")
    if timezone_score >= 12:
        reasons.append("good timezone fit")
    if salary_score >= 6:
        reasons.append("salary band appears competitive")
    if not reasons:
        reasons.append("needs manual review")
    return total, "; ".join(reasons)


def priority_bucket(score: int) -> str:
    if score >= 80:
        return "P1"
    if score >= 65:
        return "P2"
    if score >= 50:
        return "P3"
    return "P4"


def decision_for(score: int) -> str:
    if score >= 80:
        return "apply_now"
    if score >= 65:
        return "apply"
    if score >= 50:
        return "review"
    return "skip"


def next_action_for(decision: str) -> str:
    if decision == "apply_now":
        return "Apply within 24h and send outreach."
    if decision == "apply":
        return "Apply within 72h and send personalized outreach."
    if decision == "review":
        return "Read full JD and decide within 24h."
    return "Skip unless referral or unique upside appears."


def rank_leads(input_csv: Path, output_csv: Path) -> int:
    with input_csv.open("r", encoding="utf-8", newline="") as infile:
        reader = csv.DictReader(infile)
        rows = list(reader)
        if not rows:
            raise ValueError("Input CSV has no rows.")

    for row in rows:
        score, score_reason = compute_total_score(row)
        priority = priority_bucket(score)
        decision = decision_for(score)
        row["fit_score"] = str(score)
        row["priority"] = priority
        row["decision"] = decision
        row["score_reason"] = score_reason
        row["next_action"] = next_action_for(decision)

    rows.sort(key=lambda r: int(r["fit_score"]), reverse=True)

    fieldnames = list(rows[0].keys())
    for extra in ["fit_score", "priority", "decision", "score_reason", "next_action"]:
        if extra not in fieldnames:
            fieldnames.append(extra)

    output_csv.parent.mkdir(parents=True, exist_ok=True)
    with output_csv.open("w", encoding="utf-8", newline="") as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    return len(rows)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Score and rank job leads.")
    parser.add_argument(
        "--input",
        default="data/jobs_leads.csv",
        help="Input CSV with leads (default: data/jobs_leads.csv)",
    )
    parser.add_argument(
        "--output",
        default="data/jobs_scored.csv",
        help="Output CSV path (default: data/jobs_scored.csv)",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    root = Path(__file__).resolve().parents[1]
    requested_input = root / args.input
    fallback_input = root / "data" / "jobs_leads_example.csv"
    output_csv = root / args.output

    if requested_input.exists():
        source = requested_input
    elif args.input == "data/jobs_leads.csv" and fallback_input.exists():
        source = fallback_input
    else:
        raise FileNotFoundError(
            f"Input file not found: {requested_input}. "
            "Create it or use --input with an existing CSV path."
        )

    count = rank_leads(source, output_csv)
    print(f"Ranked {count} leads from: {source}")
    print(f"Output written to: {output_csv}")


if __name__ == "__main__":
    main()
