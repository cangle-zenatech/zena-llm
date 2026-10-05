# Index

Catalog of every page in this wiki. Updated on every ingest. Start here when answering
questions — find the relevant pages, then drill in.

## Frontmatter

### Jira pages

```yaml
---
source_type: jira
project: zenaQuiet-Pro | zenaQuiet-Mask | zenaQuiet-Headset | zenaQuiet-Beacon | zenaQuiet-Research
key: PRO2-142
title: raw ticket title
work_type: epic | story | feature | bug | task | subtask
status: To Do | In Progress | In Review | In Testing | Done
priority: Blocker | Critical | Major | Minor | Trivial
parent: "[[2026-09-01-PRO2-100|PRO2-100]]" # epic or parent ticket, if any
child_count: 0 # number of child work items
reporter: Full Name
assignee: Full Name | Unassigned
created: YYYY-MM-DD # when the ticket was created in Jira
updated: YYYY-MM-DD # when the ticket last changed in Jira
summarized: YYYY-MM-DD # when you last wrote this page
source: https://epazz.atlassian.net/browse/PRO2-142 # always the Jira URL
---
```

If the source doesn't contain a field, write `unknown`. Don't guess.

## Jira writing rules

### File names

- Format: `YYYY-MM-DD-<TICKET-KEY>.md`, where the date is the day the ticket was **created** in Jira.
- Never rename the file when the ticket changes. The date in the name stays fixed so links don't break.
  Changes go in the `updated` and `summarized` fields in the frontmatter.

### Audience and language

1. **Write for someone outside engineering.** After one read, they should be able to explain the main
   point of the ticket in two sentences.
2. **Plain language.** Start with the result: what's happening and why it matters. Keep sentences under
   20 words, use active voice, and pick everyday words.
3. **Explain technical terms.** Explain each one in brackets the first time it appears, e.g.
   "firmware (the software built into the device)". Spell out every acronym the first time. Add each
   term to `knowledge/glossary.md`.
4. **Translate numbers.** Keep the original value and say what it means, e.g. "300 ms (about a third
   of a second)".

### Content

5. **Architecture flow.** Redraw any architecture diagram in plain ASCII inside a `text` code
   block. Use only `+ - | > < v ^` and letters, with no Unicode box-drawing characters. Write one
   sentence below it explaining the flow in plain words. If the diagram is an image you can't read,
   write "Diagram in source could not be read" and link to it in `raw/assets/`.

```text
   +--------+  Bluetooth  +-----------+   HTTPS   +--------+
   | Beacon | ----------> | Phone App | --------> | Cloud  |
   +--------+             +-----------+           +--------+
```

The beacon sends data to the phone app, and the app uploads it to the cloud.

6. **Link generously.** The first mention of any person, project, ticket, or concept on a page becomes
   a `[[wikilink]]`. Link tickets by full file name with the key as the label:
   `[[2026-09-15-PRO2-143|PRO2-143]]`. Look up the created date in Jira. If the date
   is unknown, link `[[PRO2-143]]` and add the ticket to "Open questions".
   Link people as `[[reference#People|People Link]]`, with the person's full name as the label
   (e.g. `[[reference#People|Cang Le]]`). The link jumps to the People list. Check the
   `## People` section of `knowledge/reference.md`. If the person isn't listed, add them there as
   `- Full Name — role` (write `unknown` if the role isn't stated), and log it.
7. **Child work items.** List every child ticket in a table: linked key, plain-English summary, status.
   Link each child to its Jira URL, `https://epazz.atlassian.net/browse/<TICKET-KEY>`, with the key
   as the label, e.g. `[PRO2-249](https://epazz.atlassian.net/browse/PRO2-249)`.
   Update the parent's table whenever a child's status changes.
8. **Status in plain words.** Below "Status", add what it means:

   | Jira status | Write it as                                |
   | ----------- | ------------------------------------------ |
   | To Do       | Planned, but not started                   |
   | In Progress | Someone is actively working on it          |
   | In Review   | Work is done and a teammate is checking it |
   | In Testing  | Being tested to make sure it works         |
   | Done        | Finished                                   |

### Activity comments

9. **Show every comment.** Include every comment, oldest first, with author, date, and the original
   text in a quote block. Don't reword it. The only exception is sensitive data (rule 13). Mark
   automated or bot comments with `(automated)`.
10. **Summarize the comments.** Above the full list, write a plain-English summary of the discussion:
    - **Decided:** what was agreed, who agreed it, and the date
    - **Blockers raised:** what's stopping the work
    - **Still open:** unanswered questions

    If the comments contain no decisions or blockers, say so.

### Accuracy

11. **Never silently overwrite.** When a new source contradicts something already on the page, keep
    both and flag it:

    > ⚠️ **Contradiction.** The Jira ticket (updated YYYY-MM-DD) says X ([[...]]); the Sept transcript
    > says Y ([[...]]). Unresolved: ask the team.

    Also raise every contradiction in chat. Don't just leave it in the file.

12. **Don't guess.** If the ticket doesn't say something, write "Not stated in the ticket." Label your
    own interpretation with "This likely means…". Don't play down bugs or risks.
13. **Sensitive data.** Never copy passwords, API keys, tokens, or customer personal data, including
    inside quoted comments. Replace them with `[redacted]` and add a note to `log.md`.

### Length

14. The summary sections (TL;DR through Where it stands) should total **150–300 words**, or up to 400
    for an epic. The Activity section has no word limit.

### Log entries

15. **Log every change.** Each time you create or update a page, add one line at the top of
    `knowledge/log.md`:

    `YYYY-MM-DD · created | updated | stub | redacted · [[link]] · what changed`

    Example: `2026-10-05 · updated · [[2026-09-15-PRO2-142|PRO2-142]] · status In Review → Done`

## Jira page template

Use the sections in this order and leave out any that would be empty. For bugs, rename
"What this is" to "What's going wrong".

```markdown
# [PRO2-142] Raw ticket title

> **TL;DR:** One sentence: what this is and why it matters.

## What this is

2–4 sentences explaining the Jira description in plain language.

## Why it matters

Who it affects (customers, a team, a deadline) and what happens if it's not done.

## Architecture flow

ASCII diagram plus a one-sentence explanation (only if the source has a diagram).

## Where it stands

- **Status:** In Progress (someone is actively working on it)
- **Blocked by:** … or "Nothing reported"
- **Next step:** … or "Not stated in the ticket"

## Child work items

| Ticket                                                  | What it is            | Status |
| ------------------------------------------------------- | --------------------- | ------ |
| [PRO2-143](https://epazz.atlassian.net/browse/PRO2-143) | Plain-English summary | Done   |

## Activity

### Summary

- **Decided:** 2026-09-14: [[reference#People|People Link]] decided to … because …
- **Blockers raised:** …
- **Still open:** …

### All comments

**[[reference#People|People Link]]**, 2026-09-12

> Original comment text, copied without changes.

**Jira Automation** (automated), 2026-09-13

> Status changed from To Do to In Progress.

## Open questions

- Anything unresolved, unclear, or contradictory.
```
