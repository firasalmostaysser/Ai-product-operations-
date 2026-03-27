#!/usr/bin/env python3
"""Simple local simulator for AI support ticket triage.

This script does not call external AI APIs by default.
It uses rule-based logic so you can prove workflow architecture quickly
and later replace `classify_ticket` with an LLM call.
"""

from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Ticket:
    ticket_id: str
    source: str
    title: str
    description: str


@dataclass(frozen=True)
class TriageResult:
    ticket_id: str
    category: str
    priority: str
    owner_team: str
    suggested_response: str


KEYWORD_RULES = {
    "billing": ("billing", "high", "finance-ops"),
    "invoice": ("billing", "high", "finance-ops"),
    "payment": ("billing", "high", "finance-ops"),
    "bug": ("product-bug", "medium", "product-engineering"),
    "error": ("product-bug", "high", "product-engineering"),
    "crash": ("product-bug", "critical", "product-engineering"),
    "login": ("account-access", "high", "customer-support"),
    "password": ("account-access", "high", "customer-support"),
    "feature": ("feature-request", "low", "product-operations"),
    "integration": ("integration", "medium", "solutions-engineering"),
}


def load_tickets(path: Path) -> list[Ticket]:
    tickets: list[Ticket] = []
    with path.open(newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            tickets.append(
                Ticket(
                    ticket_id=row.get("ticket_id", "").strip(),
                    source=row.get("source", "").strip(),
                    title=row.get("title", "").strip(),
                    description=row.get("description", "").strip(),
                )
            )
    return tickets


def classify_ticket(ticket: Ticket) -> TriageResult:
    text = f"{ticket.title} {ticket.description}".lower()
    for keyword, (category, priority, owner_team) in KEYWORD_RULES.items():
        if keyword in text:
            return TriageResult(
                ticket_id=ticket.ticket_id,
                category=category,
                priority=priority,
                owner_team=owner_team,
                suggested_response=(
                    f"Ticket categorized as {category}. "
                    f"Route to {owner_team} with {priority} priority."
                ),
            )

    return TriageResult(
        ticket_id=ticket.ticket_id,
        category="general-inquiry",
        priority="low",
        owner_team="customer-support",
        suggested_response=(
            "Ticket categorized as general-inquiry. "
            "Route to customer-support for first response."
        ),
    )


def save_results(path: Path, results: list[TriageResult]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=[
                "ticket_id",
                "category",
                "priority",
                "owner_team",
                "suggested_response",
            ],
        )
        writer.writeheader()
        for result in results:
            writer.writerow(
                {
                    "ticket_id": result.ticket_id,
                    "category": result.category,
                    "priority": result.priority,
                    "owner_team": result.owner_team,
                    "suggested_response": result.suggested_response,
                }
            )


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    input_file = root / "sample-data" / "sample_tickets.csv"
    output_file = root / "results" / "triage_results.csv"

    tickets = load_tickets(input_file)
    results = [classify_ticket(ticket) for ticket in tickets]
    save_results(output_file, results)

    print(f"Processed {len(results)} tickets.")
    print(f"Results written to: {output_file}")


if __name__ == "__main__":
    main()
