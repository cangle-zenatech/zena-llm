---
type: overview
project: ZenaQuiet-Beacon
updated: 2026-11-16
---

# ZenaQuiet-Beacon

## What this project is

The Beacon is a ceiling-mounted coordinator for a floor cluster of up to 16 ZenaQuiet Pro units. It is powered over the network cable (PoE). It registers and monitors the Pros, enforces voiceprint consent, passes on cloud commands and coordinates zone settings. It also has a room microphone and a 360° LED ring, and it now carries the sound-masking function: it senses room noise and tells the Pros how to adjust their audio. The Jira key is `BC`, and stage dates follow [[reference#Stage schedule (per product)]].

## Where it stands

As of 2026-11-16, the Beacon is in [[glossary#EVT|EVT]] (the first engineering-prototype stage). The gate to DVT is on 2027-02-08, 84 days away, inside the assumed Tết holiday. Gate readiness is 62.2% (23/37 EVT Stories done), ahead of the 40.0% expected. Health is **AMBER**: there are no HIGH risks and nothing is overdue, but no Beacon board or speaker is recorded as ordered. Top issues:

1. All board layouts are finished: main-board layouts [BC-220](https://epazz.atlassian.net/browse/BC-220), [BC-223](https://epazz.atlassian.net/browse/BC-223) and [BC-226](https://epazz.atlassian.net/browse/BC-226) closed on 2026-11-16 (3 days after their due date, no comment), the masking board BC-232 on 2026-11-09. No board order is recorded; boards take 2–3 weeks to make, so hardware tests start in December at the earliest (inferred).
2. Four ME enclosure Stories (BC-155, BC-158, [BC-159](https://epazz.atlassian.net/browse/BC-159), [BC-160](https://epazz.atlassian.net/browse/BC-160)) were pushed onto the gate day itself, with no margin; BC-160 started on 2026-11-16.
3. The ceiling speaker for the masking trial is not recorded as ordered, and the speaker placement is still undecided: ID is drawing a speaker-in-the-middle model ([BC-141](https://epazz.atlassian.net/browse/BC-141), due 2026-11-17) beside the main one, while a separate housing (BC-250) is done. Epic [BC-234](https://epazz.atlassian.net/browse/BC-234) has no written decision.

Also open: the ME list (43 open tickets with one engineer), the EVT spec sign-off, the Pro/Beacon/Headset bundle-consistency request, and whether the Beacon software also serves the headset (this week's tech-lead meeting; no Jira trace yet). Latest report: [[ZenaQuiet-Beacon/jira/2026-11-16-jira|2026-11-16 report]].

## Active epics

- [BC-23](https://epazz.atlassian.net/browse/BC-23) — Industrial design (look, LED ring, speaker model BC-141) · In Progress · due 2027-11-15
- [BC-38](https://epazz.atlassian.net/browse/BC-38) — Electronics boards and ports (all layouts done, boards not yet ordered) · In Progress · due 2027-11-15
- [BC-50](https://epazz.atlassian.net/browse/BC-50) — Enclosure and mechanics (thermal, ports, antenna, materials) · In Progress · due 2027-11-15
- [BC-164](https://epazz.atlassian.net/browse/BC-164) — Beacon firmware, 19/20 Stories done · In Progress · due 2027-11-15
- [BC-165](https://epazz.atlassian.net/browse/BC-165) — Field test and release candidate (DVT) · To Do · 2027-05-24 → 2027-09-06 (re-dated 2026-11-16)
- [BC-234](https://epazz.atlassian.net/browse/BC-234) — Sound masking (Acoustic), no Stories, linked to Research RS-16 · In Review · due 2027-11-15
- [BC-107](https://epazz.atlassian.net/browse/BC-107) — Pro–Beacon device management · Done

## Recent changes

- 2026-11-16 (second redo): layouts BC-220, BC-223, BC-226 Done; BC-160 In Progress; overdue 3 → 0. Earlier the same day: Sprint 10 closed and Sprint 11 (2026-11-16 → 2026-11-30) opened; BC-165 re-dated to 2027-05-24 → 2027-09-06; stand-up (`transcripts/2026-11-16-standup.md`): speaker in the middle as a second model, port panel waits for the new board, bundle look must be consistent.
- 2026-11-13: BC-141 renamed "BEA v0b add speaker", In Progress, due 2026-11-17 (speaker facing up, on Acoustic advice).
- 2026-11-12: Health RED → AMBER. Masking-board layout BC-232 and power board BC-187 Done. The TM said no Beacon redesign: only sound masking and software continue (`transcripts/2026-11-09-standup.md`).
