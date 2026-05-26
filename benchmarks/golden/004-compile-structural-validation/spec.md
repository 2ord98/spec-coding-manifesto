<!-- SDC_COMPILE_GENERATED -->
# Feature Spec: compiled decision contract

## Specification-Driven Coding header

- Mode: full-project candidate
- Project profile: `full-stack-saas`
- Prompt normalized: Build project for user persona solving problem with constraint
- Primary user: [ASK: Confirm one of the class users or provide a specific role.] Candidate class users: account user, workspace admin, operator
- Specific problem: Build project X for user persona Y solving problem Z with constraint W.
- Non-goals: no app code generation during compile; no market-vertical assumptions from profile defaults.
- Level: [ASK: Confirm throwaway / prototype / MVP / production / enterprise.]
- Non-negotiable constraints: [ASK: Confirm constraints that affect data, security, UX, integrations, and deployment.]
- Provisional assumptions: [ASSUMPTION: Use profile `full-stack-saas` as a software-class decision boundary, not as an app template.]

## Anti-genericity constraints

- dashboard shell before workflow evidence
- auth plus CRUD as a product substitute
- multi-tenant assumptions without need

## User journeys

### Journey 1 -- primary workflow

- Actor: [ASK: Confirm primary actor.]
- Preconditions: [ASSUMPTION: User can access the intended surface.]
- Steps: [ASK: Confirm the actual workflow steps.]
- Expected outcome: The project solves the stated problem without generic default behavior.
- Edge cases: permissions, unavailable dependency, invalid input, slow network, unclear data ownership.

## Functional requirements

- FR-001: Represent the raw request as a specific workflow, not a generic shell.
- FR-002: Include class artifacts: tenant model, role matrix, data model, workflow map, billing or entitlement boundary if requested
- FR-003: Resolve open questions before implementation or keep them as explicit risks.

## Non-functional requirements

- NFR-001 Performance: satisfy the profile performance budget.
- NFR-002 Security/privacy: satisfy the profile security baseline.
- NFR-003 Accessibility: define user-facing accessibility expectations where UI exists.
- NFR-004 Reliability: define fallback and error behavior before code.
- NFR-005 Maintainability: keep architecture minimal and traceable.

## Domain model

- Entities: [ASK: Confirm entities from the raw request.]
- Relationships: [ASK: Confirm relationships and ownership.]
- Invariants: [ASSUMPTION: Do not infer sensitive data processing without explicit request evidence.]
- Permissions: [ASK: Confirm roles and permissions.]

## Blueprint requirements

- Vertical Blueprint Contract: required.
- File tree required: yes.
- Stack-specific hardening: based on selected profile-depth option.
- Output format: artifact-first, implementation second.

## Acceptance criteria

- AC-001: Blueprint has no empty critical sections.
- AC-002: Stack decision space includes default marker, alternatives, rationale, and risks.
- AC-003: Scorecard contains explicit gates and residual risks.

## Scorecard expectations

- Minimum score: 80/100
- Critical categories: profile fit, anti-genericity, security/privacy, performance, testing, assumptions.

## Open questions

- [ASK: What is the primary user role and success moment for this project?]
- [ASK: Which data, privacy, or permission boundaries are non-negotiable?]
- [ASK: What deployment, ownership, and maintenance constraints apply?]
