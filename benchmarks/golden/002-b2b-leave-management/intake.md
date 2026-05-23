# Intake: B2B leave management

## Mode

`full-project`

## Project profile

Primary: `full-stack-saas`

## Blocking questions

None for this fixture. Leave balance rules, accrual policy, and regional compliance details are treated as reversible assumptions.

## Reversible assumptions

- The first version serves one company tenant at a time with employees, managers, and HR/Admin roles.
- Leave balances and accrual formulas are simplified enough for request/approval flows and can evolve later.
- The shared calendar shows approved absences, not confidential request notes or medical context.

## Non-goals

- Payroll processing.
- Benefits administration.
- Generic HR suite expansion.
- Public exposure of sensitive employee leave details.

## Anti-genericity constraints

- Must behave like a leave workflow product, not a generic SaaS dashboard clone.
- Must not add payroll, finance, or unrelated HR modules.
- Calendar visibility must be privacy-aware and role-specific.
