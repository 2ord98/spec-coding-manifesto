# Tools

Gli script non richiedono dipendenze esterne. Per l'uso consumer bastano Python 3.11+ e Git.

Modalità consumer senza installazione da un altro progetto:

```bash
cd my-project
git clone https://github.com/2ord98/spec-coding-manifesto.git .sdc
python3 .sdc/tools/sdc.py doctor --quick
python3 .sdc/tools/sdc.py init "my project" --type marketing-site-cms --out "$PWD/sdc-workspace"
python3 .sdc/tools/sdc.py compile --workspace "$PWD/sdc-workspace/specs/001-my-project"
```

Modalità contributor repository:

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
sdc compile --workspace /private/tmp/sdc-init-smoke/specs/001-domain-app --dry-run
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
python3 tools/sdc.py compile --workspace /private/tmp/sdc-init-smoke/specs/001-domain-app --format json --dry-run
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

`pip install -e .sdc` è opzionale per i consumer project e può creare metadati `.egg-info` locali. Preferisci `python3 .sdc/tools/sdc.py ...` per uso deterministico senza installazione. Se è disponibile un comando globale `sdc`, cerca verso l'alto la checkout `.sdc/tools/sdc.py` incorporata più vicina prima di usare il fallback da checkout contributor.

- `sdc.py`: espone una command surface leggera per `/sdc.*`, stampa/ispeziona i prompt, elenca integration, extension e preset registry, delega scaffold, demo, harness e verifica lo stato della repo. `doctor` esegue tutte le fixture; `doctor --quick` usa il percorso smoke rapido.
- `sdc_cli`: wrapper installabile che espone lo stesso comando come `sdc` tramite `pyproject.toml`.
- `sdc_demo.py`: legge fixture e golden artifact esistenti e stampa un walkthrough compatto raw prompt -> artifact chain. Non genera app, non chiama API esterne e non richiede LLM.
- `sdc_enforce.py`: controlla in modo strutturale che specification, Vertical Blueprint, plan, tasks, scorecard e implementation-like files restino allineati. Non prova correttezza semantica.
- `sdc_compile.py`: compila artifact SDC densi in modo deterministico da raw request e profile-depth. Non genera app, non chiama LLM/API e usa `[ASK]` / `[ASSUMPTION]` per incertezza esplicita.
- `sdc_harness.py`: verifica fixture benchmark e golden artifacts in modo riproducibile e senza dipendenze esterne.
- `sdc_signature.py`: contiene dataclass stdlib-only ispirate a DSPy per i contratti futuri di profile compile e role handoff. Non importa DSPy, non chiama modelli e non fa IO.
- `spec_lint.py`: valida struttura, naming metodologico, assenza di tracce di provenienza non autonome, project profiles, blueprints, scorecards, skills e cataloghi JSON per integrations/extensions/presets.
- `spec_scaffold.py`: genera una workspace minima per una specification.
- `score_blueprint.py`: esegue uno score strutturale euristico 0-100 su sezioni e keyword. È un gate leggero, non una prova semantica di qualità.

La CLI è un aiuto di navigazione e validazione. Non genera applicazioni, non sceglie l’architettura prodotto e non sostituisce il metodo Specification-Driven Coding.

I profile-depth package in `project-types/<profile-id>/` descrivono confini decisionali, non template applicativi. `sdc compile` usa questi package come input; `sdc handoff` è pianificato per una fase futura e non è implementato in questo ciclo.

`extension list` e `preset list` sono comandi di discovery. Leggono `extensions/catalog.json` e `presets/catalog.json`; non installano, non applicano e non recuperano codice remoto.
