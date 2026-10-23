# ZenaQuiet-Beacon — Instructions

These instructions apply only to `knowledge/ZenaQuiet-Beacon/`. They add to `knowledge/INDEX.md`.

**Follow `knowledge/product-procedure.md`**, the procedure shared by every product: role, steps,
rules, report and self-check. In it, `{product}` means `ZenaQuiet-Beacon` and `{KEY}` means
`BC`. This file holds only what is specific to ZenaQuiet-Beacon. If something here contradicts the
shared procedure, this file wins for ZenaQuiet-Beacon; say so in chat.

## Configuration

Update this block when settings change. The procedure and `tools/wiki_jira.py` read it.

```yaml
product: ZenaQuiet-Beacon
project_key: BC # Jira name: ZenaQuiet-Beacon
today: "" # ISO date, e.g. 2026-10-07. If blank, use the system date.
lookahead_days: 14 # "due soon" window
stale_days: 14 # no update for this many days = stale
overload_factor: 1.5 # team load above this × its average = overloaded
report_max_rows: 30 # risk rows shown in the report; all HIGH are always shown
```

Stage windows: `reference.md` → `## Stage schedule`, ZenaQuiet-Beacon column.

## Product-specific notes

None yet. Add rules here that apply only to ZenaQuiet-Beacon; everything shared goes in
`knowledge/product-procedure.md`.
