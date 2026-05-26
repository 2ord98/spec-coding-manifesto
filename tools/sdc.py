#!/usr/bin/env python3
"""Lightweight command surface for Specification-Driven Coding.

This script does not replace the prompt files. It exposes the repository's
command model as a small dispatcher over existing prompts and tools.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PYTHON = sys.executable
INTEGRATIONS_CATALOG = ROOT / "integrations" / "catalog.json"
EXTENSIONS_CATALOG = ROOT / "extensions" / "catalog.json"
PRESETS_CATALOG = ROOT / "presets" / "catalog.json"
PROFILE_DEPTH_FILES = {
    "stack-options.json",
    "domain-dictionary.json",
    "security-baseline.md",
    "performance-budget.json",
    "testing-contract.md",
    "blueprint-template.md",
}


@dataclass(frozen=True)
class CommandSpec:
    name: str
    prompt: str
    purpose: str
    next_command: str


COMMANDS = [
    CommandSpec("/sdc.constitution", "prompts/constitution.prompt.md", "Establish or review project principles", "/sdc.intake"),
    CommandSpec("/sdc.intake", "prompts/intake.prompt.md", "Normalize raw request and detect mode", "/sdc.specify"),
    CommandSpec("/sdc.specify", "prompts/write-master-spec.prompt.md", "Produce a buildable specification", "/sdc.clarify"),
    CommandSpec("/sdc.clarify", "prompts/clarify.prompt.md", "Resolve blocking ambiguity", "/sdc.profile"),
    CommandSpec("/sdc.profile", "prompts/select-project-profile.prompt.md", "Select the project profile", "/sdc.blueprint"),
    CommandSpec("/sdc.blueprint", "prompts/write-vertical-blueprint.prompt.md", "Compile the execution contract", "/sdc.plan"),
    CommandSpec("/sdc.plan", "prompts/write-plan.prompt.md", "Create the technical plan", "/sdc.tasks"),
    CommandSpec("/sdc.tasks", "prompts/generate-tasks.prompt.md", "Break the plan into dependency-aware tasks", "/sdc.checklist"),
    CommandSpec("/sdc.checklist", "prompts/checklist.prompt.md", "Validate artifact readiness", "/sdc.analyze"),
    CommandSpec("/sdc.analyze", "prompts/analyze.prompt.md", "Check cross-artifact consistency", "/sdc.implement"),
    CommandSpec("/sdc.implement", "prompts/implement.prompt.md", "Implement approved tasks", "/sdc.score"),
    CommandSpec("/sdc.score", "prompts/evaluate-deliverable-scorecard.prompt.md", "Evaluate delivery", "/sdc.iterate"),
    CommandSpec("/sdc.iterate", "prompts/iterate.prompt.md", "Release, rollback, or update artifacts", "/sdc.intake"),
]


def normalize_command(value: str) -> str:
    value = value.strip()
    if value.startswith("/sdc."):
        return value
    if value.startswith("sdc."):
        return f"/{value}"
    if value.startswith("/"):
        return value
    return f"/sdc.{value}"


def command_map() -> dict[str, CommandSpec]:
    return {command.name: command for command in COMMANDS}


def print_command_list() -> None:
    print("Official pipeline:")
    print("Raw request -> Intake -> Specification -> Project Profile Selection -> Vertical Blueprint -> Plan -> Tasks -> Implementation -> Evaluation Scorecard -> Release/Iteration")
    print()
    print("| Command | Prompt | Next |")
    print("|---|---|---|")
    for command in COMMANDS:
        print(f"| `{command.name}` | `{command.prompt}` | `{command.next_command}` |")
    print()
    print("Project profiles:")
    for profile_id, title in load_project_profiles():
        print(f"{profile_id:36} {title[:48]:48} depth: {profile_depth_status(profile_id)}")


def load_project_profiles() -> list[tuple[str, str]]:
    profiles: list[tuple[str, str]] = []
    for path in sorted((ROOT / "project-types").glob("[0-9][0-9]-*.md")):
        text = path.read_text(encoding="utf-8", errors="ignore")
        profile_id = path.stem[3:]
        for line in text.splitlines():
            if line.startswith("- Profile id: `") and line.endswith("`"):
                profile_id = line.split("`", 2)[1]
                break
        title = path.stem[3:]
        for line in text.splitlines():
            if line.startswith("# "):
                title = line[2:].strip()
                break
        profiles.append((profile_id, title))
    return profiles


def profile_depth_status(profile_id: str) -> str:
    depth_dir = ROOT / "project-types" / profile_id
    if not depth_dir.is_dir():
        return "FAIL"
    for name in PROFILE_DEPTH_FILES:
        path = depth_dir / name
        if not path.is_file() or not path.read_text(encoding="utf-8", errors="ignore").strip():
            return "FAIL"
    for name in ["stack-options.json", "domain-dictionary.json", "performance-budget.json"]:
        try:
            json.loads((depth_dir / name).read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            return "FAIL"
    return "PASS"


def slugify(value: str) -> str:
    output = []
    previous_dash = False
    for char in value.lower().strip():
        if char.isalnum():
            output.append(char)
            previous_dash = False
        elif not previous_dash:
            output.append("-")
            previous_dash = True
    return "".join(output).strip("-") or "feature"


def show_prompt(command_name: str) -> int:
    command = command_map().get(normalize_command(command_name))
    if command is None:
        print(f"Unknown command: {command_name}", file=sys.stderr)
        return 2
    path = ROOT / command.prompt
    if not path.exists():
        print(f"Missing prompt file: {command.prompt}", file=sys.stderr)
        return 1
    print(path.read_text(encoding="utf-8"))
    return 0


def run(args: list[str]) -> int:
    completed = subprocess.run(args, cwd=ROOT, check=False)
    return completed.returncode


def init_workspace(args: argparse.Namespace) -> int:
    name = args.name or args.positional_name
    if not args.type:
        print(
            "sdc.py init requires --type. Example:\n"
            '  python3 tools/sdc.py init "my app" --type full-stack-saas\n'
            "  python3 tools/sdc.py list",
            file=sys.stderr,
        )
        return 2
    command = [
        PYTHON,
        "tools/spec_scaffold.py",
        "--type",
        args.type,
        "--name",
        name,
        "--out",
        args.out,
    ]
    return run(command)


def scaffold(args: argparse.Namespace) -> int:
    command = [PYTHON, "tools/spec_scaffold.py"]
    if args.list:
        command.append("--list")
    else:
        command.extend(["--type", args.type, "--name", args.name, "--out", args.out])
    return run(command)


def branch_name(args: argparse.Namespace) -> int:
    prefix = args.prefix.strip("-") or "sdc"
    slug = slugify(args.name)
    if args.strategy == "timestamp":
        number = datetime.now(timezone.utc).strftime("%Y%m%d%H%M")
    else:
        number = str(args.number).zfill(3)
    name = f"{prefix}/{number}-{slug}"
    print(name)
    if args.create:
        if not (ROOT / ".git").exists():
            print("Cannot create branch: this directory is not a git repository.", file=sys.stderr)
            return 1
        return run(["git", "switch", "-c", name])
    return 0


def artifact_manifest(args: argparse.Namespace) -> int:
    payload = {
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
        "commands": [
            {
                "command": command.name,
                "prompt": command.prompt,
                "purpose": command.purpose,
                "next": command.next_command,
            }
            for command in COMMANDS
        ],
        "required_artifacts": [
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
    }
    if args.format == "json":
        print(json.dumps(payload, indent=2))
        return 0
    print("# Specification-Driven Coding Artifact Manifest")
    print()
    print("## Required artifacts")
    for artifact in payload["required_artifacts"]:
        print(f"- `{artifact}`")
    print()
    print("## Commands")
    for command in payload["commands"]:
        print(f"- `{command['command']}` -> `{command['prompt']}` -> `{command['next']}`")
    return 0


def load_catalog(path: Path, required_keys: set[str]) -> list[dict[str, object]]:
    if not path.exists():
        raise FileNotFoundError(f"Missing catalog: {path}")
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, list):
        raise ValueError(f"{path.relative_to(ROOT)} must contain a top-level list")
    for index, entry in enumerate(payload, start=1):
        if not isinstance(entry, dict):
            raise ValueError(f"Entry {index} in {path.relative_to(ROOT)} must be an object")
        missing = sorted(required_keys - set(entry))
        if missing:
            raise ValueError(
                f"Entry {index} in {path.relative_to(ROOT)} is missing required keys: {', '.join(missing)}"
            )
    return payload


def load_integrations() -> list[dict[str, object]]:
    return load_catalog(INTEGRATIONS_CATALOG, {"id", "name", "file", "type", "primary_use"})


def integration_list(args: argparse.Namespace) -> int:
    try:
        integrations = load_integrations()
    except (FileNotFoundError, json.JSONDecodeError, ValueError) as exc:
        print(str(exc), file=sys.stderr)
        return 1
    if args.format == "json":
        print(json.dumps(integrations, indent=2))
        return 0

    print("| ID | Name | File | Type | Primary use |")
    print("|---|---|---|---|---|")
    for entry in integrations:
        print(
            "| `{id}` | {name} | `{file}` | `{type}` | {primary_use} |".format(
                id=entry["id"],
                name=entry["name"],
                file=entry["file"],
                type=entry["type"],
                primary_use=entry["primary_use"],
            )
        )
    return 0


def extension_list(args: argparse.Namespace) -> int:
    try:
        extensions = load_catalog(EXTENSIONS_CATALOG, {"id", "name", "type", "status", "primary_use"})
    except (FileNotFoundError, json.JSONDecodeError, ValueError) as exc:
        print(str(exc), file=sys.stderr)
        return 1
    if args.format == "json":
        print(json.dumps(extensions, indent=2))
        return 0

    print("| ID | Name | Type | Status | Primary use |")
    print("|---|---|---|---|---|")
    for entry in extensions:
        print(
            "| `{id}` | {name} | `{type}` | `{status}` | {primary_use} |".format(
                id=entry["id"],
                name=entry["name"],
                type=entry["type"],
                status=entry["status"],
                primary_use=entry["primary_use"],
            )
        )
    return 0


def preset_list(args: argparse.Namespace) -> int:
    try:
        presets = load_catalog(PRESETS_CATALOG, {"id", "name", "status", "project_profile", "best_for"})
    except (FileNotFoundError, json.JSONDecodeError, ValueError) as exc:
        print(str(exc), file=sys.stderr)
        return 1
    if args.format == "json":
        print(json.dumps(presets, indent=2))
        return 0

    print("| ID | Name | Status | Project profile | Best for |")
    print("|---|---|---|---|---|")
    for entry in presets:
        print(
            "| `{id}` | {name} | `{status}` | `{project_profile}` | {best_for} |".format(
                id=entry["id"],
                name=entry["name"],
                status=entry["status"],
                project_profile=entry["project_profile"],
                best_for=entry["best_for"],
            )
        )
    return 0


def doctor(args: argparse.Namespace) -> int:
    harness_check = [PYTHON, "tools/sdc_harness.py", "run", "--fixture", "001-builder-habit-dashboard"]
    enforcement_checks = [[PYTHON, "tools/sdc_enforce.py", "check", "--path", "benchmarks/golden/001-builder-habit-dashboard"]]
    if not args.quick:
        harness_check = [PYTHON, "tools/sdc_harness.py", "run", "--all"]
        enforcement_checks = [
            [PYTHON, "tools/sdc_enforce.py", "check", "--path", "benchmarks/golden/001-builder-habit-dashboard"],
            [PYTHON, "tools/sdc_enforce.py", "check", "--path", "benchmarks/golden/002-b2b-leave-management"],
            [PYTHON, "tools/sdc_enforce.py", "check", "--path", "benchmarks/golden/003-internal-pdf-rag-assistant"],
        ]
    checks = [
        [PYTHON, "tools/spec_lint.py"],
        [PYTHON, "tools/spec_scaffold.py", "--list"],
        [PYTHON, "tools/score_blueprint.py", "blueprints/02-full-project-blueprint.md"],
        harness_check,
    ] + enforcement_checks
    for check in checks:
        print(f"$ {' '.join(check)}")
        code = run(check)
        if code != 0:
            return code
    return 0


def harness(args: argparse.Namespace) -> int:
    command = [PYTHON, "tools/sdc_harness.py", args.harness_command]
    if args.fixture:
        command.extend(["--fixture", args.fixture])
    return run(command)


def demo(args: argparse.Namespace) -> int:
    command = [PYTHON, "tools/sdc_demo.py", args.demo_command]
    if args.fixture:
        command.extend(["--fixture", args.fixture])
    if args.verbose:
        command.append("--verbose")
    if args.demo_command == "run" and args.format:
        command.extend(["--format", args.format])
    return run(command)


def enforce(args: argparse.Namespace) -> int:
    command = [PYTHON, "tools/sdc_enforce.py", args.enforce_command]
    if args.path:
        command.extend(["--path", args.path])
    if args.workspace:
        command.extend(["--workspace", args.workspace])
    if args.format:
        command.extend(["--format", args.format])
    if args.write_report:
        command.append("--write-report")
    return run(command)


def compile_workspace(args: argparse.Namespace) -> int:
    command = [PYTHON, "tools/sdc_compile.py", "compile", "--workspace", args.workspace]
    if args.profile:
        command.extend(["--profile", args.profile])
    if args.raw_request:
        command.extend(["--raw-request", args.raw_request])
    if args.format:
        command.extend(["--format", args.format])
    if args.strict:
        command.append("--strict")
    if args.dry_run:
        command.append("--dry-run")
    if args.force:
        command.append("--force")
    return run(command)


def handoff_workspace(args: argparse.Namespace) -> int:
    command = [PYTHON, "tools/sdc_handoff.py", "handoff", "--workspace", args.workspace]
    if args.target:
        command.extend(["--target", args.target])
    if args.role:
        command.extend(["--role", args.role])
    if args.scope:
        command.extend(["--scope", args.scope])
    if args.format:
        command.extend(["--format", args.format])
    if args.copy:
        command.append("--copy")
    if args.out:
        command.extend(["--out", args.out])
    if args.dry_run:
        command.append("--dry-run")
    return run(command)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Specification-Driven Coding command surface")
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("list", help="list /sdc.* commands and prompt files")

    show = subparsers.add_parser("show", help="print the prompt for a command")
    show.add_argument("name", help="command name, e.g. /sdc.blueprint or blueprint")

    inspect = subparsers.add_parser("inspect", help="alias for show")
    inspect.add_argument("name", help="command name, e.g. /sdc.blueprint or blueprint")

    init = subparsers.add_parser("init", help="create a minimal SDC workspace via spec_scaffold.py")
    init.add_argument("positional_name", nargs="?", help="optional project or feature name shorthand")
    init.add_argument("--type", help="project profile id")
    init.add_argument("--name", help="project or feature name")
    init.add_argument("--out", default=".specification-driven-coding-workspace", help="output directory")

    scaffold_parser = subparsers.add_parser("scaffold", help="list profiles or create a minimal SDC workspace")
    scaffold_parser.add_argument("--list", action="store_true", help="list available project profiles")
    scaffold_parser.add_argument("--type", help="project profile id")
    scaffold_parser.add_argument("--name", default="New Specification-Driven Coding Project", help="project or feature name")
    scaffold_parser.add_argument("--out", default=".specification-driven-coding-workspace", help="output directory")

    branch = subparsers.add_parser("branch", help="print or create a methodology branch name")
    branch.add_argument("--name", required=True, help="feature, project, or change name")
    branch.add_argument("--prefix", default="sdc", help="branch prefix")
    branch.add_argument("--strategy", choices=["sequential", "timestamp"], default="sequential", help="branch numbering strategy")
    branch.add_argument("--number", type=int, default=1, help="sequential branch number")
    branch.add_argument("--create", action="store_true", help="create the branch with git switch -c")

    artifacts = subparsers.add_parser("artifacts", help="print required artifact manifest")
    artifacts.add_argument("--format", choices=["markdown", "json"], default="markdown", help="output format")

    doctor_parser = subparsers.add_parser("doctor", help="run lint, list, blueprint score, and harness checks")
    doctor_parser.add_argument("--quick", action="store_true", help="run the fast smoke path with fixture 001 only")

    harness_parser = subparsers.add_parser("harness", help="run benchmark fixture harness")
    harness_parser.add_argument("harness_command", choices=["list", "run"], help="harness command")
    harness_parser.add_argument("--fixture", help="fixture id for harness run")

    demo_parser = subparsers.add_parser("demo", help="show compact benchmark artifact walkthroughs")
    demo_parser.add_argument("demo_command", choices=["list", "run"], help="demo command")
    demo_parser.add_argument("--fixture", help="fixture id for demo run")
    demo_parser.add_argument("--verbose", action="store_true", help="include extra artifact excerpts")
    demo_parser.add_argument("--format", choices=["text", "json", "markdown"], default="text", help="output format")

    enforce_parser = subparsers.add_parser("enforce", help="run structural Continuous Specification Enforcement")
    enforce_parser.add_argument("enforce_command", choices=["check"], help="enforcement command")
    enforce_parser.add_argument("--path", help="artifact folder to check")
    enforce_parser.add_argument("--workspace", help="alias for --path")
    enforce_parser.add_argument("--format", choices=["text", "json"], default="text", help="output format")
    enforce_parser.add_argument("--write-report", action="store_true", help="write sdc-enforcement-report.md")

    compile_parser = subparsers.add_parser("compile", help="deterministically compile dense SDC artifacts")
    compile_parser.add_argument("--workspace", required=True, help="SDC workspace spec folder")
    compile_parser.add_argument("--profile", help="override detected profile id")
    compile_parser.add_argument("--raw-request", help="override raw-request.md path")
    compile_parser.add_argument("--format", choices=["text", "markdown", "json"], default="text", help="output format")
    compile_parser.add_argument("--strict", action="store_true", help="fail on compile assertion warning")
    compile_parser.add_argument("--dry-run", action="store_true", help="print output summary without writing files")
    compile_parser.add_argument("--force", action="store_true", help="overwrite scaffold/generated sections")

    handoff_parser = subparsers.add_parser("handoff", help="assemble deterministic agent/builder handoff prompt")
    handoff_parser.add_argument("--workspace", required=True, help="SDC workspace spec folder")
    handoff_parser.add_argument(
        "--target",
        choices=["generic", "codex", "claude-code", "cursor", "aider", "gemini-cli", "builder", "mcp"],
        default="generic",
        help="target CLI or builder",
    )
    handoff_parser.add_argument(
        "--role",
        choices=[
            "auto",
            "architect",
            "engineer",
            "reviewer",
            "optimizer",
            "debugger",
            "performance",
            "security",
            "techlead",
            "devops",
            "frontend",
            "ai",
            "startup",
            "refactor",
            "requirements",
        ],
        default="auto",
        help="role prompt to apply",
    )
    handoff_parser.add_argument(
        "--scope",
        choices=["auto", "blueprint", "implement", "review", "debug", "refactor", "deploy", "security", "performance"],
        default="auto",
        help="handoff scope",
    )
    handoff_parser.add_argument("--format", choices=["text", "markdown", "json"], default="markdown", help="output format")
    handoff_parser.add_argument("--copy", action="store_true", help="copy prompt to clipboard when available")
    handoff_parser.add_argument("--out", help="write prompt to file")
    handoff_parser.add_argument("--dry-run", action="store_true", help="print signature spaces without writing/copying")

    integration_parser = subparsers.add_parser("integration", help="list machine-readable adapter integrations")
    integration_subparsers = integration_parser.add_subparsers(dest="integration_command", required=True)
    integration_list_parser = integration_subparsers.add_parser("list", help="list integrations from integrations/catalog.json")
    integration_list_parser.add_argument("--format", choices=["table", "json"], default="table", help="output format")

    extension_parser = subparsers.add_parser("extension", help="list optional method extensions")
    extension_subparsers = extension_parser.add_subparsers(dest="extension_command", required=True)
    extension_list_parser = extension_subparsers.add_parser("list", help="list extensions from extensions/catalog.json")
    extension_list_parser.add_argument("--format", choices=["table", "json"], default="table", help="output format")

    preset_parser = subparsers.add_parser("preset", help="list ready operational bundles")
    preset_subparsers = preset_parser.add_subparsers(dest="preset_command", required=True)
    preset_list_parser = preset_subparsers.add_parser("list", help="list presets from presets/catalog.json")
    preset_list_parser.add_argument("--format", choices=["table", "json"], default="table", help="output format")

    args = parser.parse_args(argv)
    if args.command == "list":
        print_command_list()
        return 0
    if args.command in {"show", "inspect"}:
        return show_prompt(args.name)
    if args.command == "init":
        if not args.name and not args.positional_name:
            args.name = "New Specification-Driven Coding Project"
        return init_workspace(args)
    if args.command == "scaffold":
        if not args.list and not args.type:
            parser.error("sdc.py scaffold requires --list or --type")
        return scaffold(args)
    if args.command == "branch":
        return branch_name(args)
    if args.command == "artifacts":
        return artifact_manifest(args)
    if args.command == "doctor":
        return doctor(args)
    if args.command == "harness":
        if args.harness_command == "run" and not args.fixture:
            parser.error("sdc.py harness run requires --fixture")
        return harness(args)
    if args.command == "demo":
        if args.demo_command == "run" and not args.fixture:
            parser.error("sdc.py demo run requires --fixture")
        return demo(args)
    if args.command == "enforce":
        if not args.path and not args.workspace:
            parser.error("sdc.py enforce check requires --path or --workspace")
        return enforce(args)
    if args.command == "compile":
        return compile_workspace(args)
    if args.command == "handoff":
        return handoff_workspace(args)
    if args.command == "integration":
        if args.integration_command == "list":
            return integration_list(args)
    if args.command == "extension":
        if args.extension_command == "list":
            return extension_list(args)
    if args.command == "preset":
        if args.preset_command == "list":
            return preset_list(args)
    parser.error(f"unknown command: {args.command}")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
