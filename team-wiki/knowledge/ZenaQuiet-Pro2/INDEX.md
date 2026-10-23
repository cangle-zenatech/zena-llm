# ZenaQuiet-Pro2 — Instructions

These instructions apply only to `knowledge/ZenaQuiet-Pro2/`. They add to `knowledge/INDEX.md`.

**Follow `knowledge/product-procedure.md`**, the procedure shared by every product: role, steps,
rules, report and self-check. In it, `{product}` means `ZenaQuiet-Pro2` and `{KEY}` means
`PRO2`. This file holds only what is specific to ZenaQuiet-Pro2. If something here contradicts the
shared procedure, this file wins for ZenaQuiet-Pro2; say so in chat.

## Configuration

Update this block when settings change. The procedure and `tools/wiki_jira.py` read it.

```yaml
product: ZenaQuiet-Pro2
project_key: PRO2 # Jira name: ZenaQuiet-Pro2
today: "" # ISO date, e.g. 2026-10-07. If blank, use the system date.
lookahead_days: 14 # "due soon" window
stale_days: 14 # no update for this many days = stale
overload_factor: 1.5 # team load above this × its average = overloaded
report_max_rows: 30 # risk rows shown in the report; all HIGH are always shown
```

Stage windows: `reference.md` → `## Stage schedule`, ZenaQuiet-Pro2 column.

## Product-specific notes

None yet. Add rules here that apply only to ZenaQuiet-Pro2; everything shared goes in
`knowledge/product-procedure.md`.
