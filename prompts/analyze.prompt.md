# Prompt - Analyze

```text
Run `/sdc.analyze`.

Analyze consistency across specification, Vertical Blueprint, plan, tasks, checklist, and scorecard expectations.

Inputs:
- spec.md or equivalent specification;
- blueprint.md or Vertical Blueprint;
- plan.md;
- tasks.md;
- checklist result;
- relevant project profile.

Detect:
- contradictions;
- missing requirements;
- tasks not mapped to spec/blueprint;
- silent stack, data, auth, deployment, or integration decisions;
- generic product patterns;
- unverified assumptions;
- missing validation.

Output:
- issue list ordered by severity;
- blocking fixes;
- non-blocking risks;
- implementation readiness decision;
- next command: /sdc.implement if ready.
```
