#!/usr/bin/env python3
"""Deterministic handoff prompt assembler for Specification-Driven Coding.

This tool performs no model calls and no agent execution. It reads an SDC
workspace and assembles a paste-ready prompt with target-specific guardrails.
"""
from __future__ import annotations

import argparse
import json
import platform
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.sdc_signature import RolePromptSignature


REQUIRED_ARTIFACTS = [
    "raw-request.md",
    "intake.md",
    "spec.md",
    "blueprint.md",
    "plan.md",
    "tasks.md",
    "scorecard.md",
]

TARGETS = {
    "generic": {
        "label": "Generic coding agent",
        "instructions": "Use a model/tool-neutral, paste-friendly workflow. Read artifacts before editing.",
    },
    "codex": {
        "label": "Codex",
        "instructions": "Make repository edits as minimal diffs, run validation commands, summarize changed files, and avoid hidden provenance.",
    },
    "claude-code": {
        "label": "Claude Code",
        "instructions": "Use long-context artifact reading, plan before implementation, avoid hallucinated files, state assumptions, and update artifacts if implementation diverges.",
    },
    "cursor": {
        "label": "Cursor",
        "instructions": "Prefer editor-scoped changes and project rules. Preserve existing code, summarize changed files, and validate before final response.",
    },
    "aider": {
        "label": "Aider",
        "instructions": "Use explicit file boundaries, small commits or patches, and ask before broad edits.",
    },
    "gemini-cli": {
        "label": "Gemini CLI",
        "instructions": "Use CLI-driven inspection, separate verified facts from assumptions, and summarize validation outputs.",
    },
    "builder": {
        "label": "App builder",
        "instructions": "Treat this as an app-builder execution packet with file tree constraints, UI states, anti-genericity gates, and no generic dashboard unless justified.",
    },
    "mcp": {
        "label": "MCP-enabled workflow",
        "instructions": "Respect tool permissions, approval gates, audit logs, and attach the decision matrix and scorecard to tool calls.",
    },
}

ROLES = {
    "architect": "Systems architect",
    "engineer": "Implementation engineer",
    "reviewer": "Codebase reviewer",
    "optimizer": "Performance optimizer",
    "debugger": "Debugging engineer",
    "performance": "Performance engineer",
    "security": "Security auditor",
    "techlead": "Technical lead",
    "devops": "DevOps engineer",
    "frontend": "Frontend engineer",
    "ai": "AI engineer",
    "startup": "Startup engineer",
    "refactor": "Architecture refactorer",
    "requirements": "Requirements engineer",
}

SCOPES = {"blueprint", "implement", "review", "debug", "refactor", "deploy", "security", "performance"}


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def require_workspace(path: Path) -> tuple[int, list[Path]]:
    if not path.exists() or not path.is_dir():
        print(f"Workspace not found: {path}", file=sys.stderr)
        return 1, []
    missing = [path / name for name in REQUIRED_ARTIFACTS if not (path / name).exists()]
    if missing:
        print("Missing required artifacts:", file=sys.stderr)
        for item in missing:
            print(f"- {item.name}", file=sys.stderr)
        return 1, []
    return 0, [path / name for name in REQUIRED_ARTIFACTS]


def extract_markers(text: str, marker: str) -> list[str]:
    pattern = re.compile(r"\[" + re.escape(marker) + r": [^\]]+\]")
    seen: set[str] = set()
    values: list[str] = []
    for match in pattern.findall(text):
        if match not in seen:
            seen.add(match)
            values.append(match)
    return values


def extract_profile_id(workspace: Path) -> str:
    manifest = workspace / "artifact-manifest.json"
    if manifest.exists():
        try:
            payload = json.loads(read_text(manifest))
            profile = payload.get("project_profile") or payload.get("profile_id")
            if isinstance(profile, str) and profile:
                return profile
        except json.JSONDecodeError:
            pass
    text = read_text(workspace / "project-profile.md")
    match = re.search(r"`([a-z0-9-]+)`", text)
    if match:
        return match.group(1)
    return "unknown"


def extract_raw_request(workspace: Path) -> str:
    text = read_text(workspace / "raw-request.md").strip()
    return text or "[ASK: Provide the original raw request.]"


def extract_scorecard_target(workspace: Path) -> str:
    text = read_text(workspace / "scorecard.md")
    for pattern in [r"Minimum score:\s*([^\n]+)", r"Minimum target:\s*([^\n]+)", r"Threshold:\s*([^\n]+)"]:
        match = re.search(pattern, text, flags=re.IGNORECASE)
        if match:
            return match.group(1).strip()
    return "80/100 or stronger artifact-specific gate"


def extract_decision_matrix(workspace: Path) -> list[dict[str, str]]:
    text = read_text(workspace / "blueprint.md")
    marker = "## Stack decision space"
    start = text.find(marker)
    if start == -1:
        return []
    section = text[start:]
    next_heading = re.search(r"\n##\s+", section[len(marker):])
    if next_heading:
        section = section[: len(marker) + next_heading.start()]
    rows: list[dict[str, str]] = []
    for line in section.splitlines():
        line = line.strip()
        if not line.startswith("|") or "---" in line or "Choice" in line:
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) >= 5:
            rows.append(
                {
                    "choice": cells[0],
                    "option": cells[1],
                    "rationale": cells[2],
                    "rejected_alternative": cells[3],
                    "risk": cells[4],
                }
            )
    return rows


def load_workspace_state(workspace: Path) -> dict:
    combined = "\n\n".join(read_text(workspace / name) for name in REQUIRED_ARTIFACTS)
    return {
        "raw_request": extract_raw_request(workspace),
        "profile_id": extract_profile_id(workspace),
        "open_questions": extract_markers(combined, "ASK"),
        "assumptions": extract_markers(combined, "ASSUMPTION"),
        "scorecard_target": extract_scorecard_target(workspace),
        "decision_matrix": extract_decision_matrix(workspace),
    }


def resolve_scope(value: str, workspace_state: dict) -> str:
    if value != "auto":
        return value
    if workspace_state["open_questions"]:
        return "blueprint"
    return "implement"


def resolve_role(value: str, scope: str) -> str:
    if value != "auto":
        return value
    return {
        "blueprint": "architect",
        "implement": "engineer",
        "review": "reviewer",
        "debug": "debugger",
        "refactor": "refactor",
        "deploy": "devops",
        "security": "security",
        "performance": "performance",
    }.get(scope, "architect")


def artifact_sizes(paths: list[Path]) -> list[dict[str, object]]:
    return [{"path": str(path), "size": path.stat().st_size} for path in paths]


def render_list(items: list[str], fallback: str) -> str:
    if not items:
        return f"- {fallback}"
    return "\n".join(f"- {item}" for item in items)


def render_matrix(rows: list[dict[str, str]]) -> str:
    if not rows:
        return "- [ASK: No stack decision matrix found; read blueprint.md and create one before implementation.]"
    output = ["| Choice | Option | Rationale | Rejected alternative | Risk |", "|---|---|---|---|---|"]
    for row in rows:
        output.append(
            "| {choice} | {option} | {rationale} | {rejected_alternative} | {risk} |".format(**row)
        )
    return "\n".join(output)


def assemble_prompt(workspace: Path, target: str, role: str, scope: str, state: dict) -> str:
    target_info = TARGETS[target]
    role_name = ROLES.get(role, role.replace("-", " ").title())
    artifacts = "\n".join(f"- `{workspace / name}`" for name in REQUIRED_ARTIFACTS)
    return f"""# Specification-Driven Coding Handoff

## Role assumption

Act as {role_name} using Specification-Driven Coding. Target CLI or builder: `{target}`.

## Mission

Read the workspace artifacts first, preserve the decision contract, and execute only the `{scope}` scope. Do not implement from the raw request alone.

## Workspace

`{workspace}`

## Required artifacts to read

{artifacts}

## Raw request

{state['raw_request']}

## Project profile

`{state['profile_id']}`

## Target-specific guidance

{target_info['instructions']}

## Deliverables

- Confirm artifact state before editing.
- Complete the requested scope with the smallest safe change.
- Update specification or Vertical Blueprint if implementation diverges.
- Return changed files, validation evidence, residual risks, and scorecard.

## Guardrails

- Do not guess.
- Ask only blocking questions.
- Declare reversible assumptions.
- Do not choose stack by habit.
- Justify selected stack against alternatives.
- Do not add auth, database, or backend unless required by artifacts.
- Do not generate generic template output.
- Do not change product behavior unless explicitly requested.
- Do not infer domain-specific regulation unless the raw request states it.
- Return residual risks and scorecard evidence.

## Decision matrix instruction

Use the decision matrix as the allowed decision space. The default marker means reviewable default, not final stack.

{render_matrix(state['decision_matrix'])}

## Open questions

{render_list(state['open_questions'], '[ASK: No explicit questions found; verify whether any blocking ambiguity remains.]')}

## Assumptions

{render_list(state['assumptions'], '[ASSUMPTION: No explicit assumptions found; declare reversible assumptions before implementation.]')}

## Scorecard target

{state['scorecard_target']}

## Validation expectations

- Run the repository or project validation commands named in the artifacts.
- Run `sdc enforce` or equivalent structural enforcement when available.
- Do not claim completion without evidence.

## Final output contract

Return:
- summary of work;
- changed files;
- decisions and rejected alternatives;
- validation commands and results;
- unresolved questions or accepted risks;
- scorecard outcome.
"""


def copy_to_clipboard(text: str) -> tuple[bool, str]:
    if platform.system() == "Darwin" and shutil.which("pbcopy"):
        subprocess.run(["pbcopy"], input=text, text=True, check=False)
        return True, "Clipboard updated with pbcopy."
    for command in ["xclip", "xsel"]:
        if shutil.which(command):
            if command == "xclip":
                subprocess.run(["xclip", "-selection", "clipboard"], input=text, text=True, check=False)
            else:
                subprocess.run(["xsel", "--clipboard", "--input"], input=text, text=True, check=False)
            return True, f"Clipboard updated with {command}."
    return False, "Clipboard tool not available; print or use --out FILE."


def handoff(args: argparse.Namespace) -> int:
    workspace = Path(args.workspace).resolve()
    code, artifact_paths = require_workspace(workspace)
    if code:
        return code
    state = load_workspace_state(workspace)
    scope = resolve_scope(args.scope, state)
    role = resolve_role(args.role, scope)
    sig = RolePromptSignature(workspace_state=state, scope=scope, target_cli=args.target)
    prompt = assemble_prompt(workspace, args.target, role, scope, state)
    sig.compiled_prompt = prompt
    sig.attachments = [str(path) for path in artifact_paths]
    sig.target_instructions = TARGETS[args.target]["instructions"]
    payload = {
        "input_space": sig.input_space(),
        "output_space": sig.output_space(),
        "target_cli": args.target,
        "role": role,
        "scope": scope,
        "attachments": artifact_sizes(artifact_paths),
    }

    if args.dry_run:
        summary = dict(payload)
        summary["output_space"] = dict(sig.output_space())
        summary["output_space"]["compiled_prompt"] = sig.compiled_prompt[:500]
        print(json.dumps(summary, indent=2, ensure_ascii=False))
        return 0

    if args.format == "json":
        print(json.dumps(payload, indent=2, ensure_ascii=False))
    else:
        print(sig.output_space()["compiled_prompt"])

    if args.out:
        Path(args.out).write_text(sig.output_space()["compiled_prompt"], encoding="utf-8")
        print(f"Wrote handoff prompt: {args.out}", file=sys.stderr)
    if args.copy:
        ok, message = copy_to_clipboard(sig.output_space()["compiled_prompt"])
        print(message, file=sys.stderr)
        if not ok:
            return 1
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Assemble deterministic Specification-Driven Coding handoff prompts")
    subparsers = parser.add_subparsers(dest="command", required=True)
    check = subparsers.add_parser("handoff", help="assemble handoff prompt")
    check.add_argument("--workspace", required=True, help="SDC workspace spec folder")
    check.add_argument("--target", choices=sorted(TARGETS), default="generic", help="target CLI or builder")
    check.add_argument(
        "--role",
        choices=["auto", *sorted(ROLES)],
        default="auto",
        help="role prompt to apply",
    )
    check.add_argument("--scope", choices=["auto", *sorted(SCOPES)], default="auto", help="handoff scope")
    check.add_argument("--format", choices=["text", "markdown", "json"], default="markdown", help="output format")
    check.add_argument("--copy", action="store_true", help="copy prompt to clipboard when a local clipboard tool exists")
    check.add_argument("--out", help="write prompt to file")
    check.add_argument("--dry-run", action="store_true", help="print signature spaces without writing/copying")
    args = parser.parse_args(argv)
    if args.command == "handoff":
        return handoff(args)
    parser.error(f"unknown command: {args.command}")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
