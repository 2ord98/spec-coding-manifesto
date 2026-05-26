# Decision Space Resolution

## Purpose

Define how `sdc compile` turns profile-depth metadata into an explicit stack and architecture decision matrix without hardcoding a final implementation.

## When to use

Use this document when reviewing `tools/sdc_compile.py`, profile-depth packages, or compiled Vertical Blueprints.

## Inputs

- `stack-options.json`
- `domain-dictionary.json`
- `security-baseline.md`
- `performance-budget.json`
- `testing-contract.md`
- raw request text

## Outputs

The Vertical Blueprint must contain a Stack decision space table:

| Choice | Option | Rationale | Rejected alternative | Risk |
|---|---|---|---|---|

Each row comes from profile-depth metadata.

## Default stack semantics

The default option is marked:

```text
[DEFAULT — review and override if needed]
```

This is not a hardcoded stack. It means the option is the safest initial review candidate for the software class, but the developer or agent must still evaluate constraints, tradeoffs, and rejected alternatives.

## Alternatives and rejected options

Compile must show alternatives rather than hide them. Rejected alternatives must be framed structurally:

- rejected because the constraint does not apply;
- rejected because scope is not proven;
- rejected because risk, cost, complexity, or operational burden is unjustified;
- reconsider if the raw request adds new evidence.

## Rationale, tradeoffs, and risks

Every option row must include:

- rationale from `stack-options.json`;
- tradeoff summary;
- risk summary;
- a rejected alternative drawn from the same decision space.

## Abstract example

Project X for user Y with constraint Z may start from the default option, but if constraint Z requires offline behavior, the compiler must surface the alternative that better fits offline behavior and mark the choice as a decision, not a fact.

## Structural validation

Compiled output is valid when:

- no critical blueprint section is empty;
- `[ASK]` items are present for high-impact unknowns;
- `[ASSUMPTION]` items are present for reversible defaults;
- the default marker is present;
- the scorecard references explicit gates;
- the output remains tied to the selected profile class.

## Anti-template rule

Profile-depth files are decision-space modules. They constrain what an agent may decide, but they do not become rigid app templates or market-vertical generators.

## Next artifact

After decision space resolution, the plan and tasks may be compiled against the Vertical Blueprint.
