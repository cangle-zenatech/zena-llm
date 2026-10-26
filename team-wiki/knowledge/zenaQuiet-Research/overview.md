---
type: overview
project: ZenaQuiet-Research
updated: 2026-10-26
---

# ZenaQuiet-Research

## What this project is

The Acoustic team's research project (Jira key `RS`). It researches technologies and problems for the products Pro2, Beacon, Headset and Mask. It has no development stages of its own, so it is measured against the product work it supports. See [[ZenaQuiet-Research/INDEX|instructions]] and [[reference#Jira projects]].

## Where it stands

As of 2026-10-26 ([[ZenaQuiet-Research/jira/2026-10-26-jira|weekly report]]): 19 open items (10 Epics, 9 Stories), link coverage 10.5% (2/19), 2 overdue, health **AMBER**. Reason: few items are linked to product work, two Epics are past due, and there are 14 MEDIUM risks. Top issues:

1. **Chip decision overdue** (RS-1, due 2026-10-20). XMOS was ruled out; a Chinese chip, Rockchip RK3576, is now proposed (RS-2). That conflicts with the "no components from China" rule in [[reference#Sourcing rules]]. Pro2 tickets PRO2-461 and PRO2-486 now wait on RS-2.
2. **RK3576 evaluation-kit request** is only in a Jira comment (RS-2, 2026-10-23): no cost and no CTO approval yet.
3. **Office Acoustics behind plan:** RS-22, RS-23 and RS-24 are not started; RS-25 starts after its due date. The Beacon masking demo (RS-16) still has no confirmed board for the CTO visit.

## Active epics

- **RS-1 Chip eval + decision:** In Progress, due 2026-10-20 (overdue). Story RS-2 (TSE on NPU, due 2026-10-29) is linked to Pro2.
- **RS-4 Ultrasonic loudspeaker survey:** In Progress, due 2026-10-23 (overdue); its only Story, RS-3, is Done.
- **RS-11 Layer 2: Office Acoustics:** To Do, due 2027-02-08. Covers RS-16 Beacon sound masking (In Progress, due 2026-10-30, linked to BC-233 and BC-234), RS-21 absorbing materials (In Progress), and RS-22, RS-23, RS-24, RS-25 (To Do).
- **RS-14 Ultrasonic array:** To Do, no dates. Phased-array test RS-19 runs 2026-10-26 → 2026-11-30.
- **RS-15 Qt multi-unit app:** To Do, due 2027-03-31 (RS-18 In Progress, undated).
- **RS-8 Headset mic beamforming:** To Do, due 2027-02-08. Empty; its start date has passed.
- **Empty, undated Epics:** RS-7 Drone propeller ANC, RS-9 Android mobile app, RS-10 Sound masking impl, RS-20 TSE module for sound masking.

## Recent changes

- 2026-10-26: RS-1 and RS-4 became overdue. RS-2 due moved 2026-10-19 → 2026-10-29. RS-2 is now linked to Pro2 PRO2-461 and PRO2-486. RS-16 is now linked to BC-233, and "implements" BC-234. Comments: XMOS ruled out (RS-1, 2026-10-22); RK3576 proposed and an eval kit requested (RS-2, 2026-10-23).
- 2026-10-19: RS-3 Done; RS-21 In Progress; RS-8 dated. Priorities set for RS-16, RS-22 and RS-21. First source risks from threads and meetings.
- 2026-10-15: first product link (RS-16 → BC-234).
- 2026-10-12: first weekly report.
