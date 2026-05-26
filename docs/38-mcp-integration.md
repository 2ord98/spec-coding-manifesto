# MCP Integration

## Purpose

Design future MCP integration for Specification-Driven Coding without adding a runtime server in this repository cycle.

## Possible tools

- `sdc.compile`
- `sdc.handoff`
- `sdc.enforce`
- `sdc.list_profiles`
- `sdc.get_blueprint`
- `sdc.score`

## Permissions

Read-only tools may inspect artifacts. Write tools must require explicit approval before modifying files. Destructive operations are out of scope unless a human approves a specific action.

## Approval gates

- Tool call changes architecture, data, security, privacy, cost, or deployment.
- Tool call writes outside the declared workspace.
- Tool call invokes external services.
- Tool call deletes, moves, or rewrites user-authored artifacts.

## Audit log

Every MCP-governed workflow should record requested tool, input artifacts, decision matrix reference, scorecard target, approval status, output, and residual risks.

## Quality gate

The decision matrix and scorecard must travel with tool calls. MCP is a governance surface, not permission to bypass Specification-Driven Coding.
