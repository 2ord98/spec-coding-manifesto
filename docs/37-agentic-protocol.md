# Agentic Protocol

## Purpose

Define domain-agnostic governed agent workflows for Specification-Driven Coding.

## Workflows

### Requirements -> Architect -> Engineer -> Reviewer -> Scorecard

Use for new features and full-project slices. Requirements normalizes intent, Architect owns blueprint decisions, Engineer implements bounded tasks, Reviewer checks drift, Scorecard records evidence.

### Architect -> Engineer -> Reviewer -> Optimizer

Use when architecture is known but implementation quality needs iteration. Optimizer cannot change product behavior without updating artifacts.

### Debugger -> Fixer -> Verifier

Use for defects. Debugger identifies root cause, Fixer applies minimal patch, Verifier proves the original symptom and regression path.

### SecurityAuditor -> Implementer -> ReleaseGate

Use for security/privacy-sensitive work. SecurityAuditor names risks, Implementer applies constrained changes, ReleaseGate blocks unresolved divergence.

### MCP tool governance loop

Use when tools can mutate state. Plan tool calls, request approval for sensitive operations, log decisions, attach scorecard evidence, then enforce artifacts after execution.

## Guardrails

- No agent has unlimited authority.
- No silent domain regulation inference.
- No destructive automation without approval.
- Divergence requires update specification, update Vertical Blueprint, fix artifact, or document exception.
