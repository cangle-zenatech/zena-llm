# knowledge/ — Instructions

These instructions apply to everything in `knowledge/`. Every folder `INDEX.md` below this one adds
to them (`CLAUDE.md` → `## How instructions work`). The hard rules in `CLAUDE.md` always win.

## 1. Who reads these pages

Managers and colleagues who may not be engineers. Each page should make sense on one read, without
opening Jira. Your job is translation: say what a ticket means for the product, not just what it
says.

## 2. Writing rules

1. **Plain words first.** Explain a technical term the first time it appears on a page, in a few
   words, and link it to [[glossary]] (e.g. "EVT, the first engineering-prototype stage"). Expand
   abbreviations on first use.
2. **Short and specific.** One idea per sentence. Lead with the conclusion, then the reason. Prefer
   numbers and dates to adjectives ("12 days late", not "significantly late").
3. **Facts vs. inferences.** State only what a source says. Label everything you work out
   "(inferred)". Missing data stays missing: write "not in Jira" or "unknown", never guess.
4. **Cite everything.**
   - Jira: the ticket key. Where a link is wanted, use the full form
     `[PRO2-123](https://epazz.atlassian.net/browse/PRO2-123)`. Weekly reports follow their
     project `INDEX.md` on when to link (e.g. links in the Executive Summary, plain keys elsewhere);
     on other pages, link a key on its first mention.
   - Sources in `raw/`: file and message, e.g. `threads/2026-10-19-purchase.md · REQUEST 4` or
     `transcripts/2026-10-19-biweekly.md · [07:37]`.
   - Jira comments: (key, author, date).
5. **Dates** are ISO `YYYY-MM-DD`. Say whether a span is calendar days or working days
   ("wd"); working days follow `reference.md` → `## Holidays`.
6. **Describe steps, never judge people.** "Waiting for CTO approval since 2026-10-05", not
   "approval is slow".
7. **Contradictions** between sources (Jira vs. a meeting, a comment vs. a field, this week vs.
   last week) go on the page with both sides cited, and in chat. Never pick one silently.
8. **Never copy** passwords, keys, tokens, customer personal data, or non-company emails and phone
   numbers into a page.
9. **Shared facts live in [[reference]]** (people, stage schedule, teams, lead times, sourcing
   rules). Link to them; don't copy them onto other pages, where they would go stale.

## 3. Links

- Use `[[wikilinks]]` with the path from `knowledge/`, no `.md`:
  `[[ZenaQuiet-Pro2/jira/2026-10-15-jira|2026-10-15 report]]`, `[[ZenaQuiet-Beacon/overview]]`.
- Link to a section with `#`: `[[reference#Stage schedule (per product)]]`.
- Link only to pages that exist. Before adding a link, check the file is there.
- Every weekly report links to the previous one; every overview links to the latest report.

## 4. Frontmatter

Every page you create starts with a YAML block. Keep `updated` current when you change a page.

| Page | Frontmatter |
| --- | --- |
| Project overview | `type: overview` · `project: <folder>` · `updated: YYYY-MM-DD` |
| Weekly Jira report | `type: jira-report` · `project: <folder>` · `date: YYYY-MM-DD` · `snapshot: data/<folder>/YYYY-MM-DD.json` (written by the script) |
| Report detail page | `type: jira-detail` · same fields (written by the script; never edit) |
| Confluence page | `type: confluence` · `project: <folder>` · `source: <Confluence URL or raw/docs/ file>` · `updated: YYYY-MM-DD` |
| Portfolio roll-up | as in `portfolio/INDEX.md` → Output |
| `overview.md`, `glossary.md` | `type: overview` / `type: glossary` · `updated: YYYY-MM-DD` |

`reference.md` and `log.md` have no frontmatter. Don't add frontmatter to older pages just for the
sake of it; add it when you next update them.

Example (weekly report):

```yaml
---
type: jira-report
project: ZenaQuiet-Pro2
date: 2026-10-26
snapshot: data/ZenaQuiet-Pro2/2026-10-26.json
---
```

## 5. Page templates

### Weekly Jira report — `<project>/jira/YYYY-MM-DD-jira.md`

`tools/wiki_jira.py report` writes the page (frontmatter, source line, link to the previous report,
every number and table) and a `YYYY-MM-DD-jira-detail.md` page with the full lists. You fill the
`<!-- AI: … -->` markers. Structure, rules and self-check: `knowledge/product-procedure.md` (products)
or the Research `INDEX.md` (→ Output). Never overwrite an earlier week's report; if you redo this
week's, say so in one line under the title and list what changed in Data Gaps.

### Project overview — `<project>/overview.md`

One page per project, rewritten (not appended) after each weekly report:

```
---
type: overview
project: <folder>
updated: YYYY-MM-DD
---

# <folder>

## What this project is
2–4 plain sentences: what the product does and for whom. Jira key.

## Where it stands
As of {date}: stage and next gate (or, for Research, open items and link coverage), health and the
one-sentence reason, top 1–3 issues with ticket keys. Link the latest weekly report.

## Active epics
One line each: key, plain-words name, status, due date.

## Recent changes
What changed since the previous report, newest first, each with a ticket key or source.
```

### Confluence page — `<project>/confluence/<kebab-case-title>.md`

One page per Confluence page or document in `raw/docs/`:

```
---
type: confluence
project: <folder>
source: <URL or raw/docs/ file>
updated: YYYY-MM-DD
---

# <Title>

**In one sentence:** what this document is for.

## Key points
3–7 bullets in plain words.

## What it means for the project
Decisions, requirements or numbers the team relies on, with the Jira tickets they touch.

## Open questions
Anything the document leaves unanswered or that disagrees with Jira or another source.
```

## 6. Glossary entries — `glossary.md`

Alphabetical, one `##` heading per term:

```
## <Term>

<Plain explanation in 1–2 sentences.> First seen: [[<page where it first appeared>|<label>]].
```

"First seen" must link to a page that exists (usually a weekly report). Helpers don't edit the
glossary; they list new terms under SUGGESTED EDITS TO SHARED FILES and the main session adds them.

## 7. `log.md`

One line per page created or updated, newest first, grouped by day with a blank line between days:

`YYYY-MM-DD · created | updated · [[page]], [[page]] · what changed and why (who decided, if the human did)`

Helpers don't write to `log.md`; the main session adds their lines (`CLAUDE.md` → `## Running many
projects`).

## 8. Self-check for any page

- [ ] Frontmatter present and `updated` / `date` is today
- [ ] Every technical term explained once or linked to [[glossary]]
- [ ] Every finding cites a ticket key or source; inferences labelled "(inferred)"
- [ ] Every `[[link]]` points to a page that exists
- [ ] No secrets or personal data
- [ ] `log.md` line added (main session)
