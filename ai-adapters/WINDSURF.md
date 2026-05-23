# Windsurf adapter

Target: Windsurf Cascade, workspace rules, and AGENTS.md-aware workflows.

Use `AGENTS.md` as the durable repo-level rule. This file is a concise adapter for teams that want a named Windsurf entrypoint.

Read `README.md`, `docs/02-methodology.md`, `docs/13-blueprint-compiler.md`, `docs/14-vertical-blueprint-contracts.md`, `blueprints/`, and `scorecards/`.

Official pipeline:

Raw request -> Intake -> Specification -> Project Profile Selection -> Vertical Blueprint -> Plan -> Tasks -> Implementation -> Evaluation Scorecard -> Release/Iteration

Windsurf must not rely on conversational memory for durable project rules. Encode durable behavior in repo files, keep targeted changes surgical, and require a scorecard for significant output.

For incomplete requests, ask at most 5 blocking questions or declare reversible assumptions before building.
