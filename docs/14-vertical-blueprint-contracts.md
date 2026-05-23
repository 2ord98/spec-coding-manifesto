# Vertical Blueprint Contracts

Un Vertical Blueprint Contract è il ponte tra specification e generazione concreta.

La specification definisce cosa deve essere vero. Il blueprint verticale definisce come l’AI deve produrre file, codice, UX, integrazioni, test e valutazione.

Pipeline ufficiale:

```text
Raw request -> Intake -> Specification -> Project Profile Selection -> Vertical Blueprint -> Plan -> Tasks -> Implementation -> Evaluation Scorecard -> Release/Iteration
```

Il blueprint viene prima del plan finale e dei tasks perché è l’artefatto che fissa stack, file tree, confini, role contract, safety constraints, output format e quality gates. Senza questo contratto, il piano può ancora incorporare default generici.

## Perché serve

I modelli moderni sanno già scrivere blueprint lunghi e dettagliati. Il problema è che spesso quei blueprint sono ancora prompt lunghi, non contratti verificabili. Specification-Driven Coding migliora il pattern imponendo:

- output contract fisico;
- file tree;
- stack rationale;
- sicurezza specifica per stack;
- performance budget realistico;
- fallback;
- deployment assumptions;
- integration assumptions;
- implementation boundaries;
- anti-genericità;
- test;
- scorecard.

## Anatomia di un blueprint superiore

```markdown
# Vertical Blueprint Contract

## 1. Role contract
## 2. Product intent
## 3. Domain context
## 4. Primary users
## 5. Non-goals
## 6. Project profile
## 7. Stack contract
## 8. Architecture contract
## 9. Data/content contract
## 10. UX/design/motion contract
## 11. Security/privacy contract
## 12. Performance/accessibility contract
## 13. Output/file contract
## 14. Implementation rules
## 15. Test contract
## 16. Acceptance gates
## 17. Scorecard
```

## Miglioramento rispetto ai blueprint lunghi generici

Un blueprint generico dice:

```text
Costruisci un sito premium moderno con animazioni e codice completo.
```

Un blueprint Specification-Driven Coding dice:

```text
Costruisci questo tipo di prodotto, per questo utente, con questi vincoli, questi file obbligatori, queste assunzioni, questi fallback, questi gate, questi test e questo metodo di valutazione.
```

## Regola sui target ambiziosi

Quando l’utente chiede target assoluti come “60 FPS garantiti”, “SEO perfetta” o “sicurezza enterprise”, l’agente deve trasformarli in obiettivi verificabili:

```text
Target: 60 FPS percepiti su desktop moderno.
Fallback mobile: reduced motion, canvas disattivabile, asset lazy-loaded.
Misura: Lighthouse/performance profile/manual smoke test.
```

Non promettere ciò che non può essere verificato. Convertire sempre promesse assolute in budget, fallback e test.

## Regola sul codice completo

“Codice completo” non significa commentare ogni riga o riempire file di placeholder. Significa:

- file tree coerente;
- file chiave implementati;
- placeholder dichiarati solo dove inevitabili;
- sicurezza base inclusa;
- istruzioni di run/deploy;
- test minimi;
- confini espliciti.

## Regola anti-clone

Quando il dominio è ispirato a un brand, locale, prodotto o competitor reale, il blueprint deve usare l’ispirazione come riferimento di categoria, non come clonazione di identità, testi proprietari o asset.
