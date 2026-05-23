# Education, tutor AI e learning platform

- Profile id: `education-tutor-lms`
- Quando usarlo: Tutor AI, quiz, LMS, micro-learning, valutazione, corsi interattivi, studio assistito.

## Obiettivo del profilo

Guidare l’agente a costruire un progetto specifico per questa categoria, evitando default generici e decisioni implicite.

## Domande di intake obbligatorie

- Quale competenza deve migliorare lo studente?
- Come viene valutata la risposta?
- Il tutor può generare esercizi nuovi?
- Quali contenuti sono fuori programma?

## Stack candidates

Non sono default automatici. L’agente deve scegliere e motivare.

- Next/SvelteKit/Vue + CMS/MDX
- LMS data model custom o integrazione Moodle/Canvas
- RAG su materiale didattico
- Adaptive learning rules
- Analytics privacy-preserving

## Must-have spec fields

- Learning objectives
- Rubrics
- Student model
- Content boundaries
- Feedback policy
- Progress tracking
- Accessibility

## Anti-pattern da evitare

Non dare feedback educativo generico. Specifica obiettivi, rubriche, livello studente, safety e modalità di correzione.

## Acceptance gates

- Ogni attività mappa un obiettivo
- Feedback spiega senza sostituire lo studente
- Progress tracking definito
- Contenuti sensibili gestiti con policy

## Prompt seed

```text
Stai costruendo un progetto di tipo `education-tutor-lms`.
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
