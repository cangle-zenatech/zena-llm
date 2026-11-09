---
type: overview
project: ZenaQuiet-Pro2
updated: 2026-11-09
---

# ZenaQuiet-Pro2

## What this project is

ZenaQuiet-Pro2 is a desk device that keeps call-centre calls private **without a headset**. Microphones
pick up only the agent's voice for the customer. A directional speaker plays the customer's
voice only to the agent's seat, so neighbours can't follow the call. Jira key `PRO2`
([[ZenaQuiet-Pro2/jira/2026-11-09-jira|status report 2026-11-09]]).

## Where it stands

As of 2026-11-09 ([[ZenaQuiet-Pro2/jira/2026-11-09-jira|report]]):

- **Stage:** EVT (engineering tests of early working units), 2026-09-21 → 2027-02-08. The gate to
  DVT is 91 days away ([[reference#Stage schedule (per product)]]).
- **Health: RED**, set by the script, because of one date. The cost-tracking Story PRO2-553 is
  still due 2028-02-08, a year past the gate. This is probably a typo for 2027-02-08 (inferred),
  and it did not change this week. Otherwise progress is slightly ahead of plan: 22 of 61 EVT
  Stories are Done (36.1% against 35.0% expected). There are 4 HIGH risks (PRO2-553, the overdue
  static analyses PRO2-542 and PRO2-543, and the POC leftover PRO2-397) and 55 MEDIUM.
- **Top issues:**
  - Mechanical work is still on one engineer, who has 43 open tickets. PRO2-542 and PRO2-543 are
    10 days late and unstarted. The baffle tasks (PRO2-150, PRO2-153 to PRO2-160) are a week past
    their start dates.
  - Hinges: no delivery is recorded. The bench test PRO2-420 passed its 2026-11-06 due date
    unstarted.
  - The CTO visit week (from 2026-11-02) left no decision in Jira: sound masking in the Pro or the
    Beacon (PRO2-150), the plastic housing (PRO2-425) and the Pro version (PRO2-437). A new
    "PRO V5b for EVT-2" task (PRO2-556) hints the portable V5 line is going ahead (inferred).
    Twelve reopened electronics tasks (PRO2-501 to PRO2-512) still have no reason given.

## Active epics

- [PRO2-1](https://epazz.atlassian.net/browse/PRO2-1) — Voice Lock, Layer 3: capture only the agent's voice for the customer. In Progress, 5/11 Stories done. Due 2027-11-15.
- [PRO2-2](https://epazz.atlassian.net/browse/PRO2-2) — Voice Lock, Layer 1: clean, private customer audio for the agent through the directional speaker. In Progress, 3/7. Due 2027-11-15.
- [PRO2-3](https://epazz.atlassian.net/browse/PRO2-3) — Connectivity & Ports: power, USB, network, Wi-Fi and Bluetooth. In Progress, 5/17; 51/63 Subtasks done. Due 2027-11-15.
- [PRO2-4](https://epazz.atlassian.net/browse/PRO2-4) — User Interface: touch controls and status lights. To Do at Epic level; 1/4 Stories done. Due 2027-11-15.
- [PRO2-8](https://epazz.atlassian.net/browse/PRO2-8) — Mechanical Structure: the casing, hinges, cooling and drop tests. In Progress, 5/21; cooling layout decided. Due 2027-11-15.
- [PRO2-172](https://epazz.atlassian.net/browse/PRO2-172) — Industrial Design: at step 5 of 6 (design refinement), preparing EVT-2. In Progress, 5/6. Due 2027-11-15.
- [PRO2-449](https://epazz.atlassian.net/browse/PRO2-449) — Pro application: the software running on the device. In Progress, 16/22. Due 2027-11-15.
- [PRO2-450](https://epazz.atlassian.net/browse/PRO2-450) — Field Test + Release Candidate. To Do, 0/8. Due 2027-11-15.
- [PRO2-555](https://epazz.atlassian.net/browse/PRO2-555) — Product Reliability & Risk Management: a scored list of ways the design could fail (DFMEA) and their fixes. In Progress, no owner, no Stories yet. Due 2027-09-30.

## Recent changes

- 2026-11-09 — Five items Done: standoff spec PRO2-23 (silicone O-ring), cooling PRO2-344 and
  vent check PRO2-367, mic placement PRO2-396, and the power study PRO2-530. Cooling test: two fans
  keep the chip area at 65°C, and three fans measure 45 dB(A) (PRO2-344, Duy Nguyen, 2026-11-03).
  New task PRO2-556 (V5b for EVT-2). Three static analyses were re-dated (PRO2-544 to PRO2-546).
  PRO2-397 now starts after its due date and waits for a "new chip". No CTO-visit decision is
  recorded.
- 2026-11-03 — New Epic PRO2-555 for risk analysis (DFMEA). PRO2-553 kept its likely wrong 2028
  due date.
- Earlier reports: [[ZenaQuiet-Pro2/jira/2026-11-03-jira|2026-11-03]],
  [[ZenaQuiet-Pro2/jira/2026-11-02-jira|2026-11-02]].
