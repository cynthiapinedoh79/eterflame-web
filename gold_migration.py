"""
Gold system migration: replace hardcoded #c49a40 / #d4a843 with CSS variables.
Skips block comments (/* ... */) using placeholder technique.
Aborts on any verification failure.
"""

import re
import shutil
import sys
import os

TARGET_FILES = [
    'static/css/about.css',
    'static/css/aythnyk.css',
    'static/css/blog.css',
    'static/css/design.css',
    'static/css/poetry.css',
    'static/css/shop.css',
    'static/css/songs.css',
    'static/css/studio.css',
    'static/css/works.css',
]

GOLD_RE      = re.compile(r'#c49a40', re.IGNORECASE)
BRIGHT_RE    = re.compile(r'#d4a843', re.IGNORECASE)
COMMENT_RE   = re.compile(r'/\*.*?\*/', re.DOTALL)
REMAINING_RE = re.compile(r'#c49a40|#d4a843', re.IGNORECASE)

# Expected net replacements per file (comments excluded), from STEP A
EXPECTED = {
    'static/css/about.css':    26,
    'static/css/aythnyk.css':  16,
    'static/css/blog.css':     10,
    'static/css/design.css':    2,
    'static/css/poetry.css':    6,
    'static/css/shop.css':     14,   # 15 total minus 1 comment line
    'static/css/songs.css':     8,   # 9 total minus 1 comment line
    'static/css/studio.css':    2,
    'static/css/works.css':    17,   # 18 total minus 1 comment line
}

aborted = False
results = {}

print("=" * 62)
print("GOLD MIGRATION — STEP C")
print("=" * 62)

# ── Phase 1: backup ───────────────────────────────────────────
print("\n[1/4] Creating backups …")
for path in TARGET_FILES:
    backup = path + '.backup'
    shutil.copy2(path, backup)
    exists = os.path.isfile(backup)
    print(f"  {'OK' if exists else 'FAIL':4s}  {backup}")
    if not exists:
        print("ABORT: backup failed")
        sys.exit(1)

# ── Phase 2: apply replacements ───────────────────────────────
print("\n[2/4] Applying replacements …")

for path in TARGET_FILES:
    with open(path, 'r', encoding='utf-8') as f:
        original = f.read()

    # Extract block comments → placeholders
    placeholders = []
    def _save(m, _store=placeholders):
        idx = len(_store)
        _store.append(m.group(0))
        return f'\x00COMMENT{idx:04d}\x00'

    stripped = COMMENT_RE.sub(_save, original)

    # Count before replacement (outside comments)
    n_gold   = len(GOLD_RE.findall(stripped))
    n_bright = len(BRIGHT_RE.findall(stripped))
    n_total  = n_gold + n_bright

    # Apply replacements
    replaced = GOLD_RE.sub('var(--gold)', stripped)
    replaced = BRIGHT_RE.sub('var(--gold-bright)', replaced)

    # Restore block comments
    for i, comment_text in enumerate(placeholders):
        replaced = replaced.replace(f'\x00COMMENT{i:04d}\x00', comment_text)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(replaced)

    results[path] = {
        'gold':   n_gold,
        'bright': n_bright,
        'total':  n_total,
    }
    print(f"  {path}:  {n_gold}× #c49a40 + {n_bright}× #d4a843 = {n_total} replacements")

# ── Phase 3: verify ───────────────────────────────────────────
print("\n[3/4] Verifying — 0 gold hex values must remain outside comments …")

fail_files = []

for path in TARGET_FILES:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Strip comments again for verification
    comment_free = COMMENT_RE.sub('', content)
    remaining = REMAINING_RE.findall(comment_free)
    expected  = EXPECTED[path]
    actual    = results[path]['total']

    ok_remaining = (len(remaining) == 0)
    ok_count     = (actual == expected)

    status = 'OK  ' if (ok_remaining and ok_count) else 'FAIL'
    print(f"  {status}  {path}")
    print(f"        replacements: {actual} (expected {expected})  |  remaining outside comments: {len(remaining)}")

    if not ok_remaining or not ok_count:
        fail_files.append(path)
        if remaining:
            print(f"        REMAINING HITS: {remaining[:10]}")
        if not ok_count:
            print(f"        COUNT MISMATCH: got {actual}, expected {expected}")

if fail_files:
    print(f"\nABORT: {len(fail_files)} file(s) failed verification:")
    for p in fail_files:
        print(f"  {p}")
    print("No changes have been committed. Backups are intact.")
    aborted = True

# ── Phase 4: summary ──────────────────────────────────────────
if not aborted:
    grand_total = sum(r['total'] for r in results.values())
    print(f"\n[4/4] Summary")
    print(f"  Total replacements applied: {grand_total}")
    print(f"\n  {'File':<38} {'Applied':>8} {'Expected':>9} {'Match':>6}")
    print(f"  {'-'*38}  {'-'*8}  {'-'*8}  {'-'*5}")
    for path, r in results.items():
        name = path.replace('static/css/', '')
        exp  = EXPECTED[path]
        match = 'YES' if r['total'] == exp else 'NO '
        print(f"  {name:<38} {r['total']:>8} {exp:>9} {match:>6}")
    print(f"\n  Migration complete. All 9 backup files created.")

sys.exit(1 if aborted else 0)
