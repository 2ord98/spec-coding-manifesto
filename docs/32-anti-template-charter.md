# Anti-Template Charter

## Purpose

State what Specification-Driven Coding must not become.

## When to use

Use this charter when adding profiles, presets, extensions, role prompts, CLI features, or future compile/handoff behavior.

## Inputs

- Repository identity
- Official pipeline
- Profile-depth packages
- Scorecards and lint gates

## Outputs

- A boundary for future implementation
- A review checklist for proposed features

## Procedure

Specification-Driven Coding is not a scaffolder.

Specification-Driven Coding is not a vertical app generator.

Specification-Driven Coding is not a prompt-to-app tool.

Specification-Driven Coding is not a generic template catalog.

Specification-Driven Coding restricts AI decision space before implementation.

It turns vague requests into decision-bounded construction contracts. Those contracts guide builders and coding agents, but they do not remove engineering judgment.

## Guardrails

- Do not privilege one stack as the universal path.
- Do not make any market vertical a hidden default.
- Do not add features that silently produce application code from a vague request.
- Do not let presets weaken anti-genericity gates.
- Do not replace scorecards with vibes.
- Do not skip the Vertical Blueprint before final plan and tasks.

## Human responsibility

Humans retain final engineering judgment. The methodology can surface choices, bound assumptions, and enforce structure; it cannot prove product correctness by itself.

## Quality gate

A change passes this charter only if it makes AI-generated work more specific, more bounded, and more auditable.

## Next artifact

Use this charter when reviewing `docs/30-profile-depth-spec.md`, `docs/31-decision-space-model.md`, profile-depth files, and future compile/handoff work.
