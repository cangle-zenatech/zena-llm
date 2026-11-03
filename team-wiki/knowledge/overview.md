---
type: overview
updated: 2026-11-02
---

# Projects Overview

**Portfolio (2026-11-02):** 2 of 4 products on track for 2027-11-15 (Pro2, Beacon). Headset is Behind (POC gate forecast +36 days, MP forecast 2027-12-21) and RED because its prototype boards are still held at the supplier; Mask is At risk and falling further behind. Pro2 and Beacon show RED only because of one mistyped date each (PRO2-553, BC-141). The decisions waiting for the CTO visit, which starts today, are not yet recorded. See [[portfolio/2026-11-02-rollup]].

One paragraph per active project: what it is and where it stands. Details are on each project's overview page and in its latest weekly report.

## ZenaQuiet-Pro2

A desk unit that keeps private call audio private without a headset ("Voice Lock"). It cleans up the customer's speech and plays it through a directional speaker, so only the agent hears it. **As of 2026-11-02:** in EVT, the first engineering-prototype stage (gate 2027-02-08, 98 days away). 34% of EVT work items are finished, ahead of the 30% expected. Health RED in Jira, but only because a new cost-tracking task (PRO2-553) is due in 2028, probably a typo; otherwise AMBER. Six mechanical tasks are overdue, no hinge delivery is recorded before the 6 Nov bench test, and 12 electronics tasks were reopened without a reason. See [[ZenaQuiet-Pro2/overview]] and [[ZenaQuiet-Pro2/jira/2026-11-02-jira|2026-11-02 report]].

## ZenaQuiet-Beacon

A ceiling unit, powered over the network cable, that coordinates a cluster of Pro units on a floor. It handles voice-consent rules, relays cloud commands and keeps zone settings in sync. **As of 2026-11-02:** in EVT, gate 2027-02-08 (98 days). 49% of EVT work items are finished, well ahead of plan; a quiet week. Health RED in Jira, still only because of the misfiled design task BC-141. The sound-masking electronics and three board layouts are a few days overdue and not started, while the Pro-or-Beacon masking decision waits on the CTO visit. See [[ZenaQuiet-Beacon/overview]] and [[ZenaQuiet-Beacon/jira/2026-11-02-jira|2026-11-02 report]].

## ZenaQuiet-Headset

A call-centre headset with voice capture for Voice Lock, active noise cancelling and a detachable magnetic masking arc. **As of 2026-11-02:** in POC (gate 2027-02-08, 98 days). 33% of POC work items are marked finished, but only 21% count, and at the current pace the gate lands about 36 days late (Behind). Health **RED** once purchasing is included: the prototype boards are still held at the supplier over a small unpaid charge, now expected around 2026-11-23, about 45 working days late. A test confirmed the passive arc can't meet its target, the chip choice is still not recorded, and most tasks have no owner in Jira. See [[ZenaQuiet-Headset/overview]] and [[ZenaQuiet-Headset/jira/2026-11-02-jira|2026-11-02 report]].

## ZenaQuiet-Mask

A wearable face mask that filters the air and keeps the wearer's conversations private; the heavy voice processing runs on the paired phone. **As of 2026-11-02:** in POC (gate 2027-02-08, 98 days). 10% of POC work items are finished against 30% expected (At risk, 20.5 points behind). Health AMBER. Industrial design closed three more tasks, but engineering hasn't started, the mask spec isn't written, and the board ordered outside Jira and the processor choice are still not recorded. See [[ZenaQuiet-Mask/overview]] and [[ZenaQuiet-Mask/jira/2026-11-02-jira|2026-11-02 report]].

## ZenaQuiet-Research

The Acoustic team's research work that supports the products, such as the chip choice and office acoustics. It has no stage schedule of its own. **As of 2026-11-02:** 19 open items, 5 overdue (2 last week). The chip decision (RS-1) is 13 days late, with Qualcomm and the Rockchip RK3576 as the options; the RK3576 kit request has no cost or approval and conflicts with the "No components from China" rule. The Beacon masking prototype (RS-16) is overdue with no board. Health AMBER. See [[ZenaQuiet-Research/overview]] and [[ZenaQuiet-Research/jira/2026-11-02-jira|2026-11-02 report]].
