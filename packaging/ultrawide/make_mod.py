#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-2.0-or-later
"""Builds the drop-in ultrawide mod ZIP from an unpacked portable build.

    python3 packaging/ultrawide/make_mod.py dist/CTR-NitroFueled-PC-portable --version v0.5.2-uw

The ZIP holds only what the mod changes, laid out like the port folder, so it is extracted
over an existing v0.5.2 installation.
"""
import argparse
import hashlib
import zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
FROM_BUILD = ('bin/sacredfire.exe', 'bin/VERSION')
FROM_SOURCE = ('scripts/patches.py', 'patches/CrashTeamRacingUltrawide.xml')
FROM_HERE = ('LEEME-ULTRAWIDE.txt', 'Jugar sin HUD.bat', 'Jugar_HUD_log.bat')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('portable', type=Path, help='unpacked portable folder')
    parser.add_argument('--version', default='dev')
    parser.add_argument('--out', type=Path, default=ROOT / 'dist')
    args = parser.parse_args()
    files = [(args.portable / f, f) for f in FROM_BUILD]
    files += [(ROOT / f, f) for f in FROM_SOURCE]
    files += [(HERE / f, f) for f in FROM_HERE]
    missing = [str(src) for src, _ in files if not src.is_file()]
    if missing:
        raise SystemExit('missing: ' + ', '.join(missing))
    args.out.mkdir(parents=True, exist_ok=True)
    target = args.out / f'CTR-Ultrawide-mod-{args.version}.zip'
    with zipfile.ZipFile(target, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for src, name in files:
            z.write(src, name)
    digest = hashlib.sha256(target.read_bytes()).hexdigest()
    target.with_name(target.name + '.sha256').write_text(f'{digest} *{target.name}\n')
    print(f'{target} ({target.stat().st_size // 1024} KiB)')


if __name__ == '__main__':
    main()
