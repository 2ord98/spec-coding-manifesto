# Generic agent adapter

Target: any LLM, coding agent, app builder, MCP-enabled workflow, or prompt-to-product tool without a dedicated adapter.

Ingest this repository in this order: `AGENTS.md`, `README.md`, `docs/02-methodology.md`, `docs/04-prompt-construction-protocol.md`, `docs/13-blueprint-compiler.md`, `docs/14-vertical-blueprint-contracts.md`, relevant `project-types/`, relevant `blueprints/`, and `scorecards/`.

Official pipeline:

Raw request -> Intake -> Specification -> Project Profile Selection -> Vertical Blueprint -> Plan -> Tasks -> Implementation -> Evaluation Scorecard -> Release/Iteration

Do not implement raw vague prompts. Do not silently choose architecture, stack, auth, storage, permissions, privacy posture, deployment, integrations, or scope. Do not produce generic UI, generic seed data, or generic agent flows when the domain can be specified.

For incomplete requests, ask at most 5 blocking questions. If questions cannot be asked, declare conservative reversible assumptions and mark what must be validated after the first output.

Every significant delivery must include acceptance evidence, residual risks, and a scorecard.
