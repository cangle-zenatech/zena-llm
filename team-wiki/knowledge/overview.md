---
type: overview
updated: 2026-11-03
---

# Projects Overview

**Portfolio (2026-11-03):** 2 of 4 products on track for 2027-11-15 (Pro2, Beacon). Headset is Behind (POC gate forecast +41 days, MP forecast 2027-12-26) and RED because its prototype boards are still held at the supplier; Mask is At risk. Pro2 and Beacon show RED only because of one wrong date each (PRO2-553, BC-141). Jira barely changed since yesterday, and no CTO-visit decision is recorded yet. See [[portfolio/2026-11-03-rollup]].

One paragraph per active project: what it is and where it stands. Details are on each project's overview page and in its latest weekly report.

## ZenaQuiet-Pro2

A desk unit that keeps private call audio private without a headset ("Voice Lock"). It cleans up the customer's speech and plays it through a directional speaker, so only the agent hears it. **As of 2026-11-03:** in EVT (gate 2027-02-08, 97 days). 34% of EVT work items are finished, ahead of the 31% expected. Health RED in Jira only because of one likely mistyped date (PRO2-553, due 2028); otherwise AMBER. Six mechanical tasks are overdue, no hinge delivery is recorded before the 6 Nov bench test, and a new risk analysis (PRO2-555) finds fan and speaker noise reaching the microphones the top risk for both enclosure designs. See [[ZenaQuiet-Pro2/overview]] and [[ZenaQuiet-Pro2/jira/2026-11-03-jira|2026-11-03 report]].

## ZenaQuiet-Beacon

A ceiling unit, powered over the network cable, that coordinates a cluster of Pro units on a floor. It handles voice-consent rules, relays cloud commands and keeps zone settings in sync. **As of 2026-11-03:** in EVT, gate 2027-02-08 (97 days). 49% of EVT work items are finished, well ahead of plan; no Jira change since yesterday. Health RED in Jira, still only because of the misfiled design task BC-141. Sound-masking electronics and three board layouts are 4 days overdue and not started. See [[ZenaQuiet-Beacon/overview]] and [[ZenaQuiet-Beacon/jira/2026-11-03-jira|2026-11-03 report]].

## ZenaQuiet-Headset

A call-centre headset with voice capture for Voice Lock, active noise cancelling and a detachable magnetic masking arc. **As of 2026-11-03:** in POC (gate 2027-02-08, 97 days). Only 21% of POC work counts, and at the current pace the gate lands about 41 days late (Behind). Health **RED** once purchasing is included: the prototype boards are still held at the supplier over a small unpaid charge, now expected around 2026-11-24, about 46 working days late. The chip choice and the arc scope are still not recorded, and most tasks have no owner in Jira. See [[ZenaQuiet-Headset/overview]] and [[ZenaQuiet-Headset/jira/2026-11-03-jira|2026-11-03 report]].

## ZenaQuiet-Mask

A wearable face mask that filters the air and keeps the wearer's conversations private; the heavy voice processing runs on the paired phone. **As of 2026-11-03:** in POC (gate 2027-02-08, 97 days). 10% of POC work items are finished against 31% expected (At risk). Health AMBER. No Jira change since yesterday: engineering hasn't started, the mask spec isn't written, and the board ordered outside Jira and the processor choice are still not recorded. See [[ZenaQuiet-Mask/overview]] and [[ZenaQuiet-Mask/jira/2026-11-03-jira|2026-11-03 report]].

## ZenaQuiet-Research

The Acoustic team's research work that supports the products, such as the chip choice and office acoustics. It has no stage schedule of its own. **As of 2026-11-03:** 19 open items, 9 overdue (5 yesterday) after the four office-acoustics items passed their 2 Nov due date. The chip decision (RS-1) is 14 days late, with Qualcomm and the Rockchip RK3576 as the options; the RK3576 kit request has no cost or approval and conflicts with the "No components from China" rule. Health AMBER. See [[ZenaQuiet-Research/overview]] and [[ZenaQuiet-Research/jira/2026-11-03-jira|2026-11-03 report]].
