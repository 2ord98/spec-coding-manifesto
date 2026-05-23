# Feature Spec: Mobile app service-oriented, CDS-like placeholder

> Nota: questo è un esempio generico perché i dettagli reali del progetto CDS non sono inclusi nella repo.

## Specification-Driven Coding header

- Project profile: `mobile-app`
- Utente primario: utente finale che gestisce attività e contenuti da smartphone
- Problema specifico: fornire un flusso mobile rapido, offline-tolerant e con notifiche contestuali
- Non-obiettivi: niente porting web 1:1, niente permessi runtime non giustificati
- Vincoli: ogni schermata deve avere scopo e stato vuoto/errore/caricamento

## Functional requirements

- FR-001: onboarding breve con consenso privacy.
- FR-002: home con azioni principali visibili.
- FR-003: sincronizzazione dati con cache locale.
- FR-004: notifiche solo per eventi esplicitamente utili.

## Acceptance criteria

- AC-001: navigazione screen-by-screen documentata.
- AC-002: offline mode verificato.
- AC-003: permessi spiegati prima della richiesta OS.
