# Gemini CLI adapter

Target: Gemini CLI and Gemini-based coding workflows.

Load this file as project context, then read `AGENTS.md`, `README.md`, `docs/02-methodology.md`, `docs/13-blueprint-compiler.md`, `docs/14-vertical-blueprint-contracts.md`, `blueprints/`, and `scorecards/`.

Official pipeline:

Raw request -> Intake -> Specification -> Project Profile Selection -> Vertical Blueprint -> Plan -> Tasks -> Implementation -> Evaluation Scorecard -> Release/Iteration

Gemini CLI must use this repo as an execution discipline, not as a prompt-length amplifier. Do not jump from a raw prompt to code, do not pick default frameworks or providers without rationale, and do not hide assumptions.

For incomplete requests, ask at most 5 blocking questions. Convert non-blocking gaps into reversible assumptions and continue only when the output contract is verifiable.

Final answers should include validation performed, changed files when applicable, residual risks, and a scorecard for non-trivial work.
