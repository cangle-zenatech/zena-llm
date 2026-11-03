---
type: overview
project: ZenaQuiet-Pro2
updated: 2026-11-03
---

# ZenaQuiet-Pro2

## What this project is

ZenaQuiet-Pro2 is a desk device that keeps call-centre calls private **without a headset**. Microphones
pick up only the agent's voice for the customer. A directional speaker plays the customer's
voice only to the agent's seat, so neighbours can't follow the call. Jira key `PRO2`
([[ZenaQuiet-Pro2/jira/2026-11-03-jira|status report 2026-11-03]]).

## Where it stands

As of 2026-11-03 ([[ZenaQuiet-Pro2/jira/2026-11-03-jira|report]]):

- **Stage:** EVT (engineering tests of early working units), 2026-09-21 → 2027-02-08. The gate to
  DVT is 97 days away ([[reference#Stage schedule (per product)]]).
- **Health: RED**, set by the script, because of one date. The cost-tracking Story PRO2-553 is
  still due 2028-02-08, a year past the gate. This is probably a typo for 2027-02-08 (inferred).
  Otherwise progress is ahead of plan: 21 of 61 EVT Stories are Done (34.4% against 30.7%
  expected). There are 3 HIGH risks (PRO2-553, plus the POC leftovers PRO2-396 and PRO2-397) and
  55 MEDIUM.
- **Top issues:**
  - Mechanical work is overdue and still on one engineer. The static analyses PRO2-542 to PRO2-546
    and the standoff spec PRO2-23 are 4–7 days late and not started. The baffle tasks (PRO2-150,
    PRO2-153 to PRO2-160) are now late to start.
  - Hinges: no delivery is recorded, Revision B is being redrawn for alternative hinges (PRO2-416),
    and the bench test PRO2-420 (due 2026-11-06) has not started.
  - The CTO visit started 2026-11-02, and none of its decisions is in Jira yet: sound masking in
    the Pro or the Beacon (PRO2-150), the plastic housing (PRO2-425), and the Pro version
    (PRO2-437). Twelve reopened electronics tasks (PRO2-501 to PRO2-512) still have no reason
    given.

## Active epics

- [PRO2-1](https://epazz.atlassian.net/browse/PRO2-1) — Voice Lock, Layer 3: capture only the agent's voice for the customer. In Progress, 5/11 Stories done. Due 2027-11-15.
- [PRO2-2](https://epazz.atlassian.net/browse/PRO2-2) — Voice Lock, Layer 1: clean, private customer audio for the agent through the directional speaker. In Progress, 3/7. Due 2027-11-15.
- [PRO2-3](https://epazz.atlassian.net/browse/PRO2-3) — Connectivity & Ports: power, USB, network, Wi-Fi and Bluetooth. In Progress, 5/17; 51/63 Subtasks done. Due 2027-11-15.
- [PRO2-4](https://epazz.atlassian.net/browse/PRO2-4) — User Interface: touch controls and status lights. To Do at Epic level; 1/4 Stories done. Due 2027-11-15.
- [PRO2-8](https://epazz.atlassian.net/browse/PRO2-8) — Mechanical Structure: the casing, hinges, cooling and drop tests. In Progress, 4/21; Revision B in design. Due 2027-11-15.
- [PRO2-172](https://epazz.atlassian.net/browse/PRO2-172) — Industrial Design: at step 5 of 6 (design refinement). In Progress, 5/6. Due 2027-11-15.
- [PRO2-449](https://epazz.atlassian.net/browse/PRO2-449) — Pro application: the software running on the device. In Progress, 16/22. Due 2027-11-15.
- [PRO2-450](https://epazz.atlassian.net/browse/PRO2-450) — Field Test + Release Candidate. To Do, 0/8. Due 2027-11-15.
- [PRO2-555](https://epazz.atlassian.net/browse/PRO2-555) — Product Reliability & Risk Management: a scored list of ways the design could fail (DFMEA) and their fixes. New, In Progress, no owner, no Stories yet. Due 2027-09-30.

## Recent changes

- 2026-11-03 — New Epic PRO2-555 for risk analysis. Its first comment rates noise and vibration
  reaching the mics as the top risks for both enclosure concepts, hinged and single-body
  (PRO2-555, Duy Nguyen, 2026-11-02). PRO2-529 was retitled. There were no status or date
  changes, and PRO2-553 still has the likely wrong 2028 due date.
- 2026-11-02 — Touch controls done (PRO2-298). 12 electronics tasks were reopened (PRO2-501 to
  PRO2-512). The new cost-tracking Story PRO2-553 turned health RED.
- Earlier reports: [[ZenaQuiet-Pro2/jira/2026-11-02-jira|2026-11-02]],
  [[ZenaQuiet-Pro2/jira/2026-10-26-jira|2026-10-26]].
