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
| BC-107 | Connectivity between Pro & Beacon (all Stories Done; no open EVT work) | none |
| BC-164 | Beacon firmware development | Nguyen Minh Thien |
| BC-165 | Field Test+RC | Nguyen Minh Thien |

BC-106 "Connectivity between Cloud & Beacon" (owner: none) was listed here until 2026-10-13; it and its Stories are no longer returned by Jira (deleted or hidden, not confirmed).

## Current state (as of 2026-10-13, redone)

In EVT (gate 2027-02-08). POC is complete (21/21 Stories). EVT gate readiness 44.4% (16/36). Health AMBER: no HIGH risks, but 22 MEDIUM, mostly open EVT Stories not started or not broken down. On 2026-10-12 every Story's dates were reset to its stage window and all Epic due dates moved to 2027-11-15; field-test Stories moved to DVT. Details: [[ZenaQuiet-Beacon/jira/2026-10-13-jira|2026-10-13 report]].

## Recent changes

- 2026-10-13: Epic BC-106 (3 Done POC Stories, 10 Done Subtasks) and the 4 unowned Pro–Beacon EVT Stories BC-113, BC-114, BC-115, BC-117 disappeared from Jira; BC-233 (room-noise sensing, same title as BC-117) created under BC-164.
- 2026-10-13: Firmware release Stories BC-206, BC-207, BC-208, BC-210 started; BC-209 (production hardening) Done.
- 2026-10-12 to 2026-10-13: 15 EE Subtasks added under the EVT board Stories (BC-218 to BC-232).
- 2026-10-12: Jira re-plan (Story dates = stage windows; team tags removed from Story titles; firmware Stories tagged EVT-1, field test tagged DVT-1).
