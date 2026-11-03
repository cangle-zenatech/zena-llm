---
type: overview
project: ZenaQuiet-Pro2
updated: 2026-11-02
---

# ZenaQuiet-Pro2

## What this project is

A desk device for call-centre agents that makes calls private **without a headset**. Microphones
pick up only the agent's voice for the customer, and a directional speaker plays the customer's
voice only to the agent's seat, so neighbours can't follow the call. Jira key `PRO2`
([[ZenaQuiet-Pro2/jira/2026-11-02-jira|status report 2026-11-02]]).

## Where it stands

As of 2026-11-02 ([[ZenaQuiet-Pro2/jira/2026-11-02-jira|report]]):

- **Stage:** EVT (engineering tests of early working units), 2026-09-21 → 2027-02-08; the gate to
  DVT is 98 days away ([[reference#Stage schedule (per product)]]).
- **Health: RED**, set by the script, because of one date. The new cost-tracking Story PRO2-553 is
  due 2028-02-08, a year past the gate; this is probably a typo for 2027-02-08 (inferred).
  Otherwise progress is on plan: 21 of 61 EVT Stories Done (34.4%; 30.0% expected). There are
  3 HIGH risks (PRO2-553, plus the POC leftovers PRO2-396 and PRO2-397) and 51 MEDIUM.
- **Top issues:**
  - Mechanical work is overdue and still on one engineer: five static analyses (PRO2-542 to
    PRO2-546) and the standoff spec PRO2-23 have passed their due dates without starting.
  - Hinges: no delivery is recorded, Revision B is redrawn for alternative hinges (PRO2-416), and
    the bench test PRO2-420 (due 2026-11-06) has not started.
  - Twelve electronics board tasks (PRO2-501 to PRO2-512) were reopened and re-dated to
    2026-11-27 with no reason given. Decisions are due during the CTO's visit this week: sound
    masking in the Pro or the Beacon (PRO2-150), a plastic housing (PRO2-425), and the Pro
    version (PRO2-437).

## Active epics

- [PRO2-1](https://epazz.atlassian.net/browse/PRO2-1) — Voice Lock, Layer 3: capture only the agent's voice for the customer. In Progress, 5/11 Stories done. Due 2027-11-15.
- [PRO2-2](https://epazz.atlassian.net/browse/PRO2-2) — Voice Lock, Layer 1: clean, private customer audio for the agent through the directional speaker. In Progress, 3/7. Due 2027-11-15.
- [PRO2-3](https://epazz.atlassian.net/browse/PRO2-3) — Connectivity & Ports: power, USB, network, Wi-Fi and Bluetooth. In Progress, 5/17; 51/63 Subtasks done after 12 were reopened. Due 2027-11-15.
- [PRO2-4](https://epazz.atlassian.net/browse/PRO2-4) — User Interface: touch controls and status lights. To Do at Epic level; touch-controls Story PRO2-298 Done (1/4). Due 2027-11-15.
- [PRO2-8](https://epazz.atlassian.net/browse/PRO2-8) — Mechanical Structure: the casing, hinges, cooling and drop tests. In Progress, 4/21; Revision B in design; new cost tracking (PRO2-553). Due 2027-11-15.
- [PRO2-172](https://epazz.atlassian.net/browse/PRO2-172) — Industrial Design: at step 5 of 6 (design refinement). In Progress, 5/6. Due 2027-11-15.
- [PRO2-449](https://epazz.atlassian.net/browse/PRO2-449) — Pro application: the software running on the device. In Progress, 16/22. Due 2027-11-15.
- [PRO2-450](https://epazz.atlassian.net/browse/PRO2-450) — Field Test + Release Candidate. To Do, 0/8. Due 2027-11-15.

## Recent changes

- 2026-11-02 — Weekly report: 348 issues (2 added). Touch controls done (PRO2-298, PRO2-327,
  PRO2-329): 0.5 mm copper behind a 2 mm panel registers touch. PRO2-536 (secure updates) Done.
  12 electronics tasks reopened (PRO2-501 to PRO2-512). New cost-tracking Story PRO2-553 with a
  likely wrong due date, which turns health RED. Research item RS-3 linked to PRO2-463.
- 2026-10-26 — Weekly report: K-slot tasks removed (PRO2-300 waits on hinges); Revision B with
  an alternative hinge (PRO2-416); plastic housing proposed (PRO2-425).
- Earlier reports: [[ZenaQuiet-Pro2/jira/2026-10-26-jira|2026-10-26]],
  [[ZenaQuiet-Pro2/jira/2026-10-23-jira|2026-10-23]].
