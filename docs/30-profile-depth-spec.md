# Profile Depth Specification

## Purpose

Define the profile-depth package required for every Specification-Driven Coding project profile.

Profiles are decision boundaries, not templates. They describe a class of software, the risks that class creates, and the bounded decision space an agent may use before implementation.

## When to use

Use this document when adding or reviewing files under `project-types/<profile-id>/`.

## Inputs

- Existing profile file in `project-types/<number>-<profile-id>.md`
- Project class described by that profile
- Official pipeline:
  Raw request -> Intake -> Specification -> Project Profile Selection -> Vertical Blueprint -> Plan -> Tasks -> Implementation -> Evaluation Scorecard -> Release/Iteration

## Outputs

Each profile depth package must contain exactly these seven files:

1. `stack-options.json`
2. `domain-dictionary.json`
3. `security-baseline.md`
4. `performance-budget.json`
5. `testing-contract.md`
6. `blueprint-template.md`
7. `failure-modes.md`

## Procedure

Create one folder per profile:

```text
project-types/<profile-id>/
```

Do not delete or replace the existing flat profile Markdown file.

Populate the seven required files with class-specific decision boundaries. The content must constrain implementation without turning the profile into an app generator.

## JSON Contracts

`stack-options.json` must contain this shape:

```json
{
  "profile_id": "profile-id",
  "options": [
    {
      "id": "option-id",
      "name": "Option name",
      "default": true,
      "when_to_use": "Use when this option fits the request, constraints, and risk profile.",
      "when_not_to_use": "Avoid when another option better matches scale, safety, latency, or cost.",
      "rationale": "Why this option belongs in the decision space.",
      "tradeoffs": "Concrete tradeoffs compared with alternatives.",
      "risks": "Failure modes and mitigation concerns."
    }
  ]
}
```

`performance-budget.json` must contain measurable budgets or review targets for the software class.

`domain-dictionary.json` must contain class vocabulary, common users, common artifacts, anti-patterns, and assumption prompts.

`failure-modes.md` must contain these sections:

- `## Typical AI failure modes`
- `## Detection signals`
- `## Prevention rules`
- `## Verification checks`
- `## Scorecard impact`

## Validation Rules

- All 20 profiles must have all seven files.
- Every required file must be non-empty.
- `stack-options.json`, `domain-dictionary.json`, and `performance-budget.json` must be valid JSON.
- `failure-modes.md` must be non-empty and include all required failure-mode sections.
- `stack-options.json` must contain 3-5 stack options.
- Exactly one stack option must have `"default": true`.
- Each stack option must include:
  - `id`
  - `name`
  - `when_to_use`
  - `when_not_to_use`
  - `rationale`
  - `tradeoffs`
  - `risks`
- No profile may hardcode market verticals as defaults.
- If a market-specific example is necessary, mark it as `[APPLIES_IF example only]`.
- Profiles must not imply that one stack is always correct.
- Defaults mean `[DEFAULT -- review and override if needed]`, not automatic implementation.

## Quality gate

A profile-depth package passes only when it narrows the AI decision space while preserving engineering judgment.

## Next artifact

The next artifact is the Vertical Blueprint, which must read the selected profile-depth package before plan and tasks.
