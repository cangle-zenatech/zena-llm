# Reference

Stable reference facts: people, projects, stages and Jira conventions.

**Contents**

1. [People](#people) — owner and team contacts
2. [Projects](#projects) and [Jira projects](#jira-projects)
3. [Development stages](#development-stages-in-order) and [Stage schedule](#stage-schedule-per-product)
4. [Teams](#teams) and [Jira structure](#jira-structure)

---

## People

Everyone the wiki needs to identify: the owner, then team contacts. Match Jira names here.

### Owner

> **Cang Le** is the owner of this AI module (the team wiki and its instructions).
>
> - **Role:** Technical Manager (TM) and Software Engineer, Acoustic team, Vietnam
> - **Email:** Cang.Le@zenatech.com
> - **Jira name:** Cang Le
> - "The human", "the TM" and "the owner" in any instruction file all mean Cang Le.

### VN-Team contacts

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

#### Added 2026-10-12 — not yet confirmed

These rows were added 2026-10-12 from the Microsoft 365 company directory (job title: Industrial
Designer), not yet confirmed by the human. Found as Pro2 assignees on ID tickets (e.g. PRO2-40, PRO2-308, PRO2-400).

| Jira name                  | Microsoft Teams name | Email                          | Team              |
| -------------------------- | -------------------- | ------------------------------ | ----------------- |
| Bui Minh Tuan (Steve .Bui) | Tuan Minh Bui        | tuan.minh.bui@zenatech.com     | Industrial_Design |
| Khanh Duong                | Khanh Duong          | Khanh.Duong@zenatech.com       | Industrial_Design |
| Phan Thi Anh Nhut          | Phan Thi Anh Nhut    | Phan.Thi.Anh.Nhut@zenatech.com | Industrial_Design |
| Huynh Minh Tuan            | Huynh Minh Tuan      | Huynh.Minh.Tuan@zenatech.com   | Electronic_Electrical |
| CaoTienDat                 | Cao Tien Dat         | Cao.Tien.Dat@zenatech.com      | Electronic_Electrical |

Huynh Minh Tuan (directory: Electronics Engineer) is on HS-581 and owns BC-38. CaoTienDat (directory: Electrical
Engineer) reported BC-42 to BC-49; the Jira-to-directory name match is inferred. Team for both inferred from job title.

#### Added 2026-10-14 — not yet confirmed

Found in Jira; not found in the Microsoft 365 company directory (searched 2026-10-14). Email and team unknown.

| Jira name  | Microsoft Teams name | Email   | Team    |
| ---------- | -------------------- | ------- | ------- |
| Thang Pham | not found            | unknown | unknown |

Thang Pham is the reporter of HS-47.

#### Added 2026-10-19 — not yet confirmed

Named in `raw/threads/` and `raw/transcripts/`, not in Jira. Email from the Microsoft 365 company
directory (found by the Headset helper, 2026-10-19).

| Jira name   | Microsoft Teams name | Email               | Team / role                       |
| ----------- | -------------------- | ------------------- | --------------------------------- |
| not in Jira | Sajjad Asif          | sajjad@zenatech.com | CTO; approves purchase requests   |

---

## Projects

- [[ZenaQuiet-Pro2/overview|ZenaQuiet-Pro2]] —
  - Voice Lock — headset-free private call audio: TSE-cleaned customer speech via a
    directional speaker. Layer 1 (PRO2-2) In Progress; directional-speaker POC leading.
- [[ZenaQuiet-Beacon/overview|ZenaQuiet-Beacon]] —
  - Ceiling-mounted PoE coordinator for a floor cluster of Pro units: voiceprint consent, MQTT
    relay to the cloud, zone coordination, sound masking (Epic BC-234). Pro-to-Beacon work sits
    under BC-107 "Pro–Beacon device management & telemetry" (renamed 2026-10-14). Cluster size
    open: up to 12 Pros (BC-101, BC-107, BC-56, BC-194) vs up to 16 (BC-50). EVT.
- [[ZenaQuiet-Headset/overview|ZenaQuiet-Headset]] —
  - Call-centre (BPO) headset: voice capture for Voice Lock, hybrid ANC, magnetic Arc masking;
    USB-C and Bluetooth. POC.
- [[ZenaQuiet-Mask/overview|ZenaQuiet-Mask]] —
  - Wearable face mask that filters air and keeps the wearer's conversations private; heavy voice
    processing runs on the paired phone. POC.
- [[ZenaQuiet-Research/overview|ZenaQuiet-Research]] — Acoustic team engage in research in acoustic technologies/concepts/issues to support firmware team

## Jira projects

Wiki folder names match the Jira project (space) names.

| Jira key | Jira name / wiki folder | Note                         |
| -------- | ----------------------- | ---------------------------- |
| PRO2     | ZenaQuiet-Pro2          |                              |
| MK       | ZenaQuiet-Mask          | Confirmed in Jira 2026-10-12 |
| HS       | ZenaQuiet-Headset       | Confirmed in Jira 2026-10-12 |
| BC       | ZenaQuiet-Beacon        | Confirmed in Jira 2026-10-10 |
| RS       | ZenaQuiet-Research      | Confirmed in Jira 2026-10-12 |

---

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

---

## Purchasing lead times

Engineering raises a request in the team chat; the CTO approves; the Purchasing team passes it to
Accounting, which places the order. Purchases are not tracked in Jira. All values are **working
days** (Mon–Fri, minus `## Holidays`). A lead time quoted in a source replaces the default.

| Step                                   | Default (working days) |
| -------------------------------------- | ---------------------- |
| Approval (CTO)                         | 14                     |
| Purchasing → order placed (Accounting) | 3                      |
| Supplier delivery                      | 5                      |
| **Total, standard item**               | **22**                 |

Supplier delivery: the human gave "1 week"; 5 working days is used here.

**Order-by date** = needed-by date − total lead time (working days).
**Needed-by date** = start date of the linked Jira item; if it has none, its due date.

## Holidays

Non-working days used for lead-time maths. To confirm with HR each year. Rows without an ISO date
are not used until a date is filled in.

| Date(s)                               | Holiday                  | Applies to                      |
| ------------------------------------- | ------------------------ | ------------------------------- |
| 2027-01-01                            | New Year's Day           | Vietnam team                    |
| 2027-02-04 → 2027-02-12 (assumed; TBC) | Lunar New Year (Tết)     | Vietnam team, suppliers in Asia |
| TBC                                   | Hung Kings Commemoration | Vietnam team                    |
| 2027-04-30                            | Reunification Day        | Vietnam team                    |
| 2027-05-01                            | Labour Day               | Vietnam team                    |
| 2027-09-02 (+1 day TBC)               | National Day             | Vietnam team                    |

Tết falls on the shared 2027-02-08 gate. The 2027-02-04 → 2027-02-12 range is an assumption until
the official dates are set.

## Sourcing rules

- No components from China (CTO). Open question: does Hong Kong count?
  (`threads/2026-10-19-purchase.md · REQUEST 3`)

---

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
