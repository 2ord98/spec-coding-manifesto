# GitHub Copilot repository instructions

Work in Specification-Driven Coding mode.

Official pipeline: Raw request -> Intake -> Specification -> Project Profile Selection -> Vertical Blueprint -> Plan -> Tasks -> Implementation -> Evaluation Scorecard -> Release/Iteration.

Read `AGENTS.md` first. Use `README.md`, `docs/02-methodology.md`, `docs/13-blueprint-compiler.md`, `docs/14-vertical-blueprint-contracts.md`, `blueprints/`, and `scorecards/` as source-of-truth documents.

This file is the canonical Copilot repository instruction layer. `ai-adapters/COPILOT.md` is the companion human-readable adapter.

Do not implement vague prompts directly. Ask at most 5 blocking questions, then declare reversible assumptions for non-blocking gaps.

Do not choose stack, auth, storage, deployment, integrations, agent permissions, or scope silently. Every important technical choice needs rationale and a rejected alternative.

For targeted changes, inspect before editing, identify exact files, make the smallest patch, avoid unrelated refactors, run relevant validation, and report changed files plus residual risk.

For full projects and builder work, produce the Vertical Blueprint before final plan and tasks.

Avoid generic app defaults, repeated SaaS/dashboard patterns, decorative files, and unnecessary dependencies.

When editing this repository, run the relevant validation command: `python3 tools/spec_lint.py`, `python3 tools/sdc.py doctor --quick`, `python3 tools/sdc_harness.py run --all`, or `make lint`.

Use the official methodology name: Specification-Driven Coding. Do not write AI provenance, private prompt history, or model-authorship language.
