# Prompt — Targeted Change

```text
Work in targeted-change mode using `blueprints/12-targeted-change-blueprint.md`.

Do not expand scope.

Before editing:
1. classify the change type;
2. inspect the relevant files;
3. state probable cause;
4. identify exact files to change;
5. define the minimal patch plan;
6. state regressions to avoid;
7. define validation.

Use the official pipeline in compact form:
Raw request -> Intake -> Specification -> Project Profile Selection -> Vertical Blueprint -> Plan -> Tasks -> Implementation -> Evaluation Scorecard -> Release/Iteration.

Implement only the necessary patch. Do not refactor unless required to solve the declared problem.

Final output must follow the `Targeted Change Packet` contract from `blueprints/12-targeted-change-blueprint.md`, including changed files, reason for each change, validation results, residual risks, and targeted-change scorecard.
```
