<!-- SDC_COMPILE_GENERATED -->
# Scorecard: compiled decision contract

- Score total: __/100
- Required threshold: 80/100
- Compile assertion passes: True
- Project profile: `full-stack-saas`

| Category | Weight | Score | Evidence |
|---|---:|---:|---|
| Specification adherence | 15 | | `spec.md` is compiled from raw request and profile-depth. |
| Anti-genericity | 15 | | Profile anti-patterns are included. |
| Architecture and stack | 15 | | Stack decision matrix includes default marker and alternatives. |
| Security/privacy | 15 | | Security baseline included. |
| UX/accessibility | 10 | | UX section includes explicit questions and assumptions. |
| Performance/reliability | 10 | | Performance budget included. |
| Testability | 10 | | Testing contract included. |
| Maintainability | 5 | | Minimal architecture assumption is explicit. |
| Assumptions/risks clarity | 5 | | `[ASK]` and `[ASSUMPTION]` are visible. |

## Compile assertion report

```json
{
  "critical_section_filled": true,
  "has_default_marker": true,
  "ask_count": 3,
  "assumption_count": 3,
  "score_min": 80,
  "passes": true
}
```

## Residual risks

- Resolve `[ASK]` items before implementation.
- Review `[ASSUMPTION]` items before accepting stack or architecture.
