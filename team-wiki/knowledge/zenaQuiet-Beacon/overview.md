---
type: overview
project: ZenaQuiet-Beacon
updated: 2026-11-09
---

# ZenaQuiet-Beacon

## What this project is

The Beacon is a ceiling-mounted coordinator for a floor cluster of ZenaQuiet Pro units. It is powered over the network cable (PoE). It registers and monitors the Pros, enforces voiceprint consent, passes on cloud commands and coordinates zone settings. It also has a room microphone, a 360° LED ring and a sound-masking speaker. It senses room noise and tells the Pros how to adjust their audio, while the Pro does the audio processing itself. The Jira key is `BC`, and stage dates follow [[reference#Stage schedule (per product)]].

## Where it stands

As of 2026-11-09, the Beacon is in [[glossary#EVT|EVT]] (the first engineering-prototype stage). The gate to DVT is on 2027-02-08, 91 days away. Gate readiness is 51.4% (19/37 EVT Stories done), ahead of the 35.0% expected. Health is **RED** because of 4 HIGH risks. Three EE board layouts are 10 days late, and ID Subtask [BC-141](https://epazz.atlassian.net/browse/BC-141) is still filed under an EVT Story with DVT dates. Top issues:

1. EE circuit-board layouts [BC-220](https://epazz.atlassian.net/browse/BC-220), [BC-223](https://epazz.atlassian.net/browse/BC-223) and [BC-226](https://epazz.atlassian.net/browse/BC-226) are 10 days past due. BC-223 has no owner. ME's port and board-fit work waits on them (inferred).
2. BC-141 is unchanged since 2026-10-19. This is the fifth report it has been flagged.
3. Sound masking: EE chose the board parts and finished the schematic, and the ME speaker housing [BC-250](https://epazz.atlassian.net/browse/BC-250) is Done. But the board layout BC-232 is 3 days late, and Epic [BC-234](https://epazz.atlassian.net/browse/BC-234) still has no Stories. No decision from the CTO-visit week (Pro or Beacon, built-in or separate speaker) is recorded in Jira.

Also open: keep or drop the Beacon after EVT, and the EVT spec sign-off. Mechanical work still rests on one engineer (45 open items). Latest report: [[ZenaQuiet-Beacon/jira/2026-11-09-jira|2026-11-09 report]].

## Active epics

- [BC-23](https://epazz.atlassian.net/browse/BC-23) — Industrial design (look, LED ring, speaker) · In Progress · due 2027-11-15
- [BC-38](https://epazz.atlassian.net/browse/BC-38) — Electronics boards and ports · In Progress · due 2027-11-15
- [BC-50](https://epazz.atlassian.net/browse/BC-50) — Enclosure and mechanics (thermal, ports, antenna, materials) · In Progress · due 2027-11-15
- [BC-164](https://epazz.atlassian.net/browse/BC-164) — Beacon firmware · In Progress · due 2027-11-15
- [BC-165](https://epazz.atlassian.net/browse/BC-165) — Field test and release candidate (DVT) · To Do · due 2027-11-15
- [BC-234](https://epazz.atlassian.net/browse/BC-234) — Sound masking (Acoustic), no Stories, linked to Research RS-16 · To Do · due 2027-11-15
- [BC-107](https://epazz.atlassian.net/browse/BC-107) — Pro–Beacon device management · Done

## Recent changes

- 2026-11-09: Masking board parts and schematic Done (BC-230, BC-231), and layout BC-232 re-dated to 2026-11-06 (now late). Speaker housing BC-250 Done with BC-254 and BC-255. Material checks BC-236 and BC-237 Done, with the bottom housing proposed as ABS plastic (to confirm with ID). BC-220 assigned. Three EE layouts became HIGH (10 days late).
- 2026-11-03: No Jira change and no new comments. ME Subtasks BC-182 and BC-244 passed their start dates without starting.
- 2026-11-02: Reset-button access BC-258 Done. Six EE Subtasks due 2026-10-30 became overdue.
- 2026-10-19: BC-141 re-dated into the DVT window under EVT Story BC-153 (health RED since).
