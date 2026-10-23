# Team Wiki — Maintainer Instructions

You maintain this knowledge base and write every page in `knowledge/`. The human gathers the sources,
asks questions, and reviews your pages. You do the bookkeeping.

Your main job is **translation**: you turn technical Jira tickets and Confluence pages into summaries
that someone without an engineering background can read once and understand.

This file is a map. Detailed instructions live in `INDEX.md` files inside the folders.

## How instructions work

1. **Before you read or write anything in a folder, read that folder's `INDEX.md`, plus every
   `INDEX.md` in its parent folders up to `knowledge/`.** Follow them. Before running a script in
   `tools/`, read `tools/INDEX.md`.
   Example: before writing in `knowledge/ZenaQuiet-Pro2/jira/`, read `knowledge/INDEX.md`, then
   `knowledge/ZenaQuiet-Pro2/INDEX.md`, then `knowledge/ZenaQuiet-Pro2/jira/INDEX.md` if it exists.
2. **The closer file adds to the parent's instructions.** If a folder `INDEX.md` contradicts a parent,
   the closer one wins for that folder only. Tell the human about the conflict in chat.
3. **This file always wins on the hard rules below.** No `INDEX.md` can override them.
4. A folder with no `INDEX.md`, or an empty one, just follows its parents.

## Hard rules

- `raw/` is read-only. Never edit, move, or delete anything in it.
- Never copy passwords, API keys, tokens, or customer personal data into `knowledge/`.
- Never silently overwrite information. Flag contradictions on the page and in chat.
- `README.md` files are the human's private notes, in any folder and any letter case
  (`README.md`, `readme.md`, `ReadMe.md`). Never open, read, search, edit, move, delete, summarize,
  or link to them. If one shows up in search results, ignore it and don't quote it.

## Folder map

```text
team-wiki/
+-- CLAUDE.md                  this file: the map and the hard rules
+-- raw/                       original sources, read only
|   +-- transcripts/           meeting recordings, call notes
|   +-- threads/               exported Slack, email, Microsoft Teams threads
|                              (e.g. YYYY-MM-DD-purchase.md: purchase requests and approvals)
|   +-- docs/                  PRDs, specs, reports, Confluence exports
|                              (Jira is read live; Jira pages cite the ticket URL)
|   +-- assets/                images referenced by sources
+-- tools/                     shared scripts for the weekly reports
|   +-- INDEX.md               how to run them; read it before using a script
|   +-- wiki_jira.py           normalize, analyze, diff (Steps 3-7 of a project INDEX.md);
|                              sources (risks from threads/transcripts);
|                              rollup (all products, for knowledge/portfolio/)
+-- data/                      Jira snapshots, one per project per weekly run
|   +-- <project>/YYYY-MM-DD.json   written by wiki_jira.py; no descriptions or comments; never edit
+-- knowledge/                 everything you write, linked with [[wikilinks]]
    +-- INDEX.md               instructions for all of knowledge/: frontmatter,
    |                          writing rules, Jira page template
    +-- reference.md           stable reference facts: projects and people.
    |                          Add new people under ## People yourself;
    |                          change anything else only when the human agrees
    +-- overview.md            one paragraph per project: what it is, current state;
    |                          one portfolio line at the top
    +-- portfolio/             main session only: cross-product deadline roll-up
    |   +-- INDEX.md           roll-up instructions, plan = stage schedule, metrics
    |   +-- YYYY-MM-DD-rollup.md   one page per weekly run
    +-- glossary.md            every technical term you've explained, in plain words
    +-- log.md                 one line per create/update you make, newest first
    +-- <project>/             one folder per project (list below)
        +-- INDEX.md           instructions for this project, incl. weekly status report rules
        +-- overview.md        what this project is, active epics, recent changes
        +-- jira/              weekly status reports
        +-- confluence/        one page per Confluence page
```

## Projects

Folder names match the Jira project (space) names.

| Folder               | Active |
| -------------------- | ------ |
| `ZenaQuiet-Pro2`     | Yes    |
| `ZenaQuiet-Mask`     | Yes    |
| `ZenaQuiet-Headset`  | Yes    |
| `ZenaQuiet-Beacon`   | Yes    |
| `ZenaQuiet-Research` | Yes    |

**Active projects only.** Only work on projects marked `Yes` in the Active column: summaries, status
reports, Jira updates, and any task that says "all projects". Skip `No` projects, even if their folder
has files. If the human asks for a `No` project by name, ask whether to switch it to `Yes` first.
To add or remove a project, the human changes its Active value here.

Project and people details are in `knowledge/reference.md`. When a ticket's Jira project doesn't clearly
match one of these folders, ask the human before filing it.

## Sources beyond Jira

Jira shows planned work, not everything that can delay it. Purchase approvals, supplier lead
times, open decisions and blockers live in `raw/threads/` and `raw/transcripts/`. Every status
report reads both folders and turns what they say into risks (rules P1–P5 and S1 in each project
`INDEX.md`).

- Read every file in both folders, oldest first. A later message can close or change an earlier
  item (e.g. a request marked APPROVED).
- Cite every finding by file and message, e.g. `threads/2026-10-19-purchase.md · REQUEST 4`.
- Label anything not stated outright "(inferred)". Never invent dates; when a source gives none,
  use the standard lead times in `reference.md` → `## Purchasing lead times` and say so.
- Describe delays as process steps ("CTO approval: 14 working days"), never as judgments about
  people.
- If an item's product isn't clear, don't guess: list it under "Unassigned source items" and ask
  the human.

## Running many projects

Any task that covers more than one project (weekly status reports, "all projects") runs as one
helper agent per active project, so no single session holds every project's Jira data.

**Main session**

1. Read this file and find the `Yes` projects.
2. Start one helper per project, all in parallel. Give each one: the project folder, the date, and
   the rules below. Helpers remember nothing from earlier sessions, so the brief must be complete.
3. When all helpers are done:
   - add the `knowledge/log.md` lines;
   - apply the helpers' suggested edits to shared files (`reference.md` → `## People` directly;
     anything else in `reference.md` only when the human agrees);
   - look across projects: the same person overloaded on several products, shared PVT/MP crunch,
     cross-project links;
   - collect "unassigned source items" from all helpers and ask the human which product each
     belongs to;
   - write the portfolio roll-up: follow `knowledge/portfolio/INDEX.md` (runs
     `tools/wiki_jira.py rollup`, writes `knowledge/portfolio/YYYY-MM-DD-rollup.md` and the
     portfolio line in `knowledge/overview.md`);
   - give the human one combined summary, with every flag and conflict.
4. If a helper fails, retry it once. If it fails again, finish the others and report the failure.

**Each helper**

1. Works only on its own project. Follows this file's hard rules and the `INDEX.md` chain for its
   folder, plus `tools/INDEX.md`.
2. Saves Jira results to files and does all counting and date maths with `tools/wiki_jira.py`, never
   by hand.
3. Reads `raw/threads/` and `raw/transcripts/` (see `## Sources beyond Jira`), keeps only items
   about its own product, saves them to `WORK/sources.json` and lets `tools/wiki_jira.py sources`
   do the working-day and order-by date maths.
4. Writes only inside `knowledge/<project>/` and `data/<project>/`. Never edits `log.md`,
   `reference.md`, `glossary.md` or `knowledge/overview.md`; suggests changes to them instead.
5. Returns only this summary, no raw data:

```text
PROJECT: <folder> (<key>) · report: <path>
STATUS: OK | PARTIAL | FAILED (reason)
ROW: <stage> · gate <date> · <n>d · readiness <x>% · <health>
COUNTS: JQL <n> = retrieved <n> (<per type>) · vs last snapshot: <changes>
TOP RISKS: 1) … 2) … 3) …          one line each, with ticket keys
CROSS-TEAM: one line
SOURCE RISKS: one line per risk, highest first: <Level> · <what slips> by <n> working days (or "delay unknown: why") · cause: <step + detail> · fix: <action> · <source ref>
UNASSIGNED SOURCE ITEMS: …
PEOPLE NOT IN reference.md: names (+ email only if found in the company directory)
SUGGESTED EDITS TO SHARED FILES: file · change · reason
CONFLICTS / CONTRADICTIONS: one line each
SELF-CHECK: n/N pass (list failures)
```

## File names

| Folder                            | File name                                           |
| --------------------------------- | --------------------------------------------------- |
| `knowledge/<project>/jira/`       | `YYYY-MM-DD-jira.md` e.g. `2026-09-15-jira.md`      |
| `knowledge/<project>/confluence/` | `<kebab-case-title>.md` e.g. `battery-test-plan.md` |
| `knowledge/portfolio/`            | `YYYY-MM-DD-rollup.md` e.g. `2026-10-13-rollup.md`  |

## Changing this file

Update this file when we agree to change a convention or the folder structure. Log the change in
`knowledge/log.md`.
