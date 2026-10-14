#!/usr/bin/env python3
"""CLI for the Transport Atlas figure factory.

Framework and helpers live in figlib.py; figure definitions live in
figpart1..figpartN.py, each registering itself with @figure("name").

    /home/stav/.pixi/envs/sage/bin/python scripts/make_figures.py [name ...]
    /home/stav/.pixi/envs/sage/bin/python scripts/make_figures.py --list
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import importlib                                        # noqa: E402

for _i in range(1, 14):
    try:
        importlib.import_module("figpart%d" % _i)
    except ModuleNotFoundError:
        pass

from figlib import main                                 # noqa: E402

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
