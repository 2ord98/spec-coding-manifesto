# Specification-Driven Coding vs Vibe Coding vs Basic Specification Toolkits

## Vibe coding

Ottimo quando:

- vuoi esplorare;
- vuoi vedere qualcosa subito;
- il progetto è throwaway;
- il rischio è basso;
- il codice non deve essere mantenuto.

Debole quando:

- servono permessi;
- ci sono dati reali;
- serve sicurezza;
- il progetto cresce;
- più agenti o persone devono collaborare;
- il design deve essere distintivo.

## Basic specification toolkits

Ottimo quando:

- vuoi workflow ordinato;
- vuoi spec, plan, tasks e implement;
- vuoi usare slash commands o agent skills;
- lavori in repo con struttura chiara.

Limite possibile:

- la spec può essere ancora troppo feature-scoped;
- il project type può non guidare abbastanza lo stack;
- la lotta alla genericità non è sempre esplicita;
- in brownfield serve più context-grounding.

## Specification-Driven Coding

Aggiunge sopra il workflow specification-first:

- costruzione del prompt utente;
- project profile routing;
- anti-sameness design;
- agent roles;
- skill e plugin guide;
- compatibility con app builder;
- gates specifici per categorie;
- regola di retro-spec.

## Quando usare cosa

| Scenario | Modalità consigliata |
|---|---|
| Weekend prototype | Vibe coding con audit leggero |
| MVP pubblico | Specification-Driven Coding minimo |
| SaaS con utenti/dati | Specification-Driven Coding completo |
| Sistema multi-agente | Specification-Driven Coding + agent governance |
| Brownfield enterprise | Specification-Driven Coding + context-grounding |
| Tool interno piccolo | Specification-Driven Coding light + AGENTS.md |
