# Builder ingestion adapter

Target: prompt-to-product builders, app builders, hosted coding agents, and multi-agent build systems.

Use this file when the builder accepts one compact instruction document. For deeper context, also ingest `AGENTS.md`, `README.md`, `docs/02-methodology.md`, `docs/12-builder-ingestion-protocol.md`, `docs/13-blueprint-compiler.md`, `docs/14-vertical-blueprint-contracts.md`, `blueprints/`, and `scorecards/`.

Official pipeline:

Raw request -> Intake -> Specification -> Project Profile Selection -> Vertical Blueprint -> Plan -> Tasks -> Implementation -> Evaluation Scorecard -> Release/Iteration

Specification-Driven Coding compiles incomplete requests into execution-ready specifications and vertical blueprints that guide AI builders away from vibe coding and toward explicit, project-specific software construction.

The builder must first produce a Builder Execution Packet: normalized intent, project profile, blocking questions or assumption ledger, Vertical Blueprint, output/file contract, implementation plan, tasks, acceptance gates, and scorecard rubric.

Do not generate a product until the blueprint defines stack rationale, file tree, data assumptions, integrations, security/privacy boundaries, fallback behavior, non-goals, and quality gates.
