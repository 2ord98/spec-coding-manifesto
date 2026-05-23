# Specification-Driven Coding Constitution

## Article I — Specificity First

Ogni progetto deve essere definito in modo specifico prima dell’implementazione. Prompt generici, feature list vaghe o richieste “fammi un’app” devono essere trasformate in spec verificabile.

## Article II — Project Profile Binding

Ogni spec deve dichiarare un project profile da `project-types/`. Se il progetto è composito, usare massimo due profili primari e motivare la composizione.

## Article III — Anti-Genericity

L’agente deve identificare pattern generici da evitare e decisioni distintive da applicare. Output visivi, architetturali e testuali non devono essere template medi senza relazione col dominio.

## Article IV — Evidence Before Assumption

Quando una decisione dipende da versione, libreria, policy esterna, repo esistente o vincolo attuale, l’agente deve cercare evidenza o dichiarare l’incertezza.

## Article V — Contracts Over Guessing

Spec, blueprint, API, dati, permessi, acceptance criteria e quality gates devono funzionare come contratti. Il codice è valido solo se soddisfa questi contratti.

## Article VI — Blueprint Before Build

Prima di generare codice, prodotto o modifica sostanziale, l’agente deve produrre un blueprint verticale adatto allo strumento di esecuzione.

## Article VII — Human Control

Azioni sensibili, distruttive, economiche, legali, mediche, di sicurezza o fisiche richiedono human approval.

## Article VIII — Minimal Change

In brownfield o targeted change, modificare solo ciò che serve. Niente refactor, librerie o astrazioni non richieste.

## Article IX — Living Spec

Quando implementazione e spec divergono, aggiornare la spec o correggere il codice. La divergenza non va ignorata.

## Article X — Score Every Delivery

Ogni consegna significativa deve includere una scorecard con evidenze, blockers, rischi residui e prossima azione minima.

## Governance

Ogni plan deve includere una sezione `Constitution Check` con esito pass/fail per gli articoli rilevanti.
