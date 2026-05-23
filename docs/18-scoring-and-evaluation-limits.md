# Scoring and evaluation limits

Current scoring in this repository is structural and heuristic. It is useful as a gate, not as proof of product quality.

`tools/score_blueprint.py` checks whether important blueprint concepts appear. It does not understand whether the architecture is actually correct, whether the UX fits the domain, or whether a security model is sufficient.

## What current scoring is good for

- Catching missing sections.
- Detecting incomplete blueprint structure.
- Enforcing that scorecards exist.
- Making weak artifacts visible before implementation.

## What current scoring is not

- A semantic truth evaluator.
- A replacement for human review.
- A guarantee that generated code works.
- A guarantee that security, privacy, performance, or accessibility are sufficient.

## Future evaluation direction

Future semantic evaluation should compare generated artifacts against expected contracts:

- raw prompt fixture;
- expected intake;
- expected specification;
- expected project profile;
- expected Vertical Blueprint;
- expected plan and tasks;
- expected scorecard thresholds;
- expected non-goals and rejection criteria.

Scorecards must be reported transparently. Passing a score threshold does not replace human review, validation commands, security review, or domain review.
