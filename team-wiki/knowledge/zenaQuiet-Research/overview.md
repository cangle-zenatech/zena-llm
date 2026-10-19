# ZenaQuiet-Research — Overview

**What it is:** the Acoustic team's research project (Jira key `RS`). It researches technologies and problems for the products Pro2, Beacon, Headset and Mask. It has no development stages of its own; it is measured against the product work it supports. See [[ZenaQuiet-Research/INDEX|instructions]] and [[reference#Jira projects]].

**Current state (as of 2026-10-19, from [[ZenaQuiet-Research/jira/2026-10-19-jira|the weekly report]]):** 20 items, 19 open (10 Epics, 9 Stories); 1 Done (RS-3). Health AMBER. Only one Research item is linked to a product ticket (RS-16 → Beacon Epic BC-234, 5% coverage). Four Office Acoustics Stories are past their start date and not started. The chip decision moved from 2026-10-16 to 2026-10-20 (RS-1), with a presentation planned that day. Threads and meetings add 5 source risks: chip choice, Beacon masking demo hardware, masking speaker placement, the drone experiment and untracked Mask material research.

## Active Epics

- **RS-1 Chip eval + decision** (In Progress, due 2026-10-20, moved from 2026-10-16): which chip can run the TSE voice-isolation model for the Headset and Mask. The i.MX95 NPU was evaluated (RS-2, due 2026-10-19); an XMOS chip is to be proposed on 2026-10-20.
- **RS-4 Ultrasonic loudspeaker survey** (In Progress, due 2026-10-23; component survey RS-3 Done 2026-10-19), with **RS-14 Ultrasonic array** (phased-array steering test, RS-19, 2026-10-26 → 2026-11-30). Overlaps the Pro's approved transducer purchase.
- **RS-11 Layer 2: Office Acoustics** (To Do, 2026-09-21 → 2027-02-08): a mix of sound masking, absorbing materials, screens/layout and headset noise cancelling, replacing room-scale noise cancelling. Includes the Beacon sound-masking prototype (RS-16, In Progress, due 2026-10-30), linked to Beacon Epic BC-234, and absorbing materials (RS-21, In Progress since 2026-10-19). Priorities set 2026-10-19: RS-16, then headset ANC (RS-22), then materials (RS-21).
- **RS-15 Qt multi-unit app** (2027-01-01 → 2027-03-31).
- **RS-8 Headset mic beamforming** (To Do, dated 2026-10-19: 2026-09-21 → 2027-02-08; still empty, start date passed).
- Empty, undated Epics: RS-7 Drone propeller ANC (a point-source experiment is under way per the purchase thread, inferred link), RS-9 Android mobile app, RS-10 Sound masking impl, RS-20 TSE module for sound masking (Firmware).

## Recent changes

- 2026-10-19 (afternoon redo): RS-8 got dates 2026-09-21 → 2027-02-08 (late start, MEDIUM); report now has a plain-sentence table of thread/meeting risks.
- 2026-10-19: RS-3 Done; RS-21 In Progress; RS-1 due → 2026-10-20, RS-2 due → 2026-10-19. First report with source risks from threads and transcripts.
- 2026-10-15: first product link: RS-16 "connects to" BC-234 (Beacon).
- 2026-10-14: no Jira changes since 2026-10-13.
- 2026-10-13: no Jira changes since 2026-10-12.
- 2026-10-12: first weekly report.
