# Log

One line per change, newest first.

2026-10-23 · updated · [[ZenaQuiet-Pro2/INDEX]], [[ZenaQuiet-Beacon/INDEX]], [[ZenaQuiet-Headset/INDEX]], [[ZenaQuiet-Mask/INDEX]], [[ZenaQuiet-Research/INDEX]], CLAUDE.md, tools/INDEX.md, tools/wiki_jira.py · human agreed: reports now read Jira comments so the AI knows what engineers are discussing; `comment` added to Fields to fetch (Research label renamed from "Fields:"); new Step 8b (Research 7b) "Engineering discussion" and report subsection; "comment vs field" hygiene rule; `normalize` keeps comments (plain text, redacted) in issues_full.json only, never in snapshots

2026-10-19 · updated · [[ZenaQuiet-Pro2/INDEX]], [[ZenaQuiet-Beacon/INDEX]], [[ZenaQuiet-Headset/INDEX]], [[ZenaQuiet-Mask/INDEX]], [[reference]], tools/INDEX.md, tools/wiki_jira.py · human decided: a Subtask's team comes from its assignee (reference ## People), not the title bracket; Data Hygiene drops Subtask prefix rows, adds "no assignee" (one row per Story) and "assignee not in reference.md"; team load gains an Unassigned row (tested on 2026-10-19 snapshots: prefix rows Pro2 41 → 0, Beacon 38 → 0, Mask 8 → 0; Headset 89 no-assignee rows for 402 Subtasks)

2026-10-19 · updated · [[portfolio/2026-10-19-rollup]], [[overview]] · human asked for a redo in the new format: 6b rewritten as one plain sentence per risk (12 rows; Headset PCBs ~35 working days late, High); Beacon RED in Jira (BC-141 filed under an EVT Story with DVT dates); differences vs the morning in section 8; online copy republished
2026-10-19 · updated · tools/wiki_jira.py · `sources`: clearer "delay unknown" reasons (e.g. "waiting on a decision" instead of "depends on other"); same wording applied to the five 2026-10-19 reports
2026-10-19 · updated · [[ZenaQuiet-Pro2/jira/2026-10-19-jira]], [[ZenaQuiet-Beacon/jira/2026-10-19-jira]], [[ZenaQuiet-Headset/jira/2026-10-19-jira]], [[ZenaQuiet-Mask/jira/2026-10-19-jira]], [[ZenaQuiet-Research/jira/2026-10-19-jira]], data/<project>/2026-10-19.json, project overviews · human asked for a redo with plain-sentence risk tables; Jira re-read in the afternoon (Pro2 344 → 350; Beacon RED from BC-141; Headset RED with sources); changes vs the morning listed in each report's Data Gaps

2026-10-19 · updated · [[portfolio/INDEX]], [[ZenaQuiet-Pro2/INDEX]], [[ZenaQuiet-Beacon/INDEX]], [[ZenaQuiet-Headset/INDEX]], [[ZenaQuiet-Mask/INDEX]], [[ZenaQuiet-Research/INDEX]], CLAUDE.md, tools/INDEX.md, tools/wiki_jira.py · human asked: risks from threads shown as plain sentences (what slips, delay in working days, root cause, fix) instead of rule codes; helpers record impact, root cause step and fix; `sources` writes sources_plain.md with delay in working days; helper summary lists one line per risk (tested; sources_register.md unchanged)

2026-10-19 · created · [[portfolio/2026-10-19-rollup]] · weekly roll-up with first section 6b (risks from threads/transcripts): Jira says 4 of 4 on track, Headset RED with sources (PCBs late); purchasing pipeline; GPU rental unassigned; updated [[overview]] (portfolio line and all five paragraphs); online copy republished
2026-10-19 · updated · [[reference]] · People: added Sajjad Asif (CTO, purchase approver; email from company directory, unconfirmed)
2026-10-19 · created · [[ZenaQuiet-Research/jira/2026-10-19-jira]], data/ZenaQuiet-Research/2026-10-19.json · weekly report (20 issues); chip decision moved to 2026-10-20; 5 source risks; AMBER; updated [[ZenaQuiet-Research/overview]]
2026-10-19 · created · [[ZenaQuiet-Mask/jira/2026-10-19-jira]], data/ZenaQuiet-Mask/2026-10-19.json · weekly report (38 issues; 8 Stories became Subtasks); POC, 112 days to gate, readiness 9.5%, AMBER; 5 source risks; updated [[ZenaQuiet-Mask/overview]]
2026-10-19 · created · [[ZenaQuiet-Headset/jira/2026-10-19-jira]], data/ZenaQuiet-Headset/2026-10-19.json · weekly report (558 issues); POC, 112 days to gate, readiness 20.8% raw, RED with sources (PCBs late, HIGH); updated [[ZenaQuiet-Headset/overview]]
2026-10-19 · created · [[ZenaQuiet-Beacon/jira/2026-10-19-jira]], data/ZenaQuiet-Beacon/2026-10-19.json · weekly report (146 issues, +14, −1); EVT, 112 days to gate, readiness 47.2%, AMBER; 7 source risks; updated [[ZenaQuiet-Beacon/overview]]
2026-10-19 · created · [[ZenaQuiet-Pro2/jira/2026-10-19-jira]], data/ZenaQuiet-Pro2/2026-10-19.json · weekly report (344 issues, +15); EVT, 112 days to gate, readiness 29.7%, AMBER; hinge samples late for PRO2-420 (P1); updated [[ZenaQuiet-Pro2/overview]]

2026-10-19 · updated · CLAUDE.md, [[reference]], [[ZenaQuiet-Pro2/INDEX]], [[ZenaQuiet-Beacon/INDEX]], [[ZenaQuiet-Headset/INDEX]], [[ZenaQuiet-Mask/INDEX]], [[ZenaQuiet-Research/INDEX]], [[portfolio/INDEX]], tools/INDEX.md, tools/wiki_jira.py · human agreed: reports now read raw/threads and raw/transcripts as risk sources; new rules P1–P5 and S1; purchasing lead times (14+3+5 working days), holiday calendar (Tết 2027-02-04 → 02-12 assumed) and sourcing rule in reference; Step 2b, Order-this-week table and self-check item in every project INDEX; portfolio section 6b; new `sources` command (tested on the 2026-10-19 purchase thread, Jira-only outputs unchanged)

2026-10-15 · updated · tools/wiki_jira.py, tools/INDEX.md · human agreed: `diff` now lists issue links added and removed (checked: finds RS-16 → BC-234 in both the Research and Beacon diffs; other diff sections unchanged)
2026-10-15 · updated · [[ZenaQuiet-Research/INDEX]] · human agreed: product-link note now says one RS ticket links to a product (RS-16 → BC-234)
2026-10-15 · updated · [[reference]] · human agreed: Beacon line no longer cites deleted BC-106; adds sound masking (BC-234) and BC-107's new name; cluster-size sources now BC-101, BC-107, BC-56, BC-194 (12) vs BC-50 (16)

2026-10-15 · created · [[portfolio/2026-10-15-rollup]] · weekly roll-up: 4 of 4 on track (all low confidence); no Story closed in any product since 2026-10-13; Mask POC forecast +208d, Headset +112d; no FLAG lines; updated [[overview]] (portfolio line and all five project paragraphs); online copy republished
2026-10-15 · created · [[ZenaQuiet-Research/jira/2026-10-15-jira]], data/ZenaQuiet-Research/2026-10-15.json · weekly report (20 issues); first product link RS-16 → BC-234; chip decision RS-1/RS-2 due 2026-10-16; AMBER; updated [[ZenaQuiet-Research/overview]]
2026-10-15 · created · [[ZenaQuiet-Beacon/jira/2026-10-15-jira]], data/ZenaQuiet-Beacon/2026-10-15.json · weekly report (133 issues, +1: Epic BC-234); EVT, 116 days to gate, readiness 44.4%, AMBER; BC-107 renamed and owned; updated [[ZenaQuiet-Beacon/overview]]
2026-10-15 · created · [[ZenaQuiet-Headset/jira/2026-10-15-jira]], data/ZenaQuiet-Headset/2026-10-15.json · weekly report (558 issues, no change); POC, 116 days to gate, readiness 20.8% raw, AMBER; updated [[ZenaQuiet-Headset/overview]]
2026-10-15 · created · [[ZenaQuiet-Mask/jira/2026-10-15-jira]], data/ZenaQuiet-Mask/2026-10-15.json · weekly report (38 issues, no change); POC, 116 days to gate, readiness 6.9%, AMBER; updated [[ZenaQuiet-Mask/overview]]
2026-10-15 · created · [[ZenaQuiet-Pro2/jira/2026-10-15-jira]], data/ZenaQuiet-Pro2/2026-10-15.json · weekly report (329 issues, no change); EVT, 116 days to gate, readiness 27.9%, AMBER; first overdue item PRO2-23; updated [[ZenaQuiet-Pro2/overview]]

2026-10-14 · created · [[portfolio/2026-10-14-rollup]] · weekly roll-up: 4 of 4 on track (all low confidence); Mask POC forecast +193d, Headset +101d; no FLAG lines; updated portfolio line in [[overview]]
2026-10-14 · updated · [[reference]] · added Thang Pham (reporter of HS-47) under ## People, not in company directory
2026-10-14 · created · [[ZenaQuiet-Research/jira/2026-10-14-jira]], data/ZenaQuiet-Research/2026-10-14.json · weekly report (20 issues, no change); 0 product links, RS-1/RS-2 chip decision due 2026-10-16, AMBER
2026-10-14 · created · [[ZenaQuiet-Beacon/jira/2026-10-14-jira]], data/ZenaQuiet-Beacon/2026-10-14.json · weekly report (132 issues); EVT, 117 days to gate, readiness 44.4%, AMBER; BC-164 started, BC-229 +5d, BC-107 renamed
2026-10-14 · created · [[ZenaQuiet-Headset/jira/2026-10-14-jira]], data/ZenaQuiet-Headset/2026-10-14.json · weekly report (558 issues, no change); POC, 117 days to gate, readiness 20.8% raw, AMBER
2026-10-14 · created · [[ZenaQuiet-Mask/jira/2026-10-14-jira]], data/ZenaQuiet-Mask/2026-10-14.json · weekly report (38 issues, no change); POC, 117 days to gate, readiness 6.9%, AMBER
2026-10-14 · created · [[ZenaQuiet-Pro2/jira/2026-10-14-jira]], data/ZenaQuiet-Pro2/2026-10-14.json · weekly report (329 issues, no change); EVT, 117 days to gate, readiness 27.9%, AMBER

2026-10-13 · updated · [[portfolio/2026-10-13-rollup]], [[portfolio/INDEX]] · human asked: added "What the numbers mean" note (Raw, Adjusted, Expected, with examples) under the Products table; template now requires it; online copy republished with the same note

2026-10-13 · updated · [[portfolio/INDEX]], [[portfolio/2026-10-13-rollup]], [[overview]] · human decided same-day-closed Stories count as progress (exclude_same_day_closed: false); roll-up re-run: Pro2 0% → 27.9%, Beacon 2.8% → 44.4%, Mask 0% → 6.9%, all four On track (low confidence); online copy republished

2026-10-13 · updated · [[portfolio/2026-10-13-rollup]], [[overview]] · human asked for a redo: rollup re-run on today's snapshots (numbers unchanged), page rewritten in one pass per [[portfolio/INDEX]]; overview line now in the INDEX format (2 of 4 on track, low confidence)

2026-10-13 · updated · [[portfolio/2026-10-13-rollup]], [[overview]] · regenerated from the new Beacon snapshot: Beacon At risk → On track (low confidence), adjusted 0% → 2.8%, POC slip +15d → on time (only because BC-82, BC-97, BC-185 left Jira); earlier figures kept in Data Gaps
2026-10-13 · updated · [[ZenaQuiet-Beacon/jira/2026-10-13-jira]], [[ZenaQuiet-Beacon/overview]], data/ZenaQuiet-Beacon/2026-10-13.json · human asked for a redo; Jira changed during the day (Epic BC-106 tree and BC-113 to BC-117 removed, BC-233 added, BC-206 to BC-210 started, BC-209 Done): 149 → 132 issues, readiness 38.5% → 44.4%, AMBER; changes listed in the report's section 7

2026-10-13 · updated · [[portfolio/2026-10-13-rollup]], [[portfolio/INDEX]], tools/wiki_jira.py, tools/INDEX.md, CLAUDE.md · human agreed: slip now measured against the stage schedule in [[reference]] (plan), not a 2026-10-13 snapshot; baseline setting removed; stage rows show slip vs plan (Pro2 POC +16d, Beacon POC +15d); snapshot comparison kept as "dates moved this week" warning; page regenerated

2026-10-13 · created · [[portfolio/2026-10-13-rollup]] · first portfolio roll-up (baseline week): Pro2, Beacon, Mask At risk; Headset On track at low confidence; shared gate 2027-02-08; added portfolio line to [[overview]]
2026-10-13 · created · [[portfolio/INDEX]] · roll-up instructions, baseline 2026-10-13 (re-planned dates, human chose), metric definitions, page template, self-check
2026-10-13 · updated · CLAUDE.md · human agreed: portfolio/ in folder map and file-name table; main session step 3 now writes the roll-up
2026-10-13 · updated · tools/wiki_jira.py, tools/INDEX.md · human agreed: new `rollup` command; analyze results.json gains issue_stage (other outputs unchanged, checked on all 5 snapshots)

2026-10-13 · updated · tools/wiki_jira.py, tools/INDEX.md · human agreed: register Team column shows Subtask teams/label (not issue type); gate-impact text is stage-aware (later-stage work no longer "threatens gate"); diff adds title and assignee changes; Research team load counted from labels. Product results unchanged (checked on all 5 snapshots); reported duplicate HS-320 register row not reproduced
2026-10-13 · updated · [[ZenaQuiet-Headset/jira/2026-10-13-jira]] · reassignments corrected 17 → 14 (new diff output)
2026-10-13 · updated · [[reference]] · human agreed: filled ## Projects lines for Beacon, Headset, Mask (from project overviews); Beacon cluster size 12 vs 16 flagged

2026-10-13 · created · [[overview]] · was empty; one paragraph per active project from the 2026-10-13 reports
2026-10-13 · created · [[ZenaQuiet-Research/jira/2026-10-13-jira]] · weekly report (20 issues, no change); 0% product links, AMBER; filled [[ZenaQuiet-Research/overview]] (was empty)
2026-10-13 · created · [[ZenaQuiet-Beacon/jira/2026-10-13-jira]] · weekly report (149 issues, +15 EE Subtasks); EVT, 118 days to gate, readiness 38.5% (re-tagging), AMBER; filled [[ZenaQuiet-Beacon/overview]] (was empty)
2026-10-13 · created · [[ZenaQuiet-Headset/jira/2026-10-13-jira]] · weekly report (558 issues, no change in count); POC, 118 days to gate, readiness 21%, AMBER (was RED; HS-326 re-dated, not delivered); filled [[ZenaQuiet-Headset/overview]] (was empty)
2026-10-13 · created · [[ZenaQuiet-Mask/jira/2026-10-13-jira]] · weekly report (38 issues, no change in count); POC, 118 days to gate, readiness 7%, AMBER; bulk date reset flagged; updated [[ZenaQuiet-Mask/overview]]
2026-10-13 · created · [[ZenaQuiet-Pro2/jira/2026-10-13-jira]] · weekly report (329 issues, no change in count); EVT, 118 days to gate, readiness 28% (re-tagging), AMBER; PARTIAL raw capture (see Data Gaps); updated [[ZenaQuiet-Pro2/overview]]
2026-10-13 · created · data/<project>/2026-10-13.json × 5 · weekly Jira snapshots

2026-10-12 · updated · [[reference]] · People: added Huynh Minh Tuan, CaoTienDat (Electronic_Electrical; from M365 directory, unconfirmed)
2026-10-12 · created · [[ZenaQuiet-Research/jira/2026-10-12-jira]] · first weekly report (20 issues); support team, link coverage 0%, AMBER
2026-10-12 · created · [[ZenaQuiet-Beacon/jira/2026-10-12-jira]] · weekly report (134 issues, no change in count); EVT, 119 days to gate, readiness 5%, AMBER
2026-10-12 · created · [[ZenaQuiet-Headset/jira/2026-10-12-jira]] · first weekly report (558 issues); POC, 119 days to gate, readiness 21%, RED (one HIGH: HS-326)
2026-10-12 · note · CLAUDE.md · human set all five projects to Active Yes; first multi-project run with one helper per project

2026-10-12 · created · data/ZenaQuiet-Pro2/2026-10-12.json, data/ZenaQuiet-Mask/2026-10-12.json · first Jira snapshots (from today's report runs)
2026-10-12 · created · tools/wiki_jira.py, tools/INDEX.md · shared normalize/analyze/diff script; reproduces today's Pro2 and Mask counts, severities and health
2026-10-12 · updated · CLAUDE.md · added ## Running many projects (one helper per project, summary format), tools/ and data/ in folder map, tools/INDEX.md in How instructions work

2026-10-12 · updated · [[reference]] · layout only (human asked): title, contents, section dividers, aligned tables, unconfirmed people in own table; no facts changed

2026-10-12 · updated · [[reference]] · People: added Bui Minh Tuan, Khanh Duong, Phan Thi Anh Nhut (Industrial_Design; from M365 directory, unconfirmed)

2026-10-12 · created · [[ZenaQuiet-Mask/jira/2026-10-12-jira]] · first weekly status report from live Jira (38 issues); POC, 119 days to gate, readiness 7%, AMBER
2026-10-12 · created · [[ZenaQuiet-Pro2/jira/2026-10-12-jira]] · weekly status report from live Jira (329 issues, +6 Subtasks); EVT, 119 days to gate, readiness 3%, AMBER

2026-10-12 · updated · [[glossary]] · added KN95
2026-10-12 · created · [[overview]] · one paragraph each for the active projects, Pro2 and Mask
2026-10-12 · updated · [[ZenaQuiet-Mask/overview]] · written from live Jira (38 issues, 9 Epics); replaces stub
2026-10-12 · updated · [[ZenaQuiet-Pro2/overview]] · added what it is, where it stands, all Epics (from 2026-10-10 report)
2026-10-12 · note · CLAUDE.md · human changed Active projects: Pro2 and Mask Yes; Headset, Beacon, Research No
2026-10-12 · updated · ZenaQuiet-Research/INDEX.md · rewritten as a support team: no own stages; measured against the products it supports (Jira link > product named in title (inferred) > Unlinked); new checks D7, R11–R13; link coverage in Health
2026-10-12 · updated · knowledge/INDEX.md · weekly reports: page type renamed to report, saved in <project>/jira/ (matches CLAUDE.md)
2026-10-12 · updated · [[reference]] · Jira projects: keys confirmed in Jira: Headset HS, Mask MK, Research RS
2026-10-12 · created · ZenaQuiet-Research/INDEX.md · copied from ZenaQuiet-Pro2/INDEX.md, adapted to ZenaQuiet-Research (Jira key RS); added note: no stage schedule, stage-based checks skipped
2026-10-12 · created · ZenaQuiet-Mask/INDEX.md · copied from ZenaQuiet-Pro2/INDEX.md, adapted to ZenaQuiet-Mask (Jira key MK)
2026-10-12 · created · ZenaQuiet-Headset/INDEX.md · copied from ZenaQuiet-Pro2/INDEX.md, adapted to ZenaQuiet-Headset (Jira key HS)
