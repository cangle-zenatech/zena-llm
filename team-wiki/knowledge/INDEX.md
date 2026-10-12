# Knowledge — Instructions

> **DRAFT for Cang's review (2026-10-12).** Written from `CLAUDE.md` and the conventions already
> used in this folder. Remove this note once it's approved.

These instructions apply to everything in `knowledge/`. Project folders add their own rules in
their `INDEX.md`. The hard rules in `team-wiki/CLAUDE.md` always win.

## 1. Who you write for

The reader is smart but not an engineer. They should understand a page after reading it once.

- Start every page with a **plain-language summary** of 2–4 sentences: what this is, why it matters,
  where it stands.
- Use short sentences and everyday words. One idea per sentence.
- Explain every technical term or acronym the first time it appears on a page, in a few words in
  brackets, e.g. "TSE (software that picks out one voice from background noise)".
- Add each new term to `glossary.md` (see section 5).
- Prefer concrete numbers and comparisons over adjectives: "about half as loud", not "much quieter".
- Weekly status reports are the exception: their reader is the TM, so the project `INDEX.md` may
  allow more technical wording.

## 2. Facts, sources and gaps

- Every fact comes from a source. Cite it: the Jira ticket URL, the Confluence page, or the file in
  `raw/` (e.g. `raw/transcripts/2026-10-01-eng-planning.md`).
- Never invent tickets, dates, people, numbers or requirements.
- Keep facts and inferences apart. Mark any inference **(inferred)**.
- Missing data stays missing. Write "Not stated in the source", don't guess.
- If two sources disagree, keep both, add a **⚠ Conflict** note on the page naming both sources,
  and tell the human in chat. Never silently overwrite.
- No passwords, API keys, tokens or customer personal data. Write "[redacted]" instead.
  People's names and work emails from `reference.md` are allowed.

## 3. Frontmatter

Every page starts with YAML frontmatter. Required fields for all pages:

```yaml
---
type: jira | confluence | report | overview | glossary | reference | log
project: ZenaQuiet-Pro2 # omit for wiki-wide pages
updated: YYYY-MM-DD # date of your last change
---
```

Extra fields by page type:

| Type         | Extra fields                                                                     |
| ------------ | -------------------------------------------------------------------------------- |
| `jira`       | `key`, `issuetype`, `status`, `assignee`, `parent`, `source` (ticket URL), `read` (date you read Jira) |
| `confluence` | `title`, `source` (page URL or `raw/docs/...` file), `read`                       |
| `report`     | `period` (week covered, `YYYY-MM-DD → YYYY-MM-DD`). Saved in `<project>/jira/` as `YYYY-MM-DD-jira.md` |

## 4. Links

- Link pages with `[[wikilinks]]`. Use the path from `knowledge/` without `.md`, e.g.
  `[[ZenaQuiet-Pro2/jira/2026-09-15-PRO2-142|PRO2-142]]`.
- Link to a heading with `#`, e.g. `[[reference#Stage schedule]]`.
- Link Jira tickets you have no page for with their full URL:
  `[PRO2-142](https://epazz.atlassian.net/browse/PRO2-142)`.
- Never link to a `README.md` file.

## 5. Bookkeeping after every create or update

1. **`log.md`** — add one line at the top, newest first:
   `YYYY-MM-DD · created|updated · [[page]] · what changed, in a few words`
2. **`glossary.md`** — add each new term in A–Z order:
   `## Term`, then a plain-words explanation and `First seen: [[page|KEY]].` Update `updated:`.
3. **`<project>/overview.md`** — if a page changes what the project is, its active Epics or its
   recent changes, update the overview.
4. **`overview.md`** (wiki-wide) — keep one paragraph per active project in sync with its overview.
5. **`reference.md`** — add new people under People yourself. Change anything else only when the
   human agrees.

## 6. Jira page template

File: `knowledge/<project>/jira/YYYY-MM-DD-<TICKET-KEY>.md` (date = the ticket's Jira **created**
date, so the name never changes and links stay valid; the day you read Jira goes in `read:`).
Read Jira only; never edit, comment on or transition a ticket.

```markdown
---
type: jira
project: ZenaQuiet-Pro2
key: PRO2-142
issuetype: Epic | Story | Sub-task
status: To Do | In Progress | Done
assignee: Name or Unassigned
parent: PRO2-2 # or none
source: https://epazz.atlassian.net/browse/PRO2-142
read: YYYY-MM-DD
updated: YYYY-MM-DD
---

# PRO2-142 — {ticket title}

## In plain words

2–4 sentences: what this work is, why it matters to the product, where it stands.

## Key facts

| Field    | Value                       |
| -------- | --------------------------- |
| Stage    | EVT (from the title prefix) |
| Team(s)  | AC, ME                      |
| Owner    | Name                        |
| Dates    | start → due                 |
| Parent   | [[link]] or URL             |
| Children | count, with links           |

## What the ticket asks for

Bullets in plain words. Keep targets and numbers exactly as written, then explain them.

## Open questions and risks

What's unclear, blocked, late or missing. "None found" if nothing.

## Terms used

Terms explained on this page, each linked to `[[glossary#Term]]`.

## History

- YYYY-MM-DD — what changed since the last read (newest first).
```

## 7. Confluence page template

File: `knowledge/<project>/confluence/<kebab-case-title>.md`. Same layout as the Jira template,
without the Key facts table; use **In plain words**, **Main points**, **Numbers and targets**,
**Open questions**, **Terms used** and **History**.
