---
type: overview
project: ZenaQuiet-Mask
updated: 2026-11-03
---

# ZenaQuiet-Mask

## What this project is

A wearable face mask for everyday use, for example on the commute and at the office. It does two
jobs: it **filters the air** you breathe against city pollution (KN95-class, one small fan), and it
**keeps your conversations private** from people nearby without muffling your voice. In Jira, the
voice processing runs on the paired smartphone, not in the mask
([MK-6](https://epazz.atlassian.net/browse/MK-6), [MK-10](https://epazz.atlassian.net/browse/MK-10)).
Jira key: `MK`.

## Where it stands

As of 2026-11-03: stage **POC** (an early test to show the idea can work,
[[reference#Stage schedule (per product)]]). Next gate POC → EVT on 2027-02-08, 97 days away.
Gate readiness 9.5% (2 of 21 POC Stories Done). Health **AMBER**: 34 medium risks and progress 21.2
points behind the expected pace (20.5 a day earlier). Latest report: [[ZenaQuiet-Mask/jira/2026-11-03-jira]].

Top issues:

1. **Engineering not started (third week):** no Mechanical, Electronics or Acoustic Story has an
   owner or has started, and the mask technical spec is not written
   ([MK-7](https://epazz.atlassian.net/browse/MK-7), [MK-8](https://epazz.atlassian.net/browse/MK-8),
   [MK-22](https://epazz.atlassian.net/browse/MK-22), [MK-11](https://epazz.atlassian.net/browse/MK-11)).
2. **Board and chip outside Jira:** a mask POC circuit board is ordered and paid but has no ticket,
   and no processor decision is recorded in MK. Jira still says "no AI chip on the mask" (MK-22,
   [MK-13](https://epazz.atlassian.net/browse/MK-13)).
3. **Industrial Design ahead of its inputs:** 6 of 8 design Subtasks are Done, including the chin
   area that should be checked against face sizes still To Do
   ([MK-38](https://epazz.atlassian.net/browse/MK-38), [MK-36](https://epazz.atlassian.net/browse/MK-36),
   [MK-34](https://epazz.atlassian.net/browse/MK-34)) (inferred rework risk).

All dates are still placeholders: Stories 2026-09-21 → 2027-02-08, Epics → 2027-11-15 (inferred).

## Active epics

| Epic | In plain words | Status | Due |
| --- | --- | --- | --- |
| [MK-1](https://epazz.atlassian.net/browse/MK-1) | Industrial Design: style per age group, shell, washable fabric, two sizes, battery safety (2/4 Stories, 6/8 Subtasks done) | To Do | 2027-11-15 |
| [MK-6](https://epazz.atlassian.net/browse/MK-6) | Air Filtration: KN95-class filter, easy breathing, ~30-day filter, one fan | To Do | 2027-11-15 |
| [MK-10](https://epazz.atlassian.net/browse/MK-10) | Sound Dampening & Voice Privacy: voice 3–6 dB quieter to people nearby | To Do | 2027-11-15 |
| [MK-14](https://epazz.atlassian.net/browse/MK-14) | Mechanical Comfort & Wearability: 60–80 g, comfortable 4–6+ hours | To Do | 2027-11-15 |
| [MK-19](https://epazz.atlassian.net/browse/MK-19) | Exhale System: breathing-out vent must not leak sound | To Do | 2027-11-15 |
| [MK-21](https://epazz.atlassian.net/browse/MK-21) | Electronics & Power: Bluetooth relay board, battery, power budget | To Do | 2027-11-15 |
| [MK-24](https://epazz.atlassian.net/browse/MK-24) | Product Line Rollout: office version first; lifestyle, sport, eSport deferred | To Do | 2027-11-15 |
| [MK-29](https://epazz.atlassian.net/browse/MK-29) | Certification & Compliance: battery safety tests; claim only what was tested | To Do | 2027-11-15 |
| [MK-32](https://epazz.atlassian.net/browse/MK-32) | Field Test + Release Candidate (no description, no Stories) | To Do | 2027-11-15 |

## Recent changes

- 2026-11-03 — no change in Jira and no new comments or source files since 2026-11-02 (CTO visit
  under way). MK-31 and MK-36 passed 14 days without an update. See
  [[ZenaQuiet-Mask/jira/2026-11-03-jira]].
- 2026-11-02 — MK-33 (style direction), MK-35 (washable fabric) and MK-38 (chin area) Done on
  2026-10-30; ID Subtasks moved to "MK Sprint 4". No engineering ticket changed, the agreed board
  ticket is still missing, and there were no new comments, meetings or chats. See
  [[ZenaQuiet-Mask/jira/2026-11-02-jira]].
- 2026-10-26 — MK-34, MK-39 and MK-40 Done; MK-37 started. See [[ZenaQuiet-Mask/jira/2026-10-26-jira]].
