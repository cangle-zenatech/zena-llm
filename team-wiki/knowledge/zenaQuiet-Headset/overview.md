# ZenaQuiet-Headset — Overview

**What it is:** "ZenaHeadset Quiet", a call-centre (BPO) headset worn 8–12 hours a shift. It captures the agent's voice for the Voice Lock speech pipeline, cancels room noise with hybrid ANC, uses a clip-on magnetic Arc to reduce what neighbours overhear, and connects over USB-C and Bluetooth to Zoo Meet and the ZenaAI cloud. Jira project `HS`. Stage windows: [[reference#Stage schedule (per product)]].

**Current state (2026-10-19):** POC stage, gate to EVT on 2027-02-08 (112 days). 5 of 24 POC Stories Done (20.8%, vs 20.0% expected), health **RED** with source risks (AMBER on Jira alone: 9 HIGH Epic-date risks, none on the POC gate; 20 MEDIUM). The RED comes from the Headset PCB order (~$600, approved 2026-10-15, paid): the wrong board option was paid for, and the supplier stopped until about $35 extra is paid. If paid now, the boards arrive about 2026-11-09, 35 working days after the POC board work was due to start (HS-144), and after the CTO visit (2026-10-29/30 or 2026-11-02). Open decisions from meetings: Headset processor/ANC chip (Jira says NXP i.MX 95; Firmware proposes an XMOS chip, review 2026-10-20) and Arc scope. EE Headset tickets are not in Jira yet. Mechanical (Nguyen Trung Tin) drives almost all active work and agreed on 2026-10-19 to also support the Pro desk version; the acoustic, connectivity and Zoo Meet Epics have no owner; 484 open tickets have no assignee.

**Active Epics:** HS-1 (mic capture), HS-2 (ANC), HS-3 (power and charging), HS-4 (UI), HS-6 (mechanical enclosure, In Progress), HS-51 (Arc masking), HS-142 (industrial design), HS-380 (Zoo Meet and cloud denoise), HS-451 (connectivity and ports), HS-640 (field test and release candidate). HS-47 is an empty placeholder Epic.

**Recent changes:**

- 2026-10-19 (redone in the afternoon): first report that also reads purchase threads and meeting transcripts, now with a plain-sentence risk table (1 HIGH, 5 MEDIUM source risks; health RED). Jira: HS-86 started (In Process), 10 POC tickets moved to "[POC] Sprint 3"; later in the day 5 ME Subtasks closed (HS-156, HS-247, HS-297, HS-301, HS-585), HS-580 and three Subtasks moved to In Testing, HS-302 assigned to Phong.ngoc.nguyen. Report: [[ZenaQuiet-Headset/jira/2026-10-19-jira]].

- 2026-10-15: no Jira changes since 2026-10-13 (also none on 2026-10-14). Epics HS-47 and HS-142 now stale (no update for 14 days). ME tasks HS-129 (due 2026-10-19) and HS-335 (due 2026-10-27) wait on unowned EE envelope tasks HS-130, HS-131, HS-336, HS-337. Reports: [[ZenaQuiet-Headset/jira/2026-10-15-jira]], [[ZenaQuiet-Headset/jira/2026-10-14-jira]].

- 2026-10-13: 10 ME Subtasks Done (USB-C recess, BT antenna, fold hinge); HS-326 overdue cleared by moving its due date to 2027-02-08; HS-641 to HS-647 moved to DVT; HS-142 and HS-640 now end before their own Stories. Report: [[ZenaQuiet-Headset/jira/2026-10-13-jira]].
- 2026-10-12: first weekly report. Report: [[ZenaQuiet-Headset/jira/2026-10-12-jira]].
