# Realtime collaboration, chat, whiteboard o editor condiviso

- Profile id: `realtime-collaboration`
- Quando usarlo: App collaborative con presence, chat, editing simultaneo, board, whiteboard, multiplayer productivity.

## Obiettivo del profilo

Guidare l’agente a costruire un progetto specifico per questa categoria, evitando default generici e decisioni implicite.

## Domande di intake obbligatorie

- Cosa accade se due utenti modificano lo stesso oggetto?
- Serve offline/reconnect?
- Chi può invitare o modificare?
- Qual è il budget di latenza percepita?

## Stack candidates

Non sono default automatici. L’agente deve scegliere e motivare.

- WebSockets/Socket.IO o SignalR
- CRDT: Yjs/Automerge se editing concorrente
- Supabase Realtime/Firebase per MVP
- Redis/NATS per pub-sub
- React/Vue/Svelte/Blazor secondo stack

## Must-have spec fields

- Presence model
- Conflict resolution
- Latency budget
- Offline/reconnect behavior
- Permission per workspace
- Event persistence

## Anti-pattern da evitare

Non usare semplice polling per collaborazione complessa. Definisci conflitti, presence, permission e sincronizzazione.

## Acceptance gates

- Conflitti risolti o prevenuti
- Reconnect non perde dati
- Presence coerente
- Eventi critici persistiti

## Prompt seed

```text
Stai costruendo un progetto di tipo `realtime-collaboration`.
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
