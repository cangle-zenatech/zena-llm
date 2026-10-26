---
type: overview
project: ZenaQuiet-Pro2
updated: 2026-10-26
---

# ZenaQuiet-Pro2

## What this project is

A desk device for call-centre agents that makes calls private **without a headset**. Microphones
pick up only the agent's voice for the customer, and a directional speaker plays the customer's
voice only to the agent's seat, so neighbours can't follow the call. Jira key `PRO2`
([[ZenaQuiet-Pro2/jira/2026-10-26-jira|status report 2026-10-26]]).

## Where it stands

As of 2026-10-26 ([[ZenaQuiet-Pro2/jira/2026-10-26-jira|report]]):

- **Stage:** EVT (engineering tests of early working units), 2026-09-21 → 2027-02-08; the gate to
  DVT is 105 days away ([[reference#Stage schedule (per product)]]).
- **Health: AMBER.** 20 of 60 EVT Stories Done (33.3%, ahead of the 25.0% expected). 2 HIGH risks,
  both acoustic tasks left under closed POC Stories (PRO2-396, PRO2-397); 40 MEDIUM.
- **Top issues:**
  - The hinge is still not settled: one preferred part has not shipped, and the housing is being
    redesigned for an alternative hinge in Revision B (PRO2-416). The bench test PRO2-420 and the
    anti-theft lock PRO2-300 wait on it.
  - Mechanical work piles up on one engineer: six tasks due this week have not started
    (PRO2-542 to PRO2-546, PRO2-23); November load is about ten times the monthly average.
  - Decisions expected during the CTO's visit (from 2026-11-02): sound masking in the Pro or the
    Beacon (PRO2-150), the move from aluminium to a plastic housing (PRO2-425), and the executive
    demo. Research's AI-chip proposal ([RS-2](https://epazz.atlassian.net/browse/RS-2)) is still
    linked from PRO2-461 and PRO2-486.

## Active epics

- [PRO2-1](https://epazz.atlassian.net/browse/PRO2-1) — Voice Lock, Layer 3: capture only the agent's voice for the customer. In Progress, 5/11 Stories done. No audio or voiceprint ever leaves the device (PRO2-474, PRO2-528). Due 2027-11-15.
- [PRO2-2](https://epazz.atlassian.net/browse/PRO2-2) — Voice Lock, Layer 1: clean, private customer audio for the agent through the directional speaker. In Progress, 3/7. Due 2027-11-15.
- [PRO2-3](https://epazz.atlassian.net/browse/PRO2-3) — Connectivity & Ports: power, USB, network, Wi-Fi and Bluetooth. In Progress, 5/17; all 63 electronics Subtasks Done. Due 2027-11-15.
- [PRO2-4](https://epazz.atlassian.net/browse/PRO2-4) — User Interface: touch controls and status lights. To Do at Epic level; touch and ring-light Stories in progress, touch-plate test late (PRO2-327). Due 2027-11-15.
- [PRO2-8](https://epazz.atlassian.net/browse/PRO2-8) — Mechanical Structure: the casing, hinges, cooling and drop tests. In Progress, 4/20; Revision B in design. Due 2027-11-15.
- [PRO2-172](https://epazz.atlassian.net/browse/PRO2-172) — Industrial Design: at step 5 of 6 (design refinement). In Progress, 5/6. Due 2027-11-15.
- [PRO2-449](https://epazz.atlassian.net/browse/PRO2-449) — Pro application: the software running on the device. In Progress, 16/22. Due 2027-11-15.
- [PRO2-450](https://epazz.atlassian.net/browse/PRO2-450) — Field Test + Release Candidate. To Do, 0/8. Due 2027-11-15.

## Recent changes

- 2026-10-26 — Weekly report: 346 issues (1 added, 3 removed). The K-slot tasks PRO2-315 to
  PRO2-317 were removed because the lock waits on the hinges (PRO2-300 comment). PRO2-529 (TSE
  power measurement) and PRO2-334 (LED diffuser light) are Done; PRO2-318 started. Comments
  record Revision B with an alternative hinge (PRO2-416) and a plastic housing instead of
  aluminium (PRO2-425). PRO2-327 is newly late, waiting for test plates.
- 2026-10-23 — Weekly report, first with Jira comments read: 348 issues; last electronics
  Subtasks closed; two Pro2 Stories linked to Research's chip evaluation RS-2.
- 2026-10-19 — Weekly report (redone): first with risks from meetings and the purchase chat.
- Earlier reports: [[ZenaQuiet-Pro2/jira/2026-10-15-jira|2026-10-15]],
  [[ZenaQuiet-Pro2/jira/2026-10-13-jira|2026-10-13]].
