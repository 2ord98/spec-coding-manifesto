# Copilot adapter

Target: GitHub Copilot Chat, Copilot coding agents, and repository custom-instruction workflows.

Use this as the human-readable adapter. For automatic Copilot context, `.github/copilot-instructions.md` is the canonical repository instruction file when the host supports it.

Read `AGENTS.md`, `README.md`, `docs/02-methodology.md`, `docs/04-prompt-construction-protocol.md`, `docs/13-blueprint-compiler.md`, `blueprints/`, and `scorecards/`.

Official pipeline:

Raw request -> Intake -> Specification -> Project Profile Selection -> Vertical Blueprint -> Plan -> Tasks -> Implementation -> Evaluation Scorecard -> Release/Iteration

Copilot must keep instructions short, broadly applicable, and repository-specific. Do not implement vague prompts directly, do not invent architecture or stack defaults, and do not treat scorecards as optional for significant work.

For incomplete requests, ask at most 5 blocking questions. Otherwise declare reversible assumptions and require a verifiable output contract before code.
