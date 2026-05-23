#!/usr/bin/env python3
"""Create a minimal Specification-Driven Coding package from a project profile.

Official pipeline: Raw request -> Intake -> Specification -> Project Profile Selection -> Vertical Blueprint -> Plan -> Tasks -> Implementation -> Evaluation Scorecard -> Release/Iteration.
"""
from __future__ import annotations
from pathlib import Path
import argparse
import json
import re
import shutil

ROOT = Path(__file__).resolve().parents[1]
PROJECT_TYPES = ROOT / "project-types"
TEMPLATES = ROOT / ".specify" / "templates" / "overrides"

def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-") or "project"

def profiles() -> dict[str, Path]:
    items = {}
    for path in PROJECT_TYPES.glob("[0-9][0-9]-*.md"):
        text = path.read_text(encoding="utf-8")
        match = re.search(r"Profile id: `([^`]+)`", text)
        if match:
            items[match.group(1)] = path
    return dict(sorted(items.items()))

def list_profiles() -> None:
    for key, path in profiles().items():
        title = path.read_text(encoding="utf-8").splitlines()[0].lstrip("# ")
        print(f"{key:35s} {title}")

def create(args: argparse.Namespace) -> None:
    profs = profiles()
    if args.type not in profs:
        raise SystemExit(f"Unknown project type: {args.type}. Run --list.")
    slug = slugify(args.name)
    out = Path(args.out).resolve() / "specs" / f"001-{slug}"
    if out.exists():
        raise SystemExit(
            "Output folder already exists: "
            f"{out}. Choose a different --out path or remove the existing scaffold first."
        )
    out.parent.mkdir(parents=True, exist_ok=True)
    out.mkdir(exist_ok=False)

    replacements = {"[TITLE]": args.name}
    (out / "raw-request.md").write_text(
        f"# Raw request: {args.name}\n\nReplace this with the original unnormalized request.\n",
        encoding="utf-8",
    )
    (out / "intake.md").write_text(
        "# Intake\n\n"
        "## Mode\n\n"
        "## Blocking questions\n\n"
        "## Reversible assumptions\n\n"
        "## Non-goals\n\n"
        "## Anti-genericity constraints\n\n"
        "## Required blueprint\n\n",
        encoding="utf-8",
    )
    for template_name, target_name in [
        ("spec-template.md", "spec.md"),
        ("blueprint-template.md", "blueprint.md"),
        ("plan-template.md", "plan.md"),
        ("tasks-template.md", "tasks.md"),
        ("scorecard-template.md", "scorecard.md"),
        ("research-template.md", "research.md"),
        ("acceptance-template.md", "acceptance.md"),
        ("data-model-template.md", "data-model.md"),
        ("quickstart-template.md", "quickstart.md"),
    ]:
        text = (TEMPLATES / template_name).read_text(encoding="utf-8")
        for old, new in replacements.items():
            text = text.replace(old, new)
        (out / target_name).write_text(text, encoding="utf-8")

    shutil.copy2(profs[args.type], out / "project-profile.md")
    manifest = {
        "methodology": "Specification-Driven Coding",
        "official_pipeline": [
            "Raw request",
            "Intake",
            "Specification",
            "Project Profile Selection",
            "Vertical Blueprint",
            "Plan",
            "Tasks",
            "Implementation",
            "Evaluation Scorecard",
            "Release/Iteration",
        ],
        "project_profile": args.type,
        "artifacts": [
            "raw-request.md",
            "intake.md",
            "spec.md",
            "project-profile.md",
            "blueprint.md",
            "plan.md",
            "tasks.md",
            "scorecard.md",
            "artifact-manifest.json",
        ],
        "gates": [
            "Clarify or declare reversible assumptions before blueprint",
            "Compile Vertical Blueprint before final plan and tasks",
            "Validate implementation against scorecard before release",
        ],
    }
    (out / "artifact-manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(f"Created {out}")

def main() -> int:
    parser = argparse.ArgumentParser(description="Specification-Driven Coding scaffold utility")
    parser.add_argument("--list", action="store_true", help="list available project profiles")
    parser.add_argument("--type", help="project profile id")
    parser.add_argument("--name", default="New Specification-Driven Coding Project", help="project/feature name")
    parser.add_argument("--out", default=".specification-driven-coding-workspace", help="output directory")
    args = parser.parse_args()

    if args.list:
        list_profiles()
        return 0
    if not args.type:
        parser.error("--type is required unless --list is used")
    create(args)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
