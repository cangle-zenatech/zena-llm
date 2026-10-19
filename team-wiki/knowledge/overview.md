---
type: overview
updated: 2026-10-19
---

# Projects Overview

**Portfolio (2026-10-19):** 4 of 4 products on track for 2027-11-15 by progress, but two are RED: Headset, because its prototype boards are stuck at the supplier and the work that needs them starts about 35 working days late; and Beacon, because of a misfiled design task in Jira (probably a filing problem). Pro2 and Beacon are ahead of plan; Mask and Headset are behind it. See [[portfolio/2026-10-19-rollup]].

One paragraph per active project: what it is and where it stands. Details are on each project's overview page and in its latest weekly report.

## ZenaQuiet-Pro2

A desk unit that keeps private call audio private without a headset ("Voice Lock"). It cleans up the customer's speech and plays it through a directional speaker, so only the agent hears it. **As of 2026-10-19:** in EVT, the first engineering-prototype stage (its stage review, called the gate, is on 2027-02-08, 112 days away). 30% of EVT work items are finished, ahead of the 20% expected by now. Health AMBER. Four items are overdue, the hinge samples for the new hinge test arrive weeks after the test is planned to start, and which version of the Pro goes into EVT is still being decided. See [[ZenaQuiet-Pro2/overview]] and [[ZenaQuiet-Pro2/jira/2026-10-19-jira|2026-10-19 report]].

## ZenaQuiet-Beacon

A ceiling unit, powered over the network cable, that coordinates a cluster of Pro units on a floor. It handles voice-consent rules, relays cloud commands and keeps zone settings in sync. **As of 2026-10-19:** in EVT, gate 2027-02-08 (112 days). 47% of EVT work items are finished, ahead of plan. Health RED in Jira, because a design task with dates in the next stage is filed under a current-stage work item; it is probably just misfiled, and moving it would bring Beacon back to AMBER. The sound-masking demo promised for the CTO visit has no hardware yet, one mechanical engineer carries most of the open work, and whether the Beacon stays in the product line came up again in the 2026-10-19 meeting. The cloud-connectivity work removed from Jira on 2026-10-13 has not come back. See [[ZenaQuiet-Beacon/overview]] and [[ZenaQuiet-Beacon/jira/2026-10-19-jira|2026-10-19 report]].

## ZenaQuiet-Headset

A call-centre headset with voice capture for Voice Lock, active noise cancelling and a detachable magnetic masking arc. **As of 2026-10-19:** in POC, the proof-of-concept stage (gate 2027-02-08, 112 days). 21% of POC work items are marked finished, but only 8% count. Health **RED** once purchasing is included: the prototype circuit boards are paid for, but a wrong option on the order has stopped the supplier, so the work that needs them starts about 35 working days late (boards around 2026-11-09). Voice and noise-cancelling work hasn't started, and the processor chip choice is open again. See [[ZenaQuiet-Headset/overview]] and [[ZenaQuiet-Headset/jira/2026-10-19-jira|2026-10-19 report]].

## ZenaQuiet-Mask

A wearable face mask that filters the air and keeps the wearer's conversations private; the heavy voice processing runs on the paired phone. **As of 2026-10-19:** in POC (gate 2027-02-08, 112 days). 10% of POC work items are finished. Health AMBER. A first circuit board is already ordered and paid but not tracked in Jira, and meetings plan a processor on the mask itself, which conflicts with the phone-based design in Jira. Most engineering work still has no owner. See [[ZenaQuiet-Mask/overview]] and [[ZenaQuiet-Mask/jira/2026-10-19-jira|2026-10-19 report]].

## ZenaQuiet-Research

The Acoustic team's research work that supports the products, such as the chip choice and office acoustics. It has no stage schedule of its own. **As of 2026-10-19:** 19 open items; one finished this week. The chip decision slipped from 2026-10-16 to 2026-10-20. One work item links to a product ticket (sound masking, RS-16 → Beacon BC-234). Health AMBER. See [[ZenaQuiet-Research/overview]] and [[ZenaQuiet-Research/jira/2026-10-19-jira|2026-10-19 report]].
