---
name: specification-driven-coding-blueprint-compiler
description: Use when converting a raw brief or spec into a Vertical Blueprint Contract for an AI app builder or coding agent.
---

# specification-driven-coding-blueprint-compiler

## Instructions

Compile the request into a blueprint that an AI builder can execute without falling back to generic defaults.

Official pipeline: Raw request -> Intake -> Specification -> Project Profile Selection -> Vertical Blueprint -> Plan -> Tasks -> Implementation -> Evaluation Scorecard -> Release/Iteration.

## Required reading

- `docs/04-prompt-construction-protocol.md`
- `docs/14-vertical-blueprint-contracts.md`
- `blueprints/00-blueprint-contract.md`
- `blueprints/09-blueprint-evaluation.md`
- relevant `project-types/*.md`

## Workflow

1. Detect mode.
2. Produce intake and identify missing critical info.
3. Declare assumptions.
4. Write or validate the specification.
5. Select project profile.
6. Fill role/domain/stack/file/security/performance/test contracts.
7. Run blueprint audit.
8. Produce scorecard expectations.

## Failure condition

Do not emit a blueprint that lacks file tree, security hardening, output contract or scorecard.
