# Scorecard: B2B leave management

| Area | Score | Evidence |
|---|---:|---|
| Spec adherence | 92 | Covers employee request flow, manager approval/rejection, calendar visibility, permissions, and audit trail. |
| Anti-genericity | 92 | Stays focused on leave workflow and rejects generic SaaS dashboard defaults and payroll expansion. |
| Domain fit | 90 | Models employee, manager, and HR/Admin roles with leave-specific lifecycle states. |
| Architecture | 88 | Conventional full-stack monolith with relational persistence fits durable workflow and RBAC needs. |
| Security/privacy | 92 | Shared calendar visibility is minimized and sensitive notes remain permission-restricted. |
| Permissions | 90 | RBAC is explicit across employee, manager, and HR/Admin actions. |
| Auditability | 90 | Sensitive lifecycle transitions require append-only audit evidence. |
| Testability | 87 | Acceptance checks are explicit for create/request/approve/reject/calendar visibility. |
| Risks | 76 | Regional leave-policy edge cases and accrual complexity remain simplified assumptions. |
| Next fixes | 82 | Add policy configuration depth and external calendar integrations only after explicit scope expansion. |

## Result

Gate: PASS for benchmark fixture.
