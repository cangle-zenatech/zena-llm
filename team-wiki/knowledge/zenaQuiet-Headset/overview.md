---
type: overview
project: ZenaQuiet-Headset
updated: 2026-10-26
---

# ZenaQuiet-Headset

## What this project is

"ZenaHeadset Quiet" is a call-centre (BPO) headset for agents who wear it 8–12 hours a shift. It captures the agent's voice cleanly for the Voice Lock speech pipeline and cancels room noise at the ears. A clip-on magnetic Arc reduces what neighbours overhear. It connects over USB-C and Bluetooth to Zoo Meet and the ZenaAI cloud. Jira project `HS`; stage windows are in [[reference#Stage schedule (per product)]].

## Where it stands

As of 2026-10-26, the Headset is in the POC (proof-of-concept) stage. The gate to EVT is on 2027-02-08, 105 days away. 8 of 24 POC Stories are Done (33.3% vs 25.0% expected), but two of those are Arc Stories titled "[TO BE REMOVED]". Health is **RED** because of source risks; on Jira alone it is AMBER (9 HIGH Epic-date risks, none on the POC gate).

Top issues:

1. The Headset PCB order is still stopped at the supplier until about $35 extra is paid for a wrong board option. The board work (HS-144) now starts about 40 working days late, with boards around 2026-11-16, after the CTO visit.
2. The chip choice is not recorded. HS-164 still plans the NXP i.MX 95, and the core voice and noise-cancelling POC Stories (HS-161, HS-48) have not started. 55 POC tickets moved one sprint later this week.
3. EE Headset tickets promised on 2026-10-19 are still missing. EE inputs to Mechanical (HS-130, HS-131, HS-336, HS-337) have no owner.

Latest report: [[ZenaQuiet-Headset/jira/2026-10-26-jira|2026-10-26 report]].

## Active epics

- HS-1: mic capture for Voice Lock. To Do, due 2027-09-06, no owner.
- HS-2: active noise cancelling. To Do, due 2027-09-06, no owner.
- HS-3: power, battery and fast charging. To Do, due 2027-09-06.
- HS-4: buttons, LEDs and controls. To Do, due 2027-09-06, no owner.
- HS-6: mechanical enclosure. In Progress, due 2027-09-06.
- HS-51: Arc directional masking; scope undecided. To Do, due 2027-09-06, no owner.
- HS-142: industrial design. To Do, due 2027-02-08, which is before its own Stories end.
- HS-380: Zoo Meet integration and cloud denoise. To Do, due 2027-09-06, no owner.
- HS-451: connectivity and ports. To Do, due 2027-09-06, no owner.
- HS-640: field test and release candidate. To Do, due 2027-02-08, which is before its own Stories end.
- HS-47 is an empty placeholder Epic.

## Recent changes

- 2026-10-26:
  - HS-318 (form and appearance model), HS-86 and HS-127 closed. The last two are "[TO BE REMOVED]" Arc Stories, and their measurement Subtasks HS-248 and HS-334 were deleted.
  - HS-129 (earcup shells) and HS-583 (headband fit) are Done.
  - HS-330 is now due 2026-10-30.
  - 55 POC tickets moved one sprint later.
  - Team prefixes were removed from all Subtask titles.
  - No PCB, chip or EE-ticket update in Jira.
  - Report: [[ZenaQuiet-Headset/jira/2026-10-26-jira]].
- 2026-10-19: first report that also reads purchase threads and meeting transcripts. The PCB order was found stopped at the supplier (health RED), and 5 Mechanical Subtasks closed. Report: [[ZenaQuiet-Headset/jira/2026-10-19-jira]].
- Earlier reports: [[ZenaQuiet-Headset/jira/2026-10-15-jira]], [[ZenaQuiet-Headset/jira/2026-10-13-jira]], [[ZenaQuiet-Headset/jira/2026-10-12-jira]].
