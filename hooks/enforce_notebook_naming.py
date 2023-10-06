#!/usr/bin/env python3

import argparse
import re
import sys


def check_notebook_naming(filename):
    # Check for developing notebooks
    if re.match(r"^src/notebooks/dev_.*\.ipynb$", filename):
        return True, ""
    # Check for deliverable notebooks
    elif re.match(r"^src/notebooks/\d{2}_.*\.ipynb$", filename):
        return True, ""
    elif re.match(
        r"^src/notebooks/\d{2}_.*_[a-z]+_\d{4}-\d{2}-\d{2}\.ipynb$", filename
    ):
        return True, ""

    # Verbose error messages
    if not filename.startswith("src/notebooks/"):
        return False, "Notebook is not in the 'src/notebooks/' directory."
    elif filename.startswith("src/notebooks/dev_"):
        return (
            False,
            "Developing notebook naming is incorrect. Expected format: 'dev_description.ipynb'",
        )
    elif re.match(r"^src/notebooks/\d{2}_.*\.ipynb$", filename):
        return (
            False,
            "Deliverable notebook naming is incorrect. Expected format: '01_description.ipynb'",
        )
    elif re.match(
        r"^src/notebooks/\d{2}_.*_[a-z]+_\d{4}-\d{2}-\d{2}\.ipynb$", filename
    ):
        return (
            False,
            "Deliverable notebook with date and initials is incorrect. Expected format: '01_description_initials_YYYY-MM-DD.ipynb'",
        )

    return False, "Unknown naming error."


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="*", help="Filenames to check")
    args = parser.parse_args()

    exit_code = 0
    for filename in args.filenames:
        is_valid, error_message = check_notebook_naming(filename)
        if not is_valid:
            print(
                f"Invalid notebook naming: {filename}. Reason: {error_message}"
            )
            exit_code = 1
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
