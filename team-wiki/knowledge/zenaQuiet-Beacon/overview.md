---
type: overview
project: ZenaQuiet-Beacon
updated: 2026-10-26
---

# ZenaQuiet-Beacon

## What this project is

A ceiling-mounted, PoE-powered (power over the network cable) coordinator for a floor cluster of ZenaQuiet Pro units. It registers and monitors the Pros, enforces voiceprint consent, relays cloud commands and coordinates zone settings. It also carries a room microphone, a 360° LED ring and a sound masking speaker, and senses room noise to tell the Pros how to adjust their audio (the Pro does the audio processing). Jira key `BC`; stage dates follow [[reference#Stage schedule (per product)]].

## Where it stands

As of 2026-10-26: in [[glossary#EVT|EVT]] (first engineering-prototype stage), gate to DVT on 2027-02-08, 105 days away. Gate readiness 48.6% (18/37 EVT Stories done), ahead of the 25.0% expected. Health **RED**, only because ID Subtask [BC-141](https://epazz.atlassian.net/browse/BC-141) carries DVT dates (to 2027-09-06) under an EVT Story; most likely a filing issue (inferred). Top issues:

1. BC-141 filed under EVT Story BC-153 (the only HIGH risk).
2. Sound masking for the CTO visit (29–30 Oct or 2 Nov): EE board steps BC-230 to BC-232 due 2026-10-30 and not started; Epic BC-234 has no Stories; the ME speaker housing BC-250 is under way.
3. Mechanical work: Nguyen Trung Tin holds 51 open items, ME load peaks at 34 Subtasks in Nov-26.

Open decisions for the visit: Pro or Beacon sound masking, and Beacon speaker vs a separate ceiling speaker; keep or drop the Beacon after EVT. Latest report: [[ZenaQuiet-Beacon/jira/2026-10-26-jira|2026-10-26 report]].

## Active epics

- [BC-23](https://epazz.atlassian.net/browse/BC-23) — Industrial design (look, LED ring, speaker) · In Progress · due 2027-11-15
- [BC-38](https://epazz.atlassian.net/browse/BC-38) — Electronics boards and ports · In Progress · due 2027-11-15
- [BC-50](https://epazz.atlassian.net/browse/BC-50) — Enclosure and mechanics (thermal, ports, antenna, speaker housing) · In Progress · due 2027-11-15
- [BC-164](https://epazz.atlassian.net/browse/BC-164) — Beacon firmware · In Progress · due 2027-11-15
- [BC-165](https://epazz.atlassian.net/browse/BC-165) — Field test and release candidate (DVT) · To Do · due 2027-11-15
- [BC-234](https://epazz.atlassian.net/browse/BC-234) — Sound masking (Acoustic), no Stories, linked to Research RS-16 · To Do · due 2027-11-15
- [BC-107](https://epazz.atlassian.net/browse/BC-107) — Pro–Beacon device management · Done this week

## Recent changes

- 2026-10-26: New ME Story BC-250 (modular sound-masking speaker housing) with BC-251 to BC-255; 15 more ME Subtasks for ports (BC-256 to BC-263) and antenna clearance (BC-265 to BC-271). Done: Epic BC-107, BC-210 (firmware update via web, USB DFU, ZenaTool), BC-249 (OTA image encryption), BC-229, BC-179, BC-235. BC-234 renamed "Sound Masking"; BC-233 moved to Huỳnh Thái Hòa and linked to RS-16.
- 2026-10-19: BC-141 re-dated into the DVT window under EVT Story BC-153 (health RED); 13 ME Subtasks added (BC-236 to BC-248); BC-153 started. See [[ZenaQuiet-Beacon/jira/2026-10-19-jira|2026-10-19 report]].
- 2026-10-15: New Epic BC-234 (sound masking), linked to Research RS-16.
- 2026-10-13/14: Epic BC-106 and four Pro–Beacon EVT Stories left Jira; BC-107 renamed; firmware release Stories started.
