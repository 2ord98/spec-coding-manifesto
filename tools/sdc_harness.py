#!/usr/bin/env python3
"""Reproducible structural harness for Specification-Driven Coding fixtures."""
from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.sdc_signature import DecisionAssertion

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
COMPILE_FIXTURE = "004-compile-structural-validation"


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


def section_body(text: str, section: str) -> str:
    pattern = re.compile(rf"^## {re.escape(section)}\s*$", flags=re.MULTILINE)
    match = pattern.search(text)
    if not match:
        return ""
    next_match = re.search(r"^## .+$", text[match.end() :], flags=re.MULTILINE)
    end = match.end() + next_match.start() if next_match else len(text)
    return text[match.end() : end].strip()


def blueprint_score(path: Path) -> int:
    completed = subprocess.run(
        [sys.executable, "tools/score_blueprint.py", str(path)],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    match = re.search(r"Blueprint score:\s*(\d+)/100", completed.stdout)
    if not match:
        return 0
    return int(match.group(1))


def check_compile_fixture(fixture: str) -> list[Check]:
    fixture_dir = FIXTURES / fixture
    golden_dir = GOLDEN / fixture
    expected = load_expected(fixture)
    checks: list[Check] = []

    expected_fields = {
        "critical_sections_filled": bool,
        "has_default_marker": bool,
        "ask_count_min": int,
        "assumption_count_min": int,
        "score_min": int,
        "required_sections": list,
        "forbidden_empty_sections": bool,
        "default_marker_text": str,
    }
    for key, expected_type in expected_fields.items():
        checks.append(Check(f"expected has {key}", isinstance(expected.get(key), expected_type), key))

    for name in ["raw-request.md", "expected.json"]:
        path = fixture_dir / name
        checks.append(Check(f"fixture has {name}", path.exists(), str(path.relative_to(ROOT))))

    required_workspace = [
        "raw-request.md",
        "intake.md",
        "spec.md",
        "project-profile.md",
        "blueprint.md",
        "plan.md",
        "tasks.md",
        "scorecard.md",
        "artifact-manifest.json",
    ]
    for name in required_workspace:
        path = golden_dir / name
        checks.append(Check(f"golden has {name}", path.exists(), str(path.relative_to(ROOT))))

    if any(not check.passed for check in checks):
        return checks

    with tempfile.TemporaryDirectory(prefix="sdc-harness-004-") as temp:
        temp_workspace = Path(temp) / "workspace"
        shutil.copytree(golden_dir, temp_workspace)
        shutil.copy2(fixture_dir / "raw-request.md", temp_workspace / "raw-request.md")
        completed = subprocess.run(
            [
                sys.executable,
                "tools/sdc_compile.py",
                "compile",
                "--workspace",
                str(temp_workspace),
                "--force",
                "--format",
                "json",
            ],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        checks.append(Check("compile command exits 0", completed.returncode == 0, completed.stderr.strip() or "exit 0"))
        try:
            compile_payload = json.loads(completed.stdout)
        except json.JSONDecodeError:
            compile_payload = {}
            checks.append(Check("compile output is JSON", False, completed.stdout[:120]))
        else:
            checks.append(Check("compile output is JSON", True, "parsed"))

        blueprint = (temp_workspace / "blueprint.md").read_text(encoding="utf-8", errors="ignore")
        corpus = "\n".join(
            (temp_workspace / name).read_text(encoding="utf-8", errors="ignore")
            for name in ["intake.md", "spec.md", "blueprint.md", "plan.md", "tasks.md", "scorecard.md"]
        )
        required_sections = expected.get("required_sections", [])
        missing_sections = [section for section in required_sections if f"## {section}" not in blueprint]
        checks.append(Check("required sections present", not missing_sections, ", ".join(missing_sections) or "covered"))

        empty_sections = [section for section in required_sections if not section_body(blueprint, section)]
        critical_filled = not empty_sections
        if expected.get("forbidden_empty_sections"):
            checks.append(Check("forbidden empty sections", critical_filled, ", ".join(empty_sections) or "none"))

        marker = expected.get("default_marker_text", "")
        has_default_marker = marker in blueprint
        checks.append(Check("default marker present", has_default_marker, marker))

        ask_count = corpus.count("[ASK:")
        assumption_count = corpus.count("[ASSUMPTION:")
        assertion = DecisionAssertion(
            critical_section_filled=critical_filled,
            has_default_marker=has_default_marker,
            ask_count=ask_count,
            assumption_count=assumption_count,
            score_min=expected.get("score_min", 80),
        )
        report = assertion.report()
        checks.append(Check("DecisionAssertion passes", bool(report["passes"]), json.dumps(report, sort_keys=True)))
        checks.append(Check("ask threshold", ask_count >= expected.get("ask_count_min", 0), f"{ask_count}"))
        checks.append(
            Check(
                "assumption threshold",
                assumption_count >= expected.get("assumption_count_min", 0),
                f"{assumption_count}",
            )
        )
        checks.append(Check("security baseline included", "Security Baseline" in blueprint, "Security Baseline"))
        checks.append(Check("performance budget included", "startup_or_first_response" in blueprint, "startup_or_first_response"))
        checks.append(Check("testing contract included", "Testing Contract" in blueprint, "Testing Contract"))
        checks.append(Check("scorecard exists", (temp_workspace / "scorecard.md").exists(), "scorecard.md"))
        decisions_path = temp_workspace / "decisions.jsonl"
        boundaries_path = temp_workspace / "capability-boundaries.json"
        checks.append(Check("decision ledger exists", decisions_path.exists(), "decisions.jsonl"))
        checks.append(Check("capability boundaries exist", boundaries_path.exists(), "capability-boundaries.json"))
        if decisions_path.exists():
            decision_lines = [line for line in decisions_path.read_text(encoding="utf-8").splitlines() if line.strip()]
            valid_decisions = True
            decision_ids: set[str] = set()
            for line in decision_lines:
                try:
                    decision = json.loads(line)
                except json.JSONDecodeError:
                    valid_decisions = False
                    break
                decision_id = decision.get("id")
                valid_decisions = valid_decisions and isinstance(decision_id, str) and bool(re.fullmatch(r"DEC-\d{3}", decision_id))
                valid_decisions = valid_decisions and decision_id not in decision_ids
                valid_decisions = valid_decisions and isinstance(decision.get("reversible"), bool)
                valid_decisions = valid_decisions and bool(decision.get("verification"))
                if isinstance(decision_id, str):
                    decision_ids.add(decision_id)
            checks.append(Check("decision ledger valid", valid_decisions and bool(decision_lines), f"{len(decision_lines)} entries"))
        if boundaries_path.exists():
            try:
                boundaries = json.loads(boundaries_path.read_text(encoding="utf-8"))
            except json.JSONDecodeError:
                boundaries = {}
            required_boundaries = {
                "forbidden_libraries",
                "forbidden_patterns",
                "off_limits_layers",
                "requires_approval",
                "allowed_external_services",
                "data_boundary",
                "network_boundary",
                "write_boundary",
                "tool_boundary",
            }
            boundary_lists = [
                "forbidden_libraries",
                "forbidden_patterns",
                "off_limits_layers",
                "requires_approval",
                "allowed_external_services",
            ]
            valid_boundaries = isinstance(boundaries, dict) and required_boundaries <= set(boundaries)
            valid_boundaries = valid_boundaries and all(isinstance(boundaries.get(key), list) for key in boundary_lists)
            valid_boundaries = valid_boundaries and all(
                isinstance(boundaries.get(key), str) and boundaries.get(key, "").strip()
                for key in required_boundaries - set(boundary_lists)
            )
            checks.append(Check("capability boundaries valid", valid_boundaries, "manual schema check"))
        score = blueprint_score(temp_workspace / "blueprint.md")
        checks.append(Check("blueprint score threshold", score >= expected.get("score_min", 80), f"{score}/100"))
        checks.append(
            Check(
                "json includes assertion report",
                isinstance(compile_payload.get("assertion"), dict),
                "assertion" if compile_payload else "missing",
            )
        )
    return checks


def check_fixture(fixture: str) -> list[Check]:
    if fixture == COMPILE_FIXTURE:
        return check_compile_fixture(fixture)

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
