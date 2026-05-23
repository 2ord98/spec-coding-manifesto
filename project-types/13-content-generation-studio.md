# Studio di generazione contenuti AI

- Profile id: `content-generation-studio`
- Quando usarlo: Generazione testi, immagini, video, campagne, post social, asset marketing, localizzazione, brand workflows.

## Obiettivo del profilo

Guidare l’agente a costruire un progetto specifico per questa categoria, evitando default generici e decisioni implicite.

## Domande di intake obbligatorie

- Quali formati di contenuto servono?
- Chi approva prima della pubblicazione?
- Quali parole/visual style sono vietati?
- Gli asset devono essere esportabili o pubblicati via API?

## Stack candidates

Non sono default automatici. L’agente deve scegliere e motivare.

- Next/SvelteKit/Vue UI con asset library
- Queue worker per job lunghi
- Object storage S3-compatible
- Provider LLM/image/video pluggable
- Brand rules + review workflow

## Must-have spec fields

- Brand voice
- Asset lifecycle
- Prompt presets
- Review/approval
- Copyright/source policy
- Moderation
- Version history

## Anti-pattern da evitare

Non generare contenuti senza brand system, diritti, approval flow, versioning e policy anti-output generico.

## Acceptance gates

- Ogni output ha prompt/versione/provider
- Brand constraints applicati
- Review prima di publish se richiesto
- Asset archiviati con metadata

## Prompt seed

```text
Stai costruendo un progetto di tipo `content-generation-studio`.
Prima di proporre stack o codice, completa intake, vincoli, non-obiettivi e anti-genericity constraints.
Poi scrivi spec, blueprint, plan e task usando i template Specification-Driven Coding.
Se una scelta tecnica è implicita, fermati e dichiarala come assunzione o domanda bloccante.
```

## Output minimo richiesto all’agente

- Spec con requisiti funzionali e non funzionali.
- Piano tecnico con stack motivato e alternativa scartata.
- Task atomici ordinati per dipendenza.
- Acceptance matrix.
- Audit anti-genericità.

## Blueprint consigliato

`blueprints/02-full-project-blueprint.md`; se usato con app builder, prima compilare `blueprints/01-ai-builder-master-blueprint.md`.

Il blueprint deve includere file/output contract, security/privacy frame, anti-genericity constraints e scorecard target.
