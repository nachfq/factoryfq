#!/usr/bin/env python3
"""Install factoryfq skills without changing user instructions."""

import argparse
import difflib
import os
from pathlib import Path
import sys
import tempfile


def preview(source, target, backup_root, allow_backup, show_diff=True):
    for parent in target.parents:
        if os.path.lexists(parent) and not parent.is_dir():
            raise ValueError(f'Target parent is not a directory: {parent}')
    if target.is_symlink() and target.resolve() == source:
        print(f'Already installed: {target} -> {source}')
        return False
    if target.is_dir() and not target.is_symlink():
        raise ValueError(f'Refusing to replace a directory: {target}')
    if show_diff and source.is_file() and (not os.path.lexists(target) or target.is_file()):
        old_text = target.read_text() if target.is_file() else ''
        print(''.join(difflib.unified_diff(
            old_text.splitlines(keepends=True), source.read_text().splitlines(keepends=True),
            fromfile=str(target), tofile=str(source))), end='')
    if os.path.lexists(target):
        if not allow_backup:
            raise ValueError(f'Target exists: {target}. Use --backup to preserve it before replacement.')
        print(f'Back up {target} under {backup_root}')
    print(f'Link {target} -> {source}')
    return True


def install_link(source, target, backup_root):
    target.parent.mkdir(parents=True, exist_ok=True)
    backup = None
    if os.path.lexists(target):
        backup_root.mkdir(parents=True, exist_ok=True)
        backup = Path(tempfile.mkdtemp(prefix='link-', dir=backup_root)) / target.name
        target.rename(backup)
        print(f'Backup saved: {backup}')
    try:
        target.symlink_to(source, target_is_directory=source.is_dir())
    except OSError:
        if backup is not None and not os.path.lexists(target):
            backup.rename(target)
        raise


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--dry-run', action='store_true', help='Preview without writing')
    parser.add_argument('--backup', action='store_true',
                        help='Move an existing target to a backup before linking')
    parser.add_argument('--skills-dir', type=Path, default=Path.home() / '.agents' / 'skills',
                        help='Skill discovery directory (default: ~/.agents/skills)')
    args = parser.parse_args()

    root = Path(__file__).resolve().parent
    codex_home = Path(os.environ.get('CODEX_HOME') or Path.home() / '.codex').expanduser().absolute()
    skill_root = root / 'skills'
    if not skill_root.is_dir():
        parser.exit(1, f'Missing skills directory: {skill_root}\n')
    skills_dir = args.skills_dir.expanduser().absolute()
    backup_root = codex_home / 'backups' / 'factoryfq'
    links = [(skill_root, skills_dir / 'factoryfq')]
    pending = [(src, dst) for src, dst in links
               if preview(src, dst, backup_root, args.backup)]
    if args.dry_run:
        print('Dry run: no files changed.')
        return

    for src, dst in pending:
        install_link(src, dst, backup_root)
    if pending:
        print('Installed. Start a new Codex session to load the configuration.')


if __name__ == '__main__':
    try:
        main()
    except (OSError, UnicodeError, ValueError) as error:
        sys.exit(f'Installation failed: {error}')
