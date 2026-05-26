<!-- SDC_COMPILE_GENERATED -->
# Vertical Blueprint Contract: compiled decision contract

## Role contract

Act as a Specification-Driven Coding implementation planner. Do not implement from the raw request alone. Use profile `full-stack-saas` as a decision boundary.

## Domain contract

- User-provided intent: Build project X for user persona Y solving problem Z with constraint W.
- Software class: account-based web product with persistent data, roles, and operational workflows
- Common class users: account user, workspace admin, operator
- Common artifacts: tenant model, role matrix, data model, workflow map, billing or entitlement boundary if requested
- Open questions:
  - [ASK: What is the primary user role and success moment for this project?]
  - [ASK: Which data, privacy, or permission boundaries are non-negotiable?]
  - [ASK: What deployment, ownership, and maintenance constraints apply?]

## Mode contract

- Mode: full-project candidate
- Scope: compile artifacts only; no application code generation.
- Non-goals: no hardcoded market vertical defaults; no stack oracle behavior.
- Assumptions:
  - [ASSUMPTION: Use profile `full-stack-saas` as a software-class decision boundary, not as an app template.]
  - [ASSUMPTION: Use the smallest architecture that satisfies explicit constraints until the request proves otherwise.]
  - [ASSUMPTION: Treat the default stack option as reviewable, not final.]

## Stack decision space

| Choice | Option | Rationale | Rejected alternative | Risk |
|---|---|---|---|---|
| monolith-web-app [DEFAULT — review and override if needed] | Modular web application monolith | Keeps product iteration and deployment simple. Tradeoff: Scaling boundaries arrive later than in service-first designs. | API-first web application | Large modules can blur ownership without clear boundaries. |
| api-first-web-app | API-first web application | Clarifies backend contracts and integration points. Tradeoff: Adds contract maintenance and client coordination. | Modular web application monolith | Premature API breadth can slow product learning. |
| service-split-platform | Service-split platform | Makes operational boundaries explicit. Tradeoff: Higher deployment and observability cost. | Modular web application monolith | Distributed complexity can hide product uncertainty. |

## File tree contract

```text
/workspace/
  raw-request.md
  intake.md
  spec.md
  project-profile.md
  blueprint.md
  plan.md
  tasks.md
  scorecard.md
```

## Architecture contract

- Components: [ASK: Confirm concrete components after stack review.]
- Data flow: [ASK: Confirm data entry, storage, processing, and output boundaries.]
- State management: [ASSUMPTION: Keep state minimal until workflow evidence requires more.]
- Error model: invalid input, missing data, unavailable dependency, permission denial, timeout.
- Observability: log decision-relevant failures without leaking sensitive content.

## Data/API/tool contracts

- Data contract: [ASK: Confirm entities, retention, and ownership.]
- API contract: [ASSUMPTION: Expose only interfaces required by the selected workflow.]
- Tool contract: [ASSUMPTION: Tool calls require explicit permission and auditability.]

## UX/design/motion contract

- UX direction: fit the user-provided intent and selected software class.
- Accessibility: define keyboard, contrast, semantic structure, and error feedback where UI exists.
- Motion: [ASSUMPTION: Use motion only when it clarifies state or feedback.]

## Security hardening contract

# Security Baseline: full-stack-saas

## Purpose

Define the minimum security and privacy review baseline for the `full-stack-saas` software class.

## Required controls

- Identify data classes before choosing storage, auth, or integration boundaries.
- Use least-privilege access for users, services, automations, and tools.
- Validate all external input at trust boundaries.
- Log security-relevant events without exposing secrets or sensitive payloads.
- Document secrets handling, credential rotation, and local development safety.
- Define abuse cases and fallback behavior before implementation.

## Class-specific focus

This profile covers account-based web product with persistent data, roles, and operational workflows. The blueprint must map these controls to the actual raw request instead of assuming a market vertical.

## Quality gate

The Vertical Blueprint must state security assumptions, rejected unsafe defaults, and unresolved approval needs before plan and tasks.

## Performance budget

- startup_or_first_response: Define a measurable first-use or first-response target before implementation.
- steady_state_latency: Document acceptable latency for the primary workflow.
- resource_budget: Set explicit CPU, memory, network, storage, or bundle-size limits when relevant.
- failure_recovery: Define timeout, retry, fallback, and degraded-mode behavior.
- observability: Identify the minimum signals needed to detect performance drift.

## Testing contract

# Testing Contract: full-stack-saas

## Purpose

Define validation gates for the `full-stack-saas` software class.

## Required test layers

- Contract tests for the primary artifact or interface.
- Workflow tests for the highest-risk user path.
- Negative tests for invalid input, permission denial, unavailable dependency, and timeout behavior.
- Regression tests for assumptions that changed during specification.
- Scorecard review against specification, Vertical Blueprint, plan, and tasks.

## Class-specific checks

- Verify that the selected stack option is justified with a rejected alternative.
- Verify that anti-patterns from `domain-dictionary.json` are not present in the plan.
- Verify that performance targets from `performance-budget.json` are represented in acceptance criteria.

## Quality gate

No implementation is complete until validation evidence is linked to the scorecard.

## Output contract

- Preserve user-written artifact content unless `--force` is used.
- Keep `[ASK]` and `[ASSUMPTION]` visible until resolved.
- Plan and tasks must trace back to this blueprint.

## Scorecard

Use `scorecards/implementation-scorecard.md` plus compile assertion checks. Minimum target: 80/100 structural compile gate.
