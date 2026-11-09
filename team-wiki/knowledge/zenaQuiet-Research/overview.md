---
type: overview
project: ZenaQuiet-Research
updated: 2026-11-09
---

# ZenaQuiet-Research

## What this project is

The Acoustic team's research project (Jira key `RS`). It researches technologies and problems for the products Pro2, Beacon, Headset and Mask. It has no development stages of its own, so it is measured against the product work it supports. See [[ZenaQuiet-Research/INDEX|instructions]] and [[reference#Jira projects]].

## Where it stands

As of 2026-11-09 ([[ZenaQuiet-Research/jira/2026-11-09-jira|weekly report]]): 18 open items (10 Epics, 8 Stories), link coverage 5.6% (1/18), 8 overdue, health **RED**. Reason: the Beacon masking prototype RS-16, the only open item linked to a product, is 10 days past due (one HIGH risk). Top issues:

1. **Beacon masking demo 10 days late** (RS-16, due 2026-10-30; Beacon BC-233 due 2026-11-30 waits on it). No board, no placement decision and nothing from the CTO visit (from 2026-11-02) recorded.
2. **Chip still not chosen.** RS-1 was re-dated to 2026-11-06 and is 3 days late. Its evaluation Story RS-2 closed on 2026-11-03 without a decision; Hailo 8L and XMOS are ruled out. Qualcomm vs Rockchip RK3576 is open. The RK3576 is a Chinese chip, which conflicts with the "no components from China" rule in [[reference#Sourcing rules]] (flagged, not resolved).
3. **RK3576 evaluation-kit request** is still only in a Jira comment (RS-2, 2026-10-23): no cost, no CTO approval.

## Active epics

- **RS-1 Chip eval + decision:** In Progress, due 2026-11-06 (overdue). No product link of its own since RS-2 (linked to Pro2 PRO2-461 / PRO2-486) closed.
- **RS-4 Ultrasonic loudspeaker survey:** In Progress, due 2026-10-23 (overdue); its only Story, RS-3, is Done and links to Pro2 PRO2-463.
- **RS-11 Layer 2: Office Acoustics:** To Do, due 2027-02-08. Covers RS-16 Beacon sound masking (In Progress, overdue, linked to BC-233 and BC-234), RS-21 absorbing materials (In Progress, overdue), and RS-22, RS-23, RS-24, RS-25 (To Do, overdue).
- **RS-14 Ultrasonic array:** To Do, no dates. Phased-array test RS-19 (2026-10-26 → 2026-11-30) not started.
- **RS-15 Qt multi-unit app:** To Do, due 2027-03-31 (RS-18 In Progress, undated).
- **RS-8 Headset mic beamforming:** To Do, due 2027-02-08. Empty; its start date has passed.
- **Empty, undated Epics:** RS-7 Drone propeller ANC, RS-9 Android mobile app, RS-10 Sound masking impl, RS-20 TSE module for sound masking.

## Recent changes

- 2026-11-09: RS-2 Done (2026-11-03), Hailo 8L ruled out (RS-2 comment); RS-1 re-dated to 2026-11-06 and missed it; link coverage 10.5% → 5.6%; RS-16 became HIGH, health AMBER → RED. Nothing from the CTO visit recorded.
- 2026-11-03: RS-21 to RS-24 passed their 2026-11-02 due date (9 overdue).
- 2026-11-02: RS-2, RS-16, RS-25 overdue; RS-3 linked to Pro2 PRO2-463.
- 2026-10-26: RS-2 linked to Pro2, RS-16 to Beacon; XMOS ruled out; RK3576 proposed with a kit request.
