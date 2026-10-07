# Project instructions

Instructions for this project. They add to `knowledge/INDEX.md`.

# Weekly status report

**Mode: CLEAN-UP**  ← change to TRACKING when the team has filled in dates and labels.

Stages, team labels and the Jira project key are in `knowledge/reference.md`.

## Jira conventions

- Epic: major feature. Needs Start date and Due date.
- Story: title starts with the stage, e.g. `[POC] …`, `[EVT-1] …`. Needs Start and Due date.
- Subtask: team is a Jira label (FW, ME, EE, SW, ID, AC). Needs Start and Due date.
- Dates nest: subtask dates within its story; story dates within its epic.
- Blockers are recorded as "is blocked by" links.

## Step 1: Pull

Get every epic, story and subtask in the project with JQL. Fetch all pages.
Fields: summary, status, assignee, labels, Start date, Due date, parent, issue links, updated,
description.

## Step 2: Parse

- Stage: read from the story title, `[POC]`, `[EVT-1]` etc. Treat `[DVT-2: ME]` and `[DVT-2:ME]`
  as DVT-2.
- Team: read from subtask labels. If there's no label but the title has `[ME]` etc., use it
  and add the ticket to "Move team to label".
- Never guess. Unparseable tickets go on the clean-up list.

## Step 3: Clean-up list (both modes)

Group by owner, so each person sees their own fixes:

| Problem                         | Applies to                 |
| ------------------------------- | -------------------------- |
| No start date                   | all                        |
| No due date                     | all                        |
| No assignee                     | all                        |
| No stage in title / bad stage   | stories                    |
| Team still in title, not label  | stories, subtasks          |
| No team label                   | subtasks                   |
| Dates outside parent's dates    | stories, subtasks          |
| Same due date as every epic     | epics (likely placeholder) |

In CLEAN-UP mode, stop here: the report is the summary counts plus this list.

## Step 4: Checks (TRACKING mode only)

| Check      | Rule                                                           |
| ---------- | -------------------------------------------------------------- |
| Overdue    | Due date passed, not Done                                      |
| Late start | Start date passed, still To Do                                 |
| Stale      | In Progress, no update in 14+ days                             |
| Stage gate | Later-stage story started while an earlier-stage story is open |
| Blocked    | Open "is blocked by" link, or flagged                          |

## Step 5: Epic risk (TRACKING mode only)

- Slack = epic due date − latest due date of its open children.
- 🟢 slack ≥ 14 days, no blockers · 🟡 slack under 14 days, or a stale/late-start child ·
  🔴 negative slack, an overdue child, or an unowned blocker.
- Risk bubbles up: a late subtask flags its story; a late story flags its epic.

## Report

File: `status/YYYY-MM-DD-status.md` in this project folder. Plain language, as in `knowledge/INDEX.md`.

1. What the project is for (2–3 sentences)
2. Technical requirements (targets and pass criteria from epics and stories)
3. Stage progress: POC/EVT/DVT/PVT/MP, stories done out of total
4. Epic table: epic, owner, start, due, % done, slack, health
5. Blockers and risks: ticket, team, problem, epic affected, days at risk
6. Team load: open and overdue subtasks per team
7. Clean-up list
8. Changes since last report
