# Blueprint Template: marketing-site-cms

## Purpose

Provide class-specific fields that future compile behavior can use to fill a Vertical Blueprint without generating application code.

## Required inputs

- Raw request
- Intake notes
- Selected project profile `marketing-site-cms`
- `stack-options.json`
- `domain-dictionary.json`
- `security-baseline.md`
- `performance-budget.json`
- `testing-contract.md`

## Decision matrix

- [ASK] Confirm primary user role and primary workflow.
- [ASK] Confirm data sensitivity and external integration boundaries.
- [ASK] Confirm deployment, ownership, and maintenance expectations.
- [ASSUMPTION] Use the default stack option only as `[DEFAULT -- review and override if needed]`.
- [ASSUMPTION] Keep implementation boundaries minimal until the raw request proves larger scope.

## Stack decision

Selected option: `[DEFAULT -- review and override if needed]`

Rationale required:

Rejected alternative required:

Risks required:

## Anti-default constraints

- Do not infer a market vertical from this profile.
- Do not generate a template application from the profile alone.
- Do not skip the Vertical Blueprint before plan and tasks.
- Do not hide unresolved decisions inside implementation details.

## Quality gate

The blueprint is valid only when every critical field is filled, or explicitly marked `[ASK]` or `[ASSUMPTION]`.
