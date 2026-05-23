# Artifact toolkit model

## Purpose

Explain how Specification-Driven Coding starts from the useful specification-first toolkit model, then extends it for AI builders, coding agents, and product-generation workflows that begin from incomplete raw requests.

## When to use

Load this file when designing new prompts or tooling, or checking whether a workflow still preserves specification-first discipline.

## Inputs

- `README.md`
- `.specify/memory/constitution.md`
- `.specify/templates/overrides/`
- `docs/02-methodology.md`
- `docs/13-blueprint-compiler.md`
- `docs/14-vertical-blueprint-contracts.md`
- `prompts/`
- `tools/`

## Outputs

- Mapping from toolkit concepts to repository-native artifacts.
- Clear extension points that make Specification-Driven Coding broader than a feature-spec workflow.

## Official pipeline

Raw request -> Intake -> Specification -> Project Profile Selection -> Vertical Blueprint -> Plan -> Tasks -> Implementation -> Evaluation Scorecard -> Release/Iteration

## Artifact model adopted

Specification-Driven Coding adopts the principle that AI-assisted development works better when agents operate from explicit artifacts instead of ad hoc prompting. The core pattern is constitution, specification, clarification, checklist, plan, tasks, analysis, implementation, templates, prompts, and validation scripts.

This repository implements those concepts in its own language and adds a stronger ingestion and blueprint layer.

## Extension added

Specification-Driven Coding treats the first problem as broader than weak prompting. Raw requests are often incomplete, builders fill gaps with median product defaults, agents skip the right skills or context packs, and teams accept repeated stacks, dashboards, landing pages, and hidden assumptions. The repository therefore acts as:

- ingestion layer for incomplete requests;
- compiler from intent to specification;
- project profile router;
- Vertical Blueprint contract before plan/tasks;
- anti-genericity system;
- cross-agent adapter pack;
- evaluation and iteration gate.

## Mapping table

| Toolkit concept | Specification-Driven Coding equivalent | Extension added by this repo | File(s) that implement it |
|---|---|---|---|
| constitution | Project principles and execution discipline | Anti-genericity, human approval, living spec, score every delivery | `.specify/memory/constitution.md`, `AGENTS.md` |
| specify/specification | Specification and Specification-Driven Prompt | Raw request compilation, domain anchoring, assumption ledger | `docs/04-prompt-construction-protocol.md`, `prompts/write-master-spec.prompt.md`, `.specify/templates/overrides/spec-template.md` |
| clarify | Clarification pass | Maximum 5 blocking questions, reversible assumptions for the rest | `prompts/clarify.prompt.md`, `docs/02-methodology.md` |
| checklist | Quality checklist and acceptance gates | Anti-genericity and builder-specific readiness checks | `prompts/checklist.prompt.md`, `docs/05-quality-gates.md`, `.specify/templates/overrides/acceptance-template.md` |
| plan | Technical plan | Plan is generated after the Vertical Blueprint fixes execution boundaries | `prompts/write-plan.prompt.md`, `.specify/templates/overrides/plan-template.md` |
| tasks | Atomic tasks | Dependency-aware tasks mapped to spec and blueprint | `prompts/generate-tasks.prompt.md`, `.specify/templates/overrides/tasks-template.md` |
| analyze | Cross-artifact analysis | Checks spec, blueprint, plan, tasks, assumptions, anti-genericity, and scorecard readiness | `prompts/analyze.prompt.md`, `prompts/audit-before-implementation.prompt.md` |
| implement | Implementation workflow | Enforces blueprint-first boundaries, minimal patches, validation, and retro-spec | `prompts/implement.prompt.md`, `docs/17-agent-execution-discipline.md` |
| templates | Artifact templates | Adds blueprint, scorecard, acceptance, data model, and quickstart extensions | `.specify/templates/overrides/` |
| scripts | Validation scripts | Repository-specific command dispatch, lint, scaffold, and structural scoring | `tools/sdc.py`, `tools/spec_lint.py`, `tools/spec_scaffold.py`, `tools/score_blueprint.py` |
| agent prompts | Agent command files and adapters | Cross-agent packaging for Codex, Claude Code, Copilot, Gemini CLI, Grok, Windsurf, generic agents, and builders | `.github/prompts/`, `ai-adapters/` |
| prerequisites | Required artifacts before implementation | Requires project profile and Vertical Blueprint before final plan/tasks | `docs/14-vertical-blueprint-contracts.md`, `blueprints/02-full-project-blueprint.md`, `blueprints/12-targeted-change-blueprint.md` |
| quality gates | Checklist and review gates | Scorecards plus anti-clone, security/privacy, performance, fallback, and release/iteration gates | `scorecards/`, `docs/18-evaluation-scorecards.md`, `docs/18-scoring-and-evaluation-limits.md` |

## Procedure

1. Start with explicit artifact concepts.
2. Route the raw request through intake and clarification.
3. Produce a specification and choose a project profile.
4. Compile the Vertical Blueprint before final planning.
5. Generate plan and tasks from the blueprint.
6. Analyze artifacts before implementation.
7. Implement only after prerequisites pass.
8. Score and iterate.

## Quality gate

The workflow is aligned when every significant implementation has constitution/project principles, specification, project profile, Vertical Blueprint, plan, tasks, validation, scorecard, and release/iteration path.

## Next artifact

Use `docs/21-command-model.md` to run the repository-native command model.
