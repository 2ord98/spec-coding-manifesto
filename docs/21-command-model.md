# Command model

## Purpose

Define the repository-native command model for Specification-Driven Coding. These commands are available as prompt files, agent skills, builder instructions, and the lightweight CLI dispatcher `tools/sdc.py`.

## When to use

Use this file when an agent, app builder, or maintainer needs an executable sequence equivalent to a slash-command workflow.

## Inputs

- Raw request or existing repo context.
- `AGENTS.md`
- `.specify/memory/constitution.md`
- Relevant `project-types/`
- Relevant `blueprints/`
- Relevant `scorecards/`

## Outputs

- Ordered artifacts from intake through release/iteration.
- Gate definitions for each step.
- CLI/prompt mapping for the `/sdc.*` command surface.

## Official pipeline

Raw request -> Intake -> Specification -> Project Profile Selection -> Vertical Blueprint -> Plan -> Tasks -> Implementation -> Evaluation Scorecard -> Release/Iteration

## Commands

The commands below are the repository command layer. Some commands are helper gates around the official pipeline rather than additional methodology stages: `/sdc.constitution` records operating principles before intake, `/sdc.clarify` tightens the specification before profile selection, `/sdc.checklist` validates readiness after tasks, and `/sdc.analyze` checks cross-artifact consistency before implementation.

| Command | Purpose | Input artifacts | Output artifacts | Gate/check | Next command |
|---|---|---|---|---|---|
| `/sdc.constitution` | Establish or review project principles | Repo context, `AGENTS.md` | Constitution/project principle update | Principles do not conflict with methodology | `/sdc.intake` |
| `/sdc.intake` | Normalize raw request and detect mode | Raw request, repo context | Intake, mode, blocking questions, assumptions | No direct implementation from vague prompt | `/sdc.specify` |
| `/sdc.specify` | Produce buildable specification | Intake, assumptions | `spec.md` or equivalent specification | Requirements, non-goals, acceptance criteria present | `/sdc.clarify` |
| `/sdc.clarify` | Resolve blocking ambiguity | Specification draft | Answers or assumption ledger | Maximum 5 blocking questions | `/sdc.profile` |
| `/sdc.profile` | Select project profile | Specification, `project-types/` | Primary profile and optional secondary profile | Maximum two primary profiles, rationale present | `/sdc.blueprint` |
| `/sdc.blueprint` | Compile execution contract | Spec, profile, assumptions | Vertical Blueprint | Stack, file tree, security, output, tests, fallback present | `/sdc.plan` |
| `/sdc.plan` | Create technical plan | Spec, blueprint | Plan | Plan follows blueprint decisions | `/sdc.tasks` |
| `/sdc.tasks` | Break plan into tasks | Spec, blueprint, plan | Dependency-aware tasks | Atomic, ordered, verifiable tasks | `/sdc.checklist` |
| `/sdc.checklist` | Validate artifact readiness | Spec, blueprint, plan, tasks | Checklist result | Critical checklist items pass or block | `/sdc.analyze` |
| `/sdc.analyze` | Check cross-artifact consistency | Spec, blueprint, plan, tasks, checklist | Analysis report | No unresolved contradictions before code | `/sdc.implement` |
| `/sdc.implement` | Implement approved tasks | Spec, blueprint, plan, tasks | Code, docs, tests, changed artifacts | Validation-first or TDD where applicable | `/sdc.score` |
| `/sdc.score` | Evaluate delivery | Output, tests, artifacts | Evaluation Scorecard | Score and residual risks are explicit | `/sdc.iterate` |
| `/sdc.iterate` | Release, rollback, or update artifacts | Scorecard, changed output | Release/iteration decision, retro-spec | Spec/blueprint updated if behavior diverged | Next request or `/sdc.intake` |

## CLI surface

Use `tools/sdc.py` when a terminal-facing workflow is useful:

```bash
pip install -e .
sdc doctor
sdc doctor --quick
sdc list
sdc harness run --fixture 001-builder-habit-dashboard
python3 -m sdc_cli doctor
python3 -m sdc_cli doctor --quick
python3 tools/sdc.py list
python3 tools/sdc.py show /sdc.blueprint
python3 tools/sdc.py inspect /sdc.blueprint
python3 tools/sdc.py integration list
python3 tools/sdc.py integration list --format json
python3 tools/sdc.py extension list
python3 tools/sdc.py extension list --format json
python3 tools/sdc.py preset list
python3 tools/sdc.py preset list --format json
python3 tools/sdc.py demo list
python3 tools/sdc.py demo run --fixture 001-builder-habit-dashboard
python3 tools/sdc.py demo run --fixture 001-builder-habit-dashboard --format json
python3 tools/sdc.py demo run --fixture 001-builder-habit-dashboard --format markdown
python3 tools/sdc.py enforce check --path benchmarks/golden/001-builder-habit-dashboard
python3 tools/sdc.py enforce check --workspace examples/enforcement-smoke
python3 tools/sdc.py enforce check --workspace examples/enforcement-smoke --format json
sdc enforce check --path benchmarks/golden/001-builder-habit-dashboard
python3 tools/sdc.py init "domain app" --type full-stack-saas --out /private/tmp/sdc-init-smoke
python3 tools/sdc.py init --type full-stack-saas --name "domain app"
python3 tools/sdc.py scaffold --list
python3 tools/sdc.py branch --name "domain app" --strategy timestamp
python3 tools/sdc.py artifacts --format json
python3 tools/sdc.py harness run --fixture 001-builder-habit-dashboard
python3 tools/sdc.py doctor
python3 tools/sdc.py doctor --quick
python3 -m sdc_cli integration list
python3 -m sdc_cli extension list
python3 -m sdc_cli preset list
python3 -m sdc_cli demo run --fixture 001-builder-habit-dashboard
python3 -m sdc_cli enforce check --path benchmarks/golden/001-builder-habit-dashboard
```

The `sdc` entrypoint is intended for editable use from a repository checkout. It is not a standalone remote package manager and does not auto-install repository assets outside the checkout.

The CLI is intentionally thin. It exposes the command map, prints or inspects prompt files, delegates workspace creation to `tools/spec_scaffold.py`, and runs existing validation. It does not replace agent judgment or the artifact gates.

`integration list` is a repository integration registry utility. It is not a new `/sdc.*` methodology stage and does not alter the official pipeline.

`extension list` and `preset list` are repository discovery utilities. Extensions describe optional method modules; presets describe operational bundles that point to existing profiles, blueprints, prompts, scorecards, fixtures, and gates. They are not `/sdc.*` methodology stages, do not install or apply anything, and do not alter the official pipeline.

`demo list` and `demo run` are walkthrough utilities. They read existing benchmark fixtures and golden artifacts to show the artifact chain from raw prompt to scorecard. They do not generate applications, call external APIs, require an LLM, or add a new methodology stage.

`enforce check` is a Continuous Specification Enforcement utility. It checks that specification, Vertical Blueprint, plan, tasks, scorecard, optional exceptions, and implementation-like files remain structurally aligned. It is not a `/sdc.*` methodology stage and does not prove semantic correctness.

`init` remains a thin convenience wrapper over `tools/spec_scaffold.py`. The flagged `--type/--name/--out` form still works, and the positional name shorthand is only a backward-compatible onboarding convenience.

`doctor` runs the full release health check, including all benchmark fixtures and enforcement over the benchmark golden folders. `doctor --quick` preserves the fast smoke path with fixture `001` for local iteration.

The CLI is a navigation and validation aid. It does not generate applications, choose product architecture, or replace the Specification-Driven Coding method.

## GitHub ecosystem utilities

GitHub surfaces are repository integration aids, not methodology stages:

- `.github/copilot-instructions.md` gives Copilot the repository-wide operating contract.
- `.github/instructions/*.instructions.md` narrows Copilot behavior by path.
- `.github/workflows/validate.yml` runs the structural release checks in CI.
- `.github/PULL_REQUEST_TEMPLATE.md` and `.github/ISSUE_TEMPLATE/` keep contributions intake-first and validation-first.
- `.devcontainer/devcontainer.json` is optional and only provides a lightweight Python environment for local checks.

The official command sequence remains `/sdc.constitution` through `/sdc.iterate`. GitHub integration does not replace `AGENTS.md`, the CLI, prompts, blueprints, scorecards, or local validation.

## Branch flow

Use branch names as execution contracts, not as decoration:

```text
sdc/<number-or-timestamp>-<feature-or-change-slug>
```

Examples:

```bash
python3 tools/sdc.py branch --name "workshop RSVP builder case study"
python3 tools/sdc.py branch --name "workshop RSVP builder case study" --strategy timestamp
```

Only use `--create` inside a real Git repository and after confirming the branch is needed. A branch is ready for implementation only when the artifact manifest contains raw request, intake, specification, project profile, Vertical Blueprint, plan, tasks, and scorecard.

## Procedure

Run commands in order unless a targeted change uses the compact path from `blueprints/12-targeted-change-blueprint.md`. Compact mode still preserves the same conceptual order.

## Quality gate

Implementation must not start until `/sdc.blueprint`, `/sdc.plan`, `/sdc.tasks`, `/sdc.checklist`, and `/sdc.analyze` have produced usable artifacts or explicitly declared why a smaller mode is sufficient.

## Next artifact

Use the matching prompt in `prompts/` for the command being executed.
