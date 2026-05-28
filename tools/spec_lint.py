#!/usr/bin/env python3
"""Minimal linter for the Specification-Driven Coding repository."""
from pathlib import Path
import importlib.util
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_PROJECT_SECTIONS = [
    "## Domande di intake obbligatorie",
    "## Stack candidates",
    "## Must-have spec fields",
    "## Anti-pattern da evitare",
    "## Acceptance gates",
]

REQUIRED_ROOT = [
    "README.md",
    "AGENTS.md",
    "integrations/README.md",
    "integrations/catalog.json",
    "extensions/README.md",
    "extensions/catalog.json",
    "presets/README.md",
    "presets/catalog.json",
    "ai-adapters/README.md",
    "ai-adapters/CLAUDE.md",
    "ai-adapters/CODEX.md",
    "ai-adapters/GEMINI.md",
    "ai-adapters/COPILOT.md",
    "ai-adapters/GROK.md",
    "ai-adapters/WINDSURF.md",
    "ai-adapters/GENERIC-AGENT.md",
    "ai-adapters/BUILDER-INGESTION.md",
    ".github/copilot-instructions.md",
    ".github/PULL_REQUEST_TEMPLATE.md",
    ".github/ISSUE_TEMPLATE/bug_report.md",
    ".github/ISSUE_TEMPLATE/feature_request.md",
    ".github/ISSUE_TEMPLATE/benchmark_fixture.md",
    ".github/workflows/validate.yml",
    ".devcontainer/devcontainer.json",
    "MANIFESTO.md",
    "docs/01-manifesto.md",
    "docs/02-methodology.md",
    "docs/04-prompt-construction-protocol.md",
    "docs/12-builder-ingestion-protocol.md",
    "docs/14-vertical-blueprint-contracts.md",
    "docs/15-model-execution-principles.md",
    "docs/16-cross-tool-ingestion-matrix.md",
    "docs/22-harness-roadmap.md",
    "docs/18-evaluation-scorecards.md",
    "docs/18-scoring-and-evaluation-limits.md",
    "docs/19-english-core-roadmap.md",
    "docs/20-artifact-toolkit-model.md",
    "docs/21-command-model.md",
    "docs/25-english-public-index.md",
    "docs/26-continuous-specification-enforcement.md",
    "docs/27-end-to-end-walkthrough.md",
    "docs/28-continuous-specification-enforcement.md",
    "docs/30-profile-depth-spec.md",
    "docs/31-decision-space-model.md",
    "docs/32-anti-template-charter.md",
    "docs/33-compile-engine-spec.md",
    "docs/34-decision-space-resolution.md",
    "docs/35-handoff-engine-spec.md",
    "docs/36-cli-target-matrix.md",
    "docs/37-agentic-protocol.md",
    "docs/38-mcp-integration.md",
    "docs/39-marketplace-submission-guidelines.md",
    "docs/40-contract-schema-hardening.md",
    "schemas/decision-ledger.schema.json",
    "schemas/capability-boundary.schema.json",
    "templates/decisions/decisions.jsonl.example",
    "templates/exceptions/EXC-template.md",
    ".specify/memory/constitution.md",
    ".specify/templates/overrides/checklist-template.md",
    ".specify/templates/overrides/analysis-template.md",
    ".specify/templates/overrides/spec-template.md",
    ".specify/templates/overrides/plan-template.md",
    ".specify/templates/overrides/tasks-template.md",
    "blueprints/02-full-project-blueprint.md",
    "blueprints/03-targeted-change-blueprint.md",
    "blueprints/12-targeted-change-blueprint.md",
    "scorecards/implementation-scorecard.md",
    "scorecards/targeted-change-scorecard.md",
    "scorecards/spec-enforcement-scorecard.md",
    "scorecards/continuous-enforcement-scorecard.md",
    "skills/specification-driven-coding/SKILL.md",
    "skills/INDEX.md",
    "skills/activation-matrix.json",
    "tools/sdc.py",
    "tools/sdc_demo.py",
    "tools/sdc_enforce.py",
    "tools/sdc_compile.py",
    "tools/sdc_handoff.py",
    "tools/sdc_signature.py",
    "sdc_cli/__init__.py",
    "sdc_cli/__main__.py",
    "tools/sdc_harness.py",
    "benchmarks/fixtures/001-builder-habit-dashboard/raw-prompt.md",
    "benchmarks/fixtures/001-builder-habit-dashboard/sdc-prompt.md",
    "benchmarks/fixtures/001-builder-habit-dashboard/expected.json",
    "benchmarks/fixtures/004-compile-structural-validation/raw-request.md",
    "benchmarks/fixtures/004-compile-structural-validation/expected.json",
    "benchmarks/golden/004-compile-structural-validation/blueprint.md",
    "benchmarks/golden/004-compile-structural-validation/scorecard.md",
    "benchmarks/golden/004-compile-structural-validation/decisions.jsonl",
    "benchmarks/golden/004-compile-structural-validation/capability-boundaries.json",
    "benchmarks/golden/001-builder-habit-dashboard/intake.md",
    "benchmarks/golden/001-builder-habit-dashboard/spec.md",
    "benchmarks/golden/001-builder-habit-dashboard/blueprint.md",
    "benchmarks/golden/001-builder-habit-dashboard/plan.md",
    "benchmarks/golden/001-builder-habit-dashboard/tasks.md",
    "benchmarks/golden/001-builder-habit-dashboard/scorecard.md",
    "case-studies/001-raw-vs-sdc-builder-prompt.md",
    "case-studies/README.md",
    "demos/README.md",
    "demos/001-builder-habit-dashboard-walkthrough.md",
    "examples/enforcement-smoke/artifact-manifest.json",
    "examples/enforcement-smoke/spec.md",
    "examples/enforcement-smoke/blueprint.md",
    "examples/enforcement-smoke/plan.md",
    "examples/enforcement-smoke/tasks.md",
    "examples/enforcement-smoke/scorecard.md",
    "examples/enforcement-smoke/app.py",
    "extensions/mcp/README.md",
    "extensions/mcp/SPEC.md",
    "extensions/mcp/manifest.json",
    "plugins/claude-code/README.md",
    "plugins/codex/README.md",
    "plugins/cursor/README.md",
    "plugins/aider/README.md",
    "plugins/gemini/README.md",
    "plugins/generic/README.md",
    "plugins/builder/README.md",
]

PROFILE_DEPTH_FILES = {
    "stack-options.json",
    "domain-dictionary.json",
    "security-baseline.md",
    "performance-budget.json",
    "testing-contract.md",
    "blueprint-template.md",
    "failure-modes.md",
}

IGNORED_PROFILE_DEPTH_SIDECARS = {".DS_Store"}
IGNORED_PROFILE_DEPTH_SUFFIXES = {".swp", ".tmp", ".pyc"}
IGNORED_PROFILE_DEPTH_DIRS = {"__pycache__"}

STACK_OPTION_KEYS = {
    "id",
    "name",
    "when_to_use",
    "when_not_to_use",
    "rationale",
    "tradeoffs",
    "risks",
}

FAILURE_MODE_SECTIONS = [
    "## Typical AI failure modes",
    "## Detection signals",
    "## Prevention rules",
    "## Verification checks",
    "## Scorecard impact",
]

DECISION_LEDGER_FIELDS = {
    "id",
    "type",
    "decision",
    "reason",
    "impact",
    "reversible",
    "verification",
    "source",
    "created_at",
}

DECISION_LEDGER_TYPES = {
    "assumption",
    "constraint",
    "stack-choice",
    "scope-choice",
    "security-choice",
    "privacy-choice",
    "testing-choice",
    "performance-choice",
    "exception-reference",
}

CAPABILITY_BOUNDARY_FIELDS = {
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

CAPABILITY_BOUNDARY_LIST_FIELDS = {
    "forbidden_libraries",
    "forbidden_patterns",
    "off_limits_layers",
    "requires_approval",
    "allowed_external_services",
}

SKILL_ACTIVATION_FIELDS = {
    "id",
    "profile",
    "phase",
    "workspace_state",
    "activate",
    "never_activate",
    "condition",
    "target_cli_hints",
}

SKILL_ACTIVATION_PHASES = {
    "intake",
    "spec",
    "compile",
    "handoff",
    "implementation",
    "review",
    "verify",
    "release",
}

ROLE_PROMPT_FILES = [
    "startup-engineer.md",
    "codebase-auditor.md",
    "debugging-engineer.md",
    "performance-engineer.md",
    "architecture-refactorer.md",
    "systems-architect.md",
    "multi-agent-team.md",
    "frontend-engineer.md",
    "technical-lead.md",
    "security-auditor.md",
    "devops-engineer.md",
    "ai-engineer.md",
    "requirements-engineer.md",
]

ROLE_PROMPT_SECTIONS = [
    "## Signature",
    "## Mission",
    "## Role assumption",
    "## Mission goals",
    "## Deliverables",
    "## Guardrails",
    "## Failure modes",
    "## Scorecard focus",
    "## Compatible phases",
    "## Compatible target CLIs",
    "## Abstract demonstrations",
]

HANDOFF_TARGETS = [
    "generic",
    "codex",
    "claude-code",
    "cursor",
    "aider",
    "gemini-cli",
    "builder",
    "mcp",
]

PLUGIN_TARGET_FOLDERS = [
    "claude-code",
    "codex",
    "cursor",
    "aider",
    "gemini",
    "generic",
    "builder",
]

FORBIDDEN_PROFILE_DEFAULT_TERMS = [
    "medical",
    "healthcare",
    "clinic",
    "hospital",
    "legal",
    "lawyer",
    "fintech",
    "banking",
    "insurance",
    "restaurant",
    "gym",
    "dental",
    "pharmacy",
    "real estate",
]

REQUIRED_SDC_COMMAND_PROMPTS = {
    "/sdc.constitution": ["prompts/constitution.prompt.md"],
    "/sdc.intake": ["prompts/intake.prompt.md"],
    "/sdc.specify": ["prompts/write-master-spec.prompt.md"],
    "/sdc.clarify": ["prompts/clarify.prompt.md"],
    "/sdc.profile": ["prompts/select-project-profile.prompt.md"],
    "/sdc.blueprint": ["prompts/write-vertical-blueprint.prompt.md"],
    "/sdc.plan": ["prompts/write-plan.prompt.md"],
    "/sdc.tasks": ["prompts/generate-tasks.prompt.md"],
    "/sdc.checklist": ["prompts/checklist.prompt.md"],
    "/sdc.analyze": ["prompts/analyze.prompt.md"],
    "/sdc.implement": ["prompts/implement.prompt.md"],
    "/sdc.score": ["prompts/evaluate-deliverable-scorecard.prompt.md"],
    "/sdc.iterate": ["prompts/iterate.prompt.md"],
}

REQUIRED_BLUEPRINT_SECTIONS = [
    "Role contract",
    "Output",
]

PROVENANCE_PATTERNS = [
    "Chat" + "GPT",
    "G" + "PT-5",
    "G" + "PT 5",
    "modello " + "5.5",
    "prompt " + "iniziale" + r" dell['’]" + "utente",
    "utente" + " ha " + "richiesto",
    "created" + " by " + "Chat" + "GPT",
    "generated" + " by " + "Chat" + "GPT",
    "generato da " + "Chat" + "GPT",
    "creato da " + "Chat" + "GPT",
    "file" + " eseguito",
]

WRONG_NAME_PATTERNS = [
    r"\b" + "Spec" + r"\s+" + "Coding" + r"\b",
    r"\b" + "spec" + r"\s+" + "coding" + r"\b",
    r"\b" + "Specify" + r"\s+" + "Coding" + r"\b",
    r"\b" + "specify" + r"\s+" + "coding" + r"\b",
    r"\b" + "Specifical" + r"\s+" + "Coding" + r"\b",
    r"\b" + "specifical" + r"\s+" + "coding" + r"\b",
]

ALLOWED_BINARY_SUFFIXES = {".zip", ".png", ".jpg", ".jpeg", ".gif", ".webp", ".pdf"}

OFFICIAL_PIPELINE_STAGES = [
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
]

PIPELINE_KEY_FILES = [
    "README.md",
    "AGENTS.md",
    "ai-adapters/CLAUDE.md",
    "ai-adapters/CODEX.md",
    "ai-adapters/GEMINI.md",
    "ai-adapters/COPILOT.md",
    "ai-adapters/GROK.md",
    "ai-adapters/WINDSURF.md",
    "ai-adapters/GENERIC-AGENT.md",
    "ai-adapters/BUILDER-INGESTION.md",
    ".github/copilot-instructions.md",
    "docs/02-methodology.md",
    "docs/13-blueprint-compiler.md",
    "docs/14-vertical-blueprint-contracts.md",
    "docs/16-cross-tool-ingestion-matrix.md",
    "docs/20-artifact-toolkit-model.md",
    "docs/21-command-model.md",
    "skills/specification-driven-coding/SKILL.md",
    "prompts/write-vertical-blueprint.prompt.md",
    "prompts/write-plan.prompt.md",
    "prompts/generate-tasks.prompt.md",
    "blueprints/README.md",
    "plugins/README.md",
]

FORBIDDEN_PIPELINE_PATTERNS = [
    r"spec(?:\.md)?\s+e\s+plan(?:\.md)?\s+in\s+un\s+blueprint",
    r"Plan\s*[-–—>→]+\s*Tasks\s*[-–—>→]+\s*Vertical Blueprint",
    r"Plan\.\s*Tasks\.\s*Vertical blueprint",
]


def fail(msg: str) -> None:
    print(f"FAIL: {msg}")
    sys.exit(1)


def text_files():
    for path in ROOT.rglob("*"):
        if path.is_file() and path.suffix.lower() not in ALLOWED_BINARY_SUFFIXES and ".git" not in path.parts:
            yield path


def has_official_pipeline(text: str) -> bool:
    """Return true when the official stages appear in the required order."""
    normalized = text.lower()
    position = -1
    for stage in OFFICIAL_PIPELINE_STAGES:
        found = normalized.find(stage.lower(), position + 1)
        if found == -1:
            return False
        position = found
    return True


def check_pipeline_consistency() -> int:
    issues = 0
    for rel in PIPELINE_KEY_FILES:
        path = ROOT / rel
        text = path.read_text(encoding="utf-8", errors="ignore")
        if not has_official_pipeline(text):
            print(f"PIPELINE: {rel} does not contain the official pipeline order")
            issues += 1
    for path in text_files():
        text = path.read_text(encoding="utf-8", errors="ignore")
        for pattern in FORBIDDEN_PIPELINE_PATTERNS:
            if re.search(pattern, text, flags=re.IGNORECASE | re.DOTALL):
                print(f"PIPELINE: forbidden order found in {path.relative_to(ROOT)}: {pattern}")
                issues += 1
    return issues


def check_sdc_cli_mapping() -> int:
    """Keep the executable command surface aligned with prompt commands."""
    path = ROOT / "tools/sdc.py"
    text = path.read_text(encoding="utf-8", errors="ignore")
    issues = 0
    for command, rels in REQUIRED_SDC_COMMAND_PROMPTS.items():
        if command not in text:
            print(f"CLI: tools/sdc.py missing command {command}")
            issues += 1
        if not any(rel in text for rel in rels):
            print(f"CLI: tools/sdc.py missing prompt mapping for {command}: {', '.join(rels)}")
            issues += 1
    for utility in [
        "tools/sdc_demo.py",
        "tools/sdc_enforce.py",
        "tools/sdc_compile.py",
        "tools/sdc_handoff.py",
        "demo",
        "enforce",
        "compile",
        "handoff",
    ]:
        if utility not in text:
            print(f"CLI: tools/sdc.py missing utility mapping for {utility}")
            issues += 1
    return issues


def check_handoff_surface() -> int:
    issues = 0
    path = ROOT / "tools" / "sdc_handoff.py"
    if path.exists():
        text = path.read_text(encoding="utf-8", errors="ignore")
        if "RolePromptSignature" not in text:
            print("HANDOFF: tools/sdc_handoff.py must import/use RolePromptSignature")
            issues += 1
        for target in HANDOFF_TARGETS:
            if f'"{target}"' not in text and f"'{target}'" not in text:
                print(f"HANDOFF: missing target {target}")
                issues += 1
        for required in ["input_space", "output_space", "compiled_prompt", "attachments", "target_instructions"]:
            if required not in text:
                print(f"HANDOFF: tools/sdc_handoff.py missing {required}")
                issues += 1
    for rel in ["README.md", "README.it.md", "tools/README.md", "docs/21-command-model.md"]:
        text = (ROOT / rel).read_text(encoding="utf-8", errors="ignore")
        if "sdc handoff" not in text:
            print(f"HANDOFF: {rel} missing handoff command reference")
            issues += 1
    return issues


def check_plugin_targets() -> int:
    issues = 0
    for folder in PLUGIN_TARGET_FOLDERS:
        path = ROOT / "plugins" / folder / "README.md"
        if not path.exists():
            print(f"PLUGINS: missing plugins/{folder}/README.md")
            issues += 1
    return issues


def check_mcp_and_marketplace_docs() -> int:
    issues = 0
    manifest_path = ROOT / "extensions" / "mcp" / "manifest.json"
    if manifest_path.exists():
        try:
            json.loads(manifest_path.read_text(encoding="utf-8"))
        except (OSError, ValueError) as exc:
            print(f"MCP: invalid extensions/mcp/manifest.json: {exc}")
            issues += 1
    market_path = ROOT / "docs" / "39-marketplace-submission-guidelines.md"
    if market_path.exists():
        text = market_path.read_text(encoding="utf-8", errors="ignore")
        if "TO BE VERIFIED" not in text:
            print("MARKETPLACE: docs/39 must contain TO BE VERIFIED")
            issues += 1
        if "SDC Readiness Matrix" not in text:
            print("MARKETPLACE: docs/39 must contain SDC Readiness Matrix")
            issues += 1
    return issues


def check_enforcement_surface() -> int:
    issues = 0
    script = ROOT / "tools" / "sdc_enforce.py"
    if script.exists():
        text = script.read_text(encoding="utf-8", errors="ignore")
        for required in ["CORE_ARTIFACTS", "IMPLEMENTATION_SUFFIXES", "allowed_decisions", "structural_only"]:
            if required not in text:
                print(f"ENFORCE: tools/sdc_enforce.py missing {required}")
                issues += 1
        if "subprocess" in text:
            print("ENFORCE: tools/sdc_enforce.py must not shell out")
            issues += 1
    for rel in [
        "README.md",
        "README.it.md",
        "tools/README.md",
        "docs/21-command-model.md",
        "docs/28-continuous-specification-enforcement.md",
    ]:
        text = (ROOT / rel).read_text(encoding="utf-8", errors="ignore")
        if "sdc enforce" not in text and "sdc_enforce.py" not in text:
            print(f"ENFORCE: {rel} missing enforcement command reference")
            issues += 1
    return issues


def check_integrations_catalog() -> int:
    path = ROOT / "integrations/catalog.json"
    issues = 0
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        print(f"INTEGRATIONS: invalid JSON in {path.relative_to(ROOT)}: {exc}")
        return 1

    if not isinstance(payload, list):
        print("INTEGRATIONS: catalog.json must contain a top-level list")
        return 1

    allowed_types = {
        "generic-agent",
        "cli-agent",
        "editor-agent",
        "app-builder",
        "mcp-agent",
        "repository-instruction",
        "plugin-adapter",
    }
    required_keys = {
        "id",
        "name",
        "file",
        "type",
        "requires_cli",
        "supports_skills",
        "primary_use",
        "load_first",
        "known_limits",
        "output_contract",
        "notes",
    }
    seen_ids: set[str] = set()

    for index, entry in enumerate(payload, start=1):
        if not isinstance(entry, dict):
            print(f"INTEGRATIONS: entry {index} is not an object")
            issues += 1
            continue
        missing = sorted(required_keys - set(entry))
        if missing:
            print(f"INTEGRATIONS: entry {index} missing keys: {', '.join(missing)}")
            issues += 1
        entry_id = entry.get("id")
        if not isinstance(entry_id, str) or not entry_id:
            print(f"INTEGRATIONS: entry {index} has invalid id")
            issues += 1
            continue
        if entry_id in seen_ids:
            print(f"INTEGRATIONS: duplicate id {entry_id}")
            issues += 1
        seen_ids.add(entry_id)
        entry_type = entry.get("type")
        if entry_type not in allowed_types:
            print(f"INTEGRATIONS: invalid type for {entry_id}: {entry_type}")
            issues += 1
        file_path = entry.get("file")
        if not isinstance(file_path, str) or not (ROOT / file_path).exists():
            print(f"INTEGRATIONS: missing file for {entry_id}: {file_path}")
            issues += 1
        load_first = entry.get("load_first")
        if not isinstance(load_first, list) or not load_first:
            print(f"INTEGRATIONS: invalid load_first for {entry_id}")
            issues += 1
        else:
            for rel in load_first:
                if not isinstance(rel, str) or not (ROOT / rel).exists():
                    print(f"INTEGRATIONS: invalid load_first path for {entry_id}: {rel}")
                    issues += 1
    return issues


def check_extension_catalog() -> int:
    path = ROOT / "extensions" / "catalog.json"
    issues = 0
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        print(f"EXTENSIONS: invalid JSON in {path.relative_to(ROOT)}: {exc}")
        return 1

    if not isinstance(payload, list):
        print("EXTENSIONS: catalog.json must contain a top-level list")
        return 1

    allowed_types = {
        "benchmark-pack",
        "adapter-pack",
        "scorecard-pack",
        "workflow-pack",
        "language-pack",
        "governance-pack",
        "project-profile-pack",
    }
    allowed_status = {"core", "experimental", "planned"}
    required_keys = {
        "id",
        "name",
        "type",
        "status",
        "files",
        "primary_use",
        "requires",
        "output_contract",
        "known_limits",
    }
    forbidden_language = re.compile(
        r"marketplace|auto-install|automatically install|remote registry|fetch from GitHub|package manager",
        flags=re.IGNORECASE,
    )
    seen_ids: set[str] = set()

    for index, entry in enumerate(payload, start=1):
        if not isinstance(entry, dict):
            print(f"EXTENSIONS: entry {index} is not an object")
            issues += 1
            continue
        missing = sorted(required_keys - set(entry))
        if missing:
            print(f"EXTENSIONS: entry {index} missing keys: {', '.join(missing)}")
            issues += 1
        entry_id = entry.get("id")
        if not isinstance(entry_id, str) or not entry_id:
            print(f"EXTENSIONS: entry {index} has invalid id")
            issues += 1
            continue
        if entry_id in seen_ids:
            print(f"EXTENSIONS: duplicate id {entry_id}")
            issues += 1
        seen_ids.add(entry_id)
        if entry.get("type") not in allowed_types:
            print(f"EXTENSIONS: invalid type for {entry_id}: {entry.get('type')}")
            issues += 1
        if entry.get("status") not in allowed_status:
            print(f"EXTENSIONS: invalid status for {entry_id}: {entry.get('status')}")
            issues += 1
        if forbidden_language.search(json.dumps(entry, ensure_ascii=False)):
            print(f"EXTENSIONS: forbidden registry language for {entry_id}")
            issues += 1
        for key in ["files", "requires"]:
            values = entry.get(key)
            if not isinstance(values, list):
                print(f"EXTENSIONS: {entry_id} has invalid {key}")
                issues += 1
                continue
            for rel in values:
                if not isinstance(rel, str) or not (ROOT / rel).exists():
                    print(f"EXTENSIONS: {entry_id} references missing {key} path: {rel}")
                    issues += 1
        for key in ["primary_use", "output_contract", "known_limits"]:
            if not isinstance(entry.get(key), str) or not entry.get(key, "").strip():
                print(f"EXTENSIONS: {entry_id} has empty {key}")
                issues += 1
    return issues


def project_profile_ids() -> set[str]:
    ids: set[str] = set()
    for path in (ROOT / "project-types").glob("[0-9][0-9]-*.md"):
        ids.add(re.sub(r"^\d\d-", "", path.stem))
    return ids


def check_profile_depth() -> int:
    issues = 0
    profile_ids = project_profile_ids()
    for profile_id in sorted(profile_ids):
        depth_dir = ROOT / "project-types" / profile_id
        if not depth_dir.is_dir():
            print(f"PROFILE_DEPTH: missing folder project-types/{profile_id}")
            issues += 1
            continue

        unexpected_sidecar_dirs = [
            path.name for path in depth_dir.iterdir() if path.is_dir() and path.name not in IGNORED_PROFILE_DEPTH_DIRS
        ]
        for name in unexpected_sidecar_dirs:
            print(f"PROFILE_DEPTH: {profile_id} has unexpected directory: {name}")
            issues += 1
        actual_files = {
            path.name
            for path in depth_dir.iterdir()
            if path.is_file()
            and path.name not in IGNORED_PROFILE_DEPTH_SIDECARS
            and path.suffix not in IGNORED_PROFILE_DEPTH_SUFFIXES
        }
        missing = sorted(PROFILE_DEPTH_FILES - actual_files)
        extra = sorted(actual_files - PROFILE_DEPTH_FILES)
        if missing:
            print(f"PROFILE_DEPTH: {profile_id} missing files: {', '.join(missing)}")
            issues += 1
        if extra:
            print(f"PROFILE_DEPTH: {profile_id} has extra files: {', '.join(extra)}")
            issues += 1

        for name in PROFILE_DEPTH_FILES:
            path = depth_dir / name
            if path.exists() and not path.read_text(encoding="utf-8", errors="ignore").strip():
                print(f"PROFILE_DEPTH: {profile_id}/{name} is empty")
                issues += 1

        stack_path = depth_dir / "stack-options.json"
        if stack_path.exists():
            try:
                stack_payload = json.loads(stack_path.read_text(encoding="utf-8"))
            except (OSError, ValueError) as exc:
                print(f"PROFILE_DEPTH: {profile_id}/stack-options.json invalid JSON: {exc}")
                issues += 1
                stack_payload = {}
            options = stack_payload.get("options") if isinstance(stack_payload, dict) else None
            if not isinstance(options, list) or not (3 <= len(options) <= 5):
                print(f"PROFILE_DEPTH: {profile_id} must define 3-5 stack options")
                issues += 1
            else:
                default_count = sum(1 for option in options if isinstance(option, dict) and option.get("default") is True)
                if default_count != 1:
                    print(f"PROFILE_DEPTH: {profile_id} must have exactly one default stack option")
                    issues += 1
                for index, option in enumerate(options, start=1):
                    if not isinstance(option, dict):
                        print(f"PROFILE_DEPTH: {profile_id} stack option {index} is not an object")
                        issues += 1
                        continue
                    missing_keys = sorted(STACK_OPTION_KEYS - set(option))
                    if missing_keys:
                        print(f"PROFILE_DEPTH: {profile_id} stack option {index} missing keys: {', '.join(missing_keys)}")
                        issues += 1
                    for key in STACK_OPTION_KEYS:
                        value = option.get(key)
                        if not isinstance(value, str) or not value.strip():
                            print(f"PROFILE_DEPTH: {profile_id} stack option {index} has empty {key}")
                            issues += 1

        for name in ["domain-dictionary.json", "performance-budget.json"]:
            path = depth_dir / name
            if path.exists():
                try:
                    json.loads(path.read_text(encoding="utf-8"))
                except (OSError, ValueError) as exc:
                    print(f"PROFILE_DEPTH: {profile_id}/{name} invalid JSON: {exc}")
                    issues += 1
        failure_path = depth_dir / "failure-modes.md"
        if failure_path.exists():
            failure_text = failure_path.read_text(encoding="utf-8", errors="ignore")
            for section in FAILURE_MODE_SECTIONS:
                if section not in failure_text:
                    print(f"PROFILE_DEPTH: {profile_id}/failure-modes.md missing section {section}")
                    issues += 1
    return issues


def validate_decision_ledger(path: Path, label: str) -> int:
    issues = 0
    seen_ids: set[str] = set()
    lines = [line for line in path.read_text(encoding="utf-8", errors="ignore").splitlines() if line.strip()]
    if not lines:
        print(f"DECISION_LEDGER: {label} is empty")
        return 1
    for line_number, line in enumerate(lines, start=1):
        try:
            entry = json.loads(line)
        except ValueError as exc:
            print(f"DECISION_LEDGER: {label}:{line_number} invalid JSON: {exc}")
            issues += 1
            continue
        if not isinstance(entry, dict):
            print(f"DECISION_LEDGER: {label}:{line_number} must be an object")
            issues += 1
            continue
        missing = sorted(DECISION_LEDGER_FIELDS - set(entry))
        if missing:
            print(f"DECISION_LEDGER: {label}:{line_number} missing fields: {', '.join(missing)}")
            issues += 1
        entry_id = entry.get("id")
        if not isinstance(entry_id, str) or not re.fullmatch(r"DEC-\d{3}", entry_id):
            print(f"DECISION_LEDGER: {label}:{line_number} invalid id: {entry_id}")
            issues += 1
        elif entry_id in seen_ids:
            print(f"DECISION_LEDGER: {label}:{line_number} duplicate id: {entry_id}")
            issues += 1
        else:
            seen_ids.add(entry_id)
        if entry.get("type") not in DECISION_LEDGER_TYPES:
            print(f"DECISION_LEDGER: {label}:{line_number} invalid type: {entry.get('type')}")
            issues += 1
        if not isinstance(entry.get("reversible"), bool):
            print(f"DECISION_LEDGER: {label}:{line_number} reversible must be boolean")
            issues += 1
        for field in ["decision", "reason", "impact", "verification", "source", "created_at"]:
            if not isinstance(entry.get(field), str) or not entry.get(field, "").strip():
                print(f"DECISION_LEDGER: {label}:{line_number} empty {field}")
                issues += 1
    return issues


def validate_capability_boundaries(path: Path, label: str) -> int:
    issues = 0
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        print(f"CAPABILITY_BOUNDARY: {label} invalid JSON: {exc}")
        return 1
    if not isinstance(payload, dict):
        print(f"CAPABILITY_BOUNDARY: {label} must be an object")
        return 1
    missing = sorted(CAPABILITY_BOUNDARY_FIELDS - set(payload))
    if missing:
        print(f"CAPABILITY_BOUNDARY: {label} missing fields: {', '.join(missing)}")
        issues += 1
    for field in CAPABILITY_BOUNDARY_LIST_FIELDS:
        if not isinstance(payload.get(field), list):
            print(f"CAPABILITY_BOUNDARY: {label} field {field} must be a list")
            issues += 1
    for field in sorted(CAPABILITY_BOUNDARY_FIELDS - CAPABILITY_BOUNDARY_LIST_FIELDS):
        if not isinstance(payload.get(field), str) or not payload.get(field, "").strip():
            print(f"CAPABILITY_BOUNDARY: {label} field {field} must be non-empty text")
            issues += 1
    if payload.get("forbidden_patterns") == [] and payload.get("requires_approval") == []:
        print(f"CAPABILITY_BOUNDARY: {label} needs forbidden_patterns or requires_approval rationale")
        issues += 1
    return issues


def check_contract_schema_hardening() -> int:
    issues = 0
    for rel in ["schemas/decision-ledger.schema.json", "schemas/capability-boundary.schema.json"]:
        try:
            json.loads((ROOT / rel).read_text(encoding="utf-8"))
        except (OSError, ValueError) as exc:
            print(f"SCHEMA_HARDENING: invalid JSON in {rel}: {exc}")
            issues += 1
    issues += validate_decision_ledger(
        ROOT / "templates" / "decisions" / "decisions.jsonl.example",
        "templates/decisions/decisions.jsonl.example",
    )
    exception_text = (ROOT / "templates" / "exceptions" / "EXC-template.md").read_text(
        encoding="utf-8", errors="ignore"
    )
    for section in [
        "# Title",
        "## Status",
        "## What diverged",
        "## Expected contract",
        "## Actual behavior",
        "## Reason",
        "## Risk",
        "## Expiration / review date",
        "## Approval",
        "## Follow-up required",
        "## Linked decisions",
    ]:
        if section not in exception_text:
            print(f"SCHEMA_HARDENING: EXC-template.md missing section {section}")
            issues += 1
    docs_text = (ROOT / "docs" / "40-contract-schema-hardening.md").read_text(encoding="utf-8", errors="ignore")
    for required in ["decisions.jsonl", "capability-boundaries.json", "failure-modes.md", "activation-matrix.json", "v0.8"]:
        if required not in docs_text:
            print(f"SCHEMA_HARDENING: docs/40 missing {required}")
            issues += 1
    for rel in [
        "benchmarks/golden/004-compile-structural-validation/decisions.jsonl",
        "benchmarks/golden/004-compile-structural-validation/capability-boundaries.json",
    ]:
        path = ROOT / rel
        if path.exists():
            if path.name == "decisions.jsonl":
                issues += validate_decision_ledger(path, rel)
            else:
                issues += validate_capability_boundaries(path, rel)
    return issues


def check_skill_activation_matrix() -> int:
    issues = 0
    path = ROOT / "skills" / "activation-matrix.json"
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        print(f"SKILL_ACTIVATION: invalid JSON: {exc}")
        return 1
    rules = payload.get("rules") if isinstance(payload, dict) else None
    if not isinstance(rules, list) or not rules:
        print("SKILL_ACTIVATION: rules must be a non-empty list")
        return 1
    profile_ids = project_profile_ids()
    skill_ids = {skill_path.parent.name for skill_path in (ROOT / "skills").glob("*/SKILL.md")}
    seen_ids: set[str] = set()
    for index, rule in enumerate(rules, start=1):
        if not isinstance(rule, dict):
            print(f"SKILL_ACTIVATION: rule {index} is not an object")
            issues += 1
            continue
        missing = sorted(SKILL_ACTIVATION_FIELDS - set(rule))
        if missing:
            print(f"SKILL_ACTIVATION: rule {index} missing fields: {', '.join(missing)}")
            issues += 1
        rule_id = rule.get("id")
        if not isinstance(rule_id, str) or not re.fullmatch(r"SKILL-ACT-\d{3}", rule_id):
            print(f"SKILL_ACTIVATION: rule {index} invalid id: {rule_id}")
            issues += 1
        elif rule_id in seen_ids:
            print(f"SKILL_ACTIVATION: duplicate id {rule_id}")
            issues += 1
        else:
            seen_ids.add(rule_id)
        if rule.get("profile") not in profile_ids:
            print(f"SKILL_ACTIVATION: {rule_id} references missing profile {rule.get('profile')}")
            issues += 1
        if rule.get("phase") not in SKILL_ACTIVATION_PHASES:
            print(f"SKILL_ACTIVATION: {rule_id} invalid phase {rule.get('phase')}")
            issues += 1
        for field in ["activate", "never_activate", "target_cli_hints"]:
            if not isinstance(rule.get(field), list):
                print(f"SKILL_ACTIVATION: {rule_id} field {field} must be a list")
                issues += 1
        for field in ["activate", "never_activate"]:
            for skill in rule.get(field, []):
                if skill not in skill_ids:
                    print(f"SKILL_ACTIVATION: {rule_id} references missing skill {skill}")
                    issues += 1
        for field in ["workspace_state", "condition"]:
            if not isinstance(rule.get(field), str) or not rule.get(field, "").strip():
                print(f"SKILL_ACTIVATION: {rule_id} empty {field}")
                issues += 1
    return issues


def check_role_prompts() -> int:
    issues = 0
    role_dir = ROOT / "agents" / "role-prompts"
    if not role_dir.is_dir():
        print("ROLE_PROMPTS: missing agents/role-prompts")
        return 1
    if not ((role_dir / "README.md").exists() or (role_dir / "INDEX.md").exists()):
        print("ROLE_PROMPTS: missing README.md or INDEX.md")
        issues += 1
    for name in ROLE_PROMPT_FILES:
        path = role_dir / name
        if not path.exists():
            print(f"ROLE_PROMPTS: missing {name}")
            issues += 1
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for section in ROLE_PROMPT_SECTIONS:
            if section not in text:
                print(f"ROLE_PROMPTS: {name} missing section {section}")
                issues += 1
    return issues


def check_sdc_signatures() -> int:
    path = ROOT / "tools" / "sdc_signature.py"
    spec = importlib.util.spec_from_file_location("sdc_signature_check", path)
    if spec is None or spec.loader is None:
        print("SIGNATURE: cannot load tools/sdc_signature.py")
        return 1
    module = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(module)
    except Exception as exc:  # pragma: no cover - surfaced by CLI linter output
        print(f"SIGNATURE: import failed: {exc}")
        return 1
    issues = 0
    for name in ["ProfileSignature", "RolePromptSignature", "DecisionAssertion"]:
        if not hasattr(module, name):
            print(f"SIGNATURE: missing class {name}")
            issues += 1
        elif not hasattr(getattr(module, name), "__dataclass_fields__"):
            print(f"SIGNATURE: {name} is not a dataclass")
            issues += 1
    for class_name in ["ProfileSignature", "RolePromptSignature"]:
        cls = getattr(module, class_name, None)
        if cls and (not hasattr(cls, "input_space") or not hasattr(cls, "output_space")):
            print(f"SIGNATURE: {class_name} missing input_space/output_space")
            issues += 1
    compile_text = (ROOT / "tools" / "sdc_compile.py").read_text(encoding="utf-8", errors="ignore")
    handoff_text = (ROOT / "tools" / "sdc_handoff.py").read_text(encoding="utf-8", errors="ignore")
    if "ProfileSignature" not in compile_text:
        print("SIGNATURE: tools/sdc_compile.py must use ProfileSignature")
        issues += 1
    if "RolePromptSignature" not in handoff_text:
        print("SIGNATURE: tools/sdc_handoff.py must use RolePromptSignature")
        issues += 1
    return issues


def check_profile_domain_hardcoding() -> int:
    issues = 0
    scoped_paths = []
    scoped_paths.extend((ROOT / "project-types").glob("[0-9][0-9]-*.md"))
    for profile_id in project_profile_ids():
        depth_dir = ROOT / "project-types" / profile_id
        if depth_dir.exists():
            scoped_paths.extend(
                path
                for path in depth_dir.iterdir()
                if path.is_file()
                and path.name not in IGNORED_PROFILE_DEPTH_SIDECARS
                and path.suffix not in IGNORED_PROFILE_DEPTH_SUFFIXES
            )
    role_dir = ROOT / "agents" / "role-prompts"
    if role_dir.exists():
        scoped_paths.extend(role_dir.glob("*.md"))

    for path in scoped_paths:
        for line_number, line in enumerate(path.read_text(encoding="utf-8", errors="ignore").splitlines(), start=1):
            if "[APPLIES_IF example only]" in line:
                continue
            lowered = line.lower()
            for term in FORBIDDEN_PROFILE_DEFAULT_TERMS:
                pattern = r"\b" + re.escape(term) + r"\b"
                if re.search(pattern, lowered):
                    print(f"DOMAIN_DEFAULT: {path.relative_to(ROOT)}:{line_number} contains unscoped term {term}")
                    issues += 1
    return issues


def check_preset_catalog() -> int:
    path = ROOT / "presets" / "catalog.json"
    issues = 0
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        print(f"PRESETS: invalid JSON in {path.relative_to(ROOT)}: {exc}")
        return 1

    if not isinstance(payload, list):
        print("PRESETS: catalog.json must contain a top-level list")
        return 1

    allowed_status = {"core", "experimental", "planned"}
    required_keys = {
        "id",
        "name",
        "status",
        "project_profile",
        "blueprints",
        "prompts",
        "scorecards",
        "fixtures",
        "best_for",
        "agent_or_builder_targets",
        "quality_gates",
        "known_limits",
    }
    forbidden_language = re.compile(
        r"marketplace|auto-install|automatically install|remote registry|fetch from GitHub|package manager",
        flags=re.IGNORECASE,
    )
    fixture_ids = {path.name for path in (ROOT / "benchmarks" / "fixtures").iterdir() if path.is_dir()}
    profile_ids = project_profile_ids()
    seen_ids: set[str] = set()

    for index, entry in enumerate(payload, start=1):
        if not isinstance(entry, dict):
            print(f"PRESETS: entry {index} is not an object")
            issues += 1
            continue
        missing = sorted(required_keys - set(entry))
        if missing:
            print(f"PRESETS: entry {index} missing keys: {', '.join(missing)}")
            issues += 1
        entry_id = entry.get("id")
        if not isinstance(entry_id, str) or not entry_id:
            print(f"PRESETS: entry {index} has invalid id")
            issues += 1
            continue
        if entry_id in seen_ids:
            print(f"PRESETS: duplicate id {entry_id}")
            issues += 1
        seen_ids.add(entry_id)
        if entry.get("status") not in allowed_status:
            print(f"PRESETS: invalid status for {entry_id}: {entry.get('status')}")
            issues += 1
        if entry.get("project_profile") not in profile_ids:
            print(f"PRESETS: invalid project_profile for {entry_id}: {entry.get('project_profile')}")
            issues += 1
        if forbidden_language.search(json.dumps(entry, ensure_ascii=False)):
            print(f"PRESETS: forbidden registry language for {entry_id}")
            issues += 1
        for key in ["blueprints", "prompts", "scorecards"]:
            values = entry.get(key)
            if not isinstance(values, list):
                print(f"PRESETS: {entry_id} has invalid {key}")
                issues += 1
                continue
            for rel in values:
                if not isinstance(rel, str) or not (ROOT / rel).exists():
                    print(f"PRESETS: {entry_id} references missing {key} path: {rel}")
                    issues += 1
        fixtures = entry.get("fixtures")
        if not isinstance(fixtures, list):
            print(f"PRESETS: {entry_id} has invalid fixtures")
            issues += 1
        else:
            for fixture in fixtures:
                if fixture not in fixture_ids:
                    print(f"PRESETS: {entry_id} references missing fixture: {fixture}")
                    issues += 1
        quality_gates = entry.get("quality_gates")
        if not isinstance(quality_gates, list) or not quality_gates:
            print(f"PRESETS: {entry_id} has empty quality_gates")
            issues += 1
        else:
            for gate in quality_gates:
                if not isinstance(gate, str) or len(gate.strip().split()) < 3:
                    print(f"PRESETS: {entry_id} has non-concrete quality gate: {gate}")
                    issues += 1
        for key in ["best_for", "known_limits"]:
            if not isinstance(entry.get(key), str) or not entry.get(key, "").strip():
                print(f"PRESETS: {entry_id} has empty {key}")
                issues += 1
    return issues


def check_github_instruction_files() -> int:
    issues = 0
    instructions_dir = ROOT / ".github" / "instructions"
    if not instructions_dir.exists():
        print("GITHUB: missing .github/instructions directory")
        return 1

    instruction_files = sorted(instructions_dir.glob("*.instructions.md"))
    if not instruction_files:
        print("GITHUB: no path-specific instruction files found")
        return 1

    for path in instruction_files:
        text = path.read_text(encoding="utf-8", errors="ignore")
        if not text.startswith("---\n"):
            print(f"GITHUB: {path.relative_to(ROOT)} missing frontmatter")
            issues += 1
            continue
        end = text.find("\n---", 4)
        if end == -1:
            print(f"GITHUB: {path.relative_to(ROOT)} has unterminated frontmatter")
            issues += 1
            continue
        frontmatter = text[4:end]
        if not re.search(r"^applyTo:\s*.+", frontmatter, flags=re.MULTILINE):
            print(f"GITHUB: {path.relative_to(ROOT)} missing applyTo frontmatter")
            issues += 1
        if "Specification-Driven Coding" not in text:
            print(f"GITHUB: {path.relative_to(ROOT)} missing methodology name")
            issues += 1
    return issues


def check_benchmark_fixtures() -> int:
    issues = 0
    fixtures_root = ROOT / "benchmarks" / "fixtures"
    golden_root = ROOT / "benchmarks" / "golden"
    required_golden = ["intake.md", "spec.md", "blueprint.md", "plan.md", "tasks.md", "scorecard.md"]
    compile_expected_keys = {
        "critical_sections_filled": bool,
        "has_default_marker": bool,
        "ask_count_min": int,
        "assumption_count_min": int,
        "score_min": int,
        "required_sections": list,
        "forbidden_empty_sections": bool,
        "default_marker_text": str,
    }
    for fixture_dir in sorted(path for path in fixtures_root.iterdir() if path.is_dir()):
        fixture = fixture_dir.name
        expected_path = fixture_dir / "expected.json"
        fixture_required = ["raw-request.md", "expected.json"] if fixture == "004-compile-structural-validation" else ["raw-prompt.md", "sdc-prompt.md", "expected.json"]
        for name in fixture_required:
            if not (fixture_dir / name).exists():
                print(f"FIXTURE: {fixture} missing {name}")
                issues += 1
        if expected_path.exists():
            try:
                expected = json.loads(expected_path.read_text(encoding="utf-8"))
            except (OSError, ValueError) as exc:
                print(f"FIXTURE: {fixture} invalid expected.json: {exc}")
                issues += 1
                expected = {}
            if fixture == "004-compile-structural-validation":
                if set(expected) != set(compile_expected_keys):
                    print(f"FIXTURE: {fixture} expected.json must contain only compile threshold keys")
                    issues += 1
                for key, expected_type in compile_expected_keys.items():
                    if not isinstance(expected.get(key), expected_type):
                        print(f"FIXTURE: {fixture} expected key {key} has wrong type")
                        issues += 1
            else:
                for key in ["project_profile", "anti_genericity_constraints", "acceptance_criteria", "stack_rationale", "quality_gates"]:
                    if not expected.get(key):
                        print(f"FIXTURE: {fixture} missing expected key {key}")
                        issues += 1
        golden_dir = golden_root / fixture
        for name in required_golden:
            if not (golden_dir / name).exists():
                print(f"FIXTURE: {fixture} missing golden {name}")
                issues += 1
    return issues


def check_demo_surface() -> int:
    issues = 0
    required_paths = [
        "tools/sdc_demo.py",
        "demos/README.md",
        "demos/001-builder-habit-dashboard-walkthrough.md",
        "benchmarks/fixtures/001-builder-habit-dashboard",
        "benchmarks/golden/001-builder-habit-dashboard",
    ]
    for rel in required_paths:
        if not (ROOT / rel).exists():
            print(f"DEMO: missing {rel}")
            issues += 1

    demo_script = ROOT / "tools" / "sdc_demo.py"
    if demo_script.exists():
        text = demo_script.read_text(encoding="utf-8", errors="ignore")
        for required in ["FIXTURES", "GOLDEN", "001-builder-habit-dashboard", "format", "verbose", "markdown"]:
            if required not in text:
                print(f"DEMO: tools/sdc_demo.py missing {required}")
                issues += 1
        if "sdc_harness.py" in text:
            print("DEMO: tools/sdc_demo.py must not call the harness")
            issues += 1

    proof_text = "This demo proves reproducible artifact discipline and anti-genericity constraints."
    limit_text = "It does not prove universal product superiority without real builder comparison."
    for rel in ["demos/README.md", "demos/001-builder-habit-dashboard-walkthrough.md"]:
        path = ROOT / rel
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for required in [
            "Specification-Driven Coding",
            "Raw request -> Intake -> Specification -> Project Profile Selection -> Vertical Blueprint -> Plan -> Tasks -> Implementation -> Evaluation Scorecard -> Release/Iteration",
            "benchmarks/fixtures/001-builder-habit-dashboard",
            proof_text,
            limit_text,
        ]:
            if required not in text:
                print(f"DEMO: {rel} missing required text: {required}")
                issues += 1
    return issues



def check_internal_links() -> int:
    """Check Markdown links and backticked repository paths that point to concrete files."""
    issues = 0
    path_pattern = re.compile(r"`((?:docs|blueprints|scorecards|prompts|skills|project-types|tools|schemas|extensions|presets|integrations|benchmarks|demos|examples|case-studies|\.specify|\.github)/[^`]+?)`")
    md_link_pattern = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
    for path in ROOT.rglob("*.md"):
        text = path.read_text(encoding="utf-8", errors="ignore")
        for match in path_pattern.finditer(text):
            target = match.group(1).split("#", 1)[0]
            if "*" in target or "<" in target or target.endswith("/"):
                continue
            if not (ROOT / target).exists():
                print(f"BROKEN: {path.relative_to(ROOT)} references missing {target}")
                issues += 1
        for match in md_link_pattern.finditer(text):
            target = match.group(1).split("#", 1)[0]
            if not target or target.startswith(("http://", "https://", "mailto:")):
                continue
            if not (path.parent / target).exists():
                print(f"BROKEN: {path.relative_to(ROOT)} links missing {target}")
                issues += 1
    return issues

def main() -> int:
    for rel in REQUIRED_ROOT:
        if not (ROOT / rel).exists():
            fail(f"missing required file: {rel}")

    for command, rels in REQUIRED_SDC_COMMAND_PROMPTS.items():
        if not any((ROOT / rel).exists() for rel in rels):
            fail(f"missing prompt for {command}: expected one of {', '.join(rels)}")

    project_files = sorted((ROOT / "project-types").glob("[0-9][0-9]-*.md"))
    if len(project_files) != 20:
        fail(f"expected 20 project type files, found {len(project_files)}")

    for path in project_files:
        text = path.read_text(encoding="utf-8")
        for section in REQUIRED_PROJECT_SECTIONS:
            if section not in text:
                fail(f"{path.relative_to(ROOT)} missing section {section}")
        if "```text" not in text:
            fail(f"{path.relative_to(ROOT)} missing prompt seed")

    blueprint_files = sorted((ROOT / "blueprints").glob("*.md"))
    if len(blueprint_files) < 7:
        fail(f"expected at least 7 blueprint files, found {len(blueprint_files)}")

    scorecard_files = sorted((ROOT / "scorecards").glob("*.md"))
    if len(scorecard_files) < 4:
        fail(f"expected at least 4 scorecard files, found {len(scorecard_files)}")

    skill_files = sorted((ROOT / "skills").glob("*/SKILL.md"))
    if len(skill_files) < 8:
        fail(f"expected at least 8 skills, found {len(skill_files)}")

    for path in text_files():
        text = path.read_text(encoding="utf-8", errors="ignore")
        for pattern in PROVENANCE_PATTERNS:
            if re.search(pattern, text, flags=re.IGNORECASE):
                fail(f"provenance-like phrase found in {path.relative_to(ROOT)}: {pattern}")
        for pattern in WRONG_NAME_PATTERNS:
            if re.search(pattern, text):
                fail(f"wrong methodology name found in {path.relative_to(ROOT)}: {pattern}")

    broken_links = check_internal_links()
    if broken_links:
        fail(f"found {broken_links} broken internal links")

    pipeline_issues = check_pipeline_consistency()
    if pipeline_issues:
        fail(f"found {pipeline_issues} pipeline consistency issues")

    cli_issues = check_sdc_cli_mapping()
    if cli_issues:
        fail(f"found {cli_issues} sdc CLI mapping issues")

    enforcement_issues = check_enforcement_surface()
    if enforcement_issues:
        fail(f"found {enforcement_issues} enforcement surface issues")

    handoff_issues = check_handoff_surface()
    if handoff_issues:
        fail(f"found {handoff_issues} handoff surface issues")

    integration_issues = check_integrations_catalog()
    if integration_issues:
        fail(f"found {integration_issues} integration catalog issues")

    extension_issues = check_extension_catalog()
    if extension_issues:
        fail(f"found {extension_issues} extension catalog issues")

    preset_issues = check_preset_catalog()
    if preset_issues:
        fail(f"found {preset_issues} preset catalog issues")

    github_issues = check_github_instruction_files()
    if github_issues:
        fail(f"found {github_issues} GitHub instruction issues")

    plugin_issues = check_plugin_targets()
    if plugin_issues:
        fail(f"found {plugin_issues} plugin target issues")

    mcp_marketplace_issues = check_mcp_and_marketplace_docs()
    if mcp_marketplace_issues:
        fail(f"found {mcp_marketplace_issues} MCP/marketplace doc issues")

    demo_issues = check_demo_surface()
    if demo_issues:
        fail(f"found {demo_issues} demo surface issues")

    fixture_issues = check_benchmark_fixtures()
    if fixture_issues:
        fail(f"found {fixture_issues} benchmark fixture issues")

    profile_depth_issues = check_profile_depth()
    if profile_depth_issues:
        fail(f"found {profile_depth_issues} profile depth issues")

    contract_schema_issues = check_contract_schema_hardening()
    if contract_schema_issues:
        fail(f"found {contract_schema_issues} contract schema hardening issues")

    skill_activation_issues = check_skill_activation_matrix()
    if skill_activation_issues:
        fail(f"found {skill_activation_issues} skill activation matrix issues")

    role_prompt_issues = check_role_prompts()
    if role_prompt_issues:
        fail(f"found {role_prompt_issues} role prompt issues")

    signature_issues = check_sdc_signatures()
    if signature_issues:
        fail(f"found {signature_issues} signature issues")

    domain_default_issues = check_profile_domain_hardcoding()
    if domain_default_issues:
        fail(f"found {domain_default_issues} domain hardcoding issues")

    print("PASS: Specification-Driven Coding repo structure is valid")
    print(f"Project profiles: {len(project_files)}")
    print(f"Blueprints: {len(blueprint_files)}")
    print(f"Scorecards: {len(scorecard_files)}")
    print(f"Skills: {len(skill_files)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
