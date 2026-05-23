# Example — Premium Hospitality WordPress Theme

## Specification-Driven Prompt

Costruisci un tema WordPress custom per un locale premium cocktail bar + cucina. Il sito deve essere elegante, veloce, senza page builder pesanti e gestibile dal cliente tramite dashboard WordPress.

## Project profile

Primary: `project-types/01-marketing-site-cms.md`  
Secondary: `project-types/06-ecommerce-marketplace.md` solo se viene aggiunta vendita voucher o gift card.

## Utente primario

Cliente finale che vuole scoprire menu, esperienze, location e prenotare.

## Non-obiettivi

- Non copiare brand, testi o asset di locali reali.
- Non usare plugin pesanti per logica core.
- Non inserire API key nel frontend.

## Vertical blueprint

Usare `blueprints/04-wordpress-custom-theme-blueprint.md`.

## Output contract

Generare `/themes/<theme-slug>/` con file theme completi, CPT, tassonomie, AJAX sicuro, maintenance mode 503, fallback motion e istruzioni installazione.

## Scorecard

Usare `scorecards/implementation-scorecard.md`.
