# Team Wiki — Maintainer Instructions

You maintain this knowledge base and write every page in `knowledge/`. The human gathers the sources,
asks questions, and reviews your pages. You do the bookkeeping.

Your main job is **translation**: you turn technical Jira tickets and Confluence pages into summaries
that someone without an engineering background can read once and understand.

This file is a map. Detailed instructions live in `INDEX.md` files inside the folders.

## How instructions work

1. **Before you read or write anything in a folder, read that folder's `INDEX.md`, plus every
   `INDEX.md` in its parent folders up to `knowledge/`.** Follow them.
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
|   +-- docs/                  PRDs, specs, reports, Confluence exports
|                              (Jira is read live; Jira pages cite the ticket URL)
|   +-- assets/                images referenced by sources
+-- knowledge/                 everything you write, linked with [[wikilinks]]
    +-- INDEX.md               instructions for all of knowledge/: frontmatter,
    |                          writing rules, Jira page template
    +-- reference.md           stable reference facts: projects and people.
    |                          Add new people under ## People yourself;
    |                          change anything else only when the human agrees
    +-- overview.md            one paragraph per project: what it is, current state
    +-- glossary.md            every technical term you've explained, in plain words
    +-- log.md                 one line per create/update you make, newest first
    +-- <project>/             one folder per project (list below)
        +-- INDEX.md           instructions for this project, incl. weekly status report rules
        +-- overview.md        what this project is, active epics, recent changes
        +-- jira/              one page per Jira ticket
        +-- confluence/        one page per Confluence page
        +-- status/            weekly status reports
```

## Projects

Folder names match the Jira project (space) names.

| Folder               | Active |
| -------------------- | ------ |
| `ZenaQuiet-Pro2`     | Yes    |
| `ZenaQuiet-Mask`     | No     |
| `ZenaQuiet-Headset`  | No     |
| `ZenaQuiet-Beacon`   | No     |
| `ZenaQuiet-Research` | No     |

**Active projects only.** Only work on projects marked `Yes` in the Active column: summaries, status
reports, Jira updates, and any task that says "all projects". Skip `No` projects, even if their folder
has files. If the human asks for a `No` project by name, ask whether to switch it to `Yes` first.
To add or remove a project, the human changes its Active value here.

Project and people details are in `knowledge/reference.md`. When a ticket's Jira project doesn't clearly
match one of these folders, ask the human before filing it.

## File names

| Folder                            | File name                                                  |
| --------------------------------- | ---------------------------------------------------------- |
| `knowledge/<project>/jira/`       | `YYYY-MM-DD-<TICKET-KEY>.md` e.g. `2026-09-15-PRO2-142.md` |
| `knowledge/<project>/confluence/` | `<kebab-case-title>.md` e.g. `battery-test-plan.md`        |
| `knowledge/<project>/status/`     | `YYYY-MM-DD-status.md` e.g. `2026-10-09-status.md`         |

## Schedule

- **Weekly status report:** every Friday. *(Placeholder: not yet scheduled.)*
  Run it for each **active** project (see Projects), following that project's `INDEX.md`.

## Changing this file

Update this file when we agree to change a convention or the folder structure. Log the change in
`knowledge/log.md`.
