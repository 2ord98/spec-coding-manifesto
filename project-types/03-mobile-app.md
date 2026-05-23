# App mobile nativa o cross-platform

- Profile id: `mobile-app`
- Quando usarlo: App iOS/Android consumer, utility, community, app AI, app local-first o app con sensori/dispositivi.

## Obiettivo del profilo

Guidare l’agente a costruire un progetto specifico per questa categoria, evitando default generici e decisioni implicite.

## Domande di intake obbligatorie

- Quali schermate sono necessarie nel primo MVP?
- Quali dati devono funzionare offline?
- Quali permessi servono e come vengono spiegati?
- Serve pubblicazione store o solo prototipo?

## Stack candidates

Non sono default automatici. L’agente deve scegliere e motivare.

- Expo/React Native per iterazione rapida e app AI
- Flutter per UI cross-platform consistente
- Kotlin + Jetpack Compose per Android nativo
- SwiftUI per iOS nativo
- Backend: Supabase/Firebase/FastAPI/.NET API secondo vincoli

## Must-have spec fields

- User journey per schermate
- Offline/cache strategy
- Permessi runtime e privacy
- Push notifications se richieste
- Crash/error reporting
- Accessibilità mobile

## Anti-pattern da evitare

Non trattare mobile come sito web piccolo. Specifica navigazione, stati offline, permessi, notifiche, lifecycle e store readiness.

## Acceptance gates

- La navigazione è definita screen-by-screen
- Ogni permesso ha motivazione utente
- Empty/loading/error states sono specificati
- Il progetto include strategia di build e test device/emulatore

## Prompt seed

```text
Stai costruendo un progetto di tipo `mobile-app`.
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
