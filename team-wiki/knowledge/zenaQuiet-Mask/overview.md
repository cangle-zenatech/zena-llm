---
type: overview
project: ZenaQuiet-Mask
updated: 2026-11-16
---

# ZenaQuiet-Mask

## What this project is

A wearable face mask for everyday use, for example on the commute and at the office. It does two
jobs. It **filters the air** you breathe against city pollution (KN95-class, small fans). It also
**keeps your conversations private** from people nearby without muffling your voice
([MK-6](https://epazz.atlassian.net/browse/MK-6), [MK-10](https://epazz.atlassian.net/browse/MK-10)).
In Jira the voice processing runs on the paired smartphone; on 2026-11-16 the TM said the POC mask
will run the AI model on the mask itself (not yet in Jira). Jira key: `MK`.

## Where it stands

As of 2026-11-16, the mask is in stage **POC**, an early test to show the idea can work
([[reference#Stage schedule (per product)]]). The next gate, POC → EVT, is on 2027-02-08, 84 days
away. Gate readiness is 9.5% (2 of 21 POC Stories Done). Health is **RED**: progress is 30.5 points
behind the expected pace. All 19 MK Sprint 4 tickets were moved into MK Sprint 5
(2026-11-16 → 2026-11-30) today, 12 of them unfinished. Two Subtasks pushed in October (MK-36,
MK-37) now end on the gate day itself, which falls in the assumed Tết break, so no margin is left.
Latest report: [[ZenaQuiet-Mask/jira/2026-11-16-jira]].

Top issues:

1. **Engineering waits on ID and a spec.** 15 engineering Stories have no owner and no spec date
   ([MK-22](https://epazz.atlassian.net/browse/MK-22), [MK-23](https://epazz.atlassian.net/browse/MK-23),
   [MK-13](https://epazz.atlassian.net/browse/MK-13)).
2. **Where the AI runs changed out loud, not in Jira.** The TM wants the AI model on a new Qualcomm
   chip in the POC mask, with two fans only; the chip order (shared with the Pro) is expected around
   2026-12-03 ([MK-13](https://epazz.atlassian.net/browse/MK-13),
   [MK-22](https://epazz.atlassian.net/browse/MK-22)).
3. **Materials are unsettled.** The voice-dampening approach is reopened and Acoustic is still
   listing breath-safe options; no fabric vendor yet, and the TM's UV/sweat/waterproof requirements
   are not in Jira ([MK-11](https://epazz.atlassian.net/browse/MK-11),
   [MK-42](https://epazz.atlassian.net/browse/MK-42)).

All Story and Epic dates are still placeholders, and the mock-up Subtasks have no dates (inferred).

## Active epics

| Epic | In plain words | Status | Due |
| --- | --- | --- | --- |
| [MK-1](https://epazz.atlassian.net/browse/MK-1) | Industrial Design: style per age group, shell, washable fabric, two sizes, first mock-up (2/4 Stories, 7/15 Subtasks done) | To Do | 2027-11-15 |
| [MK-6](https://epazz.atlassian.net/browse/MK-6) | Air Filtration: KN95-class filter, easy breathing, ~30-day filter, fan (MK-8 started, no progress since 2026-11-10) | To Do | 2027-11-15 |
| [MK-10](https://epazz.atlassian.net/browse/MK-10) | Sound Dampening & Voice Privacy: voice 3–6 dB quieter to people nearby (MK-11 in progress) | To Do | 2027-11-15 |
| [MK-14](https://epazz.atlassian.net/browse/MK-14) | Mechanical Comfort & Wearability: 60–80 g, comfortable 4–6+ hours | To Do | 2027-11-15 |
| [MK-19](https://epazz.atlassian.net/browse/MK-19) | Exhale System: breathing-out vent must not leak sound | To Do | 2027-11-15 |
| [MK-21](https://epazz.atlassian.net/browse/MK-21) | Electronics & Power: main board, battery, power budget | To Do | 2027-11-15 |
| [MK-24](https://epazz.atlassian.net/browse/MK-24) | Product Line Rollout: office version first; lifestyle, sport, eSport deferred | To Do | 2027-11-15 |
| [MK-29](https://epazz.atlassian.net/browse/MK-29) | Certification & Compliance: battery safety tests; claim only what was tested | To Do | 2027-11-15 |
| [MK-32](https://epazz.atlassian.net/browse/MK-32) | Field Test + Release Candidate (no description, no Stories) | To Do | 2027-11-15 |
| [MK-48](https://epazz.atlassian.net/browse/MK-48) | Layer 3 — Inbound TSE (no description; may belong to the headset) | To Do | 2027-11-15 |

## Recent changes

- 2026-11-16 (redone twice; the second redo found no new Jira change): MK Sprint 4 tickets moved to
  MK Sprint 5; pushed-deadlines table shows MK-36 and MK-37 on the gate day and MK-1 on the final
  deadline. At the stand-up the TM set the POC direction: AI model on the mask, Qualcomm
  chip, two fans; fabric must be UV-protective and washable; Acoustic to list breath-safe dampening
  materials (`transcripts/2026-11-16-standup.md`). No status, date or owner changes in Jira since
  2026-11-13. See [[ZenaQuiet-Mask/jira/2026-11-16-jira]].
- 2026-11-13: TM comment on MK-11 reopens the dampening material choice; photos of fabric, fans and
  filters on MK-42 to MK-44. See [[ZenaQuiet-Mask/jira/2026-11-13-jira]].
- 2026-11-12: first mock-up split into MK-41 to MK-47 (MK-41 Done); 7-layer dampening proposal on
  MK-11; new Epic MK-48. See [[ZenaQuiet-Mask/jira/2026-11-12-jira]].
