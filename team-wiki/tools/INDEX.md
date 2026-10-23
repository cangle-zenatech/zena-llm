# tools/ — Instructions

Shared scripts for the weekly status reports. Agents run them; they don't rewrite them each week.
Change a script only when the human agrees, and log the change in `knowledge/log.md`.

## wiki_jira.py

Implements Steps 3–7 of a project's `INDEX.md` (normalize, D1–D6, R1–R10, severity, metrics, team
load, health). It reads its settings from the wiki, so there is nothing to edit per project:

- stage windows, team codes, people and emails → `knowledge/reference.md`
- `today`, `lookahead_days`, `stale_days`, `overload_factor` → the yaml block in `knowledge/<project>/INDEX.md`

It never calls Jira and never writes wiki pages.

### Weekly run, per project

Paths below are bash paths; `WORK` is a temporary folder (e.g. `outputs/work-<key>/`).

1. Pull Jira (Steps 1–2 of the project `INDEX.md`). Save each raw search result page as a `.json`
   file in `WORK`, unchanged.
2. `python3 -I tools/wiki_jira.py normalize --project <Folder> --raw-dir WORK [--start-field ID --sprint-field ID]`
   → writes `WORK/issues_full.json` (with descriptions, for Step 8) and the snapshot
   `data/<Folder>/<date>.json`. Check that its issue count equals the JQL total.
3. `python3 -I tools/wiki_jira.py analyze --project <Folder> --work WORK`
   → `summary.txt`, `results.json`, and ready-made tables: `register.md`, `hygiene.md`,
   `heatmap.md`, `epics.md`, `stages.md`, plus `notes.md` (worth a look, not rule hits).
4. `python3 -I tools/wiki_jira.py diff --project <Folder> --work WORK`
   → `diff.md`: issues added or removed; status, date, title and assignee changes; issue links
   added or removed (each link once, including links to other projects) since the last snapshot.
5. Write the report from these outputs. The agent still writes the Executive Summary, Product
   Detail (Step 8), impact sentences that need judgment, and Recommendations.

### Limits

- ZenaQuiet-Research has no stage schedule; stage checks are skipped. Its extra rules (D7, R11–R13
  in its `INDEX.md`) are not in the script yet: apply them by hand. Its team load is in the
  script: open items of every type, team from the Jira label (else title prefix), current month →
  last due date.
- `diff` reports added/removed issues; status, date, title and assignee changes; and added/removed
  issue links.
- Subtask team = the assignee's team from `reference.md` → `## People` (since 2026-10-19). No
  assignee → `Unassigned` (one Data Hygiene row per Story); assignee not in `## People` → `UNKNOWN`
  (one Data Hygiene row per Subtask). The title bracket is ignored for Subtasks.
- If a project's `INDEX.md` changes a rule, the script does not know. Flag the difference in chat.
- Field IDs default to `customfield_10015` (Start date) and `customfield_10020` (Sprint). Pass
  others if Step 1 finds different ones.

### sources (per project, after analyze)

`python3 -I tools/wiki_jira.py sources --project <Folder> --work WORK [--date D]`

Reads `WORK/sources.json` (written by the helper in Step 2b from `raw/threads/` and
`raw/transcripts/`), the project snapshot, `WORK/results.json` from `analyze`, and `reference.md` →
`## Purchasing lead times`, `## Holidays`, `## Stage schedule`. Writes `sources_register.md` (P1–P5,
S1 with severity), `order_this_week.md` and `sources_summary.txt`, and adds `source_risks` and
`health_with_sources` to `results.json`. Working days = Mon–Fri minus the dated rows in
`## Holidays`. Use `health_with_sources` as the report's health rating.

`sources.json` is a list, one entry per item:

```json
{
  "ref": "threads/2026-10-19-purchase.md · REQUEST 4",
  "kind": "purchase",
  "item": "Sugatsune hinge samples",
  "requester": "Duy Cong Nguyen",
  "status": "approved",
  "dates": {"requested": null, "approved": null, "ordered": null, "delivered": null},
  "quoted_lead": {"min": 5, "max": 7, "unit": "weeks", "from": "payment"},
  "needed_for": "PRO2-420",
  "needed_for_inferred": true,
  "open_question": null,
  "impact": "Hinge bench test (PRO2-420)",
  "root_cause_step": "supplier lead time",
  "root_cause": "Quoted 5–7 weeks after payment, plus Purchasing",
  "fix": "Move the test date or find samples that ship faster"
}
```

- `kind`: `purchase`, or `blocker` / `decision` for other source items (rule S1).
- `status`: `waiting approval`, `approved`, `ordered` or `delivered`.
- `dates`: ISO dates only when the source states them; otherwise `null` (the script counts from
  today and says so).
- `quoted_lead.unit`: `working_days`, `weeks` (× 5 working days) or `days` (calendar). Omit or set
  `null` to use the default supplier lead time.
- `needed_for`: the Jira key that waits on the item, or `null` (→ P5). Set `needed_for_inferred`
  when the link comes from a title match, not the source.
- `impact`, `root_cause_step` (`waiting approval` · `purchasing` · `supplier lead time` ·
  `open decision` · `not requested` · `capacity` · `other`), `root_cause`, `fix`: plain words for
  the sentence table.

Extra output `sources_plain.md`: one row per item, highest impact first:
`| Level | What's at risk | Root cause | What would fix it | Source |`. "What's at risk" = impact +
delay sentence, e.g. "Hinge bench test (PRO2-420) starts 16–26 working days late: planned
2026-11-02, arrives 2026-11-24 → 2026-12-08." Delay = working days from the needed-by date to the
forecast arrival; "delay unknown" with the reason when either date is missing. Requests waiting
for approval also show how long they've waited. `sources_register.md` (with rule codes) is
unchanged.

### Portfolio roll-up (main session, after all helpers)

`python3 -I tools/wiki_jira.py rollup --work WORK [--date D]`

Reads the newest snapshot (on or before D) of every active project that has a stage schedule, plus
the stage schedule in `reference.md` (the plan slip is measured against) and the settings in the yaml block of `knowledge/portfolio/INDEX.md`. It re-runs
`analyze` per product into `WORK/<project>/` and writes `rollup_summary.txt`, `rollup.json`,
`rollup_kpi.md`, `rollup_products.md`, `rollup_stages.md`, `rollup_timeline.md` (Mermaid gantt),
`rollup_slip.md`, `rollup_people.md` and `rollup_support.md` (Research). Metric definitions are in
`knowledge/portfolio/INDEX.md`. Lines starting `FLAG:` must go on the page and in chat.

## data/ (snapshots)

`data/<Folder>/<YYYY-MM-DD>.json` — one per weekly run, written by `normalize`. Used only for
week-on-week comparison. Descriptions are left out and likely secrets, non-company emails and phone
numbers in titles are replaced with `[redacted]`. Don't edit or delete old snapshots.
