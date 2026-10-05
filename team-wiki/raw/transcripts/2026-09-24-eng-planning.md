# Eng Planning — Sept 24, 2026
Present: Priya Raman (PM), Marcus Oyelaran (Platform), Dana Whitfield (Billing),
Sam Ko (Eng Director)

**Sam:** Where are we on Ledger v2 phase 1?

**Marcus:** Dual-write is done in staging. Production next week. The dunning coupling is
worse than I scoped — closer to five weeks, not three. I found two other services reading
v1 tables directly.

**Sam:** Does that move Phase 3?

**Marcus:** Yes. Realistically end of January, not December.

**Priya:** The Dec 15 date is in the PRD and I've told two customers. I'd rather cut
backfill than move the date.

**Dana:** Cutting backfill means support can't pull invoices older than cutover. That's
the exact ticket we're trying to eliminate.

**Priya:** Then we move the date. I'll handle the customer conversations.

**Sam:** Decision: Phase 3 moves to Jan 31. Backfill stays in scope. Priya updates the PRD
and tells the two customers this week.

**Sam:** Dunning ownership?

**Dana:** Billing should own it. We know the retry logic.

**Marcus:** Billing doesn't have capacity until November.

**Sam:** Park it. Revisit next week.

**Dana:** One more — Northwind asked about multi-currency again on Tuesday.

**Priya:** Still a 2027 thing. Not reopening it.
