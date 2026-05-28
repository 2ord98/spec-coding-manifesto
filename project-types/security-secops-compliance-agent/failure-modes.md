# Failure Modes: security-secops-compliance-agent

## Typical AI failure modes

- alerts without triage logic
- destructive remediation by default
- unclear evidence retention
- secret exposure in logs
- approval gates skipped for sensitive actions

## Detection signals

- Artifact uses generic product structure instead of the security operations, audit, and control workflow class.
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
