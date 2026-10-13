# Portfolio roll-up — Instructions

These instructions apply only to `knowledge/portfolio/`. They add to `knowledge/INDEX.md`.

Only the **main session** works here, after every project helper in the weekly run has finished
(`CLAUDE.md` → `## Running many projects`, main session step 3). Helpers never read or write this
folder.

The roll-up answers one question: **is each product on course to meet its stage gates (POC → EVT →
DVT → PVT → MP) and the final deadline, the end of MP?**

**The plan is the stage schedule** in `reference.md` → `## Stage schedule (per product)` (Pro2 and
Beacon from 2026-06-29, Mask and Headset from 2026-09-21, all ending 2027-11-15). All slip is
measured against those planned stage end dates, never against a Jira snapshot, so re-dating tickets
in Jira cannot hide slip. Changing the schedule is a `reference.md` change and needs the human's OK.

## 1. Configuration

Update this block only when the human agrees. `tools/wiki_jira.py rollup` reads it.

```yaml
bulk_redate_share: 0.2 # flag a product when more than this share of its open items are re-dated in one week
pace_min_done: 5 # a pace forecast needs at least this many adjusted Stories closed in the current stage
pace_min_days: 28 # ...and at least this many days elapsed in the current stage
exclude_same_day_closed: false # human decided 2026-10-13: same-day-closed Stories count as progress
lookahead_days: 14 # "due soon" window for Research items
today: "" # ISO date. If blank, use the system date.
```

## 2. Scope

- **Products** = projects marked `Yes` in `CLAUDE.md` that have a column in `reference.md` →
  `## Stage schedule`. Today: Pro2, Beacon, Headset, Mask.
- **Support** = projects marked `Yes` with no stage schedule (Research). They are not a product row.
  Show only what products wait on: open items, product links, overdue and due-soon items.
- Stage windows and the final deadline (MP end) come from `reference.md`. Never copy dates here.

## 3. Procedure

1. Check that every product has a snapshot `data/<project>/<today>.json` from this week's run. If one
   is missing, use the newest earlier one, say so in Data Gaps, and flag it in chat.
2. Run, from `team-wiki/` in bash:
   `python3 -I tools/wiki_jira.py rollup --work WORK --date <today>`
   (`WORK` = a temporary folder, e.g. `outputs/work-rollup/`). It calls Jira for nothing; it reads
   snapshots, `reference.md`, `CLAUDE.md` and the yaml blocks. Outputs in `WORK`:
   `rollup_summary.txt`, `rollup.json`, `rollup_kpi.md`, `rollup_products.md`, `rollup_stages.md`,
   `rollup_timeline.md`, `rollup_slip.md`, `rollup_people.md`, `rollup_support.md`.
3. Read each product's report for this week (`knowledge/<project>/jira/<today>-jira.md`) only for
   the judgment parts: why a product is behind, and its top risk. Never take numbers from the
   reports; numbers come from the script.
4. Write the page (Section 5) and add one line at the top of `knowledge/overview.md` (Section 6).
5. Add a `knowledge/log.md` line. Flag every item in `FLAG:` lines and every conflict in chat.

## 4. Metric definitions (what the script computes)

| Metric | Definition |
| --- | --- |
| Expected % | Share of the stage window elapsed today (0% before it starts, 100% after it ends) |
| Raw readiness % | Done Stories of the stage / all Stories of the stage |
| Adjusted readiness % | Like raw, but a Done Story does **not** count if it has open Subtasks, was closed before the stage started, or was created and closed within one day (logged after the fact) |
| Stage status (current stage) | **Behind**: expected − adjusted > 25 pts, or a confident pace forecast lands after the stage end. **At risk**: 15–25 pts behind. **On track**: otherwise |
| Stage status (other stages) | Past window: **Done**, or **Carryover (n open)**. Future window: **Not started** |
| Pace | Adjusted Stories closed in the current stage / days elapsed in it. Forecast = today + open Stories ÷ pace. Low confidence below `pace_min_done` closed or `pace_min_days` elapsed |
| MP outlook | **Behind** if the current stage is Behind or a confident forecast slips; **At risk** if At risk or any carryover; else **On track**, shown as "On track (early, low confidence)" while the pace forecast is low confidence. MP forecast date = MP end + the current-stage forecast slip (assumes later stages keep their length) |
| Slip vs plan (stage) | Finished stage: date its last Story closed − planned stage end (0 if on time). Past stage with open Stories: today − planned end, so far. Current stage: pace forecast − planned end (shown, low confidence when pace is). Future stage: none yet |
| Slip vs schedule (tickets) | Open Stories and Subtasks due after their stage's planned end, and open Epics due after the planned MP end (count, max days, worst 10) |
| Dates moved this week | Open items whose start or due changed since the previous snapshot, and the ones now due later (worst 5). A warning, not slip |
| Bulk re-date | More than `bulk_redate_share` of open items changed start or due since the previous snapshot |
| Next stage planned | Next-stage Stories with an owner and at least one Subtask that has both dates / all next-stage Stories |
| People across products | Assignees with open items in two or more products |

The script does not judge. If a number looks wrong, check the snapshot, then flag it; never edit the
number on the page.

## 5. Output

Save as `knowledge/portfolio/YYYY-MM-DD-rollup.md` (date = `today`). Never overwrite an earlier
week's page. Use this structure:

```
---
type: portfolio-rollup
date: {today}
slip_reference: reference.md ## Stage schedule
sources: data/<project>/{snapshot}.json for each product
---

# Portfolio Roll-up — {today}

## 1. Headline
{rollup_kpi.md}
2–3 plain sentences: which products are on course for the final deadline and which are not, and why.

## 2. Products
{rollup_products.md}
A "What the numbers mean" note under the table: one plain sentence each for Raw, Adjusted and
Expected, each with a worked example from this week's numbers, plus the At risk / Behind thresholds.
Keep the same note on the online copy of the page.
One line per product under the table: the main reason for its status, with ticket keys and a link
to its weekly report.

## 3. Stage timeline
{rollup_timeline.md}

## 4. Stage detail
{rollup_stages.md}

## 5. Slip vs schedule and dates moved this week
{rollup_slip.md}

## 6. Cross-product
- Shared gates: products whose current gate falls on the same date.
- People across products: {rollup_people.md}
- Research and other support work products wait on: {rollup_support.md}

## 7. Recommendations
3–5 actions across products, each tied to ticket keys or people.

## 8. Data Gaps & Assumptions
Snapshots used, the stage schedule used as the plan, stale or missing snapshots, `FLAG:` lines, low-confidence forecasts,
and the MP forecast assumption (later stages keep their length).
```

Writing rules: the reader may not be an engineer. Explain stage names the first time (link
[[glossary]] terms). Keep facts and inferences apart; label inferences "(inferred)". Cite a ticket
key for every finding.

## 6. Line in `knowledge/overview.md`

Keep one line directly under the title, replaced each week (the history stays in the dated pages):

`**Portfolio ({today}):** {n} of {N} products on track for {final deadline}; {worst product and why}. See [[portfolio/{today}-rollup]].`

## 7. Self-check before delivering

- [ ] Every product has a snapshot from this run, or the gap is stated
- [ ] Every number on the page comes from the script outputs
- [ ] Slip is measured against the planned stage dates in `reference.md`, and every stage row shows its slip
- [ ] Every `FLAG:` line from the script is on the page and in chat
- [ ] Every Behind or At risk product has a reason with ticket keys
- [ ] Data Gaps section is filled in, even if it says "None"
