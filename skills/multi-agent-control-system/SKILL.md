---
name: specification-driven-coding-multi-agent-control-system
description: Use when designing multi-agent orchestration, control towers, agentic operations, or tool-calling systems.
---

# specification-driven-coding-multi-agent-control-system

## Instructions

Use `project-types/09-multi-agent-control-system.md`, `docs/08-agent-governance.md` and `blueprints/05-multi-agent-system-blueprint.md`.

## Required reading

- `AGENTS.md`
- `docs/02-methodology.md`
- `docs/08-agent-governance.md`
- `docs/14-vertical-blueprint-contracts.md`
- `project-types/09-multi-agent-control-system.md`
- `blueprints/05-multi-agent-system-blueprint.md`
- `scorecards/implementation-scorecard.md`

## Required output before implementation

- Process/decision being coordinated
- Agent role cards
- State machine
- Tool registry
- Read/write permissions
- Human approval gates
- Memory/context policy
- Telemetry/evaluation
- Failure modes
- Scorecard

## Failure condition

Do not create a swarm of vague agents. Every agent must have mandate, input, output, tools, limits and reviewer.
