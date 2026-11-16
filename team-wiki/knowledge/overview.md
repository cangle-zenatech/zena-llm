---
type: overview
updated: 2026-11-16
---

# Projects Overview

**Portfolio (2026-11-16):** 2 of 4 products on track for 2027-11-15 (Beacon, Headset); Pro2 is At risk (its pace reaches the gate with no margin) and Mask is Behind. 12 Pro2 tickets are overdue since 13 Nov and not re-dated; the Beacon board layouts closed on 16 Nov, 3 days late. The new chip's purchase order only went out on 16 Nov, so the Pro2 boards and the Mask proof of concept wait about two more weeks. Decisions from the CTO visit and the team manager's 16 Nov directions are not in Jira yet. See [[portfolio/2026-11-16-rollup]].

One paragraph per active project: what it is and where it stands. Details are on each project's overview page and in its latest weekly report.

## ZenaQuiet-Pro2

A desk unit that keeps private call audio private without a headset ("Voice Lock"). It cleans up the customer's speech and plays it through a directional speaker, so only the agent hears it. **As of 2026-11-16:** in EVT (gate 2027-02-08, 84 days). 39% of EVT work counts as finished against 40% expected; on current pace it reaches the gate exactly on the gate day, so it is At risk. 12 tickets are overdue, most of them on hold for December parts. Health RED because of one likely mistyped date (PRO2-553) and a reopened proof-of-concept Story with no owner (PRO2-249). The first build review found 26 issues (5 severe), Revision B moves to a new hinge and plastic parts, sound masking moved to the Beacon, and the board is being redesigned for a changed chip whose purchase order only went out on 16 Nov. See [[ZenaQuiet-Pro2/overview]] and [[ZenaQuiet-Pro2/jira/2026-11-16-jira|2026-11-16 report]].

## ZenaQuiet-Beacon

A ceiling unit, powered over the network cable, that coordinates a cluster of Pro units on a floor. It handles voice-consent rules, relays cloud commands and keeps zone settings in sync, and now also takes over sound masking from the Pro. **As of 2026-11-16:** in EVT, gate 2027-02-08 (84 days). 62% of EVT work items are finished, well ahead of plan. Health AMBER. The three main-board layouts were finished on 16 Nov, 3 days late, but no board order is recorded; four enclosure Stories now sit on the gate day with no margin. The masking boards and the ceiling speaker still aren't ordered, so the room-noise test due 30 Nov is at risk; task BC-141 now adds a speaker to the Beacon model. See [[ZenaQuiet-Beacon/overview]] and [[ZenaQuiet-Beacon/jira/2026-11-16-jira|2026-11-16 report]].

## ZenaQuiet-Headset

A call-centre headset with voice capture for Voice Lock, active noise cancelling and a detachable magnetic masking arc. **As of 2026-11-16:** in POC (gate 2027-02-08, 84 days). 35% of POC work counts as finished against 40% expected, On track, mostly because 40 tickets were deleted and two Arc Stories closed on 12 Nov. Health AMBER (was RED): the prototype boards arrived and boot, but the audio chip on them isn't working yet and the power result is disputed. The team proposes dropping the passive arc and testing only its microphones. See [[ZenaQuiet-Headset/overview]] and [[ZenaQuiet-Headset/jira/2026-11-16-jira|2026-11-16 report]].

## ZenaQuiet-Mask

A wearable face mask that filters the air and keeps the wearer's conversations private; the heavy voice processing was planned on the paired phone. **As of 2026-11-16:** in POC (gate 2027-02-08, 84 days). 10% of POC work items are finished against 40% expected (Behind, RED). A first mock-up is printed; the voice-dampening approach reopened on 13 Nov (no thicker wall, lighter material wanted). On 16 Nov the team manager said the AI should run on the mask itself, on the new chip; Jira doesn't show this yet. Engineering waits on a spec, 15 engineering Stories have no owner, and no dampening materials are requested yet. See [[ZenaQuiet-Mask/overview]] and [[ZenaQuiet-Mask/jira/2026-11-16-jira|2026-11-16 report]].

## ZenaQuiet-Research

The Acoustic team's research work that supports the products, such as the chip choice and office acoustics. It has no stage schedule of its own. **As of 2026-11-16:** 16 open items, 6 overdue. Health RED: the ceiling speaker for the Beacon masking test isn't ordered. The chip is chosen but RS-1 still names nothing, and its purchase order only went out on 16 Nov; and no open Research item links to a product any more. See [[ZenaQuiet-Research/overview]] and [[ZenaQuiet-Research/jira/2026-11-16-jira|2026-11-16 report]].
