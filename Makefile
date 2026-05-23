.PHONY: lint list sdc-list sdc-doctor sdc-module-doctor harness harness-001 fixtures scaffold-example score-blueprint

lint:
	python3 tools/spec_lint.py

list:
	python3 tools/spec_scaffold.py --list

sdc-list:
	python3 tools/sdc.py list

sdc-doctor:
	python3 tools/sdc.py doctor

sdc-module-doctor:
	python3 -m sdc_cli doctor

harness:
	python3 tools/sdc_harness.py run --all

harness-001:
	python3 tools/sdc_harness.py run --fixture 001-builder-habit-dashboard

fixtures:
	python3 tools/sdc_harness.py list

score-blueprint:
	python3 tools/score_blueprint.py blueprints/02-full-project-blueprint.md

scaffold-example:
	python3 tools/spec_scaffold.py --type rag-knowledge-assistant --name "knowledge assistant" --out .specification-driven-coding-workspace
