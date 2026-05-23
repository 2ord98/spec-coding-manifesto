# Specification: B2B leave management

## Project profile

`full-stack-saas`

## Users

Employees request leave, managers approve or reject leave for their reporting line, and HR/Admin audits sensitive actions and maintains policy-level oversight.

## Problem

The company needs a clear, permissioned workflow for requesting, approving, rejecting, and viewing employee leave without turning the product into a generic HR suite or exposing sensitive employee data in the shared calendar.

This must remain a `business leave workflow, not a generic SaaS dashboard`, and it must keep `privacy-safe shared calendar visibility` as a first-order product constraint.

## Functional requirements

- Create, submit, edit, and cancel a leave request before final resolution when policy allows.
- Approve and reject a request with explicit status transitions and recorded decision metadata.
- Show employee request history and current status.
- Show approved leave in a shared team calendar with privacy-safe visibility.
- Enforce role permissions for employee, manager, and HR/Admin actions.
- Record audit trail events for create, submit, approve, reject, cancel, and permission-sensitive edits.
- Provide empty, loading, validation, and authorization error states.

## Non-goals

- No payroll processing.
- No payroll system.
- No benefits administration.
- No recruitment or performance management modules.
- No generic BI dashboard unrelated to leave operations.

## Acceptance criteria

- `create/request` works: an employee can create and submit a leave request with dates, leave type, and note.
- `approve` works: a manager can approve a pending request and the request becomes visible in the shared calendar according to privacy rules.
- `manager can approve or reject a request` without bypassing role permissions or audit logging.
- `reject` works: a manager can reject a pending request with a recorded reason and the request stays out of the approved-leave calendar.
- `shared calendar shows approved leave with privacy controls`: coworkers see approved absences needed for planning, while sensitive notes and private details remain restricted to employee, manager, and HR/Admin as appropriate.
- Roles and permissions are explicit and testable for employee, manager, and HR/Admin.
- Privacy behavior and audit trail expectations are documented.
- Stack rationale explains why a `relational data model with explicit RBAC` and a conventional full-stack SaaS architecture were chosen and why payroll scope was rejected.
