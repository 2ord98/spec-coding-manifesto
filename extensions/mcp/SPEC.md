# MCP Extension Specification

## Purpose

Describe a future MCP surface for Specification-Driven Coding without adding a server in this cycle.

## Tools

- `sdc.compile`: deterministic artifact completion.
- `sdc.handoff`: deterministic prompt assembly.
- `sdc.enforce`: structural contract enforcement.
- `sdc.list_profiles`: profile discovery.
- `sdc.get_blueprint`: blueprint retrieval.
- `sdc.score`: structural scoring.

## Permissions

- Read-only tools may inspect repository artifacts.
- Write tools require human approval.
- Destructive automation is disabled by default.

## Audit requirements

Every tool call should record input artifacts, decision matrix reference, scorecard target, approval state, output, and residual risks.

## Status

Design only. No runtime MCP server is included.
