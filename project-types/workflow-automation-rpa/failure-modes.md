# Failure Modes: workflow-automation-rpa

## Typical AI failure modes

- destructive automation by default
- no dry-run or rollback plan
- fragile selectors or implicit triggers
- credentials handled informally
- missing idempotency checks

## Detection signals

- Artifact uses generic product structure instead of the workflow automation and integration class.
- Blueprint leaves role, data, permission, error, or validation boundaries implicit.
- Tasks cannot be traced back to spec, blueprint, scorecard, or decision ledger entries.

## Prevention rules

- Keep the profile as a decision boundary, not a template.
- Require rationale and rejected alternatives for architecture choices.
- Mark unresolved high-impact details as `[ASK]` or reversible `[ASSUMPTION]`.
- Do not expand capability, data, network, write, or tool boundaries without approval.

## Verification checks

- Confirm blueprint critical sections are non-empty.
- Confirm stack options, capability boundaries, and decisions are aligned.
- Confirm tests and scorecard gates cover the listed failure modes.
- Confirm no implementation task bypasses unresolved questions.

## Scorecard impact

Failure modes reduce anti-genericity, architecture alignment, security/privacy, performance, testing, and release-readiness scores until resolved or documented as accepted exceptions.
