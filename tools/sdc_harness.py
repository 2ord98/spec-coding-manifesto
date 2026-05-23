#!/usr/bin/env python3
"""Reproducible structural harness for Specification-Driven Coding fixtures."""
from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "benchmarks" / "fixtures"
GOLDEN = ROOT / "benchmarks" / "golden"
REPORTS = ROOT / "benchmarks" / "reports"

REQUIRED_GOLDEN_FILES = [
    "intake.md",
    "spec.md",
    "blueprint.md",
    "plan.md",
    "tasks.md",
    "scorecard.md",
]

EXPECTED_KEYS = [
    "project_profile",
    "anti_genericity_constraints",
    "acceptance_criteria",
    "stack_rationale",
    "quality_gates",
]


@dataclass(frozen=True)
class Check:
    name: str
    passed: bool
    detail: str


def words(path: Path) -> set[str]:
    if not path.exists():
        return set()
    return set(re.findall(r"[a-zA-Z][a-zA-Z0-9_-]{2,}", path.read_text(encoding="utf-8").lower()))


def load_expected(fixture: str) -> dict:
    path = FIXTURES / fixture / "expected.json"
    if not path.exists():
        raise SystemExit(f"Missing fixture expectations: {path.relative_to(ROOT)}")
    return json.loads(path.read_text(encoding="utf-8"))


def check_fixture(fixture: str) -> list[Check]:
    fixture_dir = FIXTURES / fixture
    golden_dir = GOLDEN / fixture
    expected = load_expected(fixture)
    checks: list[Check] = []

    for name in ["raw-prompt.md", "sdc-prompt.md", "expected.json"]:
        path = fixture_dir / name
        checks.append(Check(f"fixture has {name}", path.exists(), str(path.relative_to(ROOT))))

    raw_words = words(fixture_dir / "raw-prompt.md")
    sdc_words = words(fixture_dir / "sdc-prompt.md")
    checks.append(Check("sdc prompt is more constrained than raw prompt", len(sdc_words) > len(raw_words) * 2, f"raw={len(raw_words)} unique, sdc={len(sdc_words)} unique"))

    for name in REQUIRED_GOLDEN_FILES:
        path = golden_dir / name
        checks.append(Check(f"golden has {name}", path.exists(), str(path.relative_to(ROOT))))

    all_golden = "\n".join(
        (golden_dir / name).read_text(encoding="utf-8", errors="ignore")
        for name in REQUIRED_GOLDEN_FILES
        if (golden_dir / name).exists()
    ).lower()

    for key in EXPECTED_KEYS:
        values = expected.get(key, [])
        if isinstance(values, str):
            values = [values]
        missing = [value for value in values if value.lower() not in all_golden]
        checks.append(Check(f"expected {key} covered", not missing, "missing: " + ", ".join(missing) if missing else "covered"))

    scorecard = (golden_dir / "scorecard.md").read_text(encoding="utf-8", errors="ignore").lower() if (golden_dir / "scorecard.md").exists() else ""
    for phrase in ["anti-genericity", "domain fit", "risks", "next fixes"]:
        checks.append(Check(f"scorecard includes {phrase}", phrase in scorecard, phrase))

    return checks


def write_report(fixture: str, checks: list[Check]) -> Path:
    REPORTS.mkdir(parents=True, exist_ok=True)
    passed = sum(1 for check in checks if check.passed)
    total = len(checks)
    report = REPORTS / f"{fixture}.md"
    lines = [
        f"# Harness report: {fixture}",
        "",
        "Generated: reproducible local harness run",
        f"Result: {passed}/{total}",
        "",
        "| Check | Result | Detail |",
        "|---|---:|---|",
    ]
    for check in checks:
        result = "PASS" if check.passed else "FAIL"
        lines.append(f"| {check.name} | {result} | {check.detail} |")
    lines.extend([
        "",
        "## Interpretation",
        "",
        "This harness is structural and reproducible. It verifies fixture completeness, golden artifact coverage, and scorecard shape. It does not claim semantic product quality without human or agent review.",
        "",
    ])
    content = "\n".join(lines)
    if not report.exists() or report.read_text(encoding="utf-8") != content:
        report.write_text(content, encoding="utf-8")
    return report


def list_fixtures() -> int:
    for path in sorted(FIXTURES.iterdir()):
        if path.is_dir():
            print(path.name)
    return 0


def run_single_fixture(fixture: str) -> tuple[int, int]:
    checks = check_fixture(fixture)
    report = write_report(fixture, checks)
    passed = sum(1 for check in checks if check.passed)
    total = len(checks)
    print(f"Harness: {fixture} {passed}/{total}")
    print(f"Report: {report.relative_to(ROOT)}")
    return passed, total


def run_fixture(args: argparse.Namespace) -> int:
    passed, total = run_single_fixture(args.fixture)
    return 0 if passed == total else 1


def run_all_fixtures() -> int:
    fixture_ids = [path.name for path in sorted(FIXTURES.iterdir()) if path.is_dir()]
    overall_ok = True
    for fixture in fixture_ids:
        passed, total = run_single_fixture(fixture)
        overall_ok = overall_ok and (passed == total)
    return 0 if overall_ok else 1


def main() -> int:
    parser = argparse.ArgumentParser(description="Run Specification-Driven Coding benchmark fixtures")
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("list", help="list available benchmark fixtures")
    run = subparsers.add_parser("run", help="run a benchmark fixture")
    target = run.add_mutually_exclusive_group(required=True)
    target.add_argument("--fixture", help="fixture id")
    target.add_argument("--all", action="store_true", help="run all available fixtures")

    args = parser.parse_args()
    if args.command == "list":
        return list_fixtures()
    if args.command == "run":
        if args.all:
            return run_all_fixtures()
        return run_fixture(args)
    parser.error(f"unknown command: {args.command}")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
