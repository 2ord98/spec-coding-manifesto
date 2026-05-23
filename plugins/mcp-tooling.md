# MCP Tooling Guide

Quando Specification-Driven Coding viene usato con MCP o tool calling, ogni tool deve avere contratto e permessi.

## Tool Contract

```markdown
# Tool: <name>

## Capability

## Inputs schema

## Output schema

## Side effects

## Permission level
read-only / write / destructive

## Human approval required
yes/no

## Audit log fields
```

## Regole

- Default read-only.
- Scrittura solo con motivazione.
- Destructive actions solo con approval.
- Nessun segreto in prompt o log.
- Ogni tool call deve essere spiegabile.
