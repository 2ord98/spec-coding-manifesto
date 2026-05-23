# Vertical Blueprint: B2B leave management

## Role contract

Act as a product-focused web builder implementing only the specified leave workflow. Do not silently add payroll, benefits, recruitment, or generic HR-suite modules.

## Product/domain intent

A business leave management product for employee time-off requests, manager decisions, team planning visibility, and auditable handling of sensitive employee data.

## Project profile

`full-stack-saas`

## Stack contract

Use a conventional full-stack monolith with web UI, server application layer, relational database, and explicit RBAC. The stack rationale is `domain-first full-stack SaaS`: the product needs persistent workflow state, permission checks, audit logging, and privacy-aware shared views without microservice overhead.

Rejected default: payroll or wider HRIS expansion. Reason: the fixture only requires leave workflow operations, calendar visibility, and auditable approvals.

Rejected alternative: workflow-automation-first stack. Reason: integrations can be deferred because the core requirement is the product itself, not cross-tool orchestration.

## Architecture contract

- Entities: employee profile, manager relationship, leave policy summary, leave request, approval decision, audit event, calendar visibility projection.
- Core states: draft, submitted, approved, rejected, canceled.
- Boundaries: employee self-service, manager approval surface, HR/Admin audit surface, shared calendar read model.
- Data invariants: only pending requests can be approved or rejected; approved requests appear in the calendar; rejected requests do not; audit events append for every sensitive transition.

## UX contract

Avoid generic SaaS summary cards unless they map to pending approvals, employee request status, team coverage, or calendar context. The main navigation should center on `My Leave`, `Approvals`, `Team Calendar`, and `Audit/Administration` rather than generic dashboard widgets.

## Security/privacy contract

Leave data is sensitive employee data. Restrict detailed notes and sensitive categories to authorized roles. Team calendar visibility should expose only the minimum approved absence information needed for planning. Require authentication, authorization, server-side validation, and audit logging for sensitive actions.

## Quality gates

- Privacy gate passes.
- Permissions gate passes.
- Auditability gate passes.
- Acceptance criteria can be verified for create/request/approve/reject/calendar visibility.
- Anti-genericity gate passes.
