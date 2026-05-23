# AI chatbot, customer support e assistente conversazionale

- Profile id: `ai-chatbot-support`
- Quando usarlo: Chatbot sito/app, supporto clienti, lead qualification, onboarding, FAQ dinamiche, escalation a umano.

## Obiettivo del profilo

Guidare l’agente a costruire un progetto specifico per questa categoria, evitando default generici e decisioni implicite.

## Domande di intake obbligatorie

- Quali intenti deve gestire e quali deve rifiutare?
- Quando passa a un umano?
- Quali strumenti può chiamare?
- Quale tono rappresenta il brand?

## Stack candidates

Non sono default automatici. L’agente deve scegliere e motivare.

- Botpress/Rasa/Dialogflow se serve flow control
- Provider LLM con tool calling
- Next.js/SvelteKit chat UI
- Zendesk/Intercom/Freshdesk integrations
- RAG opzionale con KB versionata

## Must-have spec fields

- Conversation policy
- Escalation rules
- Allowed tools
- PII handling
- Transcript retention
- Fallbacks
- Abuse prevention

## Anti-pattern da evitare

Non rendere il bot onnipotente. Definisci intenti, limiti, tono, escalation, logging e contenuti proibiti.

## Acceptance gates

- Intenti core testati con esempi
- Escalation verificata
- Tool calls hanno autorizzazioni
- Il bot dichiara incertezza quando serve

## Prompt seed

```text
Stai costruendo un progetto di tipo `ai-chatbot-support`.
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
