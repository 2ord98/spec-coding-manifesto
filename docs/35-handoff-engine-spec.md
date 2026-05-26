# Handoff Engine Spec

## Purpose

Define `sdc handoff` as deterministic prompt assembly for Specification-Driven Coding workspaces.

## When to use

Use after `sdc compile` or after manually completed artifacts exist and a coding agent, editor agent, app builder, or MCP-enabled workflow needs a bounded execution packet.

## Inputs

- `raw-request.md`
- `intake.md`
- `spec.md`
- `blueprint.md`
- `plan.md`
- `tasks.md`
- `scorecard.md`
- optional `artifact-manifest.json`
- target CLI: `generic`, `codex`, `claude-code`, `cursor`, `aider`, `gemini-cli`, `builder`, `mcp`
- role and scope, or `auto`

## Outputs

- compiled prompt
- attachment list
- target-specific instructions
- optional JSON representation of `RolePromptSignature`

## Procedure

1. Verify workspace artifacts exist.
2. Read `[ASK]` and `[ASSUMPTION]` markers without resolving them.
3. Extract decision matrix and scorecard target.
4. Resolve role and scope.
5. Instantiate `RolePromptSignature`.
6. Assemble a prompt with mission, guardrails, deliverables, validation expectations, and final output contract.

## Quality gate

The output must contain role assumption, mission, deliverables, guardrails, decision matrix instruction, stack selection rule, questions, assumptions, scorecard target, validation expectations, and final output contract.

## Failure behavior

Missing workspace or artifacts fail clearly. `--copy` fails only when requested and no clipboard tool is available. No LLM/API call is ever made.

## Next artifact

The handoff prompt is pasted into the selected coding agent, app builder, or MCP-governed workflow.
