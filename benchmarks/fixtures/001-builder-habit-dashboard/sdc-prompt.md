# Specification-Driven Coding prompt fixture: habit dashboard

Create a lightweight habit tracking web product for solo users who want to track daily health routines without social feeds, gamified streak pressure, or paid services.

## Mode

`full-project` for an app-builder or coding-agent run.

## Project profile

Primary: `dashboard-admin-bi`

Secondary: `full-stack-saas` only if persistence, auth, or account management becomes required.

## Domain and user

The primary user is an adult tracking 3-7 recurring personal routines such as sleep hygiene, mobility, hydration, meditation, or medication reminders. The product must feel private, calm, and non-competitive.

## Non-goals

- No social sharing.
- No public leaderboard.
- No paid analytics.
- No dark-pattern streak loss copy.
- No automatic health advice.

## Stack constraints

Prefer a static or local-first implementation unless the target builder requires a hosted stack. Do not choose accounts, databases, Supabase, Firebase, or serverless functions unless persistence requirements make them necessary.

## UX contract

Include today view, weekly progress, habit creation/editing, empty state, error state, reset/undo behavior, and accessible keyboard navigation. Avoid generic SaaS cards unless each card maps to a specific habit workflow.

## Security and privacy

Treat habit data as sensitive. Do not collect email unless accounts are required. Do not add third-party tracking. Store only the minimum data needed.

## Acceptance criteria

- User can create, complete, edit, and delete a habit.
- Weekly progress is visible without implying medical advice.
- Empty, loading, and error states are explicit.
- Stack rationale explains why heavier backend defaults were rejected.
- Output includes a scorecard covering anti-genericity, domain fit, privacy, testability, and residual risks.
