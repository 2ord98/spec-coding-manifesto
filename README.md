# Specification-Driven Coding

[![Validate](https://github.com/2ord98/spec-coding-manifesto/actions/workflows/validate.yml/badge.svg)](https://github.com/2ord98/spec-coding-manifesto/actions/workflows/validate.yml)

[Versione italiana →](README.it.md)

AI doesn't need better prompts. It needs contracts.

Specification-Driven Coding is an ingestion layer, execution contract, and continuous specification enforcement protocol for AI-native software construction. It compiles incomplete human intent into verifiable, domain-specific construction contracts that AI builders and coding agents can execute.

- A pipeline, not a prompt template. Raw request -> intake -> specification -> project profile -> Vertical Blueprint -> plan -> tasks -> implementation -> evaluation scorecard -> release.
- Anti-genericity by design. Project profiles, Vertical Blueprints, and scorecard gates reject artifacts that collapse into AI-default product patterns.
- The spec is a living contract. Continuous Specification Enforcement cross-checks specification, blueprint, plan, tasks, and implementation. Drift is named, not hidden.

## Quick Start

```bash
git clone https://github.com/2ord98/spec-coding-manifesto
cd spec-coding-manifesto
pip install -e .
sdc doctor
sdc demo run --fixture 001-builder-habit-dashboard
```

Note: install is editable from a local checkout. A PyPI package is planned but not yet published — use `pip install -e .` for now.

For a faster smoke check:

```bash
sdc doctor --quick
```

What makes this different: most workflows stop at the specification. This one enforces it from intake to release.

## Requirements

- Python 3.11+
- Git

No `uv`, `pipx`, editable install, global command, PATH setup, or shell-specific configuration is required for consumer project mode.

## Consumer Project Mode

For a project that wants to use Specification-Driven Coding as an embedded toolkit, use a deterministic no-install checkout:

```bash
cd my-project
git clone https://github.com/2ord98/spec-coding-manifesto.git .sdc
python3 .sdc/tools/sdc.py doctor --quick
python3 .sdc/tools/sdc.py init "my project" --type marketing-site-cms --out "$PWD/sdc-workspace"
python3 .sdc/tools/sdc.py compile --workspace "$PWD/sdc-workspace/specs/001-my-project"
```

`pip install -e .sdc` is optional, not required. If used directly in a consumer project, editable install may create local `.egg-info` metadata; prefer `python3 .sdc/tools/sdc.py ...` for deterministic no-install usage. If a global `sdc` command is available, it searches the current directory and parents for the nearest `.sdc/tools/sdc.py`.

## Where it fits

Vibe coding is fast: a prompt goes in, usable software often comes out, and the model's defaults quietly become the product. Basic specification-first workflows are a real step forward because they structure the path from request to specification, plan, and tasks. But they often stop at the artifact layer, leaving agents and builders to fill domain detail from their own priors. Editor rule files and coding-agent instructions configure how an agent behaves, but they do not compile what is being built into a domain-specific construction contract.

Specification-Driven Coding adds the missing layers: project profiles that narrow the design space before planning, Vertical Blueprints that encode the actual product, scorecards that judge artifacts against explicit gates rather than vibes, and Continuous Specification Enforcement that keeps specification, blueprint, plan, tasks, and implementation aligned as the project evolves.

Profiles are decision boundaries, not templates. Each profile describes a class of software, its allowed decision space, anti-default constraints, risk filters, stack options, performance budget, security baseline, and testing contract. Market verticals come from the raw request, not from profile defaults.

## Try The Demo

```bash
sdc demo run --fixture 001-builder-habit-dashboard
sdc demo run --fixture 001-builder-habit-dashboard --verbose
sdc demo run --fixture 001-builder-habit-dashboard --format markdown
sdc demo run --fixture 001-builder-habit-dashboard --format json
python3 tools/sdc_demo.py run --fixture 001-builder-habit-dashboard
```

The demo reads existing benchmark artifacts and shows how a vague raw prompt becomes a Specification-Driven Coding artifact chain. It does not generate an app, call external APIs, or require an LLM.

The official pipeline is:

```text
Raw request
  → Intake
  → Specification
  → Project Profile Selection
  → Vertical Blueprint
  → Plan
  → Tasks
  → Implementation
  → Evaluation Scorecard
  → Release/Iteration
```

The `Vertical Blueprint` comes before plan and tasks because it is the execution contract that fixes stack, file tree, boundaries, safety/security constraints, output format, and quality gates before the agent decomposes the work.

Author: **Lorenzo Cassiani**  
Repository slug: `spec-coding-manifesto`  
Methodology name: **Specification-Driven Coding**

## Why It Exists

The main problem with vibe coding is not speed. It is ambiguity.

When a user writes an incomplete request, the AI fills the gaps with median patterns: the same frontend, the same dashboard, the same stack, the same architecture, the same placeholders, and the same appearance of quality. Specification-Driven Coding treats the raw prompt only as a starting point and turns it into an operational contract:

```text
Raw request
  → Intake
  → Specification
  → Project Profile Selection
  → Vertical Blueprint
  → Plan
  → Tasks
  → Implementation
  → Evaluation Scorecard
  → Release/Iteration
```

## What It Is

**Specification-Driven Coding = development guided by explicit, living, verifiable specifications.**

In this repository, `spec` means **specification**. Specificity is the practical result: a good specification forces the AI to build software anchored to domain, users, constraints, stack, quality, and verification criteria.

## How It Differs From Vibe Coding

| Mode | Input | Typical output | Risk |
|---|---|---|---|
| Vibe coding | Natural-language prompt, iterative, often incomplete | Fast prototype | Genericity, implicit decisions, technical debt |
| Toolkit specification-first | Ordered artifacts for specification, planning, task list, and implementation | Structured process | Can still stay too feature-scoped |
| Specification-Driven Coding | Prompt transformed with project profile, blueprint, and scorecard | AI-guided but specific product | More explicit decisions before code |

## How To Use It With Agents And Builders

Load or paste this repository into the target tool, then use a prompt like this:

```text
Use this repository as the operating system for Specification-Driven Coding.
Do not just execute my raw prompt.
First transform it into a Specification-Driven Prompt using:
- AGENTS.md
- docs/04-prompt-construction-protocol.md
- docs/12-builder-ingestion-protocol.md
- docs/13-blueprint-compiler.md
- docs/14-vertical-blueprint-contracts.md
- docs/15-model-execution-principles.md
- docs/18-evaluation-scorecards.md
- the most suitable project profile in project-types/

Then produce a Vertical Blueprint Contract and implement only what the blueprint makes verifiable.
If details are missing, ask at most 5 blocking questions; otherwise declare reversible assumptions and continue.
At the end, return a 0-100 scorecard with gaps and next fixes.
```

## Repository Contents

- `AGENTS.md`: root instructions for agents and builders.
- `ai-adapters/`: concise adapters for Codex, Claude Code, Copilot, Gemini CLI, Grok, Windsurf, generic agents, and app builders.
- `integrations/`: machine-readable registry of the repository's adapters and integration surfaces.
- `extensions/`: discoverable optional method modules that extend Specification-Driven Coding without changing the official pipeline.
- `presets/`: discoverable operational bundles that point to existing profiles, blueprints, prompts, scorecards, fixtures, and gates.
- `MANIFESTO.md`: full manifesto.
- `.specify/memory/constitution.md`: constitution compatible with specification-first workflows.
- `.specify/templates/overrides/`: improved templates for spec, plan, tasks, research, and acceptance.
- `docs/20-artifact-toolkit-model.md`: operating model for artifacts, commands, templates, and validation.
- `docs/21-command-model.md`: `/sdc.*` command model for using the repository as a toolkit.
- `docs/25-english-public-index.md`: English-first public documentation and Italian companion policy.
- `project-types/`: 20 project profiles that reduce generic output. Each profile has a profile-depth package with stack options, domain dictionary, security baseline, performance budget, testing contract, and blueprint template.
- `blueprints/`: vertical contracts for full projects, small tasks, web, mobile, WordPress, RAG, and multi-agent systems.
- `prompts/`: operational prompts for transforming incomplete requests into specific prompts and blueprints.
- `agents/`: role definitions and role prompts for product, requirements, UX, platform, AI, security, QA, implementation, and release.
- `tools/sdc_signature.py`: stdlib-only, DSPy-inspired typed contracts for future compile and handoff phases.
- `skills/`: reusable skills for activating specific workflows.
- `plugins/`: adapters for app builders, AGENTS.md, MCP, Cursor, Claude Code, and specification-first flows.
- `scorecards/`: evaluation rubrics for prompts, blueprints, implementation, and multi-agent systems.
- `tools/`: stdlib-only Python scripts for command surface, scaffold, lint, and heuristic scoring.
- `benchmarks/`: fixtures, golden artifacts, and reports for reproducible harness runs.
- `case-studies/`: raw-prompt vs Specification-Driven Coding comparisons.
- `examples/`: minimal example specification packages.

## Workflow

```text
1. Read the raw request
2. Produce intake with blocking questions or reversible assumptions
3. Write a verifiable specification
4. Select the primary project profile
5. Write a Vertical Blueprint Contract
6. Define stack, file tree, data, integrations, security, performance, and tests in the blueprint
7. Generate the technical plan and atomic tasks from the blueprint
8. Implement with controlled scope
9. Evaluate with an Evaluation Scorecard
10. Run release/iteration and update spec/blueprint if code diverges
```

## Core Principles

> If the AI can choose something important without it being specified or declared as an assumption, the blueprint is not ready.

> An incomplete prompt is not permission to generate generic software. It is a signal to construct a better specification.

> A prompt that is already well structured should not be rebuilt from scratch. It should be preserved, checked, and only completed where critical decisions are missing.

> Every AI-built product must return not only output, but also an evaluation of how well it adheres to the specification.

## CLI Install And Use

Repository contributor mode:

```bash
pip install -e .
sdc doctor
sdc doctor --quick
sdc list
sdc integration list
sdc integration list --format json
sdc extension list
sdc extension list --format json
sdc preset list
sdc preset list --format json
sdc demo list
sdc demo run --fixture 001-builder-habit-dashboard
sdc enforce check --path benchmarks/golden/001-builder-habit-dashboard
sdc enforce check --workspace examples/enforcement-smoke
sdc enforce check --workspace examples/enforcement-smoke --format json
sdc init "domain app" --type full-stack-saas --out /private/tmp/sdc-init-smoke
sdc harness run --fixture 001-builder-habit-dashboard
python3 tools/sdc.py list
python3 tools/sdc.py integration list
python3 tools/sdc.py extension list
python3 tools/sdc.py preset list
python3 tools/sdc.py demo list
python3 tools/sdc.py demo run --fixture 001-builder-habit-dashboard
python3 tools/sdc.py enforce check --path benchmarks/golden/001-builder-habit-dashboard
python3 tools/sdc_enforce.py check --workspace examples/enforcement-smoke
python3 tools/sdc.py init "domain app" --type full-stack-saas --out /private/tmp/sdc-init-smoke
python3 tools/sdc.py harness run --fixture 001-builder-habit-dashboard
python3 tools/spec_lint.py
python3 tools/spec_scaffold.py --list
python3 tools/score_blueprint.py blueprints/02-full-project-blueprint.md
```

Without installation:

```bash
python3 -m sdc_cli doctor
python3 -m sdc_cli doctor --quick
python3 -m sdc_cli integration list
python3 -m sdc_cli extension list
python3 -m sdc_cli preset list
python3 -m sdc_cli demo run --fixture 001-builder-habit-dashboard
python3 -m sdc_cli enforce check --path benchmarks/golden/001-builder-habit-dashboard
python3 tools/sdc.py doctor
```

Consumer no-install mode:

```bash
cd my-project
git clone https://github.com/2ord98/spec-coding-manifesto.git .sdc
python3 .sdc/tools/sdc.py doctor --quick
python3 .sdc/tools/sdc.py init "my project" --type marketing-site-cms --out "$PWD/sdc-workspace"
```

The `sdc` entrypoint is primarily intended for repository contributor mode and embedded `.sdc` checkouts. This release does not package the whole repository as a standalone remote tool and does not auto-install repository assets outside the checkout.

`init` accepts both `--name` and an optional positional shorthand. If `--type` is missing, it fails with a clear example instead of scaffolding implicitly.

`sdc compile` is deterministic and stdlib-only. It fills decision boundaries in existing SDC artifacts from `raw-request.md` and the selected profile-depth package. It does not generate application code, call an LLM/API, or choose a final stack as fact. Unresolved choices are written as `[ASK]`; reversible defaults are written as `[ASSUMPTION]`. Compile assertions use `DecisionAssertion` from `tools/sdc_signature.py`.

`sdc handoff` is planned for a later phase and is not implemented yet.

## Integrations, Extensions, And Presets

`integrations/catalog.json` describes how tools, builders, and agents ingest or use the repository. `extensions/catalog.json` describes optional internal modules that extend the method. `presets/catalog.json` describes ready operational bundles for common Specification-Driven Coding modes.

These catalogs are machine-readable discovery metadata only. They are not automatically installed, not automatically applied, and not a marketplace. They are meant to support future contributions without weakening anti-genericity, scorecards, security, or the official pipeline.

## Continuous Specification Enforcement

Specification-Driven Coding treats the spec and Vertical Blueprint as living contracts, not one-time planning files. If implementation, tasks, scorecards, or artifacts diverge from the contract, the agent must update the specification, update the Vertical Blueprint, fix the implementation/artifact, or accept a documented exception.

```bash
sdc enforce check --path benchmarks/golden/001-builder-habit-dashboard
sdc enforce check --workspace examples/enforcement-smoke --format json
```

The enforcement tool is structural and stdlib-only. It reports alignment risks; it does not prove semantic correctness.

## GitHub And Copilot

The repository includes a lightweight GitHub ecosystem layer:

- `.github/copilot-instructions.md` gives Copilot the repository-wide Specification-Driven Coding rules.
- `.github/instructions/` adds path-specific Copilot guidance for docs, Python CLI files, benchmarks, blueprints, prompts, scorecards, and skills.
- `.github/workflows/validate.yml` runs repository validation in GitHub Actions.
- `.github/PULL_REQUEST_TEMPLATE.md` and `.github/ISSUE_TEMPLATE/` keep contributions aligned with the pipeline and validation gates.
- `.devcontainer/devcontainer.json` is an optional Codespaces/devcontainer convenience for running local checks.

GitHub integration is not required. `AGENTS.md` remains the generic agent entrypoint, and the same artifacts work with other coding agents, app builders, MCP workflows, and local CLI usage.

## Benchmarks And Harness

The repository includes a reproducible structural harness:

```bash
python3 tools/sdc_harness.py run --fixture 001-builder-habit-dashboard
python3 tools/sdc_harness.py run --fixture 002-b2b-leave-management
python3 tools/sdc_harness.py run --fixture 003-internal-pdf-rag-assistant
python3 tools/sdc_harness.py run --all
make harness
```

The current harness validates fixture completeness, golden artifact coverage, and scorecard shape. `doctor` runs all fixtures; `doctor --quick` keeps the fast fixture-001 smoke path. It is a gate, not semantic proof of product quality.

## License

MIT. See `LICENSE`.
