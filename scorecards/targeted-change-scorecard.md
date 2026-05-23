# Targeted Change Scorecard

Use this scorecard for bug fixes, small features, UI adjustments, config fixes, documentation fixes, security patches, dependency fixes, and update-related repairs.

| Area | Weight |
|---|---:|
| Solves the declared problem | 30 |
| Scope remains minimal | 20 |
| Preserves existing behavior/contracts | 15 |
| Validation is relevant and executed | 15 |
| Risk and rollback are clear | 10 |
| Changed files are explained | 10 |
| **Total** | **100** |

Gate guidance:

- 90+: ready for normal delivery.
- 75-89: acceptable with declared residual risk.
- Below 75: do not merge without another patch or explicit acceptance.
