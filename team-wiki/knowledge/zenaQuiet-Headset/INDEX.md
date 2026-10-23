# ZenaQuiet-Headset — Instructions

These instructions apply only to `knowledge/ZenaQuiet-Headset/`. They add to `knowledge/INDEX.md`.

**Follow `knowledge/product-procedure.md`**, the procedure shared by every product: role, steps,
rules, report and self-check. In it, `{product}` means `ZenaQuiet-Headset` and `{KEY}` means
`HS`. This file holds only what is specific to ZenaQuiet-Headset. If something here contradicts the
shared procedure, this file wins for ZenaQuiet-Headset; say so in chat.

## Configuration

Update this block when settings change. The procedure and `tools/wiki_jira.py` read it.

```yaml
product: ZenaQuiet-Headset
project_key: HS # Jira name: ZenaQuiet-Headset
today: "" # ISO date, e.g. 2026-10-07. If blank, use the system date.
lookahead_days: 14 # "due soon" window
stale_days: 14 # no update for this many days = stale
overload_factor: 1.5 # team load above this × its average = overloaded
report_max_rows: 30 # risk rows shown in the report; all HIGH are always shown
```

Stage windows: `reference.md` → `## Stage schedule`, ZenaQuiet-Headset column.

## Product-specific notes

None yet. Add rules here that apply only to ZenaQuiet-Headset; everything shared goes in
`knowledge/product-procedure.md`.
