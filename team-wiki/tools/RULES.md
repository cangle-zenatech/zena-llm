# Rule reference — what `wiki_jira.py` computes

The weekly-report rules, in one place. `tools/wiki_jira.py` applies them; the AI does not.

**When to read this file:** only to explain a rule in a report, to check a result that looks wrong,
or before changing the script. A weekly run does not need it.

**Changing a rule:** change it here and in `wiki_jira.py` together, only when the human agrees, and
log it in `knowledge/log.md`. If the two ever disagree, the script is what ran: flag the difference
in chat.

Settings (`today`, `lookahead_days`, `stale_days`, `overload_factor`, `report_max_rows`,
`product_keys`) come from the yaml block in each project's `INDEX.md`. Stage windows, teams, people,
lead times and holidays come from `knowledge/reference.md`.

---

## Products (Pro2, Beacon, Mask, Headset)

### Normalize

- `stage` = the bracket prefix of a Story title (case-insensitive, ignore spaces). Subtasks inherit
  the stage of their parent Story. Missing prefix on a Story → `UNKNOWN` (Data Hygiene row).
- `team` (Subtask) = the assignee's team from `reference.md` → `## People` (Team column, mapped to the
  codes in `## Teams`). The title bracket is ignored for Subtasks. No assignee → `Unassigned`;
  assignee not in `## People` → `UNKNOWN`. A Story's team set is the set of its Subtasks' teams.
- `state` = Done | In Progress | To Do, from statusCategory, never from the status name.
- Tree Epic → Story → Subtask; orphans are logged.

### Current position

`current_stage` = the stage whose window contains `today` (boundary dates are inclusive of the end
date; on a shared boundary the earlier stage wins). `next_gate` = the end of the current stage.
`days_to_gate` = next_gate − today. Dates are calendar days.

### Date checks (issues not Done)

| Rule                          | Condition                                          |
| ----------------------------- | -------------------------------------------------- |
| D1 Story outside Epic         | story.start < epic.start OR story.due > epic.due   |
| D2 Subtask outside Story      | sub.start < story.start OR sub.due > story.due     |
| D3 Story outside stage window | story.start < stage.start OR story.due > stage.end |
| D4 Inverted dates             | start > due                                        |
| D5 Missing dates              | start or due is empty                              |
| D6 Epic beyond MP             | epic.due > the product's MP end                    |

### Risks (issues not Done)

| ID  | Risk                  | Condition                                                                                                     |
| --- | --------------------- | ------------------------------------------------------------------------------------------------------------- |
| R1  | Overdue               | due < today                                                                                                   |
| R2  | Late start            | start < today AND state = To Do                                                                               |
| R3  | Due soon, not started | today ≤ due ≤ today + lookahead_days AND state = To Do                                                        |
| R4  | Stale                 | today − updated ≥ stale_days                                                                                  |
| R5  | Stage carryover       | Story's stage window has ended AND Story not Done                                                             |
| R6  | Overrun               | child.due > parent.due (Story vs. Epic and Subtask vs. Story)                                                 |
| R7  | Blocked               | has an "is blocked by" link to an issue that is not Done                                                      |
| R8  | Blocking              | has a "blocks" link to an open issue                                                                          |
| R9  | Unassigned            | no assignee AND (In Progress OR due within 30 days)                                                           |
| R10 | Long-lead gap         | Story in the current or next stage with no ME, EE or FA Subtask started, when its stage starts within 45 days |

**Severity** (highest wins; all rule IDs are listed)

- **HIGH**: R1 > 7 days late; R5; R7 or R8 on an item due before the next gate; R6 that pushes the
  Epic past its due date or past a stage end.
- **MEDIUM**: R1 ≤ 7 days; R2; R3; R10; R6 inside the parent's buffer.
- **LOW**: R4 or R9 alone; date-hygiene-only findings.

**Impact sentence** (script's first version, HIGH and MEDIUM): walks up Subtask → Story → Epic →
stage gate: what is late or blocked, which Story and Epic it holds up, whether it threatens the next
gate and by about how many days (the max of the slip and the overrun), which other teams wait on it
(links, sibling Subtasks).

### Source risks (from `WORK/sources.json`; working days, `reference.md` lead times and holidays)

| ID  | Risk                      | Condition                                                                                       |
| --- | ------------------------- | ----------------------------------------------------------------------------------------------- |
| P1  | Arrives after it's needed | forecast arrival > needed-by date of the linked Jira item                                       |
| P2  | Approval overdue          | waiting for approval longer than 14 working days                                                |
| P3  | Blocked by a decision     | an open question stops the order (e.g. sourcing rule unclear)                                   |
| P4  | Long-lead item            | total lead time > 20 working days and order-by date is within 10 working days or already passed |
| P5  | Can't trace               | no linked Jira item                                                                             |
| S1  | Blocker from sources      | a thread or transcript names a blocker or open decision with no matching Jira ticket            |

Severity: **HIGH** for P1 arriving after the linked item's stage end or after PVT start, and for
P1 + P3; **MEDIUM** for other P1, P2, P3, P4, S1; **LOW** for P5 alone. Source risks count toward
health like Jira risks.

### Metrics

| Metric                        | Formula                                                                                                 |
| ----------------------------- | ------------------------------------------------------------------------------------------------------- |
| Story completion %            | Done Stories / total Stories                                                                            |
| Subtask completion %          | Done Subtasks / total Subtasks                                                                          |
| Gate readiness %              | Done Stories of current stage / all Stories of current stage                                            |
| Next-stage readiness %        | Stories of next stage that are In Progress or Done / all Stories of next stage                          |
| Overdue count / avg days late | from R1                                                                                                 |
| Due-soon-not-started          | from R3                                                                                                 |
| Stale count                   | from R4                                                                                                 |
| Carryover count               | from R5                                                                                                 |
| Schedule variance (Epic)      | max(child due dates) − Epic due, in days (+ = over)                                                     |
| Scope added after stage start | Stories with created > their stage start                                                                |
| Expected vs. actual progress  | expected % = elapsed share of the stage window; flag if actual Story completion % < expected % − 15 pts |

Done issues are left out of risk checks but counted in completion metrics.

**Team load:** for each team and calendar month from the current month to MP end, the open Subtasks
whose [start, due] overlaps that month; open Subtasks with no assignee go in an "Unassigned" row.
Cells above `overload_factor` × the team's monthly average are marked ⚠. Watch AC and FA during
PVT/MP.

### Health

- **RED**: any HIGH risk on the current gate, OR gate readiness behind expected progress by > 25 pts,
  OR days_to_gate < 21 and gate readiness < 80%.
- **AMBER**: any HIGH risk, OR more than 3 MEDIUM, OR behind expected progress by 15–25 pts.
- **GREEN**: otherwise.

The report uses `health_with_sources` (the same rules with source risks added).

---

## Research (support project; "Research mode")

Used when a project has no stage schedule and `product_keys` in its yaml.

### Which product an item supports

| Order | Evidence                                                                                          | Mark as    |
| ----- | ------------------------------------------------------------------------------------------------- | ---------- |
| 1     | A Jira issue link (any type) to a ticket in `product_keys`, on the item or any parent              | linked     |
| 2     | A product name as a whole word in the title of the item or any parent ("Mask" ≠ "masking")         | (inferred) |
| 3     | Neither                                                                                           | Unlinked   |

- Only a link gives a **needed-by** date: the due date of the linked product ticket (earliest, if
  several). A title match gives the product, never a date.
- Linked product tickets come from `WORK/linked/` (kept in the snapshot), else the newest product
  snapshots (FALLBACK line).
- `maturity` = the bracket prefix of a Story title (`[POC]` …): how far the research has got, not a
  product stage. Missing → `none`, not an error.
- `team` = the team label, else the title prefix, else `UNKNOWN`.

### Date checks and risks (issues not Done)

| Rule | Condition |
| --- | --- |
| D1, D2, D4, D5 | as for products |
| D7 Late for the product | due > needed_by (linked items only) |
| R1–R4, R6, R7, R9 | as for products (R5, R8, R10 do not apply) |
| R11 Late for the product | D7, or needed_by < today |
| R12 Product at risk | a linked product ticket is due within `lookahead_days` |
| R13 Unlinked | product = Unlinked (Epics and Stories) |

**Severity**

- **HIGH**: R11 or R12 where the linked product ticket sits before that product's next gate (the end
  of its current stage in `reference.md` → `## Stage schedule`); R1 > 7 days late on a linked item.
- **MEDIUM**: R1 ≤ 7 days; R1 > 7 days on an inferred or Unlinked item; R2; R3; R7; R11/R12 not
  before a gate.
- **LOW**: R4, R6, R9, R13 alone; date-hygiene-only findings.

**Source risks:** P1–P5 and S1 as for products, but "needed by" is the due date of the product
ticket the RS item supports. HIGH for P1 when that product ticket sits before its product's next
gate, or P1 + P3; MEDIUM for other P1, P2, P3, P4, S1; LOW for P5 alone.

### Metrics and health

| Metric | Formula |
| --- | --- |
| Completion % | Done Stories / all Stories, overall and per Epic |
| Items per product | open Epics and Stories per product (linked / inferred), plus Unlinked |
| Link coverage % | linked open Epics and Stories / all open Epics and Stories |
| Earliest needed-by | per product, the earliest needed-by among open linked items |
| Overdue / due soon / stale | from R1, R3, R4 |

**Team load:** open items of every type per team per month, from the current month to the last due
date; ⚠ above `overload_factor` × the team's average.

**Health:** RED if any HIGH; AMBER if more than 3 MEDIUM or link coverage below 50%; else GREEN.

---

## What `report` puts in the page

- Risk Register: all HIGH, then the MEDIUM with the most days late, up to `report_max_rows`
  (default 30); Jira and source risks together, sorted by severity then days late.
- Data Hygiene / Clean-up List: counts per rule and the first 20 rows.
- The report has no Team Load section (removed by the human on 2026-11-12); team load is still
  computed (`heatmap.md` in WORK) but not shown.
- Section 4b "People and tickets": one workload table, one row per assignee: open (not Done) tickets
  by type — Epic, Story/Task (Story, Task and any other type), Subtask — total, Overdue (due before
  today) and Due ≤14d (due within `lookahead_days`); sorted by tickets assigned. ⚠ = more than 40 open
  tickets. Reported tickets are not in the table (creating a ticket is not workload); they are listed
  with the assigned ones in Appendix D.
- Roll-up section 6: 6.1 shared deadlines (`rollup_shared.md`), 6.2 who carries the work — one column
  per project, total, Overdue, Due ≤14d; ⚠ = works on 3+ projects or holds more than 40 open tickets
  (`rollup_people.md`), 6.3 work with no owner by project and type (`rollup_unowned.md`), 6.4 Research
  items overdue or due within `lookahead_days`, with the product they link to (`rollup_support.md`).
  Ticket lists per person across projects go in the roll-up's Appendix (`rollup_people_lists.md`).
- Appendix at the end of the same page: A. the remaining risk rows, B. the remaining hygiene rows,
  C. notes worth a look, D. tickets by person (one heading and one table per person: project, role, type, linked keys, and for assigned rows the overdue tickets with due date and days late; the heading shows the overdue count). The roll-up Appendix uses the same table. Every row appears exactly once. Snapshot changes are not listed (only the
  one-line count under "Since last report"; the full list stays in `WORK/diff.md`).

---

## Sprint review (Executive Summary "Last sprint" block)

- **Sprints are chosen by date, not by Jira's sprint state** (the team doesn't start or close sprints
  in Jira). Current sprint = the sprint whose start–end dates include the run date (latest start if
  two overlap). Last sprint = the sprint with the latest end date before the run date. Sprints whose
  state doesn't match their dates are listed in a one-line note.
- **In the sprint** = tickets whose Sprint field contains that sprint now (Jira doesn't say when a
  ticket was added, so this is not "planned at the start").
- Per person (assignee), **Stories and Subtasks counted separately**: done inside the sprint dates
  (Done, resolved between start and end), closed outside the sprint dates (Done, resolved before or
  after), still open, carried into the current sprint (open and also in the current sprint), overdue
  (open, due before the run date), open 2+ sprints (open and in two or more sprints that have ended).
- **Pace (products only):** Stories of the current stage resolved during the last sprint's dates
  (whatever their sprint) vs needed per sprint = open Stories of the current stage ÷ sprints left
  before the gate (days to gate ÷ sprint length, rounded up). "On pace" if closed ≥ needed, else
  "behind the pace needed for the gate".
- Appendix E lists each person's last-sprint tickets with titles. Applied to every product and
  Research (no pace line); not part of the portfolio roll-up.

