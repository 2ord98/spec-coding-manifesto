# Contract Schema Hardening

## Purpose

Schema hardening turns Specification-Driven Coding conventions into deterministic, lintable artifacts. v0.7 does not add `sdc verify`; it prepares the source-of-truth files that a future verification command can consume.

## Decision ledger

Compiled workspaces include `decisions.jsonl`. It is JSON Lines, one decision per line, with sequential `DEC-NNN` ids.

Required fields:

- `id`
- `type`
- `decision`
- `reason`
- `impact`
- `reversible`
- `verification`
- `source`
- `created_at`

Allowed decision types are defined in `schemas/decision-ledger.schema.json`. The ledger records assumptions, stack choices, scope boundaries, security/privacy choices, testing choices, performance choices, constraints, and exception references.

`sdc compile` emits the ledger deterministically from `[ASSUMPTION]` markers, the default stack option, and stable scope/security/privacy/testing decisions. It does not append ad hoc entries.

## Capability boundaries

Compiled workspaces include `capability-boundaries.json`. It defines what the implementation may not do without explicit approval.

Required fields:

- `forbidden_libraries`
- `forbidden_patterns`
- `off_limits_layers`
- `requires_approval`
- `allowed_external_services`
- `data_boundary`
- `network_boundary`
- `write_boundary`
- `tool_boundary`

Capability boundaries are generated from the selected profile class, profile-depth metadata, raw request evidence, and compile assumptions. They must not infer market-specific rules from profile defaults.

## Drift exception template

`templates/exceptions/EXC-template.md` defines the future workspace convention for exceptions:

```text
exceptions/EXC-NNN-short-slug.md
```

Allowed statuses are `proposed`, `accepted`, `expired`, and `resolved`. Exceptions are not a bypass: they require explicit reason, risk, approval, follow-up, and linked decisions.

## Failure modes

Each profile-depth package now includes `failure-modes.md`. This is the seventh profile-depth file and documents:

- Typical AI failure modes
- Detection signals
- Prevention rules
- Verification checks
- Scorecard impact

Failure modes describe software classes, not market vertical defaults.

## Skill activation matrix

`skills/activation-matrix.json` maps profile, phase, and workspace state to skills that should or should not activate. It is deterministic metadata only. It does not execute skills, install tools, or call remote services.

Each rule has:

- `id`
- `profile`
- `phase`
- `workspace_state`
- `activate`
- `never_activate`
- `condition`
- `target_cli_hints`

## Future v0.8 verify

Future `sdc verify` can consume:

- `decisions.jsonl`
- `capability-boundaries.json`
- drift exception records
- `failure-modes.md`
- `skills/activation-matrix.json`
- scorecards and enforcement reports

v0.7 only makes these contracts explicit and lintable. It does not implement runtime semantic verification.
