---
type: overview
project: ZenaQuiet-Research
updated: 2026-11-03
---

# ZenaQuiet-Research

## What this project is

The Acoustic team's research project (Jira key `RS`). It researches technologies and problems for the products Pro2, Beacon, Headset and Mask. It has no development stages of its own, so it is measured against the product work it supports. See [[ZenaQuiet-Research/INDEX|instructions]] and [[reference#Jira projects]].

## Where it stands

As of 2026-11-03 ([[ZenaQuiet-Research/jira/2026-11-03-jira|weekly report]]): 19 open items (10 Epics, 9 Stories), link coverage 10.5% (2/19), 9 overdue, health **AMBER**. Reason: nearly half the open items are past due, few items are linked to product work, and there are 18 MEDIUM risks; no product ticket is at risk yet. Top issues:

1. **Chip decision 14 days overdue** (RS-1, due 2026-10-20; RS-2, due 2026-10-29). Options: Qualcomm or Rockchip RK3576, a Chinese chip, which conflicts with the "no components from China" rule in [[reference#Sourcing rules]]. Pro2 tickets PRO2-461 and PRO2-486 wait on RS-2. The CTO visit (from 2026-11-02) has not yet produced a recorded decision.
2. **RK3576 evaluation-kit request** is still only in a Jira comment (RS-2, 2026-10-23): no cost and no CTO approval.
3. **Office Acoustics behind:** Beacon masking demo RS-16 overdue (due 2026-10-30) with no confirmed board; RS-21 to RS-24 passed their 2026-11-02 due date; RS-25 8 days late. All with one owner.

## Active epics

- **RS-1 Chip eval + decision:** In Progress, due 2026-10-20 (overdue). Story RS-2 (TSE on NPU, due 2026-10-29, overdue) is linked to Pro2.
- **RS-4 Ultrasonic loudspeaker survey:** In Progress, due 2026-10-23 (overdue); its only Story, RS-3, is Done and links to Pro2 PRO2-463 (beamforming speaker).
- **RS-11 Layer 2: Office Acoustics:** To Do, due 2027-02-08. Covers RS-16 Beacon sound masking (In Progress, overdue, linked to BC-233 and BC-234), RS-21 absorbing materials (In Progress, overdue), and RS-22, RS-23, RS-24, RS-25 (To Do, overdue).
- **RS-14 Ultrasonic array:** To Do, no dates. Phased-array test RS-19 (2026-10-26 → 2026-11-30) not started.
- **RS-15 Qt multi-unit app:** To Do, due 2027-03-31 (RS-18 In Progress, undated).
- **RS-8 Headset mic beamforming:** To Do, due 2027-02-08. Empty; its start date has passed.
- **Empty, undated Epics:** RS-7 Drone propeller ANC, RS-9 Android mobile app, RS-10 Sound masking impl, RS-20 TSE module for sound masking.

## Recent changes

- 2026-11-03: RS-21, RS-22, RS-23, RS-24 passed their 2026-11-02 due date (9 overdue in all). No other Jira change and no comment since 2026-10-23; nothing from the CTO visit recorded yet.
- 2026-11-02: RS-2, RS-16 and RS-25 became overdue (5 in all). RS-3 now links to Pro2 PRO2-463.
- 2026-10-26: RS-1 and RS-4 overdue; RS-2 linked to PRO2-461 / PRO2-486; RS-16 linked to BC-233 / BC-234. XMOS ruled out (RS-1); RK3576 proposed with a kit request (RS-2).
- 2026-10-12 to 2026-10-19: first reports, first product link (RS-16 → BC-234), RS-3 Done, priorities set for RS-16, RS-22, RS-21.
