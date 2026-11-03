---
type: overview
project: ZenaQuiet-Beacon
updated: 2026-11-03
---

# ZenaQuiet-Beacon

## What this project is

The Beacon is a ceiling-mounted coordinator for a floor cluster of ZenaQuiet Pro units, powered over the network cable (PoE). It registers and monitors the Pros, enforces voiceprint consent, relays cloud commands and coordinates zone settings. It also carries a room microphone, a 360° LED ring and a sound-masking speaker. It senses room noise and tells the Pros how to adjust their audio; the Pro does the audio processing. The Jira key is `BC`, and stage dates follow [[reference#Stage schedule (per product)]].

## Where it stands

As of 2026-11-03, the Beacon is in [[glossary#EVT|EVT]] (the first engineering-prototype stage). The gate to DVT is on 2027-02-08, 97 days away. Gate readiness is 48.6% (18/37 EVT Stories done), ahead of the 30.7% expected but unchanged for over two weeks. Health is **RED** only because ID Subtask [BC-141](https://epazz.atlassian.net/browse/BC-141) carries DVT dates (to 2027-09-06) under an EVT Story, most likely a filing issue (inferred). Without it, health would be AMBER. Top issues:

1. BC-141 is still filed under EVT Story BC-153 (the only HIGH risk), unchanged since 2026-10-19.
2. Sound masking: the EE board steps BC-230 to BC-232 are 4 days late and not started. Epic BC-234 has no Stories. The CTO visit started on 2026-11-02, but no decision on masking (Pro or Beacon, built-in or separate speaker) is in Jira yet; the speaker housing BC-250 is due 2026-11-06.
3. EE circuit-board layouts BC-220, BC-223 and BC-226 are 4 days late, and two have no owner. Mechanical work rests on one engineer (50 open items, ME peaks at 34 Subtasks in November).

Also open: keep or drop the Beacon after EVT, and the EVT spec sign-off. Latest report: [[ZenaQuiet-Beacon/jira/2026-11-03-jira|2026-11-03 report]].

## Active epics

- [BC-23](https://epazz.atlassian.net/browse/BC-23) — Industrial design (look, LED ring, speaker) · In Progress · due 2027-11-15
- [BC-38](https://epazz.atlassian.net/browse/BC-38) — Electronics boards and ports · In Progress · due 2027-11-15
- [BC-50](https://epazz.atlassian.net/browse/BC-50) — Enclosure and mechanics (thermal, ports, antenna, speaker housing) · In Progress · due 2027-11-15
- [BC-164](https://epazz.atlassian.net/browse/BC-164) — Beacon firmware · In Progress · due 2027-11-15
- [BC-165](https://epazz.atlassian.net/browse/BC-165) — Field test and release candidate (DVT) · To Do · due 2027-11-15
- [BC-234](https://epazz.atlassian.net/browse/BC-234) — Sound masking (Acoustic), no Stories, linked to Research RS-16 · To Do · due 2027-11-15
- [BC-107](https://epazz.atlassian.net/browse/BC-107) — Pro–Beacon device management · Done

## Recent changes

- 2026-11-03: No Jira change since yesterday and no new comments; nothing from the CTO visit is recorded yet. ME Subtasks BC-182 and BC-244 passed their start dates without starting.
- 2026-11-02: Reset-button access BC-258 Done, panel CAD BC-262 started. Six EE Subtasks due 2026-10-30 became overdue (BC-220, BC-223, BC-226, BC-230 to BC-232). See [[ZenaQuiet-Beacon/jira/2026-11-02-jira|2026-11-02 report]].
- 2026-10-26: New ME Story BC-250 (modular sound-masking speaker housing) and 15 more ME Subtasks. Epic BC-107 Done; BC-210 and BC-249 Done.
- 2026-10-19: BC-141 re-dated into the DVT window under EVT Story BC-153 (health RED).
