---
type: overview
project: ZenaQuiet-Mask
updated: 2026-11-09
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

As of 2026-11-09: stage **POC** (an early test to show the idea can work,
[[reference#Stage schedule (per product)]]). Next gate POC → EVT on 2027-02-08, 91 days away.
Gate readiness 9.5% (2 of 21 POC Stories Done). Health **RED**: progress is 25.5 points behind the
expected pace, past the 25-point RED line. Nothing new went wrong; no Story reached Done while the
calendar moved on. Latest report: [[ZenaQuiet-Mask/jira/2026-11-09-jira]].

Top issues:

1. **Engineering has no owners and no spec:** 17 engineering Stories have no assignee and the mask
   technical spec is undated. Passive voice dampening started on 2026-11-03 but has no owner
   ([MK-7](https://epazz.atlassian.net/browse/MK-7), [MK-8](https://epazz.atlassian.net/browse/MK-8),
   [MK-22](https://epazz.atlassian.net/browse/MK-22), [MK-11](https://epazz.atlassian.net/browse/MK-11)).
2. **Board and chip outside Jira:** a mask POC circuit board is ordered and paid but has no ticket,
   and no processor decision is recorded in MK. Jira still says "no AI chip on the mask" (MK-22,
   [MK-13](https://epazz.atlassian.net/browse/MK-13)).
3. **Industrial Design ahead of its inputs:** 3D-printed prototyping started while face sizes,
   board and battery are still open
   ([MK-5](https://epazz.atlassian.net/browse/MK-5), [MK-36](https://epazz.atlassian.net/browse/MK-36),
   [MK-38](https://epazz.atlassian.net/browse/MK-38)) (inferred rework risk).

All dates are still placeholders: Stories 2026-09-21 → 2027-02-08, Epics → 2027-11-15 (inferred).

## Active epics

| Epic | In plain words | Status | Due |
| --- | --- | --- | --- |
| [MK-1](https://epazz.atlassian.net/browse/MK-1) | Industrial Design: style per age group, shell, washable fabric, two sizes, battery safety, prototypes (2/4 Stories, 6/8 Subtasks done) | To Do | 2027-11-15 |
| [MK-6](https://epazz.atlassian.net/browse/MK-6) | Air Filtration: KN95-class filter, easy breathing, ~30-day filter, one fan | To Do | 2027-11-15 |
| [MK-10](https://epazz.atlassian.net/browse/MK-10) | Sound Dampening & Voice Privacy: voice 3–6 dB quieter to people nearby | To Do | 2027-11-15 |
| [MK-14](https://epazz.atlassian.net/browse/MK-14) | Mechanical Comfort & Wearability: 60–80 g, comfortable 4–6+ hours | To Do | 2027-11-15 |
| [MK-19](https://epazz.atlassian.net/browse/MK-19) | Exhale System: breathing-out vent must not leak sound | To Do | 2027-11-15 |
| [MK-21](https://epazz.atlassian.net/browse/MK-21) | Electronics & Power: Bluetooth relay board, battery, power budget | To Do | 2027-11-15 |
| [MK-24](https://epazz.atlassian.net/browse/MK-24) | Product Line Rollout: office version first; lifestyle, sport, eSport deferred | To Do | 2027-11-15 |
| [MK-29](https://epazz.atlassian.net/browse/MK-29) | Certification & Compliance: battery safety tests; claim only what was tested | To Do | 2027-11-15 |
| [MK-32](https://epazz.atlassian.net/browse/MK-32) | Field Test + Release Candidate (no description, no Stories) | To Do | 2027-11-15 |

## Recent changes

- 2026-11-09 — MK-5 (3D-printed prototypes) and MK-11 (passive voice dampening) moved to In
  Progress on 2026-11-03; MK-11 has no assignee. Health AMBER → RED from the calendar alone. One
  image-only comment (MK-11); nothing in Jira from the CTO visit. See
  [[ZenaQuiet-Mask/jira/2026-11-09-jira]].
- 2026-11-03 — no change in Jira since 2026-11-02 (CTO visit under way). See
  [[ZenaQuiet-Mask/jira/2026-11-03-jira]].
- 2026-11-02 — MK-33, MK-35 and MK-38 Done on 2026-10-30; the agreed board ticket still missing.
  See [[ZenaQuiet-Mask/jira/2026-11-02-jira]].
