---
type: overview
project: ZenaQuiet-Headset
updated: 2026-11-09
---

# ZenaQuiet-Headset

## What this project is

"ZenaHeadset Quiet" is a headset for call-centre (BPO) agents who wear it for 8–12 hours a shift. It captures the agent's voice cleanly for the Voice Lock speech pipeline and cancels room noise at the ears. A clip-on magnetic Arc is meant to reduce what neighbours overhear. It connects over USB-C and Bluetooth to Zoo Meet and the ZenaAI cloud. Jira project `HS`; stage windows are in [[reference#Stage schedule (per product)]].

## Where it stands

As of 2026-11-09, the Headset is in the POC (proof-of-concept) stage. The gate to EVT is on 2027-02-08, 91 days away. 8 of 24 POC Stories are Done (33.3%), now 1.7 points behind the expected 35.0%; two of those are Arc Stories titled "[TO BE REMOVED]". Health is **RED** because of source risks. On Jira alone it is AMBER: 9 HIGH Epic-date risks, none on the POC gate. Jira records nothing from the CTO visit week (from 2026-11-02).

Top issues:

1. The Headset PCB order is still stopped at the supplier until about $35 extra is paid for a wrong board option. Board work (HS-144) now starts about 50 working days late, with boards around 2026-11-30.
2. The chip choice is not recorded. HS-164 still plans the NXP i.MX 95, while Research proposes the Rockchip RK3576 (RS-2). The core voice and noise-cancelling POC Stories (HS-161, HS-48) have not started.
3. Arc scope is still open after the HS-79 print test missed the 8–12 dB passive target. EE tickets are still missing, and 482 of 516 open items have no assignee.

Latest report: [[ZenaQuiet-Headset/jira/2026-11-09-jira|2026-11-09 report]].

## Active epics

- HS-1: mic capture for Voice Lock. To Do, due 2027-09-06, no owner.
- HS-2: active noise cancelling. To Do, due 2027-09-06, no owner.
- HS-3: power, battery and fast charging. To Do, due 2027-09-06.
- HS-4: buttons, LEDs and controls. To Do, due 2027-09-06, no owner.
- HS-6: mechanical enclosure. In Progress, due 2027-09-06.
- HS-51: Arc directional masking; passive target missed, scope undecided. To Do, due 2027-09-06, no owner.
- HS-142: industrial design. To Do, due 2027-02-08, which is before its own Stories end.
- HS-380: Zoo Meet integration and cloud denoise. To Do, due 2027-09-06, no owner.
- HS-451: connectivity and ports. To Do, due 2027-09-06, no owner.
- HS-640: field test and release candidate. To Do, due 2027-02-08, which is before its own Stories end.
- HS-47 is an empty placeholder Epic.

## Recent changes

- 2026-11-09: only ID work moved. HS-330 re-dated from 2026-10-30 to 2026-11-27 (no longer late); HS-326 to HS-330 moved to POC Sprint 4. No new comments, no PCB payment, chip or Arc decision recorded. PCB forecast slips to 2026-11-30. Report: [[ZenaQuiet-Headset/jira/2026-11-09-jira]].
- 2026-11-03: no Jira change since 2026-11-02. Stale items jumped from 99 to 504 because the 2026-10-20 bulk edit turned 14 days old. Report: [[ZenaQuiet-Headset/jira/2026-11-03-jira]].
- Earlier reports: [[ZenaQuiet-Headset/jira/2026-11-02-jira]], [[ZenaQuiet-Headset/jira/2026-10-26-jira]], [[ZenaQuiet-Headset/jira/2026-10-19-jira]].
