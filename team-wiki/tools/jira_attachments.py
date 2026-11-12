#!/usr/bin/env python3
"""Download Jira attachments for the team wiki (approved exception, see CLAUDE.md).

RUN BY THE HUMAN ON THEIR OWN PC, never by the AI. It reads the Jira login from zena-llm/.env
(git-ignored) and never prints, logs or writes the token anywhere.

What it does
  1. Finds open tickets (not Done) in every active project that were updated in the last N days.
  2. Downloads their attachments (images, PDF, Word, Excel, PowerPoint, text) up to a size limit.
  3. Saves them to team-wiki/raw/jira-attachments/<KEY>/<attachment id>-<file name>
     and updates team-wiki/raw/jira-attachments/manifest.json.
  Files already downloaded are skipped. Nothing in Jira is changed (read-only GET requests).

Setup (once)
  1. Copy zena-llm/.env.example to zena-llm/.env and fill in JIRA_SITE, JIRA_EMAIL, JIRA_API_TOKEN
     (a read-only account's token, with an expiry date).
  2. Check git ignores it:   git check-ignore -v .env

Run (before each weekly report run), from the team-wiki folder:
  Windows:  py tools\\jira_attachments.py
  Options:  --days 14   --max-mb 20   --max-per-project 100   --projects PRO2,BC   --dry-run

Only the Python standard library is used.
"""
import argparse, base64, datetime as dt, json, os, re, sys, time, urllib.error, urllib.parse, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))          # team-wiki/
OUT = os.path.join(ROOT, 'raw', 'jira-attachments')
MANIFEST = os.path.join(OUT, 'manifest.json')
ALLOWED_EXT = {'.png', '.jpg', '.jpeg', '.gif', '.webp', '.bmp', '.pdf', '.docx', '.doc', '.xlsx', '.xls',
               '.csv', '.pptx', '.ppt', '.txt', '.md', '.json'}


# ------------------------------------------------------------------ settings
def load_env():
    """Read KEY=VALUE lines from zena-llm/.env (or team-wiki/.env). Values never leave this process."""
    for p in (os.path.join(os.path.dirname(ROOT), '.env'), os.path.join(ROOT, '.env')):
        if os.path.exists(p):
            env = {}
            for line in open(p, encoding='utf-8'):
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    k, v = line.split('=', 1)
                    env[k.strip()] = v.strip().strip('"').strip("'")
            return env, p
    sys.exit('No .env found. Copy zena-llm/.env.example to zena-llm/.env and fill it in.')


def active_keys():
    """Jira keys of the projects marked Yes in CLAUDE.md, mapped through reference.md ## Jira projects."""
    claude = open(os.path.join(ROOT, 'CLAUDE.md'), encoding='utf-8').read()
    active = re.findall(r'^\|\s*`([^`]+)`\s*\|\s*Yes\s*\|', claude, re.M)
    ref = open(os.path.join(ROOT, 'knowledge', 'reference.md'), encoding='utf-8').read()
    k2f = dict(re.findall(r'^\|\s*([A-Z0-9]+)\s*\|\s*(ZenaQuiet-[\w-]+)', ref, re.M))
    return [k for k, f in k2f.items() if f in active]


# ------------------------------------------------------------------ Jira
class Jira:
    def __init__(self, site, email, token):
        self.site = site.rstrip('/')
        self.auth = 'Basic ' + base64.b64encode(f'{email}:{token}'.encode()).decode()

    def _open(self, url, accept='application/json'):
        req = urllib.request.Request(url, headers={'Authorization': self.auth, 'Accept': accept})
        for attempt in range(3):
            try:
                return urllib.request.urlopen(req, timeout=60)
            except urllib.error.HTTPError as e:
                if e.code in (401, 403):
                    sys.exit(f'Jira refused the login (HTTP {e.code}). The token may be wrong, expired or lack '
                             'Browse permission. Create a new one and update .env.')
                if e.code == 429 or e.code >= 500:
                    time.sleep(5 * (attempt + 1)); continue
                raise
            except urllib.error.URLError:
                time.sleep(5 * (attempt + 1))
        raise RuntimeError(f'Could not reach {urllib.parse.urlsplit(url).netloc}')

    def search(self, jql):
        """All issues for a JQL query, with key, status and attachments (enhanced search API)."""
        token = None
        while True:
            q = {'jql': jql, 'fields': 'attachment,status,updated', 'maxResults': '100'}
            if token: q['nextPageToken'] = token
            data = json.load(self._open(f'{self.site}/rest/api/3/search/jql?' + urllib.parse.urlencode(q)))
            yield from data.get('issues', [])
            token = data.get('nextPageToken')
            if not token or data.get('isLast'):
                break

    def download(self, att_id, dest):
        """Jira answers with a redirect to a short-lived media link; follow it WITHOUT the login header."""
        class NoRedirect(urllib.request.HTTPRedirectHandler):
            def redirect_request(self, *args, **kw): return None
        req = urllib.request.Request(f'{self.site}/rest/api/3/attachment/content/{att_id}',
                                     headers={'Authorization': self.auth, 'Accept': '*/*'})
        try:
            r = urllib.request.build_opener(NoRedirect).open(req, timeout=60)
        except urllib.error.HTTPError as e:
            if e.code in (301, 302, 303, 307, 308) and e.headers.get('Location'):
                r = urllib.request.urlopen(urllib.request.Request(e.headers['Location']), timeout=120)
            elif e.code in (401, 403):
                sys.exit(f'Jira refused the download (HTTP {e.code}). Check the token in .env.')
            else:
                raise
        with r, open(dest + '.part', 'wb') as f:
            while True:
                chunk = r.read(1 << 16)
                if not chunk: break
                f.write(chunk)
        os.replace(dest + '.part', dest)


# ------------------------------------------------------------------ main
def safe_name(name):
    return re.sub(r'[^\w.\- ()]+', '_', name).strip()[:120] or 'file'


def main():
    ap = argparse.ArgumentParser(description='Download Jira attachments for the team wiki (run by the human).')
    ap.add_argument('--days', type=int, default=14, help='tickets updated in the last N days (default 14)')
    ap.add_argument('--max-mb', type=float, default=20, help='skip files larger than this (default 20 MB)')
    ap.add_argument('--max-per-project', type=int, default=100, help='new downloads per project per run (default 100)')
    ap.add_argument('--projects', default='', help='comma-separated Jira keys (default: all active projects)')
    ap.add_argument('--dry-run', action='store_true', help='list what would be downloaded, download nothing')
    a = ap.parse_args()

    env, env_path = load_env()
    missing = [k for k in ('JIRA_SITE', 'JIRA_EMAIL', 'JIRA_API_TOKEN') if not env.get(k)]
    if missing:
        sys.exit(f'{os.path.basename(env_path)} is missing: {", ".join(missing)}')
    jira = Jira(env['JIRA_SITE'], env['JIRA_EMAIL'], env['JIRA_API_TOKEN'])
    del env  # nothing below needs the raw values

    keys = [k.strip().upper() for k in a.projects.split(',') if k.strip()] or active_keys()
    os.makedirs(OUT, exist_ok=True)
    man = json.load(open(MANIFEST, encoding='utf-8')) if os.path.exists(MANIFEST) else {'files': []}
    have = {f['attachment_id'] for f in man['files']}
    now = dt.datetime.now().astimezone()
    stats = {}
    for key in keys:
        got = skipped = 0
        jql = f'project = {key} AND statusCategory != Done AND updated >= -{a.days}d ORDER BY updated DESC'
        for iss in jira.search(jql):
            for att in iss['fields'].get('attachment') or []:
                aid = str(att['id'])
                if aid in have: continue
                name = att.get('filename', 'file'); ext = os.path.splitext(name)[1].lower()
                size = att.get('size') or 0
                reason = ('type not allowed' if ext not in ALLOWED_EXT else
                          f'larger than {a.max_mb:g} MB' if size > a.max_mb * 1024 * 1024 else
                          'per-project limit reached' if got >= a.max_per_project else None)
                rec = dict(attachment_id=aid, ticket=iss['key'], filename=name, mime=att.get('mimeType'), size=size,
                           uploaded=(att.get('created') or '')[:10], uploaded_by=(att.get('author') or {}).get('displayName'),
                           ticket_status=((iss['fields'].get('status') or {}).get('name')))
                if reason:
                    skipped += 1
                    print(f'  skip {iss["key"]} {name}: {reason}')
                    continue
                rel = os.path.join(iss['key'], f'{aid}-{safe_name(name)}')
                if a.dry_run:
                    print(f'  would download {iss["key"]} {name} ({size // 1024} KB)'); got += 1; continue
                os.makedirs(os.path.join(OUT, iss['key']), exist_ok=True)
                jira.download(aid, os.path.join(OUT, rel))
                rec.update(path=rel.replace(os.sep, '/'), downloaded=now.isoformat(timespec='seconds'))
                man['files'].append(rec); have.add(aid); got += 1
                print(f'  saved {rel}')
        stats[key] = (got, skipped)
    if not a.dry_run:
        man['updated'] = now.isoformat(timespec='seconds')
        man['settings'] = dict(days=a.days, max_mb=a.max_mb, max_per_project=a.max_per_project, projects=keys)
        tmp = MANIFEST + '.tmp'
        json.dump(man, open(tmp, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        os.replace(tmp, MANIFEST)
    print(('DRY RUN · ' if a.dry_run else '') + ' · '.join(f'{k}: {g} new, {s} skipped' for k, (g, s) in stats.items()) +
          f' · manifest: {len(man["files"])} files')


if __name__ == '__main__':
    main()
