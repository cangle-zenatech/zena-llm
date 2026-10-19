---
type: overview
project: ZenaQuiet-Pro2
updated: 2026-10-19
---

# ZenaQuiet-Pro2

## What this project is

A desk device for call-centre agents that makes calls private **without a headset**. Microphones
pick up only the agent's voice for the customer, and a directional speaker plays the customer's
voice only to the agent's seat, so neighbours can't follow the call
([[ZenaQuiet-Pro2/jira/2026-10-10-jira|status report 2026-10-10]]).

## Where it stands

- **Stage:** EVT (engineering tests of early working units), 2026-09-21 → 2027-02-08
  ([[reference#Stage schedule (per product)]]).
- **Health on 2026-10-19:** AMBER (Jira and source risks). 19 of 64 EVT Stories Done, 15 In
  Progress, 112 days to the EVT → DVT gate. 2 items overdue (PRO2-396, PRO2-452) after the team
  re-dated Jira on the afternoon of 2026-10-19. From meetings and the purchase chat: hinge samples
  (approved 2026-10-15, 5–7 weeks after payment) arrive 16–26 working days after the hinge bench
  test PRO2-420 is due to start; the team must pick one Pro version for EVT-1 (decision meeting
  2026-10-20); mechanical work sits on one engineer (59 open PRO2 items)
  ([[ZenaQuiet-Pro2/jira/2026-10-19-jira|report, redone 2026-10-19]]).
- **Health on 2026-10-15:** AMBER. 17 of 61 EVT Stories Done, 13 In Progress, 116 days to the
  EVT → DVT gate (2027-02-08). No Jira edits since 2026-10-13; first overdue item (PRO2-23, 1 day
  late) ([[ZenaQuiet-Pro2/jira/2026-10-15-jira|report]]).
- **Health on 2026-10-13:** AMBER. 17 of 61 EVT Stories Done, 13 In Progress, 118 days to the
  EVT → DVT gate (2027-02-08). The jump from 1 of 39 comes from tagging 22 firmware Stories as
  EVT-1 (16 already Done), not from new finished work
  ([[ZenaQuiet-Pro2/jira/2026-10-13-jira|report]]).
- **Dates reset on 2026-10-12:** every Story now spans its whole stage window, and every Epic runs
  to 2027-11-15 (MP end). Before, most Epics were due 2027-09-06. Flagged in the
  [[ZenaQuiet-Pro2/jira/2026-10-13-jira|2026-10-13 report]]; not yet confirmed as intended.

## Active epics

- [[2026-06-18-PRO2-2|PRO2-2]] — Voice Lock, Layer 1: clean, private call audio for the agent without a headset. In Progress.
  Jira title since 2026-10-19 (or shortly before): "Layer 1 — Voice Lock: Outbound TSE (sound bubble)" (was "Inbound").
- [PRO2-1](https://epazz.atlassian.net/browse/PRO2-1) — Voice Lock, Layer 3: capture only the agent's voice for the customer.
  Jira title now "Layer 3 — Voice Lock: Inbound TSE (agent voice capture)" (was "Outbound"); the
  descriptions of both Epics still use the old direction (flagged, not resolved). New EVT-1 firmware
  Stories: PRO2-526 (TSE model upgrade), PRO2-527 (i.MX95 power/thermal), PRO2-528 (secure voiceprint).
- [PRO2-3](https://epazz.atlassian.net/browse/PRO2-3) — Connectivity & Ports: power, USB, network, Wi-Fi and Bluetooth.
- [PRO2-4](https://epazz.atlassian.net/browse/PRO2-4) — User Interface: touch controls and status lights.
- [PRO2-8](https://epazz.atlassian.net/browse/PRO2-8) — Mechanical Structure: the casing, weight and drop tests.
- [PRO2-172](https://epazz.atlassian.net/browse/PRO2-172) — Industrial Design: at step 5 of 6 (design refinement).
- [PRO2-449](https://epazz.atlassian.net/browse/PRO2-449) — Pro application: the software running on the device.
- [PRO2-450](https://epazz.atlassian.net/browse/PRO2-450) — Field Test + Release Candidate. Was
  dated to start 2027-02-08; Jira now says 2026-06-29 → 2027-11-15 (changed 2026-10-12), while its
  Stories run Nov–Dec 2026. Contradiction flagged, not resolved.

## Recent changes

- 2026-10-19 (redo) — Report rewritten with a plain-sentence table of risks from meetings and the
  purchase chat. Jira changed since the morning: 350 issues (+6 ME static analyses PRO2-541 to
  PRO2-546), Story PRO2-422 reopened, PRO2-11 closed, masking/baffle Subtasks PRO2-153 to PRO2-160
  dated 2026-11-02 → 2026-11-13; overdue 4 → 2.
- 2026-10-19 — Weekly report: 15 issues added (3 firmware Stories, 12 Subtasks), 11 closed incl.
  Stories PRO2-422 and PRO2-427; PRO2-1/PRO2-2 titles swapped Inbound/Outbound. First report with
  source risks from meetings and the purchase chat (6 MEDIUM). Hong Kong / China sourcing answered
  verbally on 2026-10-15 ("for these products" China and Hong Kong are OK); `reference.md` not yet
  updated.
- 2026-10-15 — Weekly report: no Jira changes since 2026-10-13 (0 added, removed, status or date
  changes). PRO2-23 is now 1 day overdue; PRO2-396, PRO2-451 and PRO2-452 are due 2026-10-16.
- 2026-10-14 — Weekly report: no changes; only the text of Epic PRO2-1 was edited (2026-10-13).

- 2026-10-13 — Weekly report: no issues added or closed; 96 issues re-dated on 2026-10-12; EVT
  readiness 28% after the firmware Stories PRO2-467 to PRO2-488 were re-tagged EVT-1.
- 2026-10-12 — Added "What this project is", "Where it stands" and the other Epics, from the
  2026-10-10 status report.
- 2026-10-10 — 41 Stories and 23 Subtasks added since 2026-10-08 (323 issues now).
