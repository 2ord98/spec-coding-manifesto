# Pull Request Checklist

- [ ] Preserves the official Specification-Driven Coding pipeline.
- [ ] Keeps the Vertical Blueprint before final plan and tasks where applicable.
- [ ] Does not introduce generic output, vague prompts, or silent stack defaults.
- [ ] Uses the official methodology name and repository slug correctly.
- [ ] Contains no AI provenance, private prompt history, or model-authorship language.
- [ ] Runs relevant validation commands and reports results.
- [ ] Updates fixtures, golden artifacts, or harness expectations if benchmark behavior changed.
- [ ] Keeps extension and preset entries discovery-only if touched.

## Validation

```bash
python3 tools/spec_lint.py
python3 tools/sdc.py doctor --quick
```

Add `python3 tools/sdc_harness.py run --all` when fixtures, golden artifacts, scorecards, or harness logic changed.
