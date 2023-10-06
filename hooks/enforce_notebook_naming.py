#!/usr/bin/env python3

import argparse
import re
import sys


def check_notebook_naming(filename):
    # Check for developing notebooks
    if re.match(r"^dev_.*\.ipynb$", filename):
        return True
    # Check for deliverable notebooks
    elif re.match(r"^\d{2}_.*\.ipynb$", filename) or re.match(
        r"^\d{2}_.*_[a-z]+_\d{4}-\d{2}-\d{2}\.ipynb$", filename
    ):
        return True
    return False


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="*", help="Filenames to check")
    args = parser.parse_args()

    exit_code = 0
    for filename in args.filenames:
        if not check_notebook_naming(filename):
            print(f"Invalid notebook naming: {filename}")
            exit_code = 1
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
