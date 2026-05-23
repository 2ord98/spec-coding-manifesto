# Codex adapter

Target: OpenAI Codex and Codex-style coding agents.

Ingest this repository through `AGENTS.md` first, then read `README.md`, `docs/02-methodology.md`, `docs/04-prompt-construction-protocol.md`, `docs/13-blueprint-compiler.md`, `docs/14-vertical-blueprint-contracts.md`, `blueprints/`, and `scorecards/`.

Official pipeline:

Raw request -> Intake -> Specification -> Project Profile Selection -> Vertical Blueprint -> Plan -> Tasks -> Implementation -> Evaluation Scorecard -> Release/Iteration

Codex must not implement directly from a vague request, silently choose stack/auth/data/deploy, introduce broad refactors for targeted changes, or perform sensitive tool calls without approval.

For incomplete requests, ask at most 5 blocking questions. Treat other gaps as reversible assumptions with rationale, impact, reversibility, and verification.

Before implementation, produce the relevant intake, project profile, Vertical Blueprint, plan, tasks, output contract, acceptance gates, and expected scorecard. For small fixes, use `blueprints/12-targeted-change-blueprint.md` and keep the patch minimal.
