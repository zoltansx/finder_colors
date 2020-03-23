#!/usr/bin/env python

import argparse
from pathlib import Path
from finder_colors import get as get_color, set as set_color, COLORS


def setup_args():
    parser = argparse.ArgumentParser(description='Walk through assignments dirs')
    parser.add_argument('--assignments', '-a')
    parser.add_argument('--dry_run', '-d', action='store_true')

    args = parser.parse_args()

    return args

def main():
    args = setup_args()

    assignemnts_path = args.assignments

    main_dir = Path(assignemnts_path)

    # We only look for panni and luca
    for subdir in [x for x in main_dir.iterdir() if x.is_dir() and not x.name.startswith('.')]:
        # We skip .DS_Store
        for assignment in [path for path in subdir.rglob('*.*') if not path.name.startswith('.')]:
            path = str(assignment)

            # get_color is buggy: a file can have more than one color
            color = get_color(path)

            if color == 'none':
                if args.dry_run:
                    print("set_color(%s, COLORS['blue'])" % path)
                else:
                    set_color(path, 'blue')



main()