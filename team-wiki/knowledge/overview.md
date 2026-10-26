---
type: overview
updated: 2026-10-26
---

# Projects Overview

**Portfolio (2026-10-26):** 2 of 4 products on track for 2027-11-15 (Pro2, Beacon). Headset is Behind (POC gate forecast +7 days) and RED because its prototype boards are still held at the supplier; Mask is At risk with most of its work unowned; Beacon is RED in Jira only because of a misfiled task. A proposed chip change (RK3576, RS-2) affects Pro2, Headset and Mask and waits on the CTO. See [[portfolio/2026-10-26-rollup]].

One paragraph per active project: what it is and where it stands. Details are on each project's overview page and in its latest weekly report.

## ZenaQuiet-Pro2

A desk unit that keeps private call audio private without a headset ("Voice Lock"). It cleans up the customer's speech and plays it through a directional speaker, so only the agent hears it. **As of 2026-10-26:** in EVT, the first engineering-prototype stage (its stage review, called the gate, is on 2027-02-08, 105 days away). 33% of EVT work items are finished, ahead of the 25% expected. Health AMBER. The hinge is still not settled and the housing is being redesigned for an alternative hinge; mechanical work piles up on one engineer; and the team has moved from an aluminium to a plastic housing without a recorded CTO approval. See [[ZenaQuiet-Pro2/overview]] and [[ZenaQuiet-Pro2/jira/2026-10-26-jira|2026-10-26 report]].

## ZenaQuiet-Beacon

A ceiling unit, powered over the network cable, that coordinates a cluster of Pro units on a floor. It handles voice-consent rules, relays cloud commands and keeps zone settings in sync. **As of 2026-10-26:** in EVT, gate 2027-02-08 (105 days). 49% of EVT work items are finished, well ahead of plan. Health RED in Jira, still only because a design task with next-stage dates (BC-141) is filed under a current-stage work item. The sound-masking hardware hasn't started and a separate ceiling-speaker housing is being drafted while the Pro-or-Beacon masking decision waits on the CTO. One mechanical engineer carries most open work. See [[ZenaQuiet-Beacon/overview]] and [[ZenaQuiet-Beacon/jira/2026-10-26-jira|2026-10-26 report]].

## ZenaQuiet-Headset

A call-centre headset with voice capture for Voice Lock, active noise cancelling and a detachable magnetic masking arc. **As of 2026-10-26:** in POC, the proof-of-concept stage (gate 2027-02-08, 105 days). 33% of POC work items are marked finished, but only 21% count, and at the current pace the gate lands about 7 days late (Behind). Health **RED** once purchasing is included: the prototype boards are still held at the supplier over a small extra payment, so the work that needs them starts about 40 working days late (boards around 2026-11-16). The chip choice is still not recorded, and most Headset tasks have no owner in Jira. See [[ZenaQuiet-Headset/overview]] and [[ZenaQuiet-Headset/jira/2026-10-26-jira|2026-10-26 report]].

## ZenaQuiet-Mask

A wearable face mask that filters the air and keeps the wearer's conversations private; the heavy voice processing runs on the paired phone. **As of 2026-10-26:** in POC (gate 2027-02-08, 105 days). 10% of POC work items are finished against 25% expected (At risk). Health AMBER. Industrial design closed three layout tasks, but no engineering work has started, the mask spec is not written, the first circuit board was ordered outside Jira, and the processor choice is not recorded. See [[ZenaQuiet-Mask/overview]] and [[ZenaQuiet-Mask/jira/2026-10-26-jira|2026-10-26 report]].

## ZenaQuiet-Research

The Acoustic team's research work that supports the products, such as the chip choice and office acoustics. It has no stage schedule of its own. **As of 2026-10-26:** 19 open items, 2 overdue. The chip decision (RS-1) is overdue: XMOS was ruled out and the Rockchip RK3576 is now proposed (RS-2), which two Pro2 Stories now link to, and which conflicts with the "No components from China" sourcing rule. Two items link to product tickets (Pro2 via RS-2, Beacon via RS-16). Health AMBER. See [[ZenaQuiet-Research/overview]] and [[ZenaQuiet-Research/jira/2026-10-26-jira|2026-10-26 report]].
