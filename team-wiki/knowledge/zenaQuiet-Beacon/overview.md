# ZenaQuiet-Beacon — Overview

Jira project `BC`. Stage schedule: same as ZenaQuiet-Pro2 (see [[reference#Stage schedule (per product)]]).

## What it is

A ceiling-mounted, PoE-powered coordinator for a floor cluster of ZenaQuiet Pro units. It registers and monitors the Pros, enforces voiceprint consent, relays cloud commands over MQTT and coordinates zone settings. It also carries a room microphone, a 360° LED ring and a sound masking module, and uses the microphone to tell Pros how to adjust audio to room noise. (From Epics BC-50, BC-107, BC-164 and Stories BC-191, BC-233. Earlier versions also cited Epic BC-106, which is no longer in Jira since 2026-10-13.)

## Active Epics

| Epic | Feature | Owner |
| --- | --- | --- |
| BC-23 | Product Industrial Design | Chico Ly |
| BC-38 | Connectivity & Ports (hardware/PCB) | Huynh Minh Tuan |
| BC-50 | Mechanical Structure (Product Enclosure) | Nguyen Trung Tin |
| BC-107 | Pro–Beacon device management & telemetry (renamed 2026-10-14 from "Connectivity between Pro & Beacon"; up to 16 Pros since 2026-10-15; all Stories Done; no open EVT work) | Nguyen Minh Thien (since 2026-10-14; was none) |
| BC-164 | Beacon firmware development | Nguyen Minh Thien |
| BC-165 | Field Test+RC | Nguyen Minh Thien |
| BC-234 | Sound Masketing (sic) — new 2026-10-15, no Stories yet; linked to Research RS-16 | Huỳnh Thái Hòa |

BC-106 "Connectivity between Cloud & Beacon" (owner: none) was listed here until 2026-10-13; it and its Stories are no longer returned by Jira (deleted or hidden, not confirmed).

## Current state (as of 2026-10-19)

In EVT (gate 2027-02-08, 112 days). POC is complete (21/21 Stories, 26/26 Subtasks). EVT gate readiness 47.2% (17/36). Health RED (report redone the afternoon of 2026-10-19; AMBER in the morning version): ID Subtask BC-141 was re-dated to 2027-02-08 → 2027-09-06 ("based on the DVT phase") but still sits under EVT Story BC-153, so it counts as a HIGH risk on the EVT gate; most likely a filing issue (inferred). Other concerns: Beacon sound masking was promised for 2026-10-19 and for the Sajjad Asif visit (29–30 Oct or 2 Nov) but has no board with mic and speaker and no Stories under BC-234; mechanical work sits with one engineer (39 open items, ME peak 27 Subtasks in Nov-26) who also agreed to support the Pro; the Beacon's future and the EVT spec sign-off are not tracked in Jira. 31 MEDIUM risks (24 Jira, 7 from meetings). Cluster size in Jira: BC-50, BC-107, BC-194 say 16 Pros; BC-56, BC-101 say 12. Details: [[ZenaQuiet-Beacon/jira/2026-10-19-jira|2026-10-19 report]] (earlier: [[ZenaQuiet-Beacon/jira/2026-10-15-jira|2026-10-15 report]]).

## Recent changes

- 2026-10-19 (afternoon): BC-141 re-dated into the DVT window under EVT Story BC-153 (HIGH, health RED); BC-154 Done; start dates added to BC-172, BC-175 to BC-177, BC-229; BC-233 dated 2026-10-19 → 2026-11-30.
- 2026-10-19: 13 new ME Subtasks (BC-236 to BC-248: material validation, ceiling fixture, PoE+ thermal) and ID Subtask BC-235 (design spec, CMF, BOM). BC-153 Design Refinement started; BC-142, BC-166, BC-207 Done. EE Subtasks BC-218 to BC-226 dated, four assigned. BC-128 (Done POC Subtask) no longer in Jira. BC-107 and BC-194 changed "up to 12" → "up to 16" Pros.

- 2026-10-15: New Epic BC-234 "Sound Masketing" (owner Huỳnh Thái Hòa, no Stories), linked to Research RS-16. ID Subtask BC-142 started. EE layouts BC-220, BC-223, BC-226 got due 2026-10-30 (still unassigned).
- 2026-10-14: Epic BC-107 renamed "Pro–Beacon device management & telemetry" and assigned to Nguyen Minh Thien; firmware Epic BC-164 moved to In Progress; EE power layout BC-229 due moved 2026-10-16 → 2026-10-21.
- 2026-10-13: Epic BC-106 (3 Done POC Stories, 10 Done Subtasks) and the 4 unowned Pro–Beacon EVT Stories BC-113, BC-114, BC-115, BC-117 disappeared from Jira; BC-233 (room-noise sensing, same title as BC-117) created under BC-164.
- 2026-10-13: Firmware release Stories BC-206, BC-207, BC-208, BC-210 started; BC-209 (production hardening) Done.
- 2026-10-12 to 2026-10-13: 15 EE Subtasks added under the EVT board Stories (BC-218 to BC-232).
- 2026-10-12: Jira re-plan (Story dates = stage windows; team tags removed from Story titles; firmware Stories tagged EVT-1, field test tagged DVT-1).
