---
type: overview
project: ZenaQuiet-Beacon
updated: 2026-11-02
---

# ZenaQuiet-Beacon

## What this project is

The Beacon is a ceiling-mounted coordinator for a floor cluster of ZenaQuiet Pro units, powered over the network cable (PoE). It registers and monitors the Pros, enforces voiceprint consent, relays cloud commands and coordinates zone settings. It also carries a room microphone, a 360° LED ring and a sound-masking speaker. It senses room noise and tells the Pros how to adjust their audio; the Pro does the audio processing. The Jira key is `BC`, and stage dates follow [[reference#Stage schedule (per product)]].

## Where it stands

As of 2026-11-02, the Beacon is in [[glossary#EVT|EVT]] (the first engineering-prototype stage). The gate to DVT is on 2027-02-08, 98 days away. Gate readiness is 48.6% (18/37 EVT Stories done), ahead of the 30.0% expected but unchanged for two weeks. Health is **RED** only because ID Subtask [BC-141](https://epazz.atlassian.net/browse/BC-141) carries DVT dates (to 2027-09-06) under an EVT Story, most likely a filing issue (inferred). Without it, health would be AMBER. Top issues:

1. BC-141 is still filed under EVT Story BC-153 (the only HIGH risk).
2. Sound masking: the EE board steps BC-230 to BC-232 were due 2026-10-30 and are not started. Epic BC-234 has no Stories. No CTO-visit decision on masking (Pro or Beacon, built-in or separate speaker) is in Jira yet.
3. EE circuit-board layouts BC-220, BC-223 and BC-226 are 3 days late, and two of them have no owner. Mechanical work rests on one engineer (50 open items, ME peaks at 34 Subtasks in November).

Also open: keep or drop the Beacon after EVT, and the EVT spec sign-off. Latest report: [[ZenaQuiet-Beacon/jira/2026-11-02-jira|2026-11-02 report]].

## Active epics

- [BC-23](https://epazz.atlassian.net/browse/BC-23) — Industrial design (look, LED ring, speaker) · In Progress · due 2027-11-15
- [BC-38](https://epazz.atlassian.net/browse/BC-38) — Electronics boards and ports · In Progress · due 2027-11-15
- [BC-50](https://epazz.atlassian.net/browse/BC-50) — Enclosure and mechanics (thermal, ports, antenna, speaker housing) · In Progress · due 2027-11-15
- [BC-164](https://epazz.atlassian.net/browse/BC-164) — Beacon firmware · In Progress · due 2027-11-15
- [BC-165](https://epazz.atlassian.net/browse/BC-165) — Field test and release candidate (DVT) · To Do · due 2027-11-15
- [BC-234](https://epazz.atlassian.net/browse/BC-234) — Sound masking (Acoustic), no Stories, linked to Research RS-16 · To Do · due 2027-11-15
- [BC-107](https://epazz.atlassian.net/browse/BC-107) — Pro–Beacon device management · Done

## Recent changes

- 2026-11-02: A quiet week. Reset-button access BC-258 is Done and panel CAD BC-262 has started. There were no new issues and no comments since 2026-10-22. Six EE Subtasks due 2026-10-30 are now overdue (BC-220, BC-223, BC-226, BC-230 to BC-232).
- 2026-10-26: New ME Story BC-250 (modular sound-masking speaker housing) and 15 more ME Subtasks (ports, antenna). Epic BC-107 Done; firmware update BC-210 and OTA encryption BC-249 Done. See [[ZenaQuiet-Beacon/jira/2026-10-26-jira|2026-10-26 report]].
- 2026-10-19: BC-141 re-dated into the DVT window under EVT Story BC-153 (health RED); 13 ME Subtasks added.
- 2026-10-15: New Epic BC-234 (sound masking), linked to Research RS-16.
