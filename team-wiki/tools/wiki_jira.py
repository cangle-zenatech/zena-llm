#!/usr/bin/env python3
"""Shared Jira analysis for the team wiki weekly status reports.

Implements the procedure in knowledge/<project>/INDEX.md (Steps 3-7): normalize, date checks D1-D6,
risks R1-R10, severity, metrics, team load, health. It does NOT call Jira and does NOT write wiki
pages: the agent pulls Jira, runs this, then writes the report from the outputs.

Settings come from the wiki itself, never from this file:
  - stage windows, team codes, people/emails  -> knowledge/reference.md
  - today / lookahead_days / stale_days / overload_factor -> the yaml block in knowledge/<project>/INDEX.md

Commands (run with python3 -I):
  normalize --project ZenaQuiet-Pro2 --raw-dir WORK [--date D] [--start-field F] [--sprint-field F]
      Reads every *.json in WORK that holds Jira search results ({"issues": {"nodes": [...]}} or
      {"issues": [...]}) and writes:
        WORK/issues_full.json            all fields incl. description (temporary, for Step 8 reading)
        data/<project>/<D>.json          snapshot: no descriptions, secrets redacted (kept for diffs)
  analyze --project ZenaQuiet-Pro2 --work WORK [--date D]
      Reads the snapshot for D and writes to WORK: results.json, register.md, hygiene.md,
      heatmap.md, epics.md, stages.md, notes.md (things for a human look, not rule hits), summary.txt
  diff --project ZenaQuiet-Pro2 --work WORK [--date D]
      Compares the snapshot for D with the newest earlier snapshot; writes WORK/diff.md
  rollup --work WORK [--date D]
      Portfolio roll-up across every active product with a stage schedule (settings: yaml block in
      knowledge/portfolio/INDEX.md); writes WORK/rollup*.md, rollup.json, rollup_summary.txt
"""
import argparse, calendar, glob, json, os, re, sys
from collections import Counter, defaultdict
from datetime import date, timedelta

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # team-wiki/
KNOW = os.path.join(ROOT, 'knowledge')
DATA = os.path.join(ROOT, 'data')
ORDER = ['POC', 'EVT', 'DVT', 'PVT', 'MP']
BROWSE = 'https://epazz.atlassian.net/browse/'


def D(s):
    return date.fromisoformat(s[:10]) if s else None


# ----------------------------------------------------------------- wiki settings
def md_tables(text):
    """Yield (heading, rows) for every markdown table; rows are lists of cell strings."""
    head, cur, out = '', None, []
    for line in text.splitlines():
        if line.startswith('#'):
            head = line.lstrip('#').strip()
        if line.strip().startswith('|'):
            cells = [c.strip() for c in line.strip().strip('|').split('|')]
            if cur is None:
                cur = (head, [])
                out.append(cur)
            if not all(re.fullmatch(r':?-+:?', c) for c in cells):
                cur[1].append(cells)
        else:
            cur = None
    return out


def load_reference(folder):
    text = open(os.path.join(KNOW, 'reference.md'), encoding='utf-8').read()
    stages, teams, email = {}, {}, {}
    for head, rows in md_tables(text):
        hdr = rows[0] if rows else []
        if head.startswith('Stage schedule'):
            col = next((i for i, h in enumerate(hdr) if h.split(' ')[0] == folder), None)
            if col is not None:
                for r in rows[1:]:
                    a, b = [x.strip() for x in r[col].split('→')]
                    stages[r[0].upper()] = (D(a), D(b))
        elif head == 'Teams' and hdr and hdr[0] == 'Code':
            for r in rows[1:]:
                teams[r[0]] = r[1]
        elif 'Jira name' in hdr and 'Email' in hdr:
            j, e = hdr.index('Jira name'), hdr.index('Email')
            for r in rows[1:]:
                email[r[j]] = r[e]
    m = re.search(r'\*\*Email:\*\*\s*(\S+).*?\*\*Jira name:\*\*\s*([^\n]+)', text, re.S)
    if m:
        email[m.group(2).strip()] = m.group(1).strip()
    return stages, teams, email


def load_config(folder):
    path = os.path.join(KNOW, folder, 'INDEX.md')
    text = open(path, encoding='utf-8').read()
    block = re.search(r'```yaml\n(.*?)```', text, re.S)
    cfg = {}
    for line in (block.group(1) if block else '').splitlines():
        m = re.match(r'\s*(\w+):\s*("?)([^"#]*)\2', line)
        if m:
            cfg[m.group(1)] = m.group(3).strip()
    return cfg


# ----------------------------------------------------------------- redaction
SECRET = [
    (re.compile(r'(?i)\b(password|passwd|pwd|pass|token|api[_ -]?key|secret|bearer)\b\s*[:=]\s*\S+'), r'\1: [redacted]'),
    (re.compile(r'\b[A-Za-z0-9_\-]{32,}\b'), '[redacted]'),
    (re.compile(r'\b[\w.+-]+@(?!zenatech\.com\b)[\w-]+\.[\w.]+\b'), '[email redacted]'),
    (re.compile(r'(?<!\d)\+?\d[\d \-().]{8,}\d(?!\d)'), '[number redacted]'),
]


def redact(s):
    if not s:
        return s
    for rx, rep in SECRET:
        s = rx.sub(rep, s)
    return s


# ----------------------------------------------------------------- normalize
def cmd_normalize(a):
    nodes = []
    for f in sorted(glob.glob(os.path.join(a.raw_dir, '*.json'))):
        try:
            d = json.load(open(f, encoding='utf-8'))
        except Exception:
            continue
        iss = d.get('issues') if isinstance(d, dict) else None
        if isinstance(iss, dict):
            iss = iss.get('nodes')
        if isinstance(iss, list) and iss and 'fields' in iss[0]:
            nodes += iss
    seen, out = set(), []
    for n in nodes:
        if n['key'] in seen:
            continue
        seen.add(n['key'])
        f = n['fields']
        nm = lambda u: u.get('displayName') if u else None
        links = []
        for l in f.get('issuelinks') or []:
            t = l['type']
            for side, lab, dirn in (('outwardIssue', t['outward'], 'out'), ('inwardIssue', t['inward'], 'in')):
                if side in l:
                    o = l[side]
                    links.append(dict(dir=dirn, label=lab, type=t['name'], key=o['key'],
                                      scat=o['fields']['status']['statusCategory']['key']))
        out.append(dict(
            key=n['key'], summary=f['summary'], type=f['issuetype']['name'], status=f['status']['name'],
            scat=f['status']['statusCategory']['key'], assignee=nm(f.get('assignee')), reporter=nm(f.get('reporter')),
            start=f.get(a.start_field), due=f.get('duedate'),
            sprints=[[s.get('name'), s.get('state')] for s in (f.get(a.sprint_field) or [])],
            parent=(f.get('parent') or {}).get('key'), subtasks=[s['key'] for s in f.get('subtasks') or []],
            links=links, created=f['created'][:10], updated=f['updated'][:10],
            resolved=(f.get('resolutiondate') or '')[:10] or None, labels=f.get('labels') or [],
            desc=f.get('description') or ''))
    out.sort(key=lambda o: int(o['key'].split('-')[1]))
    json.dump(out, open(os.path.join(a.raw_dir, 'issues_full.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
    snap = [dict({k: v for k, v in o.items() if k != 'desc'}, summary=redact(o['summary'])) for o in out]
    os.makedirs(os.path.join(DATA, a.project), exist_ok=True)
    sp = os.path.join(DATA, a.project, f'{a.date}.json')
    json.dump(dict(project=a.project, date=a.date, start_field=a.start_field, sprint_field=a.sprint_field,
                   count=len(snap), issues=snap), open(sp, 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
    print(f'{len(out)} unique issues', dict(Counter(o['type'] for o in out)), '->', sp)


def load_snapshot(project, day):
    p = os.path.join(DATA, project, f'{day}.json')
    if not os.path.exists(p):
        sys.exit(f'No snapshot {p}. Run "normalize" for this project and date first.')
    return json.load(open(p, encoding='utf-8'))['issues']


# ----------------------------------------------------------------- analyze
def cmd_analyze(a):
    folder = a.project
    cfg = load_config(folder)
    TODAY = D(a.date)
    LOOK = int(cfg.get('lookahead_days') or 14)
    STALE = int(cfg.get('stale_days') or 14)
    OVF = float(cfg.get('overload_factor') or 1.5)
    STG, TEAMMAP, EMAIL = load_reference(folder)
    TEAMS = set(TEAMMAP) or {'FW', 'ME', 'EE', 'SW', 'ID', 'AC', 'FA'}
    has_stages = bool(STG)
    I = load_snapshot(folder, a.date)
    by = {o['key']: o for o in I}
    kk = lambda x: int(x.split('-')[1])
    for o in I:
        o['st'], o['du'], o['upd'], o['cr'] = D(o['start']), D(o['due']), D(o['updated']), D(o['created'])
        o['state'] = {'done': 'Done', 'indeterminate': 'In Progress', 'new': 'To Do'}[o['scat']]
    subtype = next((o['type'] for o in I if o['type'].lower().replace('-', '') == 'subtask'), 'Subtask')
    hyg = []

    def stage_of(title):
        tags = re.findall(r'\[([^\]]*)\]', title)
        for i, t in enumerate(tags):
            m = re.match(r'^(POC|EVT|DVT|PVT|MP)(-\d+)?(:.*)?$', t.replace(' ', '').upper())
            if m:
                return m.group(1), i, t
        return 'UNKNOWN', None, None

    def team_of(title):
        tags = re.findall(r'\[([^\]]*)\]', title)
        for i, t in enumerate(tags):
            for part in re.split(r'[:/]', t.replace(' ', '').upper()):
                if part in TEAMS:
                    return part, (i == 0 and title.strip().startswith('[' + t + ']') and t.replace(' ', '').upper() == part)
        return 'UNKNOWN', None

    FLAG = re.compile(r'\[(TO BE REMOVED|TO BE DELETED|NEED CONFIRMING|DEFERRED)\]', re.I)
    for o in I:
        t = o['summary']
        o['team'], o['stage'] = '—', '—'
        if o['type'] == 'Story':
            s, i, tag = stage_of(t)
            o['stage'], o['team'] = s, 'Story'
            if s == 'UNKNOWN':
                hyg.append((o['key'], 'prefix', 'No stage prefix in Story title'))
            elif i > 0 or not t.strip().startswith('[' + tag + ']'):
                pre = re.match(r'\s*(\[[^\]]*\])', t)
                hyg.append((o['key'], 'prefix', f'Title starts with "{pre.group(1) if pre else t[:15]}" before the stage tag'))
        if o['type'] == subtype:
            tm, clean = team_of(t)
            o['team'] = tm
            if tm == 'UNKNOWN':
                hyg.append((o['key'], 'prefix', 'No team prefix in Subtask title'))
            elif not clean:
                hyg.append((o['key'], 'prefix', f'Team tag is not a clean leading [{tm}] prefix'))
        m = FLAG.search(t)
        if m:
            hyg.append((o['key'], 'flag-tag', f'Title tagged "{m.group(0)}" ' +
                        ('— issue is Done but still in Jira' if o['state'] == 'Done' else f'but issue is still {o["state"]}')))
    for o in I:
        if o['type'] == subtype:
            p = by.get(o['parent'])
            o['stage'] = p['stage'] if p else 'UNKNOWN'
    orph = []
    for o in I:
        p = by.get(o['parent'])
        if o['type'] == 'Story' and (not p or p['type'] != 'Epic'):
            orph.append(o['key']); hyg.append((o['key'], 'orphan', 'Story has no Epic parent'))
        if o['type'] == subtype and (not p or p['type'] != 'Story'):
            orph.append(o['key']); hyg.append((o['key'], 'orphan', f'Subtask parent {o["parent"]} is not a Story'))

    def epic_of(o):
        if o['type'] == 'Epic': return o['key']
        if o['type'] == 'Story': return o['parent']
        p = by.get(o['parent']); return p['parent'] if p else None

    stories = [o for o in I if o['type'] == 'Story']
    subs = [o for o in I if o['type'] == subtype]
    epics = [o for o in I if o['type'] == 'Epic']
    for s in stories:
        s['kids'] = [by[k] for k in s['subtasks'] if k in by]
    # team shown in the register, and the team used for load when there are no Subtasks to count.
    # Subtask: its title prefix. Story: its Subtasks' teams; else its team label; else its title prefix.
    # Epic: its team label, else '—'. Labels map to codes through reference.md ## Teams.
    LABEL2CODE = {v.lower(): k for k, v in TEAMMAP.items()}
    def label_team(o):
        return next((LABEL2CODE[l.lower()] for l in o.get('labels') or [] if l.lower() in LABEL2CODE), None)
    for o in I:
        if o['type'] == subtype:
            o['tdisp'] = o['team']
        elif o['type'] == 'Story':
            kt = sorted({s['team'] for s in o['kids'] if s['team'] != 'UNKNOWN'})
            pt = team_of(o['summary'])[0]
            o['tdisp'] = ', '.join(kt) if kt else (label_team(o) or (pt if pt != 'UNKNOWN' else '—'))
        else:
            o['tdisp'] = label_team(o) or '—'
    # notes: not D/R rules, but worth a human look; the agent decides what goes in the report
    notes = []
    pkey = I[0]['key'].split('-')[0] if I else ''
    for e in epics:
        if not any(s['parent'] == e['key'] for s in stories):
            notes.append((e['key'], 'empty-epic', 'Epic has no Stories'))
    for o in I:
        if o['type'] == 'Story':
            m = re.match(r'\s*\[([^\]]*)\]', o['summary'])
            if m and ':' in m.group(1):
                notes.append((o['key'], 'stage-tag', f'Combined stage tag "[{m.group(1)}]"; read as {o["stage"]}'))
        for l in o['links']:
            if l['key'].split('-')[0] != pkey:
                notes.append((o['key'], 'cross-project-link', f'"{l["label"]}" {l["key"]}'))
        for sp_name, sp_state in o.get('sprints') or []:
            if o['state'] != 'Done' and sp_name and re.search(r'\[(POC|EVT|DVT|PVT|MP)\]', sp_name) and \
                    not sp_name.upper().startswith('[' + str(o['stage'])) and o['type'] != 'Epic' and sp_state == 'active':
                notes.append((o['key'], 'sprint-stage', f'Open item in active sprint "{sp_name}" but stage is {o["stage"]}'))

    # Step 4 position
    if has_stages:
        # boundary dates are inclusive of the end date, so on a shared boundary the earlier stage wins
        inside = [k for k in ORDER if k in STG and STG[k][0] <= TODAY <= STG[k][1]]
        cur = inside[0] if inside else None
        if cur is None:
            cur = 'MP' if TODAY > STG['MP'][1] else 'POC'
        nxt = ORDER[ORDER.index(cur) + 1] if cur != 'MP' else None
        gate = STG[cur][1]
        dtg = (gate - TODAY).days
        MP_END = STG['MP'][1]
    else:
        cur = nxt = gate = dtg = MP_END = None

    # Step 5 date checks
    dd = []
    for o in I:
        if o['state'] == 'Done': continue
        k = o['key']
        if o['type'] == 'Story':
            e = by.get(o['parent'])
            if e:
                if o['st'] and e['st'] and o['st'] < e['st']: dd.append((k, 'D1', f"start {o['st']} < Epic {e['key']} start {e['st']} ({(e['st']-o['st']).days}d)"))
                if o['du'] and e['du'] and o['du'] > e['du']: dd.append((k, 'D1', f"due {o['du']} > Epic {e['key']} due {e['du']} (+{(o['du']-e['du']).days}d)"))
            if o['stage'] in STG:
                s0, s1 = STG[o['stage']]
                if o['st'] and o['st'] < s0: dd.append((k, 'D3', f"start {o['st']} < {o['stage']} start {s0} ({(s0-o['st']).days}d)"))
                if o['du'] and o['du'] > s1: dd.append((k, 'D3', f"due {o['du']} > {o['stage']} end {s1} (+{(o['du']-s1).days}d)"))
        if o['type'] == subtype:
            s = by.get(o['parent'])
            if s:
                if o['st'] and s['st'] and o['st'] < s['st']: dd.append((k, 'D2', f"start {o['st']} < Story {s['key']} start {s['st']} ({(s['st']-o['st']).days}d)"))
                if o['du'] and s['du'] and o['du'] > s['du']: dd.append((k, 'D2', f"due {o['du']} > Story {s['key']} due {s['du']} (+{(o['du']-s['du']).days}d)"))
        if o['st'] and o['du'] and o['st'] > o['du']: dd.append((k, 'D4', f"start {o['st']} > due {o['du']} ({(o['st']-o['du']).days}d)"))
        if not o['st'] or not o['du']:
            miss = 'start and due' if not o['st'] and not o['du'] else ('start' if not o['st'] else 'due')
            dd.append((k, 'D5', f'missing {miss}'))
        if MP_END and o['type'] == 'Epic' and o['du'] and o['du'] > MP_END: dd.append((k, 'D6', f"due {o['du']} > MP end {MP_END}"))

    # Step 6 risks
    R, info, sev, dl = defaultdict(list), defaultdict(list), {}, {}
    openi = [o for o in I if o['state'] != 'Done']
    for o in openi:
        k = o['key']
        if o['du'] and o['du'] < TODAY:
            R[k].append('R1'); dl[k] = (TODAY - o['du']).days; info[k].append(f"Due {o['du']}, {dl[k]}d late")
        if o['st'] and o['st'] < TODAY and o['state'] == 'To Do':
            R[k].append('R2'); info[k].append(f"Start date passed {(TODAY-o['st']).days}d ago, still To Do")
        if o['du'] and TODAY <= o['du'] <= TODAY + timedelta(LOOK) and o['state'] == 'To Do':
            R[k].append('R3')
            info[k].append(f"Due in {(o['du']-TODAY).days}d, not started" + (f"; gate buffer {(gate-o['du']).days}d" if gate else ''))
        if (TODAY - o['upd']).days >= STALE:
            R[k].append('R4'); info[k].append(f"Not updated for {(TODAY-o['upd']).days}d")
        if o['type'] == 'Story' and o['stage'] in STG and STG[o['stage']][1] < TODAY:
            R[k].append('R5'); info[k].append(f"{o['stage']} window ended {STG[o['stage']][1]}, Story not Done")
        p = by.get(o['parent']) if o['type'] != 'Epic' else None
        if p and o['du'] and p['du'] and o['du'] > p['du']:
            R[k].append('R6'); ov = (o['du'] - p['du']).days
            stg_end = STG[o['stage']][1] if o['stage'] in STG else None
            e = by.get(epic_of(o))
            o['r6high'] = bool((e and e['du'] and o['du'] > e['du']) or (stg_end and o['du'] > stg_end))
            info[k].append(f"Due {o['du']}, {ov}d after parent {p['key']} due {p['du']}" +
                           ('; parent is Done' if p['state'] == 'Done' else f'; parent slips ≥{ov}d') +
                           (f"; past {o['stage']} end {stg_end}" if stg_end and o['du'] > stg_end else ''))
        for l in o['links']:
            if l['label'] == 'is blocked by' and l['scat'] != 'done': R[k].append('R7'); info[k].append(f"Blocked by open {l['key']}")
            if l['label'] == 'blocks' and l['scat'] != 'done': R[k].append('R8'); info[k].append(f"Blocks open {l['key']}")
        if not o['assignee'] and (o['state'] == 'In Progress' or (o['du'] and o['du'] <= TODAY + timedelta(30))):
            R[k].append('R9'); info[k].append('No assignee')
        if has_stages and o['type'] == 'Story' and o['stage'] in (cur, nxt) and (STG[o['stage']][0] - TODAY).days <= 45:
            if not [s for s in o['kids'] if s['team'] in ('ME', 'EE', 'FA') and s['state'] != 'To Do']:
                R[k].append('R10')
                info[k].append(f"No ME/EE/FA Subtask started ({len(o['kids'])} Subtasks)" if o['kids'] else 'No Subtasks at all — work not broken down')
    for k, rs in R.items():
        R[k] = rs = list(dict.fromkeys(rs))
        o, s = by[k], 'LOW'
        if ('R1' in rs and dl[k] > 7) or 'R5' in rs: s = 'HIGH'
        if ('R7' in rs or 'R8' in rs) and o['du'] and gate and o['du'] < gate: s = 'HIGH'
        if 'R6' in rs and o.get('r6high'): s = 'HIGH'
        if s != 'HIGH' and any(r in rs for r in ('R1', 'R2', 'R3', 'R10', 'R6')): s = 'MEDIUM'
        sev[k] = s

    # Step 7 metrics
    pct = lambda n, d: round(100 * n / d, 1) if d else None
    M = {}
    M['story'] = (sum(s['state'] == 'Done' for s in stories), len(stories))
    M['sub'] = (sum(s['state'] == 'Done' for s in subs), len(subs))
    cs = [s for s in stories if s['stage'] == cur] if cur else []
    ns = [s for s in stories if s['stage'] == nxt] if nxt else []
    M['gate'] = (sum(s['state'] == 'Done' for s in cs), len(cs), sum(s['state'] == 'In Progress' for s in cs))
    M['gate_pct'] = pct(M['gate'][0], M['gate'][1])
    M['next'] = (sum(s['state'] != 'To Do' for s in ns), len(ns))
    r1 = [k for k in R if 'R1' in R[k]]
    M['overdue'] = (len(r1), round(sum(dl[k] for k in r1) / len(r1), 1) if r1 else 0)
    for r in ('R2', 'R3', 'R4', 'R5', 'R6', 'R9', 'R10'):
        M[r] = sorted([k for k in R if r in R[k]], key=kk)
    M['scope_added'] = sorted([s['key'] for s in stories if s['stage'] in STG and s['cr'] > STG[s['stage']][0]], key=kk)
    if cur:
        s0, s1 = STG[cur]
        exp = 100 * (TODAY - s0).days / (s1 - s0).days
        act = M['gate_pct'] or 0.0
        M['expected_vs_actual'] = (round(exp, 1), act, round(act - exp, 1))
        behind = exp - act
    else:
        behind = 0
    ep = []
    for e in epics:
        ch = [s for s in stories if s['parent'] == e['key']]
        sb = [x for s in ch for x in s['kids']]
        dues = [x['du'] for x in ch + sb if x['du']]
        mx = max(dues) if dues else None
        var = (mx - e['du']).days if (mx and e['du']) else None
        ep.append(dict(key=e['key'], title=e['summary'].strip(), state=e['state'], stories_done=sum(s['state'] == 'Done' for s in ch),
                       stories=len(ch), subs_done=sum(x['state'] == 'Done' for x in sb), subs=len(sb), start=e['st'], due=e['du'],
                       latest_child_due=mx, variance=var, assignee=e['assignee']))
    stg = []
    for st in ORDER + ['UNKNOWN']:
        ch = [s for s in stories if s['stage'] == st]
        sb = [x for s in ch for x in s['kids']]
        if ch:
            stg.append(dict(stage=st, stories_done=sum(s['state'] == 'Done' for s in ch), stories=len(ch),
                            subs_done=sum(x['state'] == 'Done' for x in sb), subs=len(sb), in_progress=sum(s['state'] == 'In Progress' for s in ch)))
    # team load
    # Products: open Subtasks, current month → MP end (project INDEX.md Step 7).
    # No stage schedule (Research): open items of every type, team from label or title prefix,
    # current month → the last due date (ZenaQuiet-Research/INDEX.md Team load).
    if has_stages:
        load_items = [(s, s['team']) for s in subs if s['state'] != 'Done']
        end = MP_END
    else:
        load_items = [(o, o['tdisp'] if o['tdisp'] in TEAMS else 'UNKNOWN') for o in openi]
        dues = [o['du'] for o, _ in load_items if o['du'] and o['du'] >= TODAY]
        end = max(dues) if dues else TODAY + timedelta(days=180)
    months, (y, m) = [], (TODAY.year, TODAY.month)
    while (y, m) <= (end.year, end.month):
        months.append((y, m)); m += 1
        if m == 13: y, m = y + 1, 1
    teams = sorted(TEAMS) + ['UNKNOWN']
    heat, undated, inverted = {t: [0] * len(months) for t in teams}, Counter(), []
    for s, tm in load_items:
        s = dict(s, team=tm)
        if not (s['st'] and s['du']): undated[s['team']] += 1; continue
        if s['st'] > s['du']: inverted.append(s['key']); continue
        for i, (yy, mm) in enumerate(months):
            if s['st'] <= date(yy, mm, calendar.monthrange(yy, mm)[1]) and s['du'] >= date(yy, mm, 1):
                heat[s['team']][i] += 1
    highs = [k for k in sev if sev[k] == 'HIGH']
    meds = [k for k in sev if sev[k] == 'MEDIUM']
    hi_gate = [k for k in highs if cur and by[k]['stage'] == cur]
    if hi_gate or behind > 25 or (dtg is not None and dtg < 21 and (M['gate_pct'] or 0) < 80): health = 'RED'
    elif highs or len(meds) > 3 or 15 <= behind <= 25: health = 'AMBER'
    else: health = 'GREEN'
    people = sorted({p for o in I for p in (o['assignee'], o['reporter']) if p and p not in EMAIL})

    # ---- markdown fragments
    W = a.work
    os.makedirs(W, exist_ok=True)
    url = lambda k: f'[{k}]({BROWSE}{k})'
    short = lambda t, n=60: (lambda t: t if len(t) <= n else t[:n - 1] + '…')(t.strip().replace('|', '/'))

    def chain(o):
        if o['type'] == 'Epic': return '—'
        if o['type'] == 'Story': return o['parent'] or '—'
        p = by.get(o['parent']); return f"{o['parent']} → {p['parent'] if p else '?'}"

    def impact(o):
        parts = list(info[o['key']])
        if sev[o['key']] in ('HIGH', 'MEDIUM') and o['type'] != 'Epic':
            e = epic_of(o)
            what = f"Story {o['parent']} / Epic {e}" if o['type'] == subtype else f'Epic {e}'
            kids_due = [s['du'] for s in o.get('kids', []) if s['du']]
            last = max(kids_due + ([o['du']] if o['du'] else [])) if (kids_due or o['du']) else None
            st = o['stage']
            rank = lambda s_: ORDER.index(s_) if s_ in ORDER else None
            if not gate:
                parts.append(f'holds up {what}; no stage gate for this project, so gate impact is not measured here')
            elif not last:
                parts.append(f'holds up {what}; no due date, gate threat not measurable')
            else:
                slip = max(dl.get(o['key'], 0), (last - o['du']).days if o['du'] else 0)
                if rank(st) is not None and rank(cur) is not None and rank(st) > rank(cur):
                    # later-stage work: it cannot threaten the current gate; say whether it overruns its own stage
                    own = STG[st][1]
                    g = f'{st} work, current gate {gate} not affected' + (f'; runs {(last-own).days}d past {st} end {own}' if last > own else f'; inside {st} window')
                elif rank(st) is not None and rank(cur) is not None and rank(st) < rank(cur):
                    g = f'{st} gate already passed ({STG[st][1]})' + ('; threatens current gate' if last > gate else '')
                else:
                    g = f'threatens gate {gate} by {(last-gate).days}d' if last > gate else f'gate buffer {(gate-last).days}d → no gate threat'
                parts.append(f'holds up {what}; ≈{slip}d slip; {g}')
            sib = by.get(o['parent']) if o['type'] == subtype else o
            ts = sorted({s['team'] for s in sib.get('kids', []) if s['key'] != o['key'] and s['state'] != 'Done' and s['team'] not in (o['team'], 'UNKNOWN')}) if sib else []
            if ts: parts.append('teams waiting: ' + ', '.join(ts))
        return '; '.join(dict.fromkeys(parts))

    def action(o, rs):
        a_ = o['assignee']
        if 'R5' in rs: return 'Close, or move to a current-stage Story'
        if 'R6' in rs and o.get('r6high'): return f"Re-parent to an open Story or close; confirm with {a_ or 'owner'}"
        if 'R7' in rs or 'R8' in rs: return 'Resolve blocking link first'
        if 'R1' in rs: return f"Re-baseline due date; owner {a_ or 'unassigned'}"
        if 'R6' in rs: return f"Extend {o['parent']} due date or pull in Subtask; owner {a_ or 'unassigned'}"
        if 'R3' in rs: return f'Confirm start with {a_}' if a_ else 'Assign owner this week'
        if 'R2' in rs: return 'Move to In Progress or re-plan start date'
        if 'R10' in rs: return 'Break down into dated [ME]/[EE] Subtasks' if not o.get('kids') else 'Start first long-lead Subtask'
        if 'R4' in rs: return 'Confirm still needed; update or close'
        if 'R9' in rs: return 'Assign owner'
        return ''

    SO = {'HIGH': 0, 'MEDIUM': 1, 'LOW': 2}
    rows = sorted(R, key=lambda k: (SO[sev[k]], -dl.get(k, 0), kk(k)))
    L = ['| Sev | Key | Title | Team | Stage | Rules | Days late | Story → Epic | Gate impact | Suggested action |', '| --- ' * 10 + '|']
    for k in rows:
        o = by[k]
        L.append(f"| {sev[k]} | {url(k)} | {short(o['summary'])} | {o['tdisp']} | {o['stage']} | {', '.join(R[k])} | {dl.get(k, 0)} | {chain(o)} | {impact(o)} | {action(o, R[k])} |")
    open(os.path.join(W, 'register.md'), 'w', encoding='utf-8').write('\n'.join(L) + '\n')
    em = lambda r: EMAIL.get(r, 'not in reference.md') if r else 'unknown'
    H = ['| Key | Rule (D1–D6 / prefix / orphan) | Detail | Reporter | Email | Assignee |', '| --- ' * 6 + '|']
    for k, r, d in dd + hyg:
        o = by[k]
        H.append(f"| {k} | {r} | {d} | {o['reporter'] or 'unknown'} | {em(o['reporter'])} | {o['assignee'] or 'Unassigned'} |")
    open(os.path.join(W, 'hygiene.md'), 'w', encoding='utf-8').write('\n'.join(H) + '\n')
    mon = [f'{calendar.month_abbr[mm]}-{str(yy)[2:]}' for yy, mm in months]
    T = ['| Team | ' + ' | '.join(mon) + ' | Avg | Open, undated |', '| --- ' * (len(mon) + 3) + '|']
    for t in teams:
        v = heat[t]; av = sum(v) / len(v)
        T.append(f'| {t} | ' + ' | '.join(f'{x} ⚠' if av > 0 and x > OVF * av else str(x) for x in v) + f' | {av:.2f} | {undated.get(t, 0)} |')
    open(os.path.join(W, 'heatmap.md'), 'w', encoding='utf-8').write('\n'.join(T) + '\n')
    E = ['| Epic | Stories done | Subtasks done | Due | Latest child due | Variance |', '| --- ' * 6 + '|']
    for e in ep:
        v = e['variance']
        E.append(f"| {e['key']} | {e['stories_done']}/{e['stories']} | {e['subs_done']}/{e['subs']} | {e['due'] or 'unknown'} | {e['latest_child_due'] or '—'} | {('+' if v and v > 0 else '') + str(v) + 'd' if v is not None else 'n/a'} |")
    open(os.path.join(W, 'epics.md'), 'w', encoding='utf-8').write('\n'.join(E) + '\n')
    S = ['| Stage | Stories done | Subtasks done |', '| --- | --- | --- |']
    for s in stg:
        S.append(f"| {'No stage tag' if s['stage'] == 'UNKNOWN' else s['stage']} | {s['stories_done']}/{s['stories']} | {s['subs_done']}/{s['subs']} |")
    open(os.path.join(W, 'stages.md'), 'w', encoding='utf-8').write('\n'.join(S) + '\n')
    N = ['| Key | Note | Detail |', '| --- | --- | --- |'] + [f'| {k} | {r} | {d} |' for k, r, d in notes]
    open(os.path.join(W, 'notes.md'), 'w', encoding='utf-8').write('\n'.join(N) + '\n')

    res = dict(project=folder, date=a.date, config=dict(lookahead_days=LOOK, stale_days=STALE, overload_factor=OVF),
               has_stage_schedule=has_stages, current_stage=cur, next_stage=nxt, gate=gate, days_to_gate=dtg, health=health,
               high_on_gate=hi_gate, counts=Counter(o['type'] for o in I), severity=Counter(sev.values()), metrics=M,
               epics=ep, stages=stg, months=mon, heat=heat, undated=dict(undated), inverted_excluded=inverted,
               orphans=orph, notes=notes, people_not_in_reference=people, risk_rows=len(rows), hygiene_rows=len(dd) + len(hyg),
               open_by_assignee=Counter(o['assignee'] or 'Unassigned' for o in openi).most_common(),
               issue_stage={o['key']: o['stage'] for o in I},
               risks={k: dict(sev=sev[k], rules=R[k], info=info[k]) for k in rows})
    json.dump(res, open(os.path.join(W, 'results.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1, default=str)
    sc = res['severity']
    summ = [
        f"PROJECT: {folder} · report: knowledge/{folder}/jira/{a.date}-jira.md",
        f"ROW: {cur or 'n/a'} · gate {gate or 'n/a'} · {dtg if dtg is not None else 'n/a'}d · readiness {M['gate_pct']}% ({M['gate'][0]}/{M['gate'][1]}) · {health}",
        f"COUNTS: {len(I)} issues " + ' / '.join(f'{v} {k}' for k, v in res['counts'].items()),
        f"RISKS: HIGH {sc.get('HIGH', 0)} · MEDIUM {sc.get('MEDIUM', 0)} · LOW {sc.get('LOW', 0)} · overdue {M['overdue'][0]}",
        f"PEOPLE NOT IN reference.md: {', '.join(people) or 'none'}",
    ]
    open(os.path.join(W, 'summary.txt'), 'w', encoding='utf-8').write('\n'.join(summ) + '\n')
    print('\n'.join(summ))
    if not has_stages:
        print('NOTE: no stage schedule column for this project in reference.md; stage checks skipped.')


# ----------------------------------------------------------------- diff
def cmd_diff(a):
    files = sorted(glob.glob(os.path.join(DATA, a.project, '*.json')))
    prev = [f for f in files if os.path.basename(f)[:10] < a.date]
    if not prev:
        msg = 'No earlier snapshot; no week-on-week comparison.'
    else:
        p = os.path.basename(prev[-1])[:10]
        old = {o['key']: o for o in load_snapshot(a.project, p)}
        new = {o['key']: o for o in load_snapshot(a.project, a.date)}
        added = sorted(set(new) - set(old), key=lambda x: int(x.split('-')[1]))
        removed = sorted(set(old) - set(new), key=lambda x: int(x.split('-')[1]))
        moved, redated, retitled, reassigned = [], [], [], []
        for k in sorted(set(new) & set(old), key=lambda x: int(x.split('-')[1])):
            if new[k]['status'] != old[k]['status']: moved.append(f"{k}: {old[k]['status']} → {new[k]['status']}")
            for f in ('start', 'due'):
                if new[k][f] != old[k][f]: redated.append(f"{k}: {f} {old[k][f]} → {new[k][f]}")
            if new[k]['summary'] != old[k]['summary']:
                retitled.append(f"{k}: \"{old[k]['summary'].strip()}\" → \"{new[k]['summary'].strip()}\"")
            if new[k].get('assignee') != old[k].get('assignee'):
                reassigned.append(f"{k}: {old[k].get('assignee') or 'Unassigned'} → {new[k].get('assignee') or 'Unassigned'}")
        lines = ([f'Compared with snapshot {p}: {len(old)} → {len(new)} issues.',
                  f"Added ({len(added)}): {', '.join(added) or 'none'}", f"Removed ({len(removed)}): {', '.join(removed) or 'none'}",
                  f'Status changes ({len(moved)}):'] + [f'- {x}' for x in moved] + [f'Date changes ({len(redated)}):'] + [f'- {x}' for x in redated]
                 + [f'Title changes ({len(retitled)}):'] + [f'- {x}' for x in retitled]
                 + [f'Assignee changes ({len(reassigned)}):'] + [f'- {x}' for x in reassigned])
        msg = '\n'.join(lines)
    os.makedirs(a.work, exist_ok=True)
    open(os.path.join(a.work, 'diff.md'), 'w', encoding='utf-8').write(msg + '\n')
    print(msg)


# ----------------------------------------------------------------- rollup
def active_folders():
    """Folders marked Yes in the CLAUDE.md ## Projects table."""
    text = open(os.path.join(ROOT, 'CLAUDE.md'), encoding='utf-8').read()
    out = []
    for head, rows in md_tables(text):
        if rows and rows[0][:2] == ['Folder', 'Active']:
            out += [r[0].strip('`') for r in rows[1:] if r[1].strip().lower() == 'yes']
    return out


def snap_on_or_before(folder, day):
    fs = sorted(os.path.basename(f)[:10] for f in glob.glob(os.path.join(DATA, folder, '*.json')))
    ok = [f for f in fs if f <= day]
    return ok[-1] if ok else None


def snap_on_or_after(folder, day):
    fs = sorted(os.path.basename(f)[:10] for f in glob.glob(os.path.join(DATA, folder, '*.json')))
    ok = [f for f in fs if f >= day]
    return ok[0] if ok else None


def cmd_rollup(a):
    """Portfolio roll-up: every active product with a stage schedule, from snapshots only.
    Slip is measured against the stage schedule in reference.md (the plan), never against a snapshot.
    Settings: the yaml block in knowledge/portfolio/INDEX.md (bulk_redate_share, pace_min_done,
    pace_min_days, exclude_same_day_closed, lookahead_days). Writes WORK/rollup*.md, rollup.json, rollup_summary.txt."""
    import contextlib, io
    cfg = load_config('portfolio')
    BULK = float(cfg.get('bulk_redate_share') or 0.2)
    PMIN_DONE = int(cfg.get('pace_min_done') or 5)
    PMIN_DAYS = int(cfg.get('pace_min_days') or 28)
    LOOK = int(cfg.get('lookahead_days') or 14)
    SAMEDAY = (cfg.get('exclude_same_day_closed') or 'true').lower() != 'false'
    TODAY = D(a.date)
    W = a.work
    os.makedirs(W, exist_ok=True)
    act = active_folders()
    products, support, P, flags = [], [], {}, []
    for f in act:
        (products if load_reference(f)[0] else support).append(f)

    for f in products:
        STG = load_reference(f)[0]
        sd = snap_on_or_before(f, a.date)
        if not sd:
            flags.append(f'{f}: no snapshot on or before {a.date}; left out'); continue
        if sd != a.date:
            flags.append(f'{f}: newest snapshot is {sd}, not {a.date} (stale)')
        sub = os.path.join(W, f)
        with contextlib.redirect_stdout(io.StringIO()):
            cmd_analyze(argparse.Namespace(project=f, date=sd, work=sub))
        res = json.load(open(os.path.join(sub, 'results.json'), encoding='utf-8'))
        I = load_snapshot(f, sd)
        by = {o['key']: o for o in I}
        stage = res['issue_stage']
        state = lambda o: {'done': 'Done', 'indeterminate': 'In Progress', 'new': 'To Do'}[o['scat']]
        stories = [o for o in I if o['type'] == 'Story']
        subtype = next((o['type'] for o in I if o['type'].lower().replace('-', '') == 'subtask'), 'Subtask')
        cur, nxt, gate = res['current_stage'], res['next_stage'], D(res['gate']) if res['gate'] else None

        def adjusted_done(s, s0):
            """Done Story that counts as progress in its stage, and why not if it doesn't."""
            if state(s) != 'Done': return False, None
            kids = [by[k] for k in s['subtasks'] if k in by]
            if any(state(k) != 'Done' for k in kids): return False, 'Done with open Subtasks'
            if s['resolved'] and D(s['resolved']) < s0: return False, 'closed before the stage started'
            if SAMEDAY and s['resolved'] and s['created'] and (D(s['resolved']) - D(s['created'])).days <= 1:
                return False, 'created and closed within a day (logged after the fact)'
            return True, None

        stages = []
        for st in ORDER:
            if st not in STG: continue
            s0, s1 = STG[st]
            ch = [s for s in stories if stage.get(s['key']) == st]
            done = [s for s in ch if state(s) == 'Done']
            adj, excl = [], Counter()
            for s in ch:
                ok, why = adjusted_done(s, s0)
                if ok: adj.append(s)
                elif why: excl[why] += 1
            n = len(ch)
            exp = 100.0 if TODAY > s1 else (0.0 if TODAY < s0 else 100 * (TODAY - s0).days / max((s1 - s0).days, 1))
            raw_p = round(100 * len(done) / n, 1) if n else None
            adj_p = round(100 * len(adj) / n, 1) if n else None
            openst = [s for s in ch if state(s) != 'Done']
            planned = [s for s in ch if s['assignee'] and any(by[k]['start'] and by[k]['due'] for k in s['subtasks'] if k in by)]
            cov = round(100 * len(planned) / n, 1) if n else None
            row = dict(stage=st, start=str(s0), end=str(s1), stories=n, done=len(done), adj_done=len(adj),
                       in_progress=sum(state(s) == 'In Progress' for s in ch), expected=round(exp, 1), raw=raw_p, adj=adj_p,
                       excluded=dict(excl), planned=len(planned), coverage=cov,
                       unowned=sorted([s['key'] for s in openst if not s['assignee']], key=lambda k: int(k.split('-')[1])),
                       no_subtasks=sorted([s['key'] for s in openst if not s['subtasks']], key=lambda k: int(k.split('-')[1])))
            if TODAY > s1:
                row['status'] = 'Done' if not openst else f'Carryover ({len(openst)} open)'
            elif TODAY < s0:
                row['status'] = 'Not started'
            else:
                gap = exp - (adj_p or 0)
                # pace: adjusted Stories closed inside this stage window, per day elapsed
                el = max((TODAY - s0).days, 1)
                rate = len(adj) / el
                conf = len(adj) >= PMIN_DONE and el >= PMIN_DAYS
                fc = (TODAY + timedelta(days=round(len(openst) / rate))) if rate > 0 else None
                row.update(gap=round(gap, 1), pace_per_week=round(rate * 7, 2), pace_confident=conf,
                           forecast=str(fc) if fc else None,
                           forecast_slip=((fc - s1).days if fc else None))
                late = conf and fc and fc > s1
                row['status'] = 'Behind' if (gap > 25 or late) else ('At risk' if gap >= 15 else 'On track')
            # slip vs the planned stage end (reference.md ## Stage schedule)
            if TODAY > s1 and not openst and done:
                fin = max((D(s['resolved']) for s in done if s['resolved']), default=None)
                row['slip_days'] = max(0, (fin - s1).days) if fin else None
                row['slip_note'] = (f"finished {fin}" + (f", +{(fin - s1).days}d late" if fin > s1 else ', on time')) if fin else 'finish date unknown'
            elif TODAY > s1 and openst:
                row['slip_days'] = (TODAY - s1).days
                row['slip_note'] = f"{len(openst)} Stories still open, +{(TODAY - s1).days}d past plan so far"
            elif s0 <= TODAY <= s1:
                fs = row.get('forecast_slip')
                row['slip_days'] = fs if (fs is not None and row.get('pace_confident')) else None
                row['slip_note'] = ('forecast ' + ('+' if fs > 0 else '') + f"{fs}d" + ('' if row.get('pace_confident') else ' (low confidence)')) if fs is not None else 'no forecast yet'
            else:
                row['slip_days'], row['slip_note'] = None, '—'
            stages.append(row)

        # ticket slip vs the plan: open Stories/Subtasks due after their stage's planned end; Epics due after MP end
        slip = []
        for o in I:
            if o['scat'] == 'done' or not o['due']: continue
            st = stage.get(o['key'])
            end = STG['MP'][1] if o['type'] == 'Epic' else (STG[st][1] if st in STG else None)
            if end and D(o['due']) > end:
                slip.append(dict(key=o['key'], type=o['type'], stage='Epic→MP' if o['type'] == 'Epic' else st,
                                 due=o['due'], plan_end=str(end), days=(D(o['due']) - end).days))
        slip.sort(key=lambda x: (-x['days'], int(x['key'].split('-')[1])))
        prev = [x for x in sorted(os.path.basename(p)[:10] for p in glob.glob(os.path.join(DATA, f, '*.json'))) if x < sd]
        redate = None
        if prev:
            old = {o['key']: o for o in load_snapshot(f, prev[-1])}
            op = [o for o in I if o['scat'] != 'done' and o['key'] in old]
            ch = [o for o in op if (o['start'], o['due']) != (old[o['key']]['start'], old[o['key']]['due'])]
            share = len(ch) / len(op) if op else 0
            later = sorted([dict(key=o['key'], type=o['type'], was=old[o['key']]['due'], now=o['due'], days=(D(o['due']) - D(old[o['key']]['due'])).days)
                            for o in op if o['due'] and old[o['key']]['due'] and D(o['due']) > D(old[o['key']]['due'])], key=lambda x: -x['days'])
            redate = dict(since=prev[-1], changed=len(ch), open=len(op), share=round(100 * share, 1), bulk=share > BULK, later=later)
            if share > BULK:
                flags.append(f'{f}: {len(ch)} of {len(op)} open items ({round(100*share)}%) re-dated since {prev[-1]} (bulk re-plan?)')
        # outlook to MP: current-stage forecast slip carried forward; later stages assumed to keep their length
        cs = next((s for s in stages if s['stage'] == cur), None)
        if cs and cs.get('pace_confident') and cs.get('forecast_slip') is not None:
            mp = dict(kind='forecast', slip=max(0, cs['forecast_slip']), date=str(STG['MP'][1] + timedelta(days=max(0, cs['forecast_slip']))))
        else:
            mp = dict(kind='not enough data', slip=None, date=None)
        carry = [s for s in stages if s['status'].startswith('Carryover')]
        ns = next((s for s in stages if s['stage'] == nxt), None)
        if cs is None: outlook = 'n/a'
        elif cs['status'] == 'Behind' or (mp['slip'] or 0) > 0: outlook = 'Behind'
        elif cs['status'] == 'At risk' or carry: outlook = 'At risk'
        else: outlook = 'On track'
        if outlook == 'On track' and mp['kind'] != 'forecast': outlook = 'On track (early, low confidence)'
        openi = [o for o in I if o['scat'] != 'done']
        P[f] = dict(folder=f, key=I[0]['key'].split('-')[0] if I else '', snapshot=sd, current=cur, next=nxt,
                    gate=res['gate'], days_to_gate=res['days_to_gate'], health=res['health'], severity=res['severity'],
                    stages=stages, slip=slip, redate=redate, mp=mp, outlook=outlook,
                    next_coverage=ns['coverage'] if ns else None, mp_end=str(STG['MP'][1]),
                    open_by_assignee=Counter(o['assignee'] for o in openi if o['assignee']),
                    unassigned=sum(1 for o in openi if not o['assignee']))

    # people across products
    people = defaultdict(dict)
    for f, p in P.items():
        for n, c in p['open_by_assignee'].items(): people[n][f] = c
    multi = sorted([(n, d) for n, d in people.items() if len(d) >= 2], key=lambda x: -sum(x[1].values()))
    # shared gates
    gates = defaultdict(list)
    for f, p in P.items():
        if p['gate']: gates[p['gate']].append(f'{f} ({p["current"]})')
    # support projects (Research): open items, product links, due soon
    sup = {}
    pkeys = {p['key'] for p in P.values()}
    for f in support:
        sd = snap_on_or_before(f, a.date)
        if not sd: continue
        I = load_snapshot(f, sd)
        op = [o for o in I if o['scat'] != 'done']
        linked = [o for o in op if any(l['key'].split('-')[0] in pkeys for l in o['links'])]
        soon = [o for o in op if o['due'] and TODAY <= D(o['due']) <= TODAY + timedelta(LOOK)]
        over = [o for o in op if o['due'] and D(o['due']) < TODAY]
        sup[f] = dict(snapshot=sd, open=len(op), linked=len(linked), unlinked=len(op) - len(linked),
                      due_soon=[(o['key'], o['due'], o['summary'].strip()) for o in soon],
                      overdue=[(o['key'], o['due'], o['summary'].strip()) for o in over])

    # ---- outputs
    kk = lambda k: int(k.split('-')[1])
    url = lambda k: f'[{k}]({BROWSE}{k})'
    final = max((D(p['mp_end']) for p in P.values()), default=None)
    on = [f for f, p in P.items() if p['outlook'].startswith('On track')]
    fc = [(p['mp']['slip'], f) for f, p in P.items() if p['mp']['slip'] is not None]
    worst = max(fc) if fc else None
    nextgate = min(gates) if gates else None
    kpi = [f'- Days to final deadline ({final}): {(final - TODAY).days}' if final else '- Final deadline: n/a',
           f'- On track for MP: {len(on)} of {len(P)}' + (' (' + ', '.join(f + (' — low confidence' if P[f]['outlook'] != 'On track' else '') for f in on) + ')' if on else ''),
           f'- Worst MP forecast slip: ' + (f'{worst[1]} +{worst[0]}d' if worst and worst[0] > 0 else
                                            ('none' if fc else 'not enough data yet (pace needs more closed Stories or more time)')),
           f'- Next gate: {nextgate} ({(D(nextgate) - TODAY).days}d): ' + ', '.join(gates[nextgate]) if nextgate else '- Next gate: n/a']
    open(os.path.join(W, 'rollup_kpi.md'), 'w', encoding='utf-8').write('\n'.join(kpi) + '\n')

    L = ['| Product | Stage | Gate (days) | Readiness raw / adjusted | Expected | Stage status | Pace forecast for gate | MP outlook | Slip vs schedule | Next stage planned | HIGH / MED | Health |',
         '| --- ' * 12 + '|']
    for f, p in P.items():
        cs = next((s for s in p['stages'] if s['stage'] == p['current']), {})
        if cs.get('forecast'):
            pf = f"{cs['forecast']} ({'+' if cs['forecast_slip'] > 0 else ''}{cs['forecast_slip']}d)" + ('' if cs['pace_confident'] else ', low confidence')
        else:
            pf = 'no adjusted progress yet'
        sl = f"{len(p['slip'])} open items past stage end, max +{p['slip'][0]['days']}d" if p['slip'] else 'none past stage end'
        mpo = p['outlook'] + (f", MP {p['mp']['date']}" if p['mp']['date'] else ', forecast n/a')
        sev = p['severity']
        L.append(f"| {f} | {p['current']} | {p['gate']} ({p['days_to_gate']}) | {cs.get('raw')}% / {cs.get('adj')}% | {cs.get('expected')}% | {cs.get('status')} | {pf} | {mpo} | {sl} | "
                 f"{str(p['next_coverage']) + '%' if p['next_coverage'] is not None else 'n/a'} | {sev.get('HIGH', 0)} / {sev.get('MEDIUM', 0)} | {p['health']} |")
    open(os.path.join(W, 'rollup_products.md'), 'w', encoding='utf-8').write('\n'.join(L) + '\n')

    S = []
    for f, p in P.items():
        S += [f'### {f}', '', '| Stage | Planned window | Stories done (adjusted) / total | Expected | Raw | Adjusted | Planned (owner + dated Subtasks) | Status | Slip vs plan |', '| --- ' * 9 + '|']
        for s in p['stages']:
            S.append(f"| {s['stage']} | {s['start']} → {s['end']} | {s['done']} ({s['adj_done']}) / {s['stories']} | {s['expected']}% | "
                     f"{s['raw'] if s['raw'] is not None else '—'}% | {s['adj'] if s['adj'] is not None else '—'}% | {s['planned']}/{s['stories']} | {s['status']} | {s['slip_note']} |")
        cs = next((s for s in p['stages'] if s['stage'] == p['current']), None)
        if cs and cs['excluded']:
            S.append(''); S.append('Not counted in adjusted readiness: ' + '; '.join(f'{v} {k}' for k, v in cs['excluded'].items()) + '.')
        if cs:
            S.append(''); S.append(f"Pace in {cs['stage']}: {cs.get('pace_per_week')} adjusted Stories/week" +
                                   ('' if cs.get('pace_confident') else f' (low confidence: needs ≥{PMIN_DONE} closed and ≥{PMIN_DAYS} days in stage)') + '.')
            if cs['unowned']: S.append(f"Open {cs['stage']} Stories with no owner ({len(cs['unowned'])}): " + ', '.join(cs['unowned'][:10]) + (' …' if len(cs['unowned']) > 10 else '') + '.')
            if cs['no_subtasks']: S.append(f"Open {cs['stage']} Stories with no Subtasks ({len(cs['no_subtasks'])}): " + ', '.join(cs['no_subtasks'][:10]) + (' …' if len(cs['no_subtasks']) > 10 else '') + '.')
        S.append('')
    open(os.path.join(W, 'rollup_stages.md'), 'w', encoding='utf-8').write('\n'.join(S) + '\n')

    G = ['```mermaid', 'gantt', '    dateFormat YYYY-MM-DD', '    axisFormat %b %y', f'    todayMarker on']
    for f, p in P.items():
        G.append(f'    section {f.replace("ZenaQuiet-", "")}')
        for s in p['stages']:
            tag = 'done' if s['status'] == 'Done' else ('crit' if s['status'].startswith(('Behind', 'Carryover')) else
                                                         ('active' if s['status'] in ('On track', 'At risk') else ''))
            lab = f"{s['stage']} {s['status']}" + (f" {s['adj']}%" if s['status'] in ('On track', 'At risk', 'Behind') else '')
            G.append(f"    {lab.replace(':', '')} :{tag + ', ' if tag else ''}{f[10:].lower()}{s['stage'].lower()}, {s['start']}, {s['end']}")
    G.append('```')
    open(os.path.join(W, 'rollup_timeline.md'), 'w', encoding='utf-8').write('\n'.join(G) + '\n')

    X = []
    for f, p in P.items():
        X.append(f"### {f}")
        X.append(f"Open items due after their stage's planned end ([[reference#Stage schedule (per product)]]): " +
                 (f"{len(p['slip'])}." if p['slip'] else 'none.'))
        for s_ in p['slip'][:10]:
            X.append(f"- {url(s_['key'])} ({s_['type']}, {s_['stage']}): due {s_['due']}, plan end {s_['plan_end']} (+{s_['days']}d)")
        if len(p['slip']) > 10: X.append(f"- + {len(p['slip']) - 10} more")
        r = p['redate']
        if r:
            X.append(f"Dates moved since {r['since']}: {r['changed']} of {r['open']} open items ({r['share']}%)" + (' — BULK RE-DATE' if r['bulk'] else '') +
                     f"; {len(r['later'])} now due later.")
            for m in r['later'][:5]:
                X.append(f"- {url(m['key'])} ({m['type']}): {m['was']} → {m['now']} (+{m['days']}d)")
            if len(r['later']) > 5: X.append(f"- + {len(r['later']) - 5} more")
        X.append('')
    open(os.path.join(W, 'rollup_slip.md'), 'w', encoding='utf-8').write('\n'.join(X) + '\n')

    short = lambda f: f.replace('ZenaQuiet-', '')
    Q = ['| Person | Open items | By product |', '| --- | --- | --- |']
    for n, d in multi:
        Q.append(f"| {n} | {sum(d.values())} | " + ', '.join(f'{short(k)} {v}' for k, v in sorted(d.items(), key=lambda x: -x[1])) + ' |')
    Q.append(''); Q.append('Unassigned open items: ' + ', '.join(f"{short(f)} {p['unassigned']}" for f, p in P.items()) + '.')
    open(os.path.join(W, 'rollup_people.md'), 'w', encoding='utf-8').write('\n'.join(Q) + '\n')

    R_ = []
    for f, s in sup.items():
        R_.append(f"### {f} (snapshot {s['snapshot']})")
        R_.append(f"Open {s['open']}; linked to a product ticket {s['linked']}; unlinked {s['unlinked']}.")
        for k, d_, t in s['overdue']: R_.append(f'- Overdue: {url(k)} due {d_} — {t}')
        for k, d_, t in s['due_soon']: R_.append(f'- Due within {LOOK}d: {url(k)} due {d_} — {t}')
        R_.append('')
    open(os.path.join(W, 'rollup_support.md'), 'w', encoding='utf-8').write('\n'.join(R_) + '\n')

    out = dict(date=a.date, slip_reference='reference.md ## Stage schedule', products=P, support=sup, people_multi=multi, gates=dict(gates), flags=flags)
    json.dump(out, open(os.path.join(W, 'rollup.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1, default=str)
    summ = [f'ROLLUP {a.date} · slip vs stage schedule · products {len(P)} · support {", ".join(sup) or "none"}'] + kpi + \
           [f"{f}: {p['current']} · {p['outlook']} · adj {next((s['adj'] for s in p['stages'] if s['stage'] == p['current']), None)}% vs exp "
            f"{next((s['expected'] for s in p['stages'] if s['stage'] == p['current']), None)}% · health {p['health']}" for f, p in P.items()] + \
           [f'FLAG: {x}' for x in flags]
    open(os.path.join(W, 'rollup_summary.txt'), 'w', encoding='utf-8').write('\n'.join(summ) + '\n')
    print('\n'.join(summ))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest='cmd', required=True)
    for name in ('normalize', 'analyze', 'diff', 'rollup'):
        p = sp.add_parser(name)
        if name != 'rollup':
            p.add_argument('--project', required=True, help='wiki folder name, e.g. ZenaQuiet-Pro2')
        p.add_argument('--date', default=None, help='ISO date; default = INDEX.md today, else system date')
        if name == 'normalize':
            p.add_argument('--raw-dir', required=True)
            p.add_argument('--start-field', default='customfield_10015')
            p.add_argument('--sprint-field', default='customfield_10020')
        else:
            p.add_argument('--work', required=True)
    a = ap.parse_args()
    if a.cmd == 'rollup':
        a.date = a.date or load_config('portfolio').get('today') or date.today().isoformat()
        return cmd_rollup(a)
    if not os.path.isdir(os.path.join(KNOW, a.project)):
        sys.exit(f'Unknown project folder: {a.project}')
    a.date = a.date or load_config(a.project).get('today') or date.today().isoformat()
    {'normalize': cmd_normalize, 'analyze': cmd_analyze, 'diff': cmd_diff}[a.cmd](a)


if __name__ == '__main__':
    main()
