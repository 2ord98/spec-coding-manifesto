# Vertical Blueprint: local-first habit dashboard

## Role contract

Act as a product-focused web builder implementing only the specified habit dashboard. Do not silently add auth, social, analytics, or cloud persistence.

## Product/domain intent

A private, calm, and non-competitive dashboard for recurring health routines.

## Project profile

`dashboard-admin-bi`

## Stack contract

Use a local-first frontend with browser storage or equivalent local persistence. The stack rationale is `local-first`: it satisfies the fixture without account, database, or backend overhead.

Rejected default: hosted database or account system. Reason: heavier backend defaults were rejected because no multi-device or team sync requirement exists.

## Architecture contract

- Habit model: name, cadence, completions, created timestamp, archived flag.
- Views: today, weekly progress, habit editor, empty/error fallback.
- Data boundary: local storage only for first version.

## UX contract

Avoid generic SaaS cards. Cards are allowed only when they represent a concrete habit workflow: completion, progress, edit, or recovery.

## Security/privacy contract

Habit data is sensitive. No email collection, no third-party tracking, no medical recommendation.

## Quality gates

- Privacy gate passes.
- Testability gate passes.
- Anti-genericity gate passes.
- Acceptance criteria can be verified without paid services.
