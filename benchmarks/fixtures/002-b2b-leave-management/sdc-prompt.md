# Specification-Driven Coding prompt fixture: B2B leave management

Create a domain-specific B2B leave management web product for companies that need structured employee time-off requests, manager approval, shared team calendar visibility, role-based permissions, and an audit trail.

## Mode

`full-project` for an app-builder or coding-agent run.

## Project profile

Primary: `full-stack-saas`

Secondary: `workflow-automation-rpa` only if the scope shifts toward integrations-first orchestration instead of a core product UI.

## Domain and users

The product serves three core roles:

- Employee who creates and tracks their own leave requests.
- Manager who approves or rejects requests for their reporting line.
- HR/Admin who configures policies, reviews exceptions, and audits history.

The product is a business workflow tool, not a payroll suite or generic company dashboard.

## Core workflows

- Employee creates a leave request with type, dates, partial-day details when needed, note, and optional handoff note.
- Manager reviews pending requests with overlap context and approves or rejects with an explicit decision record.
- Team members see approved leave in a shared calendar with privacy-aware visibility rules.
- HR/Admin can inspect audit history for request lifecycle events and permission-sensitive changes.

## Non-goals

- No payroll processing.
- No benefits administration.
- No performance review tooling.
- No generic CRM, finance, or analytics dashboard expansion.
- No public calendar exposing private employee notes or medical details.

## Stack constraints

Use a conventional full-stack SaaS stack with server-rendered or SPA web UI, relational persistence, and explicit RBAC. Do not choose microservices, event buses, RAG, or multi-agent architecture by default. Do not add payroll integrations unless explicitly required.

## UX contract

Include employee request flow, manager approval inbox, leave calendar, request history, clear status states, and privacy-safe visibility. Avoid generic SaaS cards unless each card maps to a leave workflow such as pending approvals, team coverage, or request status.

## Security and privacy

Treat leave data as sensitive employee data. Store only the minimum data needed for operations. Separate public team-calendar visibility from manager/HR-only request details. Require audit logging for create, submit, approve, reject, cancel, and policy-sensitive edits.

## Acceptance criteria

- Employee can create and submit a leave request.
- Manager can approve a request and the decision appears in history and calendar visibility updates correctly.
- Manager can reject a request with a recorded reason.
- Shared calendar shows approved leave to authorized coworkers without exposing private notes or sensitive categories beyond policy.
- Roles and permissions are explicit for employee, manager, and HR/Admin.
- Stack rationale explains why a conventional full-stack monolith was chosen and why payroll scope was rejected.
- Output includes a scorecard covering anti-genericity, domain fit, privacy, permissions, auditability, testability, and residual risks.
