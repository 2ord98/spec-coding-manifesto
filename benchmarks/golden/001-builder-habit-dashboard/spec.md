# Specification: local-first habit dashboard

## Project profile

`dashboard-admin-bi`

## User

Solo user tracking 3-7 daily health routines in a private, calm, and non-competitive product.

## Problem

The user needs a simple way to create, complete, edit, and delete a habit and inspect weekly progress without accounts, social pressure, or medical claims.

## Functional requirements

- Create, complete, edit, and delete a habit.
- Show today view.
- Show weekly progress is visible for each habit.
- Provide empty, loading, and error states.
- Provide reset or undo behavior for accidental completions.

## Non-goals

- No social sharing.
- No public leaderboard.
- No paid analytics.
- No automatic health advice.

## Acceptance criteria

- `create, complete, edit, and delete a habit` works in the same local session.
- `weekly progress is visible` without implying medical advice.
- Privacy behavior is documented.
- Stack rationale explains why heavier backend defaults were rejected.
