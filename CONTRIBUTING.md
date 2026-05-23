# Contributing

[Versione italiana →](CONTRIBUTING.it.md)

This repository accepts contributions that improve the **Specification-Driven Coding** protocol without making it more generic.

The goal is not to add more prompts, more documentation, or more complexity.  
The goal is to make AI output more specific, more verifiable, and less dependent on median defaults, recycled templates, and hidden assumptions.

## Guiding Principle

Every contribution must improve at least one of these qualities:

- domain specificity;
- artifact clarity;
- reduction of implicit assumptions;
- quality of Vertical Blueprints;
- anti-genericity of the output;
- security;
- testability;
- scorecard-based evaluation;
- compatibility with builders, coding agents, or multi-agent workflows;
- reproducibility through fixtures, golden artifacts, or harness runs.

If a contribution adds text but does not improve one of these properties, it probably does not belong in the repository.

## Accepted Contribution Types

Contributions are welcome for:

- new project profiles;
- new Vertical Blueprint Contracts;
- new operational prompts;
- new scorecards;
- new skills;
- new adapters for builders or coding agents;
- new benchmark fixtures;
- new golden artifacts;
- new case studies;
- improvements to `tools/sdc.py`;
- improvements to `tools/spec_lint.py`;
- improvements to `tools/sdc_harness.py`;
- naming, link, consistency, or pipeline corrections;
- documentation that makes the protocol more applicable.

## Rejected Contribution Types

Contributions are not accepted if they:

- make the method more generic;
- add vague prompts;
- add templates without quality gates;
- introduce unnecessary mandatory tools;
- turn the repository into a list of links;
- add frameworks or dependencies without rationale;
- duplicate existing content;
- remove security, privacy, or validation constraints;
- reduce the importance of blueprints, scorecards, or anti-genericity;
- present generic output as acceptable just because it works.

## Official Pipeline

Every contribution must respect the official pipeline:

```text
Raw request -> Intake -> Specification -> Project Profile Selection -> Vertical Blueprint -> Plan -> Tasks -> Implementation -> Evaluation Scorecard -> Release/Iteration
```

The **Vertical Blueprint** comes before the final plan and tasks.

## Naming

Always use the official methodology name:

```text
Specification-Driven Coding
```

`spec-coding-manifesto` is allowed only as the repository slug.

## PR Rules

### Project profile

Every new project profile must include:

- when to use it;
- blocking questions;
- stack candidates;
- must-have fields;
- anti-patterns;
- acceptance gates;
- security/privacy considerations;
- performance or deployment assumptions;
- expected scorecard focus.

### Blueprint

Every new blueprint must include:

- role contract;
- domain intent;
- project profile;
- stack rationale;
- architecture/file contract;
- security/privacy contract;
- quality gates;
- validation;
- expected scorecard.

### Prompt

Every new prompt must:

- reduce ambiguity;
- declare inputs and outputs;
- handle incomplete requests;
- use reversible assumptions;
- avoid bloat;
- produce verifiable artifacts.

### Scorecard

Every new scorecard must:

- use weighted criteria;
- include anti-genericity;
- include domain fit;
- include residual risks;
- distinguish structural gates from semantic evaluation.

### Adapter/plugin

Every new adapter must explain:

- the target tool or builder;
- when to use it;
- which files to load;
- the tool limits;
- the required output contract;
- the expected validation.

### Extension catalog entry

Every new extension proposal must include:

- `id`;
- `type`;
- `status`;
- `files`;
- `primary_use`;
- `requires`;
- `output_contract`;
- `known_limits`;
- validation command.

Extensions are discovery metadata only. They must not introduce remote code execution, automatic install behavior, hidden dependencies, generic bundles, or weaker anti-genericity, scorecard, security, privacy, or pipeline constraints. Every listed file must exist.

### Preset catalog entry

Every new preset proposal must include:

- `id`;
- `project_profile`;
- `blueprints`;
- `prompts`;
- `scorecards`;
- `fixtures` when available;
- `best_for`;
- `quality_gates`;
- `known_limits`.

Presets must strengthen specificity, not dilute it. They must not auto-apply files, hide dependencies, bypass validation, or point to generic workflows. Every listed file and fixture must exist.

### Benchmark fixture

Every new benchmark fixture must include:

- `raw-prompt.md`;
- `sdc-prompt.md`;
- `expected.json`;
- golden artifacts:
  - `intake.md`;
  - `spec.md`;
  - `blueprint.md`;
  - `plan.md`;
  - `tasks.md`;
  - `scorecard.md`.

The fixture must pass:

```bash
python3 tools/sdc_harness.py run --fixture <fixture-id>
```

## Contributor Checklist

Before opening a PR:

- [ ] I respected the official pipeline.
- [ ] I avoided generic phrasing.
- [ ] I added verifiable constraints.
- [ ] I included concrete examples.
- [ ] I declared non-goals or anti-patterns.
- [ ] I included quality gates.
- [ ] I updated scorecards or benchmarks when needed.
- [ ] I avoided unnecessary new dependencies.
- [ ] I checked internal links and paths.
- [ ] I ran `python3 tools/spec_lint.py`.
- [ ] I ran `python3 tools/sdc.py doctor`.
- [ ] I ran `make harness`.

## Maintainer Checklist

Before merge:

- [ ] The contribution makes the protocol more specific, not more generic.
- [ ] It does not introduce ambiguity into the pipeline.
- [ ] It does not introduce AI provenance or non-autonomous authorship language.
- [ ] It does not weaken privacy, security, or validation.
- [ ] It does not duplicate content already present.
- [ ] Validation commands pass.
- [ ] The contribution is coherent with the manifesto, command model, blueprints, and scorecards.

## Philosophy

A good contribution does not only add content.  
It adds **operational control**.

A good contribution does not make the AI freer to invent.  
It makes the AI more capable of building specific, verifiable, non-generic products.
