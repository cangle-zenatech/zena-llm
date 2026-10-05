# Ledger v2 — Product Requirements

Author: Priya Raman · Status: approved · Last updated 2026-09-10

## Problem

Ledger v1 recalculates invoice totals on read. At 40k active subscriptions this takes
800ms p95 and is the top source of support tickets ("my invoice changed").

## Goals

- Immutable invoice records, computed once at close
- p95 invoice read under 200ms
- Full audit trail for every line item

## Non-goals

- Multi-currency (deferred to 2027)
- Self-serve plan changes

## Plan

Three phases. Phase 1 dual-writes to v1 and v2. Phase 2 reads from v2 behind a flag.
Phase 3 removes v1. Target for Phase 3 complete: **Dec 15, 2026**.

## Risks

Dunning logic is coupled to v1 internals. Marcus estimates 3 weeks to untangle;
this is the critical path.

## Open questions

- Do we backfill historical invoices, or only forward from cutover?
- Who owns the dunning rewrite — Billing or Platform?
