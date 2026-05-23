# Prompt - Checklist

```text
Run `/sdc.checklist`.

Validate artifact readiness before analysis or implementation.

Inputs:
- spec.md or equivalent specification;
- blueprint.md or Vertical Blueprint;
- plan.md;
- tasks.md;
- docs/05-quality-gates.md.

Check:
- specificity;
- anti-genericity;
- assumptions;
- non-goals;
- stack rationale;
- security/privacy;
- output/file contract;
- tests and acceptance criteria;
- scorecard requirement.

Output:
- PASS/FAIL table;
- blocking gaps;
- smallest correction needed;
- next command: /sdc.analyze if pass.

Do not implement until critical checklist items pass.
```
