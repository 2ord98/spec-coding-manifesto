#!/usr/bin/env python3
"""Deterministic Specification-Driven Coding compile engine.

This tool assembles decision-bounded artifacts from a raw request and
profile-depth metadata. It is stdlib-only and performs no model/API calls.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.sdc_signature import DecisionAssertion, ProfileSignature

PROJECT_TYPES = ROOT / "project-types"
REQUIRED_ARTIFACTS = [
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
PROFILE_DEPTH_FILES = [
    "stack-options.json",
    "domain-dictionary.json",
    "security-baseline.md",
    "performance-budget.json",
    "testing-contract.md",
    "blueprint-template.md",
    "failure-modes.md",
]
CRITICAL_BLUEPRINT_SECTIONS = [
    "Role contract",
    "Domain contract",
    "Mode contract",
    "Stack decision space",
    "File tree contract",
    "Architecture contract",
    "Data/API/tool contracts",
    "UX/design/motion contract",
    "Security hardening contract",
    "Performance budget",
    "Testing contract",
    "Output contract",
    "Scorecard",
]
DEFAULT_MARKER = "[DEFAULT — review and override if needed]"
DECISION_CREATED_AT = "1970-01-01T00:00:00Z"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def write(path: Path, text: str, dry_run: bool) -> bool:
    if dry_run:
        return False
    if path.exists() and read(path) == text:
        return False
    path.write_text(text, encoding="utf-8")
    return True


def slug_text(value: str, fallback: str = "project") -> str:
    words = re.findall(r"[A-Za-zÀ-ÿ0-9][A-Za-zÀ-ÿ0-9_-]+", value)
    return " ".join(words[:10]) if words else fallback


def validate_workspace(workspace: Path) -> None:
    if not workspace.exists() or not workspace.is_dir():
        raise SystemExit(f"Workspace not found: {workspace}")
    missing = [name for name in REQUIRED_ARTIFACTS if not (workspace / name).exists()]
    if missing:
        raise SystemExit(f"Workspace missing required artifacts: {', '.join(missing)}")


def detect_profile_id(workspace: Path, override: str | None) -> str:
    if override:
        return override
    manifest_path = workspace / "artifact-manifest.json"
    if manifest_path.exists():
        try:
            manifest = json.loads(read(manifest_path))
            profile = manifest.get("project_profile")
            if isinstance(profile, str) and profile.strip():
                return profile.strip()
        except json.JSONDecodeError:
            pass
    project_profile = read(workspace / "project-profile.md")
    match = re.search(r"Profile id:\s*`([^`]+)`", project_profile)
    if match:
        return match.group(1)
    raise SystemExit("Cannot detect project profile. Use --profile PROFILE_ID.")


def load_profile_depth(profile_id: str) -> dict[str, Any]:
    depth_dir = PROJECT_TYPES / profile_id
    if not depth_dir.is_dir():
        raise SystemExit(f"Missing profile-depth folder: project-types/{profile_id}")
    missing = [name for name in PROFILE_DEPTH_FILES if not (depth_dir / name).exists()]
    if missing:
        raise SystemExit(f"Profile-depth {profile_id} missing files: {', '.join(missing)}")
    try:
        stack = json.loads(read(depth_dir / "stack-options.json"))
        dictionary = json.loads(read(depth_dir / "domain-dictionary.json"))
        performance = json.loads(read(depth_dir / "performance-budget.json"))
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Invalid profile-depth JSON for {profile_id}: {exc}") from exc
    return {
        "profile_id": profile_id,
        "dir": depth_dir,
        "stack": stack,
        "dictionary": dictionary,
        "security": read(depth_dir / "security-baseline.md"),
        "performance": performance,
        "testing": read(depth_dir / "testing-contract.md"),
        "blueprint_template": read(depth_dir / "blueprint-template.md"),
        "failure_modes": read(depth_dir / "failure-modes.md"),
    }


def build_questions(raw_request: str, dictionary: dict[str, Any]) -> list[str]:
    questions = [
        "[ASK: What is the primary user role and success moment for this project?]",
        "[ASK: Which data, privacy, or permission boundaries are non-negotiable?]",
        "[ASK: What deployment, ownership, and maintenance constraints apply?]",
    ]
    lowered = raw_request.lower()
    if any(term in lowered for term in ["prenot", "booking", "contact", "contatt", "form", "account", "data", "dati"]):
        questions.append("[ASK: Is the workflow only informational/contact-based, or does it manage accounts, bookings, or stored user data?]")
    if any(term in lowered for term in ["privacy", "gdpr", "personal", "personali", "sensitive", "sensibili"]):
        questions.append("[ASK: Which jurisdiction, retention, and consent requirements must be applied?]")
    if len(questions) < 3:
        questions.extend(f"[ASK: Confirm {item}.]" for item in dictionary.get("common_artifacts", [])[: 3 - len(questions)])
    return questions[:5]


def build_assumptions(profile_id: str) -> list[str]:
    return [
        f"[ASSUMPTION: Use profile `{profile_id}` as a software-class decision boundary, not as an app template.]",
        "[ASSUMPTION: Use the smallest architecture that satisfies explicit constraints until the request proves otherwise.]",
        "[ASSUMPTION: Treat the default stack option as reviewable, not final.]",
    ]


def decision_rows(stack_payload: dict[str, Any]) -> list[dict[str, str]]:
    options = stack_payload.get("options", [])
    rows: list[dict[str, str]] = []
    ids = [option.get("name", option.get("id", "alternative")) for option in options if isinstance(option, dict)]
    for index, option in enumerate(options):
        if not isinstance(option, dict):
            continue
        rejected = next((name for name in ids if name != option.get("name")), "No alternative available")
        choice = option.get("id", f"option-{index + 1}")
        if option.get("default") is True:
            choice = f"{choice} {DEFAULT_MARKER}"
        rows.append(
            {
                "choice": str(choice),
                "option": str(option.get("name", "")),
                "rationale": str(option.get("rationale", "")),
                "rejected_alternative": rejected,
                "risk": str(option.get("risks", "")),
                "tradeoffs": str(option.get("tradeoffs", "")),
            }
        )
    return rows


def matrix_markdown(rows: list[dict[str, str]]) -> str:
    lines = [
        "| Choice | Option | Rationale | Rejected alternative | Risk |",
        "|---|---|---|---|---|",
    ]
    for row in rows:
        lines.append(
            f"| {row['choice']} | {row['option']} | {row['rationale']} Tradeoff: {row['tradeoffs']} | {row['rejected_alternative']} | {row['risk']} |"
        )
    return "\n".join(lines)


def marker_text(value: str) -> str:
    return re.sub(r"^\[(ASK|ASSUMPTION):\s*|\]$", "", value.strip()).strip()


def next_decision_id(index: int) -> str:
    return f"DEC-{index:03d}"


def build_decision_ledger(sig: ProfileSignature) -> list[dict[str, Any]]:
    """Create deterministic JSONL decision records from compile output space."""
    rows: list[dict[str, Any]] = []

    def add(
        decision_type: str,
        decision: str,
        reason: str,
        impact: str,
        reversible: bool,
        verification: str,
    ) -> None:
        rows.append(
            {
                "id": next_decision_id(len(rows) + 1),
                "type": decision_type,
                "decision": decision,
                "reason": reason,
                "impact": impact,
                "reversible": reversible,
                "verification": verification,
                "source": "sdc compile",
                "created_at": DECISION_CREATED_AT,
            }
        )

    for assumption in sig.assumptions:
        add(
            "assumption",
            marker_text(assumption),
            "The request does not provide enough evidence to treat this as a fixed fact.",
            "Keeps uncertainty visible before implementation.",
            True,
            "Resolve or accept the assumption before release.",
        )

    default_row = next((row for row in sig.decision_matrix if DEFAULT_MARKER in row.get("choice", "")), None)
    if default_row:
        add(
            "stack-choice",
            f"Review stack option: {default_row.get('option', '')}",
            default_row.get("rationale", "Default option from profile-depth metadata."),
            "Constrains stack discussion without making the stack final.",
            True,
            "Blueprint stack decision space must keep the default marker and rejected alternatives visible.",
        )

    add(
        "scope-choice",
        "Compile artifacts only; do not generate application code.",
        "Compile is a deterministic contract compiler, not an app generator.",
        "Prevents implementation from starting before artifacts are reviewed.",
        True,
        "Workspace should contain SDC artifacts and no generated app code from compile.",
    )
    add(
        "security-choice",
        "Require explicit approval before adding authentication, storage, tracking, or destructive tool behavior.",
        "The raw request may omit sensitive boundary decisions.",
        "Reduces unsafe default expansion and hidden data collection.",
        True,
        "Capability boundaries and blueprint security contract must list approval gates.",
    )
    add(
        "privacy-choice",
        "Collect only data explicitly required by the approved workflow.",
        "Data boundaries must come from request evidence and artifact review.",
        "Limits accidental personal data handling.",
        True,
        "Spec, blueprint, and capability boundaries must agree on data collection scope.",
    )
    add(
        "testing-choice",
        "Use the profile testing contract and scorecard as release gates.",
        "Testing expectations must be tied to the software class before implementation.",
        "Keeps validation explicit and repeatable.",
        True,
        "Tasks and scorecard must reference testing gates before release.",
    )
    return rows


def render_decision_jsonl(decisions: list[dict[str, Any]]) -> str:
    return "\n".join(json.dumps(row, ensure_ascii=False) for row in decisions) + "\n"


def build_capability_boundaries(depth: dict[str, Any], sig: ProfileSignature) -> dict[str, Any]:
    dictionary = depth["dictionary"]
    anti_patterns = [
        item
        for item in dictionary.get("anti_patterns", [])
        if isinstance(item, str) and item.strip()
    ]
    forbidden_patterns = list(dict.fromkeys(anti_patterns + ["generic-saas-dashboard", "stack-by-habit"]))
    return {
        "forbidden_libraries": [],
        "forbidden_patterns": forbidden_patterns,
        "off_limits_layers": [
            "undeclared payment processing",
            "undeclared account management",
            "undeclared background automation",
        ],
        "requires_approval": [
            "collect-sensitive-data",
            "add-authentication",
            "add-database",
            "add-third-party-tracking",
            "call-external-api",
        ],
        "allowed_external_services": [],
        "data_boundary": "Collect only data explicitly required by the approved workflow.",
        "network_boundary": "No external API calls unless declared in the blueprint.",
        "write_boundary": "Do not modify files outside the approved project tree.",
        "tool_boundary": "No destructive tool calls without explicit approval.",
    }


def generated_notice() -> str:
    return "<!-- SDC_COMPILE_GENERATED -->"


def is_placeholder_artifact(text: str) -> bool:
    if generated_notice() in text:
        return True
    meaningful = [
        line.strip()
        for line in text.splitlines()
        if line.strip()
        and not line.strip().startswith("#")
        and line.strip() not in {"|---|---|---|---|---|", "|---|---:|---:|---|", "```text", "```"}
    ]
    if not meaningful:
        return True
    placeholders = 0
    for line in meaningful:
        if re.search(r"\[TITLE\]|\[azione atomica\]|PASS/FAIL|__|:\s*$|-\s*$|^\|\s*[^|]*\s*\|", line):
            placeholders += 1
    return placeholders >= max(3, len(meaningful) // 2)


def merge_artifact(path: Path, generated: str, force: bool, dry_run: bool) -> bool:
    existing = read(path)
    if force or is_placeholder_artifact(existing):
        return write(path, generated, dry_run)
    if generated_notice() in existing:
        before = existing.split(generated_notice(), 1)[0].rstrip()
        return write(path, before + "\n\n" + generated, dry_run)
    merged = existing.rstrip() + "\n\n" + generated
    return write(path, merged, dry_run)


def render_intake(raw_request: str, profile_id: str, dictionary: dict[str, Any], questions: list[str], assumptions: list[str]) -> str:
    return f"""{generated_notice()}
# Intake

## Mode

full-project candidate, pending clarification.

## Project profile

`{profile_id}`

## Normalized request

{slug_text(raw_request, "The request describes a software project.")}

## User intent summary

{raw_request.strip()}

## Blocking questions

{chr(10).join(f"- {item}" for item in questions)}

## Reversible assumptions

{chr(10).join(f"- {item}" for item in assumptions)}

## Non-goals

- [ASSUMPTION: Do not generate application code during compile.]
- [ASSUMPTION: Do not expand beyond the selected software class without explicit request evidence.]

## Anti-genericity constraints

{chr(10).join(f"- Avoid: {item}" for item in dictionary.get("anti_patterns", [])[:5])}

## Required blueprint

Vertical Blueprint required before final plan and tasks.
"""


def render_spec(raw_request: str, profile_id: str, dictionary: dict[str, Any], questions: list[str], assumptions: list[str]) -> str:
    users = ", ".join(dictionary.get("common_users", []))
    artifacts = ", ".join(dictionary.get("common_artifacts", []))
    return f"""{generated_notice()}
# Feature Spec: compiled decision contract

## Specification-Driven Coding header

- Mode: full-project candidate
- Project profile: `{profile_id}`
- Prompt normalized: {slug_text(raw_request)}
- Primary user: [ASK: Confirm one of the class users or provide a specific role.] Candidate class users: {users}
- Specific problem: {raw_request.strip()}
- Non-goals: no app code generation during compile; no market-vertical assumptions from profile defaults.
- Level: [ASK: Confirm throwaway / prototype / MVP / production / enterprise.]
- Non-negotiable constraints: [ASK: Confirm constraints that affect data, security, UX, integrations, and deployment.]
- Provisional assumptions: {assumptions[0]}

## Anti-genericity constraints

{chr(10).join(f"- {item}" for item in dictionary.get("anti_patterns", [])[:5])}

## User journeys

### Journey 1 -- primary workflow

- Actor: [ASK: Confirm primary actor.]
- Preconditions: [ASSUMPTION: User can access the intended surface.]
- Steps: [ASK: Confirm the actual workflow steps.]
- Expected outcome: The project solves the stated problem without generic default behavior.
- Edge cases: permissions, unavailable dependency, invalid input, slow network, unclear data ownership.

## Functional requirements

- FR-001: Represent the raw request as a specific workflow, not a generic shell.
- FR-002: Include class artifacts: {artifacts}
- FR-003: Resolve open questions before implementation or keep them as explicit risks.

## Non-functional requirements

- NFR-001 Performance: satisfy the profile performance budget.
- NFR-002 Security/privacy: satisfy the profile security baseline.
- NFR-003 Accessibility: define user-facing accessibility expectations where UI exists.
- NFR-004 Reliability: define fallback and error behavior before code.
- NFR-005 Maintainability: keep architecture minimal and traceable.

## Domain model

- Entities: [ASK: Confirm entities from the raw request.]
- Relationships: [ASK: Confirm relationships and ownership.]
- Invariants: [ASSUMPTION: Do not infer sensitive data processing without explicit request evidence.]
- Permissions: [ASK: Confirm roles and permissions.]

## Blueprint requirements

- Vertical Blueprint Contract: required.
- File tree required: yes.
- Stack-specific hardening: based on selected profile-depth option.
- Output format: artifact-first, implementation second.

## Acceptance criteria

- AC-001: Blueprint has no empty critical sections.
- AC-002: Stack decision space includes default marker, alternatives, rationale, and risks.
- AC-003: Scorecard contains explicit gates and residual risks.

## Scorecard expectations

- Minimum score: 80/100
- Critical categories: profile fit, anti-genericity, security/privacy, performance, testing, assumptions.

## Open questions

{chr(10).join(f"- {item}" for item in questions)}
"""


def render_blueprint(raw_request: str, profile_id: str, depth: dict[str, Any], sig: ProfileSignature) -> str:
    dictionary = depth["dictionary"]
    rows = sig.decision_matrix
    perf = depth["performance"].get("targets", {})
    return f"""{generated_notice()}
# Vertical Blueprint Contract: compiled decision contract

## Role contract

Act as a Specification-Driven Coding implementation planner. Do not implement from the raw request alone. Use profile `{profile_id}` as a decision boundary.

## Domain contract

- User-provided intent: {raw_request.strip()}
- Software class: {dictionary.get("software_class", "selected profile class")}
- Common class users: {", ".join(dictionary.get("common_users", []))}
- Common artifacts: {", ".join(dictionary.get("common_artifacts", []))}
- Open questions:
{chr(10).join(f"  - {item}" for item in sig.open_questions)}

## Mode contract

- Mode: full-project candidate
- Scope: compile artifacts only; no application code generation.
- Non-goals: no hardcoded market vertical defaults; no stack oracle behavior.
- Assumptions:
{chr(10).join(f"  - {item}" for item in sig.assumptions)}

## Stack decision space

{matrix_markdown(rows)}

## File tree contract

```text
/workspace/
  raw-request.md
  intake.md
  spec.md
  project-profile.md
  blueprint.md
  plan.md
  tasks.md
  scorecard.md
```

## Architecture contract

- Components: [ASK: Confirm concrete components after stack review.]
- Data flow: [ASK: Confirm data entry, storage, processing, and output boundaries.]
- State management: [ASSUMPTION: Keep state minimal until workflow evidence requires more.]
- Error model: invalid input, missing data, unavailable dependency, permission denial, timeout.
- Observability: log decision-relevant failures without leaking sensitive content.

## Data/API/tool contracts

- Data contract: [ASK: Confirm entities, retention, and ownership.]
- API contract: [ASSUMPTION: Expose only interfaces required by the selected workflow.]
- Tool contract: [ASSUMPTION: Tool calls require explicit permission and auditability.]

## UX/design/motion contract

- UX direction: fit the user-provided intent and selected software class.
- Accessibility: define keyboard, contrast, semantic structure, and error feedback where UI exists.
- Motion: [ASSUMPTION: Use motion only when it clarifies state or feedback.]

## Security hardening contract

{depth["security"].strip()}

## Performance budget

{chr(10).join(f"- {key}: {value}" for key, value in perf.items())}

## Testing contract

{depth["testing"].strip()}

## Output contract

- Preserve user-written artifact content unless `--force` is used.
- Keep `[ASK]` and `[ASSUMPTION]` visible until resolved.
- Plan and tasks must trace back to this blueprint.

## Scorecard

Use `scorecards/implementation-scorecard.md` plus compile assertion checks. Minimum target: {sig.scorecard_target}.
"""


def render_plan(profile_id: str, rows: list[dict[str, str]], questions: list[str]) -> str:
    first = rows[0] if rows else {"choice": "[ASK]", "option": "[ASK]", "rationale": "[ASK]", "rejected_alternative": "[ASK]", "risk": "[ASK]"}
    return f"""{generated_notice()}
# Implementation Plan: compiled decision contract

## Constitution Check

| Article | Result | Notes |
|---|---|---|
| Specificity First | PASS | Raw request preserved; uncertainty marked. |
| Project Profile Binding | PASS | Bound to `{profile_id}`. |
| Vertical Blueprint | PASS | Blueprint compiled before final tasks. |
| Anti-Genericity | PASS | Profile anti-patterns included. |
| Contracts Over Guessing | PASS | `[ASK]` and `[ASSUMPTION]` markers are explicit. |

## Technical context

- Project profile: `{profile_id}`
- Stack candidate to review: {first['choice']} / {first['option']}
- Rationale: {first['rationale']}
- Rejected alternative: {first['rejected_alternative']}
- Risk: {first['risk']}

## Stack decisions

{matrix_markdown(rows)}

## Architecture

- Components: resolve after answering blocking questions.
- Data flow: trace raw request inputs through outputs before implementation.
- Fallback: preserve safe degraded behavior for unavailable dependencies.

## Testing strategy

- Unit: validate core transformations and boundary behavior.
- Integration: validate critical workflow contracts.
- E2E/manual: validate primary user journey.
- Security checks: validate input, permissions, privacy, and logs.

## Implementation slices

1. Resolve blocking questions: {questions[0] if questions else '[ASK: Confirm blockers.]'}
2. Freeze stack decision with rationale and rejected alternative.
3. Implement the smallest vertical slice that proves the primary workflow.

## Risk register

| Risk | Probability | Impact | Mitigation |
|---|---:|---:|---|
| Unresolved scope | Medium | High | Answer `[ASK]` items before implementation. |
| Generic output | Medium | High | Enforce profile anti-patterns and scorecard. |
| Stack overbuild | Medium | Medium | Require rejected alternative and risk review. |

## Scorecard target

- Threshold: 80/100
- Critical categories: spec adherence, anti-genericity, architecture, security/privacy, performance, testing.
"""


def render_tasks(profile_id: str) -> str:
    return f"""{generated_notice()}
# Tasks: compiled decision contract

## Rules

- Every task maps to spec, blueprint, plan, or scorecard.
- Do not implement unresolved `[ASK]` items as facts.
- Do not treat `{profile_id}` as an app template.

## Task list

- [ ] T001 -- Resolve open questions and update intake/spec
  - Input: `intake.md`, `spec.md`
  - Blueprint: `blueprint.md` Domain contract
  - Output: updated assumption and question ledger
  - Verification: no high-impact unknown hidden in implementation

- [ ] T002 -- Confirm stack decision
  - Input: `blueprint.md` Stack decision space
  - Output: selected stack with rationale and rejected alternative
  - Verification: default marker reviewed and either accepted or overridden

- [ ] T003 -- Implement smallest validated slice
  - Input: `plan.md`
  - Output: minimal behavior tied to primary workflow
  - Verification: tests and scorecard evidence

## Final audit tasks

- [ ] Verify mapping requirements -> implementation
- [ ] Verify mapping blueprint -> produced files
- [ ] Run tests and enforcement
- [ ] Complete scorecard
"""


def render_scorecard(assertion: DecisionAssertion, profile_id: str) -> str:
    report = assertion.report()
    return f"""{generated_notice()}
# Scorecard: compiled decision contract

- Score total: __/100
- Required threshold: {report['score_min']}/100
- Compile assertion passes: {report['passes']}
- Project profile: `{profile_id}`

| Category | Weight | Score | Evidence |
|---|---:|---:|---|
| Specification adherence | 15 | | `spec.md` is compiled from raw request and profile-depth. |
| Anti-genericity | 15 | | Profile anti-patterns are included. |
| Architecture and stack | 15 | | Stack decision matrix includes default marker and alternatives. |
| Security/privacy | 15 | | Security baseline included. |
| UX/accessibility | 10 | | UX section includes explicit questions and assumptions. |
| Performance/reliability | 10 | | Performance budget included. |
| Testability | 10 | | Testing contract included. |
| Maintainability | 5 | | Minimal architecture assumption is explicit. |
| Assumptions/risks clarity | 5 | | `[ASK]` and `[ASSUMPTION]` are visible. |

## Compile assertion report

```json
{json.dumps(report, indent=2)}
```

## Residual risks

- Resolve `[ASK]` items before implementation.
- Review `[ASSUMPTION]` items before accepting stack or architecture.
"""


def critical_sections_filled(text: str) -> bool:
    for index, section in enumerate(CRITICAL_BLUEPRINT_SECTIONS):
        pattern = re.compile(rf"^## {re.escape(section)}\s*$", flags=re.MULTILINE)
        match = pattern.search(text)
        if not match:
            return False
        next_match = None
        for later in CRITICAL_BLUEPRINT_SECTIONS[index + 1 :]:
            candidate = re.search(rf"^## {re.escape(later)}\s*$", text[match.end() :], flags=re.MULTILINE)
            if candidate:
                next_match = match.end() + candidate.start()
                break
        body = text[match.end() : next_match].strip() if next_match else text[match.end() :].strip()
        if not body:
            return False
    return True


def compile_with_assertions(
    sig: ProfileSignature, critical_section_filled: bool, has_default_marker: bool
) -> DecisionAssertion:
    assertion = DecisionAssertion(
        critical_section_filled=critical_section_filled,
        has_default_marker=has_default_marker,
        ask_count=len(sig.open_questions),
        assumption_count=len(sig.assumptions),
        score_min=80,
    )
    return assertion


def compile_workspace(args: argparse.Namespace) -> dict[str, Any]:
    workspace = Path(args.workspace).resolve()
    validate_workspace(workspace)
    raw_request_path = Path(args.raw_request).resolve() if args.raw_request else workspace / "raw-request.md"
    if not raw_request_path.exists():
        raise SystemExit(f"Raw request file not found: {raw_request_path}")
    raw_request = read(raw_request_path).strip()
    profile_id = detect_profile_id(workspace, args.profile)
    depth = load_profile_depth(profile_id)
    dictionary = depth["dictionary"]

    sig = ProfileSignature(raw_request=raw_request, profile_id=profile_id, workspace_path=workspace)
    sig.open_questions = build_questions(raw_request, dictionary)
    sig.assumptions = build_assumptions(profile_id)
    sig.decision_matrix = decision_rows(depth["stack"])
    sig.scorecard_target = "80/100 structural compile gate"

    generated = {
        "intake.md": render_intake(raw_request, profile_id, dictionary, sig.open_questions, sig.assumptions),
        "spec.md": render_spec(raw_request, profile_id, dictionary, sig.open_questions, sig.assumptions),
        "blueprint.md": render_blueprint(raw_request, profile_id, depth, sig),
        "plan.md": render_plan(profile_id, sig.decision_matrix, sig.open_questions),
        "tasks.md": render_tasks(profile_id),
    }
    pre_assertion = compile_with_assertions(
        sig,
        critical_section_filled=critical_sections_filled(generated["blueprint.md"]),
        has_default_marker=DEFAULT_MARKER in generated["blueprint.md"],
    )
    generated["scorecard.md"] = render_scorecard(pre_assertion, profile_id)
    decisions = build_decision_ledger(sig)
    capability_boundaries = build_capability_boundaries(depth, sig)
    assertion = compile_with_assertions(
        sig,
        critical_section_filled=critical_sections_filled(generated["blueprint.md"]),
        has_default_marker=DEFAULT_MARKER in generated["blueprint.md"],
    )

    written: list[str] = []
    if not args.dry_run:
        for name, text in generated.items():
            if merge_artifact(workspace / name, text, args.force, args.dry_run):
                written.append(name)
        if write(workspace / "decisions.jsonl", render_decision_jsonl(decisions), args.dry_run):
            written.append("decisions.jsonl")
        boundaries_text = json.dumps(capability_boundaries, indent=2, ensure_ascii=False) + "\n"
        if write(workspace / "capability-boundaries.json", boundaries_text, args.dry_run):
            written.append("capability-boundaries.json")

    if args.strict and (len(sig.open_questions) > 5 or not assertion.passes()):
        payload = assertion.report()
        print("COMPILE ASSERTION FAILED:", payload, file=sys.stderr)
        raise SystemExit(1)

    return {
        "workspace": str(workspace),
        "profile_id": profile_id,
        "input_space": sig.input_space(),
        "output_space": sig.output_space(),
        "assertion": assertion.report(),
        "artifacts": {
            **{name: str(workspace / name) for name in generated},
            "decisions.jsonl": str(workspace / "decisions.jsonl"),
            "capability-boundaries.json": str(workspace / "capability-boundaries.json"),
        },
        "decisions": decisions,
        "capability_boundaries": capability_boundaries,
        "written": written,
        "dry_run": args.dry_run,
    }


def print_text(payload: dict[str, Any]) -> None:
    print("Specification-Driven Coding compile")
    print(f"Workspace: {payload['workspace']}")
    print(f"Profile: {payload['profile_id']}")
    print(f"Files written: {', '.join(payload['written']) if payload['written'] else 'none'}")
    print(f"Assertion: {'PASS' if payload['assertion']['passes'] else 'WARN'}")
    if not payload["assertion"]["passes"]:
        print("WARNING: compile assertion did not pass")


def print_markdown(payload: dict[str, Any]) -> None:
    print("# Specification-Driven Coding Compile")
    print()
    print(f"- Workspace: `{payload['workspace']}`")
    print(f"- Profile: `{payload['profile_id']}`")
    print(f"- Dry run: `{payload['dry_run']}`")
    print(f"- Files written: {', '.join(payload['written']) if payload['written'] else 'none'}")
    print()
    print("## Output space")
    print()
    for key, value in payload["output_space"].items():
        print(f"- `{key}`: {value}")
    print()
    print("## Assertion")
    print()
    print("```json")
    print(json.dumps(payload["assertion"], indent=2))
    print("```")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Deterministic Specification-Driven Coding compile engine")
    subparsers = parser.add_subparsers(dest="command", required=True)
    check = subparsers.add_parser("compile", help="compile a workspace into dense SDC artifacts")
    check.add_argument("--workspace", required=True, help="SDC workspace spec folder")
    check.add_argument("--profile", help="override detected profile id")
    check.add_argument("--raw-request", help="override raw-request.md path")
    check.add_argument("--format", choices=["text", "markdown", "json"], default="text")
    check.add_argument("--strict", action="store_true", help="fail on compile assertion warning or too many questions")
    check.add_argument("--dry-run", action="store_true", help="print output summary without writing files")
    check.add_argument("--force", action="store_true", help="overwrite scaffold/generated sections")
    args = parser.parse_args(argv)
    if args.command == "compile":
        payload = compile_workspace(args)
        if args.format == "json":
            print(json.dumps(payload, indent=2))
        elif args.format == "markdown":
            print_markdown(payload)
        else:
            print_text(payload)
        return 0
    parser.error(f"unknown command: {args.command}")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
