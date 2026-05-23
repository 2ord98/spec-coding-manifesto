# Targeted Change Blueprint

Use this blueprint for bug fixes, small features, UI adjustments, config fixes, documentation fixes, security patches, dependency fixes, and update-related repairs.

Legacy path note: `blueprints/03-targeted-change-blueprint.md` is kept only as a compatibility alias that points here.

Official pipeline for targeted work:

Raw request -> Intake -> Specification -> Project Profile Selection -> Vertical Blueprint -> Plan -> Tasks -> Implementation -> Evaluation Scorecard -> Release/Iteration.

For a targeted change, the Vertical Blueprint is intentionally compact: it defines the exact patch boundary before the plan and tasks.

## Role contract

Act as a senior maintainer in surgical patch mode.

## Intake

- Change type:
- Expected behavior:
- Current behavior:
- Exact area or files to inspect:
- Non-goals:
- Risk level:
- Human approval needed:

## Inspect before edit

Before changing files, identify:

- probable cause;
- exact files inspected;
- exact files likely to change;
- public APIs or contracts that must remain stable;
- tests or validation commands to run.

## Minimal patch contract

- Change only what is required.
- Do not refactor unless the bug cannot be fixed without it.
- Do not add dependencies unless the existing stack cannot solve the issue safely.
- Do not alter architecture, storage, auth, permissions, or deployment without promoting the work to feature mode.
- Preserve existing style and naming unless the requested change is about naming.

## Supported change types

| Type | Required extra check |
|---|---|
| Bug fix | Reproduce or explain the probable cause before patching |
| Small feature | State acceptance criteria and non-goals |
| UI adjustment | State affected view, responsive risk, and accessibility check |
| Config fix | State environment and rollback path |
| Documentation fix | State source of truth and changed doc scope |
| Security patch | State threat, sensitive data impact, and approval gate |
| Dependency/update fix | State compatibility risk and lockfile impact |

## Output contract

```markdown
# Targeted Change Packet

## Mode

## Change type

## Probable cause

## Files inspected

## Files to change

## Minimal patch plan

## Regressions to avoid

## Validation

## Rollback

## Scorecard
```

## Stop conditions

Stop before implementation if the patch requires new permissions, new data flows, destructive automation, unclear sensitive-data handling, or architectural changes beyond the declared scope.
