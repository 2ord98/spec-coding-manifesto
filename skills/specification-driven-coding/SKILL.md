---
name: specification-driven-coding
description: Use when a user wants to build, modify, evaluate or improve software with an AI agent or app builder.
---

# specification-driven-coding

## Instructions

Follow `AGENTS.md`. Treat raw requests as material to compile into a Specification-Driven Coding workflow.

Use this order:

1. Raw request intake.
2. Mode detection.
3. Blocking questions or assumption ledger.
4. Master specification.
5. Project profile selection.
6. Vertical blueprint.
7. Plan.
8. Tasks.
9. Implementation.
10. Evaluation scorecard.
11. Release/iteration or retro-spec.

## Required reading

- `AGENTS.md`
- `docs/01-manifesto.md`
- `docs/02-methodology.md`
- `docs/04-prompt-construction-protocol.md`
- `docs/13-blueprint-compiler.md`
- `docs/14-vertical-blueprint-contracts.md`
- `docs/15-model-execution-principles.md`
- `docs/16-task-and-project-modes.md`
- `docs/18-evaluation-scorecards.md`
- relevant `project-types/*.md`
- relevant `blueprints/*.md`

## Required output before implementation

- Mode.
- Normalized prompt.
- Project profile.
- Assumption ledger.
- Master spec.
- Vertical blueprint.
- Plan.
- Tasks.
- Output/file contract.
- Acceptance gates.
- Expected scorecard.

## Failure condition

Do not proceed directly from a vague request to code. If information is missing, ask maximum 5 blocking questions or declare reversible assumptions.
