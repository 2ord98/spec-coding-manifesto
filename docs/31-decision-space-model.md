# Decision Space Model

## Purpose

Explain how Specification-Driven Coding restricts AI decision space before implementation without becoming a scaffolder or hardcoded template system.

## When to use

Use this document when designing profiles, compile behavior, role prompts, blueprints, or lint gates.

## Inputs

- Raw request
- Selected project profile
- Profile-depth package
- Existing specification artifacts

## Outputs

- Decision matrix
- Open questions marked as `[ASK]`
- Reversible assumptions marked as `[ASSUMPTION]`
- Stack rationale with rejected alternatives
- Scorecard target

## Procedure

Treat the project profile as a decision-space module:

- It declares what kinds of choices are allowed.
- It identifies defaults that must be reviewed.
- It blocks common AI-default shortcuts.
- It forces the agent to explain why an option fits this project.

Decision space is not a template. A template says "build this shape." A decision space says "choose only inside these justified boundaries, then explain the choice."

Stack recommendation is not a hardcoded stack. A default option means:

```text
[DEFAULT -- review and override if needed]
```

The default is an accountable starting point. It is not permission to skip rationale.

## Rationale and rejected alternatives

A stack choice is incomplete unless it includes:

- why this option fits the request;
- why at least one plausible alternative was rejected;
- what risks remain;
- which assumptions could reverse the choice.

This beats fixed scaffolds because it exposes the engineering decision instead of hiding it inside a generated file tree.

## DSPy-inspired mapping

Specification-Driven Coding uses a DSPy-inspired structural model without a DSPy dependency:

- Signature: raw request + profile metadata -> decision matrix + blueprint fields + assumptions + scorecard target.
- Module: each project profile acts as a module with declared inputs and outputs.
- Demonstration: benchmark golden artifacts show expected artifact shape.
- Metric: scorecards and lint gates measure structural completeness.
- Assertion: critical sections must be filled; uncertain fields become `[ASK]` or `[ASSUMPTION]`; stack choices require rationale and rejected alternatives.

No runtime model call is implied. The model is a repository-native contract.

## Quality gate

Before implementation, the agent must prove that the decision space was narrowed by the profile and Vertical Blueprint.

## Next artifact

The next artifact is the plan, generated only after the Vertical Blueprint resolves the decision matrix.
