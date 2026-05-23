#!/usr/bin/env python3
"""Terminal demo for Specification-Driven Coding benchmark artifacts."""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "benchmarks" / "fixtures"
GOLDEN = ROOT / "benchmarks" / "golden"
PRIMARY_DEMO_FIXTURE = "001-builder-habit-dashboard"


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8").strip()


def first_paragraph(text: str, limit: int = 280) -> str:
    lines = [line.strip() for line in text.splitlines() if line.strip() and not line.startswith("#")]
    value = " ".join(lines)
    if len(value) <= limit:
        return value
    return value[: limit - 3].rstrip() + "..."


def section(text: str, heading: str) -> str:
    pattern = re.compile(rf"^##\s+{re.escape(heading)}\s*$", flags=re.MULTILINE | re.IGNORECASE)
    match = pattern.search(text)
    if not match:
        return ""
    start = match.end()
    next_heading = re.search(r"^##\s+", text[start:], flags=re.MULTILINE)
    end = start + next_heading.start() if next_heading else len(text)
    return text[start:end].strip()


def bullets(text: str, limit: int | None = None) -> list[str]:
    items = []
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("- [ ] "):
            items.append(stripped[6:].strip())
        elif stripped.startswith("- "):
            items.append(stripped[2:].strip())
    return items[:limit] if limit else items


def scorecard_result(text: str) -> str:
    result = section(text, "Result")
    if result:
        return first_paragraph(result, 160)
    gate = re.search(r"Gate:\s*(\w+)", text, flags=re.IGNORECASE)
    return f"Gate: {gate.group(1).upper()}" if gate else "Scorecard result unavailable"


def scorecard_scores(text: str) -> list[str]:
    rows = []
    for line in text.splitlines():
        if not line.startswith("|") or line.startswith("|---") or "Area" in line:
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) >= 2:
            rows.append(f"{cells[0]}: {cells[1]}")
    return rows


def fallback_less_generic(expected: dict[str, object], fixture: str) -> str:
    constraints = expected.get("anti_genericity_constraints", [])
    criteria = expected.get("acceptance_criteria", [])
    rationale = expected.get("stack_rationale", [])
    parts = [
        f"The raw prompt for {fixture} leaves product shape open.",
        "The Specification-Driven Coding chain adds a project profile.",
    ]
    if constraints:
        parts.append(f"It adds anti-genericity constraints ({'; '.join(str(item) for item in constraints[:3])}).")
    if criteria:
        parts.append(f"It adds acceptance criteria ({'; '.join(str(item) for item in criteria[:3])}).")
    if rationale:
        parts.append(f"It adds stack rationale ({'; '.join(str(item) for item in rationale[:3])}).")
    parts.append("It requires a scorecard before release.")
    return " ".join(parts)


def fixture_ids() -> list[str]:
    if not FIXTURES.exists():
        return []
    return sorted(path.name for path in FIXTURES.iterdir() if path.is_dir())


def load_demo(fixture: str) -> dict[str, object]:
    fixture_dir = FIXTURES / fixture
    golden_dir = GOLDEN / fixture
    if not fixture_dir.exists():
        raise FileNotFoundError(f"Unknown fixture: {fixture}")
    if not golden_dir.exists():
        raise FileNotFoundError(f"Missing golden artifacts for fixture: {fixture}")

    expected = json.loads((fixture_dir / "expected.json").read_text(encoding="utf-8"))
    raw_prompt = read_text(fixture_dir / "raw-prompt.md")
    sdc_prompt = read_text(fixture_dir / "sdc-prompt.md")
    intake = read_text(golden_dir / "intake.md")
    blueprint = read_text(golden_dir / "blueprint.md")
    plan = read_text(golden_dir / "plan.md")
    tasks = read_text(golden_dir / "tasks.md")
    scorecard = read_text(golden_dir / "scorecard.md")

    task_items = bullets(tasks)
    plan_slices = [line.strip("# ").strip() for line in plan.splitlines() if line.startswith("## Slice")]
    anti_genericity = expected.get("anti_genericity_constraints", [])
    assumptions = bullets(section(intake, "Reversible assumptions"), limit=4)
    blueprint_summary = first_paragraph(section(blueprint, "Product/domain intent") or blueprint, 220)

    return {
        "fixture": fixture,
        "raw_prompt": first_paragraph(raw_prompt, 280),
        "sdc_prompt_summary": first_paragraph(sdc_prompt, 320),
        "project_profile": expected.get("project_profile", ""),
        "anti_genericity_constraints": anti_genericity,
        "reversible_assumptions": assumptions,
        "vertical_blueprint_summary": blueprint_summary,
        "plan_slices": plan_slices,
        "task_count": len(task_items),
        "scorecard_result": scorecard_result(scorecard),
        "scorecard_scores": scorecard_scores(scorecard),
        "why_less_generic": fallback_less_generic(expected, fixture),
        "artifacts": {
            "fixture_dir": str(fixture_dir.relative_to(ROOT)),
            "golden_dir": str(golden_dir.relative_to(ROOT)),
        },
    }


def print_list() -> int:
    for fixture in fixture_ids():
        expected_path = FIXTURES / fixture / "expected.json"
        profile = ""
        if expected_path.exists():
            profile = json.loads(expected_path.read_text(encoding="utf-8")).get("project_profile", "")
        print(f"{fixture:36} {profile}")
    return 0


def print_demo(payload: dict[str, object], verbose: bool) -> int:
    print("# Specification-Driven Coding Demo")
    print()
    print(f"Fixture: {payload['fixture']}")
    print(f"Project profile: {payload['project_profile']}")
    print()
    print("Raw prompt:")
    print(f"  {payload['raw_prompt']}")
    print()
    print("SDC prompt summary:")
    print(f"  {payload['sdc_prompt_summary']}")
    print()
    print("Anti-genericity constraints:")
    for item in payload["anti_genericity_constraints"]:
        print(f"  - {item}")
    print()
    print("Reversible assumptions:")
    for item in payload["reversible_assumptions"]:
        print(f"  - {item}")
    print()
    print("Vertical Blueprint:")
    print(f"  {payload['vertical_blueprint_summary']}")
    print()
    print("Plan slices:")
    for item in payload["plan_slices"]:
        print(f"  - {item}")
    print()
    print(f"Task count: {payload['task_count']}")
    print(f"Scorecard: {payload['scorecard_result']}")
    if verbose:
        print()
        print("Scorecard scores:")
        for item in payload["scorecard_scores"]:
            print(f"  - {item}")
    print()
    print("Why this is less generic:")
    print(f"  {payload['why_less_generic']}")
    print()
    print("Demo scope:")
    print("  Proves reproducible artifact discipline and anti-genericity constraints.")
    print("  Does not prove universal product superiority without real builder comparison.")
    return 0


def print_markdown(payload: dict[str, object], verbose: bool) -> int:
    print("# Specification-Driven Coding Demo")
    print()
    print(f"- Fixture: `{payload['fixture']}`")
    print(f"- Project profile: `{payload['project_profile']}`")
    print(f"- Task count: `{payload['task_count']}`")
    print(f"- Scorecard: {payload['scorecard_result']}")
    print()
    print("## Raw Prompt")
    print()
    print(payload["raw_prompt"])
    print()
    print("## Specification-Driven Coding Prompt Summary")
    print()
    print(payload["sdc_prompt_summary"])
    print()
    print("## Anti-Genericity Constraints")
    print()
    for item in payload["anti_genericity_constraints"]:
        print(f"- {item}")
    print()
    print("## Vertical Blueprint Highlights")
    print()
    print(payload["vertical_blueprint_summary"])
    print()
    print("## Plan Slices")
    print()
    for item in payload["plan_slices"]:
        print(f"- {item}")
    print()
    print("## What The Raw Prompt Would Likely Miss")
    print()
    print(payload["why_less_generic"])
    print()
    print("## What SDC Forces The Agent Or Builder To Decide")
    print()
    print("- Project profile and execution mode.")
    print("- Stack rationale and rejected defaults.")
    print("- Non-goals, assumptions, acceptance criteria, and scorecard risks.")
    if verbose:
        print()
        print("## Scorecard Scores")
        print()
        for item in payload["scorecard_scores"]:
            print(f"- {item}")
    return 0


def run_demo(args: argparse.Namespace) -> int:
    try:
        payload = load_demo(args.fixture)
    except (FileNotFoundError, json.JSONDecodeError) as exc:
        print(str(exc), file=sys.stderr)
        return 1
    if args.format == "json":
        print(json.dumps(payload, indent=2))
        return 0
    if args.format == "markdown":
        return print_markdown(payload, args.verbose)
    return print_demo(payload, args.verbose)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Show a compact Specification-Driven Coding artifact demo")
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("list", help="list demo fixtures")
    run = subparsers.add_parser("run", help="run a terminal walkthrough for a fixture")
    run.add_argument("--fixture", required=True, help="benchmark fixture id")
    run.add_argument("--verbose", action="store_true", help="include extra artifact excerpts")
    run.add_argument("--format", choices=["text", "json", "markdown"], default="text", help="output format")

    args = parser.parse_args(argv)
    if args.command == "list":
        return print_list()
    if args.command == "run":
        return run_demo(args)
    parser.error(f"unknown command: {args.command}")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
