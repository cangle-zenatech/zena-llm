---
type: overview
updated: 2026-11-09
---

# Projects Overview

**Portfolio (2026-11-09):** 2 of 4 products on track for 2027-11-15 (Pro2, Beacon), but Pro2 has no margin left. Headset is Behind (POC gate forecast +66 days, MP forecast 2028-01-20; prototype boards held at the supplier for three weeks) and Mask is now Behind too. Every project shows RED this week: real slippage in Headset, Mask, Beacon (late board layouts) and Research, plus two uncorrected dates (PRO2-553, BC-141). No CTO-visit decision is recorded in Jira. See [[portfolio/2026-11-09-rollup]].

One paragraph per active project: what it is and where it stands. Details are on each project's overview page and in its latest weekly report.

## ZenaQuiet-Pro2

A desk unit that keeps private call audio private without a headset ("Voice Lock"). It cleans up the customer's speech and plays it through a directional speaker, so only the agent hears it. **As of 2026-11-09:** in EVT (gate 2027-02-08, 91 days). 34% of EVT work items count as finished, just under the 35% expected, and at the current pace the gate is reached with no margin. Health RED in Jira, mainly because of one likely mistyped date (PRO2-553, due 2028). Two mechanical analyses are 10 days late, the hinge bench test passed its due date unstarted, and no decision from the CTO visit is recorded. See [[ZenaQuiet-Pro2/overview]] and [[ZenaQuiet-Pro2/jira/2026-11-09-jira|2026-11-09 report]].

## ZenaQuiet-Beacon

A ceiling unit, powered over the network cable, that coordinates a cluster of Pro units on a floor. It handles voice-consent rules, relays cloud commands and keeps zone settings in sync. **As of 2026-11-09:** in EVT, gate 2027-02-08 (91 days). 51% of EVT work items are finished, well ahead of plan; the sound-masking board's parts, schematic and speaker housing were done this week. Health RED: three circuit-board layouts are 10 days late (one has no owner), and the misfiled task BC-141 is still there. See [[ZenaQuiet-Beacon/overview]] and [[ZenaQuiet-Beacon/jira/2026-11-09-jira|2026-11-09 report]].

## ZenaQuiet-Headset

A call-centre headset with voice capture for Voice Lock, active noise cancelling and a detachable magnetic masking arc. **As of 2026-11-09:** in POC (gate 2027-02-08, 91 days). Only 21% of POC work counts against 35% expected, and at the current pace the gate lands about 66 days late (Behind). Health **RED**: the prototype boards have been held at the supplier for three weeks over a small unpaid charge, now expected around 2026-11-30, about 50 working days late. Almost nothing moved in Jira this week, and the chip and arc decisions are still not recorded. See [[ZenaQuiet-Headset/overview]] and [[ZenaQuiet-Headset/jira/2026-11-09-jira|2026-11-09 report]].

## ZenaQuiet-Mask

A wearable face mask that filters the air and keeps the wearer's conversations private; the heavy voice processing runs on the paired phone. **As of 2026-11-09:** in POC (gate 2027-02-08, 91 days). 10% of POC work items are finished against 35% expected, so Mask is now Behind (25.5 points) and RED. A prototype and the dampening-material research started, but engineering has no owners or spec, and the board ordered outside Jira and the processor choice are still not recorded. See [[ZenaQuiet-Mask/overview]] and [[ZenaQuiet-Mask/jira/2026-11-09-jira|2026-11-09 report]].

## ZenaQuiet-Research

The Acoustic team's research work that supports the products, such as the chip choice and office acoustics. It has no stage schedule of its own. **As of 2026-11-09:** 18 open items, 8 overdue. Health RED because the Beacon masking prototype (RS-16) is 10 days late. The chip evaluation RS-2 was closed after Hailo 8L was ruled out, but no chip is chosen and the decision RS-1 missed its new 6 Nov date; the RK3576 kit request still has no cost or approval and conflicts with the "No components from China" rule. See [[ZenaQuiet-Research/overview]] and [[ZenaQuiet-Research/jira/2026-11-09-jira|2026-11-09 report]].
