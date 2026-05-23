# Prompts

## Purpose

Prompt files are the instruction surface for Specification-Driven Coding. They provide repository-native equivalents to a slash-command workflow and are exposed through the lightweight `tools/sdc.py` command surface when terminal access is useful.

Official pipeline: Raw request -> Intake -> Specification -> Project Profile Selection -> Vertical Blueprint -> Plan -> Tasks -> Implementation -> Evaluation Scorecard -> Release/Iteration.

## When to use

Use these files when an agent or builder needs a compact operational instruction for one pipeline step.

## Command mapping

| Command | Prompt file |
|---|---|
| `/sdc.constitution` | `prompts/constitution.prompt.md` |
| `/sdc.intake` | `prompts/intake.prompt.md` |
| `/sdc.specify` | `prompts/write-master-spec.prompt.md` |
| `/sdc.clarify` | `prompts/clarify.prompt.md` |
| `/sdc.profile` | `prompts/select-project-profile.prompt.md` |
| `/sdc.blueprint` | `prompts/write-vertical-blueprint.prompt.md` |
| `/sdc.plan` | `prompts/write-plan.prompt.md` |
| `/sdc.tasks` | `prompts/generate-tasks.prompt.md` |
| `/sdc.checklist` | `prompts/checklist.prompt.md` |
| `/sdc.analyze` | `prompts/analyze.prompt.md` |
| `/sdc.implement` | `prompts/implement.prompt.md` |
| `/sdc.score` | `prompts/evaluate-deliverable-scorecard.prompt.md` |
| `/sdc.iterate` | `prompts/iterate.prompt.md` |

To inspect this mapping from the terminal:

```bash
python3 tools/sdc.py list
python3 tools/sdc.py show /sdc.blueprint
```

## Quality gate

No implementation prompt should run before specification, project profile, Vertical Blueprint, plan, tasks, checklist, and analysis are present, unless targeted-change mode explicitly narrows the artifact set.
