---
type: overview
project: ZenaQuiet-Headset
updated: 2026-11-16
---

# ZenaQuiet-Headset

## What this project is

"ZenaHeadset Quiet" is a headset for call-centre (BPO) agents who wear it for 8–12 hours a shift. It picks up the agent's voice cleanly for the Voice Lock speech pipeline, which uses the same AI voice model as the Pro, and cancels room noise at the ears with active noise cancelling (ANC). A clip-on magnetic Arc with two extra microphones is meant to limit what neighbours overhear. It is sold as a bundle with the Pro and Beacon. The Jira project is `HS`; stage windows are in [[reference#Stage schedule (per product)]].

## Where it stands

As of 2026-11-16, the Headset is in POC (proof of concept). The gate to EVT is on 2027-02-08, 84 days away, and Tết is assumed to cover its last days ([[reference#Holidays]]). 11 of 23 POC Stories are Done (47.8%, ahead of the expected 40.0%). Some of that lead comes from closed Arc Stories rather than finished work (inferred). Health is **AMBER**, unchanged. The first board boots, but its audio chip does not work yet, and the board rework has no electronics owner.

Sprint 4 (2026-11-01 → 2026-11-15) had 26 tickets: 9 were done inside the sprint dates, 9 were closed outside them, and 8 were carried into Sprint 5 (2026-11-16 → 2026-11-29). The pace line says "on pace" (3 POC Stories closed, about 2 needed per sprint), but 2 of the 3 are Arc Stories closed as out of scope (inferred). Sprint 5 has 109 tickets, and 54 of them have no owner. Pushed deadlines: 12 rows. Epic HS-1 is dated 85 days after the MP (mass production) end, and the form model HS-326 is due on the POC gate day itself.

Top issues:

1. Board tests have stalled on the hardware (HS-652, HS-648). The audio chip is not working (stand-up, 2026-11-16), and the power result is disputed: Jira says FAILED, the stand-up says done. ANC calibration waits for a crystal to be soldered (HS-2). None of this has an EE (electronics) ticket, and the test is now due 2026-11-25, 5 days later.
2. Where Voice Lock runs is undecided: on the NXP i.MX 95 headset chip or in a mobile or web app. The tech-lead meeting is this week; nothing is in Jira yet (HS-1, HS-178, HS-164).
3. The Arc re-scope has had no answer for 6 days (HS-51). The bundle-consistent look requested on 2026-11-16 is not in any ticket (HS-326, HS-330).

Latest report: [[ZenaQuiet-Headset/jira/2026-11-16-jira|2026-11-16 report]].

## Active epics

- HS-1: Layer 3, inbound voice capture for Voice Lock (TSE, target speaker extraction). To Do, due 2028-02-08 (after the MP end), owner KhuongNguyen.
- HS-2: Layer 1, outbound active noise cancelling. To Do (calibration paused for the crystal), due 2027-09-06, owner Nguyen Binh Minh.
- HS-3: power, battery and fast charging. To Do, no due date, owner Phong.ngoc.nguyen.
- HS-4: buttons, LEDs and controls. To Do, due 2027-09-06, owner Chico Ly.
- HS-6: mechanical enclosure. In Progress, due 2027-09-06.
- HS-51: Arc directional masking, re-scope proposed. In Process, due 2027-09-06, owner Nguyen Trung Tin.
- HS-142: industrial design. To Do, due 2027-02-08, which is before its own Stories end. Owner Chico Ly.
- HS-451: connectivity and ports. To Do, due 2027-09-06.
- HS-640: field test and release candidate. To Do, due 2027-02-08, which is before its own Stories end. Owner Phi Tuong.
- HS-47 is an empty placeholder Epic.

## Recent changes

- 2026-11-16 (second redo, fresh Jira pull): no Jira change since the afternoon pull; report text re-checked and carried.
- 2026-11-16 (redo with the sprint check and the 2026-11-16 stand-up):
  - Sprint 4 was closed and Sprint 5 started in Jira, with 109 tickets. The boom-mic Story HS-144 moved to Sprint 10, the last POC sprint.
  - Board test HS-652 is now due 2026-11-25 (was 2026-11-20), after its Story HS-648. The stand-up said the audio chip is not working yet.
  - New requirement from the stand-up: the Headset must look consistent with the Pro and Beacon.
  - No new comments. There is no Jira sign of the crystal being soldered, the Arc answer or the Voice Lock meeting. Report: [[ZenaQuiet-Headset/jira/2026-11-16-jira]].
- 2026-11-13: HS-144 now covers beamforming; ANC calibration paused for the crystal. Report: [[ZenaQuiet-Headset/jira/2026-11-13-jira]].
- 2026-11-12: boards arrived and Linux boots (HS-651), but the power test failed (HS-652); chip confirmed as i.MX 95 (HS-165); health RED → AMBER. Report: [[ZenaQuiet-Headset/jira/2026-11-12-jira]].
