# My notes

1. [Running the AI module](#1-running-the-ai-module)
2. [What CLAUDE.md is doing](#2-what-claudemd-is-doing)
3. [Using Foam (VS Code)](#3-using-foam-vs-code)

---

## 1. Running the AI module

### Key words to start

1. Connect the folder C:\Users\Admin\Documents\zena-llm
2. read team-wiki/CLAUDE.md and follow it.
3. `<task>.` Then replace `<task>` with one of these:

### Tasks

| Goal                    | What to type                                                                |
| ----------------------- | --------------------------------------------------------------------------- |
| Weekly reports          | `write weekly status reports` (all projects marked Yes)                     |
|                         | `write the status report for Pro2 only`                                     |
|                         | `redo today's Mask report` (replaces it and lists what changed)             |
| Ask questions           | `what changed in Beacon since last week?`                                   |
|                         | `who is overloaded across all projects?`                                    |
|                         | `what is blocking the Headset POC gate?`                                    |
|                         | `explain why Headset is RED`                                                |
| Turn sources into pages | `turn the new files in raw/ into wiki pages`                                |
|                         | `summarize PRO2-142 in plain language`                                      |
|                         | `summarize this Confluence page: <link>`                                    |
| Keep the wiki tidy      | `fill in the empty overview pages`                                          |
|                         | `add the new technical terms to the glossary`                               |
|                         | `check the wiki for contradictions`                                         |
| People                  | `add <name> to reference.md`                                                |
|                         | `confirm the unconfirmed people in reference.md`                            |
| Change settings         | `set stale_days to 21 for Mask`                                             |
|                         | `switch Research to No` (or edit the Active table in CLAUDE.md yourself)    |
|                         | `update the script so it <change>` (I'll show you the change before saving) |
| Automate                | `run the weekly reports every Monday at 8am`                                |
| Understand it           | `explain how the health rating works`                                       |
|                         | `which file controls <thing>?`                                              |

---

## 2. What CLAUDE.md is doing

1. **My job.** I maintain the wiki and write every page in `knowledge/`. My main task is turning
   technical Jira tickets and Confluence pages into summaries someone without an engineering
   background can understand. You gather sources, ask questions and review.
2. **Where to find more detailed instructions.** It's a map, not the full manual. Before I work in a
   folder, I read that folder's `INDEX.md` and the ones above it. The closer file wins if two
   disagree, and I tell you when that happens.
3. **Hard rules no other file can override:**
   - `raw/` is read-only.
   - No passwords, keys, tokens or customer personal data in the wiki.
   - No silent overwrites; contradictions get flagged.
   - README files are your private notes, and I never touch them.
4. **What lives where.** A folder map: `raw/` for sources, `tools/` for the script, `data/` for
   snapshots, `knowledge/` for the pages I write.
5. **Which projects to work on.** The Active table is your on/off switch for each project. I skip any
   project marked No.
6. **How to handle many projects at once.** One helper per project, running in parallel. Each helper
   sends back a short summary in a fixed format, and the main session updates the shared files and
   gives you one combined answer.

---

## 3. Using Foam (VS Code)

1. **Open the folder:** File → Open Folder → `C:\Users\Admin\Documents\zena-llm\team-wiki` (exactly this folder).
2. **Open a page:** e.g. `knowledge/zenaQuiet-Pro/jira/2026-06-18-PRO2-2.md`.
3. **Follow a link:** Ctrl + click it. Hover to preview.
4. **Read nicely:** Ctrl+Shift+V (or Ctrl+K, then V for side by side).
5. **Backlinks:** Foam icon (left sidebar) → Connections.
6. **Graph:** Ctrl+Shift+P → `Foam: Show Graph` → Enter.
