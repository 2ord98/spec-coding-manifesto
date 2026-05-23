# English public index

## Purpose

Define the public language policy for Specification-Driven Coding.

## Policy

Root public documents are English-first:

- `README.md`
- `MANIFESTO.md`
- `CONTRIBUTING.md`

Italian companion versions use the `.it.md` suffix:

- `README.it.md`
- `MANIFESTO.it.md`
- `CONTRIBUTING.it.md`

Not every internal Markdown file is translated yet. This is intentional for the current release candidate.

## Translation priority

Future translation work should prioritize files that affect public adoption, onboarding, adapter ingestion, or benchmark interpretation.

Internal implementation docs may remain Italian temporarily when they are not public entry points and do not block English-speaking agents from following the official pipeline:

```text
Raw request -> Intake -> Specification -> Project Profile Selection -> Vertical Blueprint -> Plan -> Tasks -> Implementation -> Evaluation Scorecard -> Release/Iteration
```

## Quality gate

English public docs must remain aligned with their Italian companions. If a public capability is added to `README.md`, the corresponding Italian companion should either include the same capability or explicitly point back to the English source of truth.
