#!/usr/bin/env python3
"""Structural Continuous Specification Enforcement gate."""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

CORE_ARTIFACTS = ["spec.md", "blueprint.md", "plan.md", "tasks.md", "scorecard.md"]
WORKSPACE_ARTIFACTS = [
    "raw-request.md",
    "intake.md",
    "spec.md",
    "project-profile.md",
    "blueprint.md",
    "plan.md",
    "tasks.md",
    "scorecard.md",
]
OPTIONAL_ARTIFACTS = ["intake.md", "artifact-manifest.json", "implementation-notes.md", "exceptions.md"]
IMPLEMENTATION_SUFFIXES = {
    ".py",
    ".js",
    ".ts",
    ".tsx",
    ".jsx",
    ".php",
    ".cs",
    ".java",
    ".go",
    ".rs",
    ".swift",
    ".kt",
    ".sql",
    ".html",
    ".css",
}
TIMESTAMP_DRIFT_SECONDS = 2.0
EXCLUDED_DIRS = {".git", "__pycache__", "node_modules", ".venv", "benchmarks/reports"}
STOPWORDS = {
    "about",
    "after",
    "also",
    "and",
    "are",
    "before",
    "contract",
    "from",
    "into",
    "must",
    "not",
    "only",
    "that",
    "the",
    "this",
    "with",
    "without",
}


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def has_checked_task(text: str) -> bool:
    return bool(re.search(r"- \[[xX]\]", text)) or "done" in text.lower() or "complete" in text.lower()


def key_terms(*texts: str, limit: int = 28) -> list[str]:
    counts: dict[str, int] = {}
    for text in texts:
        for token in re.findall(r"[A-Za-z][A-Za-z0-9-]{4,}", text.lower()):
            if token in STOPWORDS:
                continue
            counts[token] = counts.get(token, 0) + 1
    return [term for term, _ in sorted(counts.items(), key=lambda item: (-item[1], item[0]))[:limit]]


def coverage(terms: list[str], text: str) -> tuple[int, list[str]]:
    if not terms:
        return 100, []
    normalized = text.lower()
    missing = [term for term in terms if term not in normalized]
    score = round(((len(terms) - len(missing)) / len(terms)) * 100)
    return score, missing[:10]


def implementation_files(path: Path) -> list[Path]:
    files: list[Path] = []
    for child in path.rglob("*"):
        if not child.is_file():
            continue
        parts = set(child.relative_to(path).parts)
        if parts & EXCLUDED_DIRS:
            continue
        if "benchmarks" in parts and "reports" in parts:
            continue
        if child.name in set(WORKSPACE_ARTIFACTS + CORE_ARTIFACTS + OPTIONAL_ARTIFACTS):
            continue
        if child.suffix.lower() in IMPLEMENTATION_SUFFIXES:
            files.append(child)
    return sorted(files)


def add_issue(issues: list[dict[str, str]], severity: str, kind: str, message: str, decision: str) -> None:
    issues.append({"severity": severity, "type": kind, "message": message, "decision": decision})


def check_workspace(path: Path) -> dict[str, object]:
    path = path.resolve()
    issues: list[dict[str, str]] = []
    if not path.exists() or not path.is_dir():
        add_issue(issues, "FAIL", "workspace", f"Path does not exist or is not a directory: {path}", "provide a valid workspace path")
        return result(path, issues, {}, [], 0)

    manifest_exists = (path / "artifact-manifest.json").exists()
    required = WORKSPACE_ARTIFACTS if manifest_exists or (path / "raw-request.md").exists() else CORE_ARTIFACTS
    artifacts = {name: path / name for name in sorted(set(required + OPTIONAL_ARTIFACTS))}

    for name in required:
        if not (path / name).exists():
            add_issue(issues, "FAIL", "artifact-completeness", f"Missing required artifact: {name}", "update specification package")

    if not (path / "scorecard.md").exists():
        add_issue(issues, "FAIL", "scorecard", "Missing scorecard.md", "create or refresh scorecard")

    if (path / "plan.md").exists() and not (path / "blueprint.md").exists():
        add_issue(issues, "FAIL", "blueprint-order", "plan.md exists without blueprint.md", "create Vertical Blueprint before final plan")
    if (path / "tasks.md").exists() and not (path / "blueprint.md").exists():
        add_issue(issues, "FAIL", "blueprint-order", "tasks.md exists without blueprint.md", "create Vertical Blueprint before tasks")

    texts = {name: read(file) for name, file in artifacts.items() if file.exists() and file.suffix == ".md"}
    spec_text = texts.get("spec.md", "")
    blueprint_text = texts.get("blueprint.md", "")
    plan_text = texts.get("plan.md", "")
    tasks_text = texts.get("tasks.md", "")
    scorecard_text = texts.get("scorecard.md", "")
    combined_downstream = "\n".join([plan_text, tasks_text, scorecard_text])

    terms = key_terms(spec_text, blueprint_text)
    term_score, missing_terms = coverage(terms, combined_downstream)
    if term_score < 70:
        add_issue(
            issues,
            "WARN",
            "requirement-drift",
            f"Plan/tasks/scorecard weakly cover spec and blueprint terms: missing {', '.join(missing_terms)}",
            "update specification, update Vertical Blueprint, fix implementation/artifact, or accept documented exception",
        )

    checks = {
        "non-goals": "non-goal",
        "assumptions": "assumption",
        "acceptance criteria": "acceptance",
        "security/privacy": "privacy",
        "anti-genericity": "generic",
        "risks": "risk",
    }
    for label, needle in checks.items():
        if needle not in "\n".join(texts.values()).lower():
            add_issue(issues, "WARN", label, f"Missing or weak {label} coverage", "update relevant artifact or accept documented exception")

    impl_files = implementation_files(path)
    if impl_files:
        if tasks_text and not has_checked_task(tasks_text):
            add_issue(
                issues,
                "WARN",
                "implementation-without-task-update",
                "Implementation-like files exist but tasks.md has no completed markers.",
                "update tasks or accept documented exception",
            )
        newest_impl = max(file.stat().st_mtime for file in impl_files)
        for name in ["spec.md", "blueprint.md", "scorecard.md"]:
            file = path / name
            if file.exists() and newest_impl - file.stat().st_mtime > TIMESTAMP_DRIFT_SECONDS:
                kind = "scorecard-freshness" if name == "scorecard.md" else "potential-drift"
                add_issue(
                    issues,
                    "WARN",
                    kind,
                    f"Implementation-like files are newer than {name}.",
                    "review divergence and update artifact or correct implementation",
                )

    if "exception" in scorecard_text.lower() and not (path / "exceptions.md").exists():
        add_issue(issues, "WARN", "documented-exceptions", "Scorecard mentions exception without exceptions.md.", "create exceptions.md or remove unresolved exception")

    score = enforcement_score(issues, term_score, texts, impl_files)
    return result(path, issues, artifacts, impl_files, score, term_score=term_score, key_terms=terms)


def enforcement_score(
    issues: list[dict[str, str]], term_score: int, texts: dict[str, str], impl_files: list[Path]
) -> int:
    score = 100
    score -= sum(18 for issue in issues if issue["severity"] == "FAIL")
    score -= sum(6 for issue in issues if issue["severity"] == "WARN")
    score -= max(0, 85 - term_score) // 3
    required_needles = ["acceptance", "privacy", "generic", "risk"]
    corpus = "\n".join(texts.values()).lower()
    score -= sum(4 for needle in required_needles if needle not in corpus)
    if impl_files and "scorecard.md" not in texts:
        score -= 10
    return max(0, min(100, score))


def result(
    path: Path,
    issues: list[dict[str, str]],
    artifacts: dict[str, Path],
    impl_files: list[Path],
    score: int,
    term_score: int | None = None,
    key_terms: list[str] | None = None,
) -> dict[str, object]:
    if any(issue["severity"] == "FAIL" for issue in issues):
        status = "FAIL"
    elif issues or score < 90:
        status = "WARN"
    else:
        status = "PASS"
    if score >= 90:
        gate = "strong alignment"
    elif score >= 75:
        gate = "acceptable with declared risk"
    else:
        gate = "requires decision before release"
    return {
        "status": status,
        "score": score,
        "gate": gate,
        "path": rel(path),
        "structural_only": True,
        "artifacts": {name: file.exists() for name, file in artifacts.items()},
        "implementation_files": [rel(file) for file in impl_files],
        "term_coverage": term_score,
        "key_terms": key_terms or [],
        "divergences": issues,
        "required_decisions": sorted({issue["decision"] for issue in issues}),
        "allowed_decisions": [
            "update specification",
            "update Vertical Blueprint",
            "fix implementation/artifact",
            "accept documented exception",
        ],
    }


def print_text(payload: dict[str, object]) -> None:
    print("# Continuous Specification Enforcement")
    print()
    print(f"Path: {payload['path']}")
    print(f"Status: {payload['status']}")
    print(f"Score: {payload['score']}/100")
    print(f"Gate: {payload['gate']}")
    print("Scope: structural enforcement gate, not semantic proof.")
    print()
    divergences = payload["divergences"]
    if divergences:
        print("Divergences:")
        for item in divergences:
            print(f"- {item['severity']} {item['type']}: {item['message']}")
            print(f"  Decision: {item['decision']}")
    else:
        print("Divergences: none detected structurally.")
    print()
    print("Allowed decisions if divergence appears:")
    for decision in payload["allowed_decisions"]:
        print(f"- {decision}")


def report_markdown(payload: dict[str, object]) -> str:
    lines = [
        "# Continuous Specification Enforcement Report",
        "",
        f"- Path: `{payload['path']}`",
        f"- Status: `{payload['status']}`",
        f"- Score: `{payload['score']}/100`",
        f"- Gate: {payload['gate']}",
        "- Scope: structural enforcement gate, not semantic proof.",
        "",
        "## Divergences",
    ]
    divergences = payload["divergences"]
    if divergences:
        for item in divergences:
            lines.append(f"- `{item['severity']}` `{item['type']}`: {item['message']} Decision: {item['decision']}.")
    else:
        lines.append("- None detected structurally.")
    lines.extend(["", "## Allowed Decisions"])
    for decision in payload["allowed_decisions"]:
        lines.append(f"- {decision}")
    lines.append("")
    return "\n".join(lines)


def check(args: argparse.Namespace) -> int:
    target = Path(args.path or args.workspace)
    payload = check_workspace(target)
    if args.write_report:
        report_path = target / "sdc-enforcement-report.md"
        report_path.write_text(report_markdown(payload), encoding="utf-8")
        payload["report"] = rel(report_path)
    if args.format == "json":
        print(json.dumps(payload, indent=2))
    else:
        print_text(payload)
        if "report" in payload:
            print()
            print(f"Report: {payload['report']}")
    return 1 if payload["status"] == "FAIL" else 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Structural Continuous Specification Enforcement")
    subparsers = parser.add_subparsers(dest="command", required=True)
    check_parser = subparsers.add_parser("check", help="check artifact alignment in a workspace or golden folder")
    check_parser.add_argument("--path", help="artifact folder to check")
    check_parser.add_argument("--workspace", help="alias for --path")
    check_parser.add_argument("--format", choices=["text", "json"], default="text", help="output format")
    check_parser.add_argument("--write-report", action="store_true", help="write sdc-enforcement-report.md in the target folder")
    args = parser.parse_args(argv)
    if args.command == "check":
        if not args.path and not args.workspace:
            parser.error("sdc_enforce.py check requires --path or --workspace")
        return check(args)
    parser.error(f"unknown command: {args.command}")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
