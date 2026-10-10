### Owner

> **Cang Le** is the owner of this AI module (the team wiki and its instructions).
>
> - **Role:** Technical Manager (TM) and Software Engineer, Acoustic team, Vietnam
> - **Email:** Cang.Le@zenatech.com
> - **Jira name:** Cang Le
> - "The human", "the TM" and "the owner" in any instruction file all mean Cang Le.

## VN-Team contacts

Confirmed by the human, 2026-10-08. "Jira name" is the name on Jira tickets; "Microsoft Teams name" is
the name in Outlook / Teams. Team names match `## Teams`.

| Jira name         | Microsoft Teams name | Email                           | Team                  |
| ----------------- | -------------------- | ------------------------------- | --------------------- |
| KhuongNguyen      | Khuong Dinh Nguyen   | khuong.dinh.nguyen@zenatech.com | Firmware              |
| Nguyen Minh Thien | Thien Minh Nguyen    | thien.minh.nguyen@zenatech.com  | Firmware              |
| Phi Tuong         | Tuong Phi Lau        | tuong.phi.lau@zenatech.com      | Firmware              |
| Huỳnh Thái Hòa    | Hoa Huynh            | Hoa.Huynh@zenatech.com          | Acoustic              |
| Nguyen Binh Minh  | Minh Nguyen          | Minh.Nguyen@zenatech.com        | Acoustic              |
| Elly Nhi Nguyen   | Elly Nguyen          | Elly.Nguyen@zenatech.com        | Industrial_Design     |
| Chico Ly          | Chi Co Ly            | chi.co.ly@zenatech.com          | Industrial_Design     |
| Phong.ngoc.nguyen | Phong Ngoc Nguyen    | Phong.Ngoc.Nguyen@zenatech.com  | Electronic_Electrical |
| Nguyen Manh Tuan  | Tuan Manh Nguyen     | tuan.manh.nguyen@zenatech.com   | Electronic_Electrical |
| Hung Pham Nguyen  | Pham Nguyen Ngoc     | Hung.Pham.Nguyen@zenatech.com   | Electronic_Electrical |
| Nguyen Trung Tin  | Tin Trung Nguyen     | TinTrung.Nguyen@zenatech.com    | Mechanical            |
| Duy Nguyen        | Duy Cong Nguyen      | DuyCong.Nguyen@zenatech.com     | Mechanical            |

## Projects

- [[ZenaQuiet-Pro2/overview|ZenaQuiet-Pro2]] —
  - Voice Lock — headset-free private call audio: TSE-cleaned customer speech via a
    directional speaker. Layer 1 (PRO2-2) In Progress; directional-speaker POC leading.
- [[ZenaQuiet-Beacon/overview|ZenaQuiet-Beacon]] —
- [[ZenaQuiet-Headset/overview|ZenaQuiet-Headset]] —
- [[ZenaQuiet-Mask/overview|ZenaQuiet-Mask]] —
- [[ZenaQuiet-Research/overview|ZenaQuiet-Research]] — Acoustic team engage in research in acoustic technologies/concepts/issues to support firmware team

## Jira projects

Wiki folder names match the Jira project (space) names.

| Jira key | Jira name / wiki folder | Note                          |
| -------- | ----------------------- | ----------------------------- |
| PRO2     | ZenaQuiet-Pro2          |                               |
| unknown  | ZenaQuiet-Mask          | Key not confirmed in Jira yet |
| unknown  | ZenaQuiet-Headset       | Key not confirmed in Jira yet |
| BC       | ZenaQuiet-Beacon        | Confirmed in Jira 2026-10-10  |
| unknown  | ZenaQuiet-Research      | Key not confirmed in Jira yet |

## Development stages (in order)

POC → EVT → DVT → PVT → MP. A stage may be numbered, e.g. EVT-1, DVT-2.

| Stage | Meaning                                                  |
| ----- | -------------------------------------------------------- |
| POC   | Proof of concept: show the idea can work                 |
| EVT   | Engineering validation test: does the design meet specs? |
| DVT   | Design validation test: is the final design ready?       |
| PVT   | Production validation test: can the factory build it?    |
| MP    | Mass production                                          |

## Stage schedule (per product)

Each window is `start → end`. A stage's end date is the next stage's start date.

| Stage | ZenaQuiet-Pro2 (PRO2)   | ZenaQuiet-Mask          | ZenaQuiet-Headset       | ZenaQuiet-Beacon        |
| ----- | ----------------------- | ----------------------- | ----------------------- | ----------------------- |
| POC   | 2026-06-29 → 2026-09-21 | 2026-09-21 → 2027-02-08 | 2026-09-21 → 2027-02-08 | 2026-06-29 → 2026-09-21 |
| EVT   | 2026-09-21 → 2027-02-08 | 2027-02-08 → 2027-05-24 | 2027-02-08 → 2027-05-24 | 2026-09-21 → 2027-02-08 |
| DVT   | 2027-02-08 → 2027-09-06 | 2027-05-24 → 2027-09-06 | 2027-05-24 → 2027-09-06 | 2027-02-08 → 2027-09-06 |
| PVT   | 2027-09-06 → 2027-10-18 | 2027-09-06 → 2027-10-18 | 2027-09-06 → 2027-10-18 | 2027-09-06 → 2027-10-18 |
| MP    | 2027-10-18 → 2027-11-15 | 2027-10-18 → 2027-11-15 | 2027-10-18 → 2027-11-15 | 2027-10-18 → 2027-11-15 |

Headset uses the same schedule as Mask; Beacon uses the same schedule as Pro2. ZenaQuiet-Research has
no stage schedule. All four products are in PVT/MP together from Sep to Nov 2027.

## Teams

Each Subtask names its team twice: the code as a title prefix (e.g. `[ME] …`) and the team name as a
Jira label (e.g. `Mechanical`). Checked on [PRO2-252](https://epazz.atlassian.net/browse/PRO2-252).

| Code | Team (Jira label)     |
| ---- | --------------------- |
| FW   | Firmware              |
| ME   | Mechanical            |
| EE   | Electronic_Electrical |
| SW   | Software              |
| ID   | Industrial_Design     |
| AC   | Acoustic              |
| FA   | Factory               |

## Jira structure

| Level   | Meaning                                                      | Naming rule                                                          | Date rule                                              |
| ------- | ------------------------------------------------------------ | -------------------------------------------------------------------- | ------------------------------------------------------ |
| Epic    | A major product feature. All Epics done = product delivered. | Free text                                                            | Has start and due date                                 |
| Story   | Work needed to complete the Epic in one stage                | Starts with `[POC]`, `[EVT]`, `[DVT]`, `[PVT]` or `[MP]`             | Must fall within its Epic's dates AND its stage window |
| Subtask | A small task owned by one discipline                         | Starts with `[FW]`, `[ME]`, `[EE]`, `[SW]`, `[ID]`, `[AC]` or `[FA]` | Must fall within its Story's dates                     |

Examples: PRO2-250 "[POC] Adjustable emitting sound angle" → Story, POC stage.
PRO2-252 "[ME] Select POC material for the Directional Speaker Panel" → Subtask, ME team.
