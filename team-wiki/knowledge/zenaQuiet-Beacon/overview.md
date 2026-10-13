# ZenaQuiet-Beacon — Overview

Jira project `BC`. Stage schedule: same as ZenaQuiet-Pro2 (see [[reference#Stage schedule (per product)]]).

## What it is

A ceiling-mounted, PoE-powered coordinator for a floor cluster of ZenaQuiet Pro units. It registers and monitors the Pros, enforces voiceprint consent, relays cloud commands over MQTT and coordinates zone settings. It also carries a room microphone, a 360° LED ring and a sound masking module. (From Epics BC-50, BC-106, BC-107, BC-164 and Story BC-191.)

## Active Epics

| Epic | Feature | Owner |
| --- | --- | --- |
| BC-23 | Product Industrial Design | Chico Ly |
| BC-38 | Connectivity & Ports (hardware/PCB) | Huynh Minh Tuan |
| BC-50 | Mechanical Structure (Product Enclosure) | Nguyen Trung Tin |
| BC-106 | Connectivity between Cloud & Beacon | none |
| BC-107 | Connectivity between Pro & Beacon | none |
| BC-164 | Beacon firmware development | Nguyen Minh Thien |
| BC-165 | Field Test+RC | Nguyen Minh Thien |

## Current state (as of 2026-10-13)

In EVT (gate 2027-02-08). POC is complete (24/24 Stories). Health AMBER: no HIGH risks, but many open EVT Stories are not started or not broken down. On 2026-10-12 every Story's dates were reset to its stage window and all Epic due dates moved to 2027-11-15; field-test Stories moved to DVT. Details: [[ZenaQuiet-Beacon/jira/2026-10-13-jira|2026-10-13 report]].

## Recent changes

- 2026-10-12 to 2026-10-13: 15 EE Subtasks added under the EVT board Stories (BC-218 to BC-232).
- 2026-10-12: Jira re-plan (Story dates = stage windows; team tags removed from Story titles; firmware Stories tagged EVT-1, field test tagged DVT-1).
