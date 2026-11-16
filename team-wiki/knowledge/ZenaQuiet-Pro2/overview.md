---
type: overview
project: ZenaQuiet-Pro2
updated: 2026-11-16
---

# ZenaQuiet-Pro2

## What this project is

ZenaQuiet-Pro2 is a desk device that keeps call-centre calls private **without a headset**. Microphones
pick up only the agent's voice for the customer. A directional ultrasonic speaker plays the customer's
voice only to the agent's seat, so neighbours can't follow the call. Sound masking, which plays
background noise to cover nearby voices, moved to the Beacon on 2026-11-09. Jira key `PRO2`
([[ZenaQuiet-Pro2/jira/2026-11-16-jira|status report 2026-11-16]]).

## Where it stands

As of 2026-11-16 ([[ZenaQuiet-Pro2/jira/2026-11-16-jira|report]], second redo on fresh Jira data):

- **Stage:** EVT (engineering tests of early working units), 2026-09-21 → 2027-02-08. The gate to
  DVT is 84 days away ([[reference#Stage schedule (per product)]]).
- **Health: RED**, set by the script, because of two HIGH risks:
  - the cost Story PRO2-553 is still due 2028-02-08 (probably a typo, inferred);
  - the POC Story PRO2-249 was reopened on 2026-11-16 with no owner.
- **Progress:** 25 of 61 EVT Stories are Done (41.0% vs 40.0% expected), after the AI-accelerator
  Story PRO2-461 closed late on 2026-11-16. Sprint 10 closed 4 EVT Stories against about 5.1 needed
  per sprint, so the team is behind the pace for the gate.
- **Top issues:**
  - **New chip and board.** The new main chip's purchase order was only sent on 2026-11-16, with
    about two weeks' delivery. PRO2-461 is Done in Jira with no comment, but the chip isn't in hand.
    The board redesign (PRO2-501 to PRO2-512) is due 2026-11-27; new boards would arrive around late
    December, leaving about 25 working days before Tết for board tests, PRO2-26 and PRO2-397 (inferred).
  - **Overdue work.** 12 tickets are still overdue from 2026-11-13. Seven are commented "Push out
    to December" but not re-dated (PRO2-453, PRO2-153, PRO2-26).
  - **Gate-day tickets.** 26 open tickets have been pushed onto the EVT gate day itself, with no
    margin left (PRO2-422, PRO2-424, PRO2-433 and others; report section 2b).
  - **One mechanical engineer** holds the Rev B housing fixes (PRO2-424, PRO2-416).
- **Watch this week:** the tech-lead meeting on where voice enrollment and the AI models run
  (PRO2-528, PRO2-449). There is no Jira trace of it, and Monday's stand-up didn't mention it.

## Active epics

- [PRO2-1](https://epazz.atlassian.net/browse/PRO2-1) — Voice Lock, Layer 3: capture only the agent's voice for the customer. In Progress, 5/11 Stories done. Due 2027-11-15.
- [PRO2-2](https://epazz.atlassian.net/browse/PRO2-2) — Voice Lock, Layer 1: clean, private customer audio for the agent through the directional speaker. In Progress, 3/7 (PRO2-249 reopened). Due 2027-11-15.
- [PRO2-3](https://epazz.atlassian.net/browse/PRO2-3) — Connectivity & Ports: power, USB, network, Wi-Fi and Bluetooth; board being redesigned for the new chip. In Progress, 6/17 (PRO2-461 closed 2026-11-16). Due 2027-11-15.
- [PRO2-4](https://epazz.atlassian.net/browse/PRO2-4) — User Interface: touch controls, status lights, anti-theft slot. To Do at Epic level; 1/4 Stories done. Due 2027-11-15.
- [PRO2-8](https://epazz.atlassian.net/browse/PRO2-8) — Mechanical Structure: the casing, hidden hinges, cooling, materials and cost. In Progress, 5/21. Due 2027-11-15.
- [PRO2-172](https://epazz.atlassian.net/browse/PRO2-172) — Industrial Design: step 5 of 6; EVT-2 design V5b in progress (overdue, reviewed 2026-11-16). In Progress, 5/6. Due 2027-11-15.
- [PRO2-449](https://epazz.atlassian.net/browse/PRO2-449) — Pro application: the software running on the device. In Progress, 17/22. Due 2027-11-15.
- [PRO2-450](https://epazz.atlassian.net/browse/PRO2-450) — Field Test + Release Candidate. To Do, 0/8; test plan PRO2-489 re-dated to 2027-02-08. Due 2027-11-15.
- [PRO2-555](https://epazz.atlassian.net/browse/PRO2-555) — Product Reliability & Risk Management (DFMEA, a scored list of ways the design could fail). In Progress, no owner, no Stories yet. Due 2027-09-30.

## Recent changes

- 2026-11-16 (second redo): AI-accelerator Story PRO2-461 Done, no comment; the only Jira change
  since the afternoon version.
- 2026-11-16:
  - Sprint 10 closed and Sprint 11 started in Jira (178 tickets).
  - Diffuser task PRO2-333 Done, with LED mock-up results (PRO2-299).
  - Field-test plan PRO2-489 re-dated to 2027-02-08; POC Story PRO2-249 reopened.
  - 7 overdue tickets commented "Push out to December".
  - Stand-up: chip purchase order only now going out; EVT-2 design to stay close to the current
    one and match the Beacon and Headset (`transcripts/2026-11-16-standup.md`).
- 2026-11-12: sound masking moved to the Beacon (PRO2-156); Rev B uses the hidden HG-TE03 hinge
  (PRO2-557); Rev A printed and reviewed (PRO2-424); Rev B BOM about $54 per unit, mechanical only (PRO2-553).
- Earlier reports: [[ZenaQuiet-Pro2/jira/2026-11-13-jira|2026-11-13]],
  [[ZenaQuiet-Pro2/jira/2026-11-12-jira|2026-11-12]].
