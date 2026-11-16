---
type: overview
project: ZenaQuiet-Research
updated: 2026-11-16
---

# ZenaQuiet-Research

## What this project is

This is the Acoustic team's research project (Jira key `RS`). The team researches technologies and problems for four products: Pro2, Beacon, Headset and Mask. The project has no development stages of its own, so it is measured against the product work it supports. See [[ZenaQuiet-Research/INDEX|instructions]] and [[reference#Jira projects]].

## Where it stands

As of 2026-11-16 ([[ZenaQuiet-Research/jira/2026-11-16-jira|weekly report]], second redo with a fresh Jira pull):

| Open items | Link coverage | Overdue | Health |
| --- | --- | --- | --- |
| 16 (10 Epics, 6 Stories) | 0% (0/16) | 6 | **RED** |

Health is RED because of a source risk. The loudspeaker for the Beacon sound-masking test is still not recorded as ordered. It is forecast to arrive 2026-12-03, three working days after Beacon story BC-233 is due (2026-11-30). Jira alone would rate Research AMBER.

Top issues:

1. **Masking speaker not ordered.**
   - The Beacon sound-masking prototype RS-16 is Done (2026-11-09).
   - The follow-up ceiling test on the Beacon board needs a speaker that is not recorded as ordered. It has no Jira ticket.
2. **New chip not recorded and not yet ordered.**
   - RS-1 is still In Progress, 10 days late, re-dated twice before. It names no chip.
   - The 2026-11-16 stand-up points to a Qualcomm chip (inferred); the purchase order was only sent that morning, about two weeks to arrive. On 2026-11-09 the board was said to be "ordered last week" (contradiction, flagged).
   - Pro2 story PRO2-461 (AI accelerator), which RS-2 links to, was set to Done on 2026-11-16 without any chip named in RS-1.
   - The Pro2 board redesign, Pro EVT1 chip tests and the Mask proof of concept wait on it (inferred).
   - The China sourcing-rule conflict from the earlier RK3576 proposal ([[reference#Sourcing rules]]) is still flagged, not resolved.
   - The tech-lead meeting on where Voice Lock enrollment and the AI models run has no Jira trace.
3. **Office Acoustics plan out of date.**
   - RS-21 (materials) was pushed into Sprint 5 but is still due 2026-11-16; its review with the CTO moved to next week.
   - RS-23 and RS-25 started on 2026-11-16 but keep past due dates; RS-22 and RS-24 are 14 days late and not started.
   - All of them sit with one person.

## Active epics

- **RS-1 Chip eval + decision:** In Progress, due 2026-11-06 (overdue). No product link of its own; it linked to Pro2 through RS-2, now Done.
- **RS-4 Ultrasonic loudspeaker survey:** In Progress, due 2026-10-23 (overdue). Its only Story, RS-3, is Done and links to Pro2 PRO2-463.
- **RS-11 Layer 2: Office Acoustics:** To Do, due 2027-02-08. RS-16 Done; RS-21, RS-23, RS-25 In Progress in Sprint 5; RS-22, RS-24 To Do and overdue.
- **RS-14 Ultrasonic array:** To Do, no dates. Phased-array test RS-19 (2026-10-26 → 2026-11-30) not started.
- **RS-15 Qt multi-unit app:** To Do, due 2027-03-31. RS-18 is Done (2026-11-09).
- **RS-8 Headset microphone beamforming:** To Do, due 2027-02-08. Empty; its start date has passed.
- **Empty, undated Epics:** RS-7 Drone propeller ANC, RS-9 Android mobile app, RS-10 Sound masking implementation, RS-20 TSE module for sound masking.

## Recent changes

- **2026-11-16 (second redo):** PRO2-461 (Pro2 AI accelerator, linked through RS-2) moved In Review → Done. No other change in RS.
- **2026-11-16 (redo):** RS-23 and RS-25 moved to In Progress (Sprint 5). Sprint 4 closed; RS-21 moved into Sprint 5 unfinished. Done Stories RS-2, RS-3, RS-16, RS-18 now show only future Sprint 6. New stand-up: chip purchase order sent 2026-11-16 (Qualcomm, inferred); RS-21 review moved to next week; Hoa asked to help with Mask materials. No new comments or attachments.
- **2026-11-13:** no Jira change. Speaker forecast 2026-12-02.
- **2026-11-12:** RS-16 and RS-18 Done (2026-11-09); RS-21 re-dated to 2026-11-16. Link coverage fell to 0%. Masking speaker not ordered (new HIGH source risk).
