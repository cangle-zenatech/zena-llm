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
   → `diff.md`: issues added or removed, status and date changes since the last snapshot.
5. Write the report from these outputs. The agent still writes the Executive Summary, Product
   Detail (Step 8), impact sentences that need judgment, and Recommendations.

### Limits

- ZenaQuiet-Research has no stage schedule; stage checks are skipped. Its extra rules (D7, R11–R13
  in its `INDEX.md`) are not in the script yet: apply them by hand.
- If a project's `INDEX.md` changes a rule, the script does not know. Flag the difference in chat.
- Field IDs default to `customfield_10015` (Start date) and `customfield_10020` (Sprint). Pass
  others if Step 1 finds different ones.

## data/ (snapshots)

`data/<Folder>/<YYYY-MM-DD>.json` — one per weekly run, written by `normalize`. Used only for
week-on-week comparison. Descriptions are left out and likely secrets, non-company emails and phone
numbers in titles are replaced with `[redacted]`. Don't edit or delete old snapshots.
