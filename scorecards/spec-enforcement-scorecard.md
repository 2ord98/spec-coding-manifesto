# Specification Enforcement Scorecard

## Purpose

Score whether Specification-Driven Coding artifacts remain aligned as a living contract during implementation.

## Criteria

| Area | Weight | Evidence |
|---|---:|---|
| Specification and blueprint alignment | 20 | Plan, tasks, implementation notes, and scorecard preserve the spec and Vertical Blueprint. |
| Task coverage | 10 | Tasks cover the planned slices and are updated as work completes. |
| Acceptance criteria coverage | 10 | Acceptance criteria appear in plan, tasks, tests, or scorecard. |
| Non-goals preserved | 10 | Implementation does not silently add rejected scope. |
| Assumptions tracked | 10 | Reversible assumptions are explicit or retired with rationale. |
| Security/privacy constraints preserved | 10 | Privacy, security, and data handling constraints are not bypassed. |
| Anti-genericity preserved | 10 | Domain-specific constraints remain visible through implementation. |
| Scorecard/risk coverage | 10 | Scorecard is fresh and includes residual risks. |
| Documented exceptions | 5 | Accepted deviations are recorded in `exceptions.md` or equivalent notes. |
| Decision required for divergence | 5 | Unresolved divergence triggers update specification, update Vertical Blueprint, fix implementation/artifact, or accept documented exception. |

## Gate

- 90-100: strong alignment.
- 75-89: acceptable with declared risk.
- Below 75: decision required before release.

## Limitation

This is a structural and rubric-based scorecard. It is not proof of semantic correctness.
