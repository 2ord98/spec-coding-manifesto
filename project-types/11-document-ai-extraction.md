# Document AI, OCR, estrazione e classificazione

- Profile id: `document-ai-extraction`
- Quando usarlo: Parsing PDF, fatture, contratti, moduli, documenti tecnici, estrazione campi, classificazione, verifica.

## Obiettivo del profilo

Guidare l’agente a costruire un progetto specifico per questa categoria, evitando default generici e decisioni implicite.

## Domande di intake obbligatorie

- Quali tipi di documenti entrano?
- Quali campi sono obbligatori?
- Quale errore costa di più: falso positivo o falso negativo?
- Chi approva i casi ambigui?

## Stack candidates

Non sono default automatici. L’agente deve scegliere e motivare.

- Python + FastAPI + Pydantic schemas
- OCR: Tesseract/PaddleOCR/servizi cloud se necessario
- LLM structured outputs/function calling
- Vector search per retrieval su documenti
- Human review UI per casi incerti

## Must-have spec fields

- Document taxonomy
- Schema campi
- Validation rules
- Confidence thresholds
- Human review queue
- Provenance per ogni campo
- PII/security policy

## Anti-pattern da evitare

Non fidarti di estrazioni senza confidence, schema, validazione e revisione umana per casi critici.

## Acceptance gates

- Ogni campo ha fonte e confidence
- Output aderisce a schema validato
- Casi sotto soglia vanno in review
- Test set con documenti realistici

## Prompt seed

```text
Stai costruendo un progetto di tipo `document-ai-extraction`.
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
