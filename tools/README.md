# Tools

Gli script non richiedono dipendenze esterne.

```bash
pip install -e .
sdc doctor
sdc doctor --quick
sdc list
sdc integration list
sdc integration list --format json
sdc extension list
sdc extension list --format json
sdc preset list
sdc preset list --format json
sdc demo list
sdc demo run --fixture 001-builder-habit-dashboard
sdc demo run --fixture 001-builder-habit-dashboard --format markdown
sdc demo run --fixture 001-builder-habit-dashboard --format json
sdc enforce check --path benchmarks/golden/001-builder-habit-dashboard
sdc enforce check --workspace examples/enforcement-smoke
sdc init "domain app" --type full-stack-saas --out /private/tmp/sdc-init-smoke
sdc harness run --fixture 001-builder-habit-dashboard
python3 -m sdc_cli doctor
python3 -m sdc_cli doctor --quick
python3 -m sdc_cli integration list
python3 -m sdc_cli extension list
python3 -m sdc_cli preset list
python3 -m sdc_cli demo run --fixture 001-builder-habit-dashboard
python3 -m sdc_cli enforce check --path benchmarks/golden/001-builder-habit-dashboard
python3 tools/sdc.py list
python3 tools/sdc.py init "domain app" --type full-stack-saas --out /private/tmp/sdc-init-smoke
python3 tools/sdc.py show /sdc.blueprint
python3 tools/sdc.py inspect /sdc.blueprint
python3 tools/sdc.py integration list
python3 tools/sdc.py extension list
python3 tools/sdc.py preset list
python3 tools/sdc.py demo list
python3 tools/sdc.py demo run --fixture 001-builder-habit-dashboard
python3 tools/sdc.py enforce check --path benchmarks/golden/001-builder-habit-dashboard
python3 tools/sdc_enforce.py check --workspace examples/enforcement-smoke --format json
python3 tools/sdc.py scaffold --list
python3 tools/sdc.py branch --name "workshop RSVP"
python3 tools/sdc.py harness run --fixture 001-builder-habit-dashboard
python3 tools/sdc.py doctor
python3 tools/sdc.py doctor --quick
python3 tools/spec_lint.py
python3 tools/spec_scaffold.py --list
python3 tools/score_blueprint.py blueprints/02-full-project-blueprint.md
```

The `sdc` entrypoint is intended for editable use from a repository checkout. This release does not package the whole repository as a standalone remote tool and does not auto-install repository assets outside the checkout.

- `sdc.py`: espone una command surface leggera per `/sdc.*`, stampa/ispeziona i prompt, elenca integration, extension e preset registry, delega scaffold, demo, harness e verifica lo stato della repo. `doctor` esegue tutte le fixture; `doctor --quick` usa il percorso smoke rapido.
- `sdc_cli`: wrapper installabile che espone lo stesso comando come `sdc` tramite `pyproject.toml`.
- `sdc_demo.py`: legge fixture e golden artifact esistenti e stampa un walkthrough compatto raw prompt -> artifact chain. Non genera app, non chiama API esterne e non richiede LLM.
- `sdc_enforce.py`: controlla in modo strutturale che specification, Vertical Blueprint, plan, tasks, scorecard e implementation-like files restino allineati. Non prova correttezza semantica.
- `sdc_harness.py`: verifica fixture benchmark e golden artifacts in modo riproducibile e senza dipendenze esterne.
- `spec_lint.py`: valida struttura, naming metodologico, assenza di tracce di provenienza non autonome, project profiles, blueprints, scorecards, skills e cataloghi JSON per integrations/extensions/presets.
- `spec_scaffold.py`: genera una workspace minima per una specification.
- `score_blueprint.py`: esegue uno score strutturale euristico 0-100 su sezioni e keyword. È un gate leggero, non una prova semantica di qualità.

La CLI è un aiuto di navigazione e validazione. Non genera applicazioni, non sceglie l’architettura prodotto e non sostituisce il metodo Specification-Driven Coding.

`extension list` e `preset list` sono comandi di discovery. Leggono `extensions/catalog.json` e `presets/catalog.json`; non installano, non applicano e non recuperano codice remoto.
