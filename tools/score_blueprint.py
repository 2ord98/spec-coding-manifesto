#!/usr/bin/env python3
"""Heuristic structural scorer for Specification-Driven Coding blueprints.

This checks section/keyword coverage. It is a lightweight gate, not a
semantic quality evaluator.

Usage:
  python3 tools/score_blueprint.py blueprints/02-full-project-blueprint.md
"""
from pathlib import Path
import sys

CHECKS = [
    ("Role contract", 10, ["role contract", "agisci come"]),
    ("Product/domain intent", 10, ["product", "intent", "dominio", "domain"]),
    ("Project/profile or routing", 10, ["project profile", "profile"]),
    ("Assumptions/questions", 10, ["assumption", "assun", "domande"]),
    ("Stack/architecture", 15, ["stack", "architecture", "architettura"]),
    ("Security/privacy", 15, ["security", "sicurezza", "privacy", "nonce"]),
    ("Performance/fallback", 10, ["performance", "fallback", "budget"]),
    ("Output/file contract", 10, ["output", "file", "root folder", "file tree"]),
    ("Tests/acceptance", 5, ["test", "acceptance", "gate"]),
    ("Scorecard", 5, ["scorecard", "punteggio"]),
]


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python3 tools/score_blueprint.py <blueprint.md>")
        return 2
    path = Path(sys.argv[1])
    if not path.exists():
        print(f"FAIL: file not found: {path}")
        return 1
    text = path.read_text(encoding="utf-8", errors="ignore").lower()
    total = 0
    rows = []
    for name, weight, keywords in CHECKS:
        hit = any(k.lower() in text for k in keywords)
        score = weight if hit else 0
        total += score
        rows.append((name, score, weight))
    print(f"Blueprint score: {total}/100")
    for name, score, weight in rows:
        status = "PASS" if score else "MISS"
        print(f"{status:4} {score:>2}/{weight:<2} {name}")
    if total < 75:
        print("Gate: FAIL — improve the blueprint before implementation")
        return 1
    print("Gate: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
