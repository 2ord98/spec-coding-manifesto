# Plan: B2B leave management

## Slice 1: domain model and permissions

Define leave request states, role model, approval invariants, and privacy rules for calendar visibility.

## Slice 2: employee request workflow

Implement create, edit, submit, and cancel flows for employee leave requests.

## Slice 3: manager decision workflow

Implement manager approval and rejection flows with recorded reasons, status transitions, and overlap context.

## Slice 4: shared calendar and history

Implement approved-leave calendar visibility, employee request history, and audit trail views.

## Slice 5: validation

Validate permissions, privacy, auditability, testability, anti-genericity, and scorecard readiness.

## Stack rationale

Use a conventional full-stack monolith with relational persistence because the product needs durable workflow state, RBAC, and audit logging. Reject payroll scope and heavier distributed architectures because they do not serve the MVP leave workflow.
