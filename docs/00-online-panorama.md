# Mappa fonti online

Questa repo è un manifesto originale di **Specification-Driven Coding**. Usa la letteratura e gli strumenti specification-first come contesto di mercato, ma definisce un protocollo autonomo più specifico, progettuale e anti-output-generico.

## Fonti primarie e riferimenti di contesto

Questa mappa non sostituisce una verifica live dei link al momento della release. Le fonti esterne sono riferimenti di contesto e possono cambiare nel tempo.

- GitHub Blog, “Spec-driven development with AI”: https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit/
- Martin Fowler / Birgitta Böckeler, “Understanding Spec-Driven-Development”: https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html
- Andrej Karpathy, tweet originario “vibe coding”: https://x.com/karpathy/status/1886192184808149383
- Simon Willison, “Not all AI-assisted programming is vibe coding”: https://simonwillison.net/2025/Mar/19/vibe-coding/
- arXiv, “Spec-Driven Development: From Code to Contract in the Age of AI Coding Assistants”: https://arxiv.org/html/2602.00180v1
- Hugging Face paper page per lo stesso lavoro: https://huggingface.co/papers/2602.00180
- arXiv, “Constitutional Spec-Driven Development”: https://arxiv.org/html/2602.02584v1
- AGENTS.md standard: https://agents.md/
- Agent Skills overview: https://agentskills.io/home
- Emergent AI app builder: https://www.emergent.sh/
- Manus app/mobile builder references: https://manus.im/ and https://manus.im/tools/mobile-app-builder

## Riferimenti aggiunti per builder e blueprint moderni

- Google AI Studio / Gemini model pages: https://aistudio.google.com/models/gemini-3
- Gemini 3 developer guide: https://ai.google.dev/gemini-api/docs/gemini-3
- Google Cloud Gemini Enterprise model catalog: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/google-models
- Google AI Studio Build Mode: https://ai.google.dev/gemini-api/docs/aistudio-build-mode

## Lezione metodologica dai builder moderni

I modelli e i builder più recenti sono già capaci di generare blueprint lunghi e strutturati. Specification-Driven Coding non compete sulla lunghezza del prompt: compete sulla qualità del contratto.

Un blueprint superiore deve rendere espliciti ruolo, dominio, utenti, non-obiettivi, stack decision space, file tree, sicurezza specifica, performance budget, fallback, test e scorecard. Il valore della repo è far applicare questa struttura anche quando la richiesta iniziale è incompleta.

## Lettura sintetica della ricerca

1. **I toolkit specification-first sono maturi**: dimostrano che constitution, specification, plan, tasks, implement, estensioni, preset e integrazioni con agenti sono un modello pratico.
2. **“Specification-Driven Coding” non ha ancora una definizione pubblica unificata**: viene usato in modo vario in discussioni, post e strumenti, spesso come sinonimo pratico di AI coding guidato da specifiche.
3. **La differenza forte rispetto al vibe coding** non è “meno AI”, ma più controllo: il codice resta prodotto dall’AI, però l’intento viene prima trasformato in contratti, vincoli, scelta architetturale, test, qualità e audit.
4. **Il gap da colmare** è la genericità: molti app builder e agenti producono layout, stack e architetture simili quando il brief iniziale è povero. Specification-Driven Coding introduce profili progetto, domande obbligatorie, anti-template rules e quality gates.
5. **Il trend agente+spec è confermato**: lavori recenti su context-grounding, constitution/security e workflow multi-agent rafforzano l’idea che l’AI debba essere guidata da evidenza, contratti e permessi.
