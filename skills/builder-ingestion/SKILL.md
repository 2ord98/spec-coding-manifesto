---
name: specification-driven-coding-builder-ingestion
description: Use when an AI builder receives this repository as guidance for turning incomplete requests into specific products.
---

# specification-driven-coding-builder-ingestion

## Instructions

Apply `docs/12-builder-ingestion-protocol.md`.

The builder must not execute raw prompts directly. It must compile them into a Builder Execution Packet, then implement.

Official pipeline: Raw request -> Intake -> Specification -> Project Profile Selection -> Vertical Blueprint -> Plan -> Tasks -> Implementation -> Evaluation Scorecard -> Release/Iteration.

## Required output

- Raw intent summary
- Specification-Driven Prompt
- Project profile
- Blocking questions or assumptions
- Vertical Blueprint Contract
- Implementation plan
- Tasks
- Scorecard

## Failure condition

Do not produce a generic app, landing, dashboard or agent flow when the request can be made domain-specific.
