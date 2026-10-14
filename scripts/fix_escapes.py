#!/usr/bin/env python3
"""Repair LaTeX escapes inside math spans of *Python* source files.

In ordinary (non-raw) Python strings a LaTeX command needs TWO backslashes:
    "$\\nabla\\cdot\\mathbf{u}$"  ->  runtime  $\nabla\cdot\mathbf{u}$
Layered editors/quoting often leave one too few or one too many.  Inside a
$...$ span of a Python file, this script forces:
    runs of 2+ backslashes  ->  exactly 2
    lone backslash + letter ->  exactly 2

NOTE: markdown notes must keep SINGLE backslashes, so do not run this on .md.

    python3 scripts/fix_escapes.py scripts/make_figures.py
"""
import re
import sys

BS = chr(92)
LETTER = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
RUNS = BS * 2 + '{2,}'
LONE = '(?<!' + BS * 2 + ')' + BS * 2 + '(?=[' + LETTER + '])'


def fix_line(line: str) -> str:
    parts = line.split('$')
    for i in range(1, len(parts), 2):
        seg = re.sub(RUNS, BS * 2, parts[i])
        parts[i] = re.sub(LONE, BS * 2, seg)
    return '$'.join(parts)


def main(paths):
    for path in paths:
        if not path.endswith('.py'):
            print('skipped (not .py):', path)
            continue
        try:
            src = open(path, encoding='utf-8').read()
        except (OSError, IsADirectoryError):
            continue
        fixed = chr(10).join(fix_line(l) for l in src.split(chr(10)))
        if fixed != src:
            open(path, 'w', encoding='utf-8').write(fixed)
            print('fixed', path, len(src), '->', len(fixed))
        else:
            print('clean', path)


if __name__ == '__main__':
    main(sys.argv[1:])
