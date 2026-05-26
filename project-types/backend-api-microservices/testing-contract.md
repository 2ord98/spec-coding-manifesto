# Testing Contract: backend-api-microservices

## Purpose

Define validation gates for the `backend-api-microservices` software class.

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
