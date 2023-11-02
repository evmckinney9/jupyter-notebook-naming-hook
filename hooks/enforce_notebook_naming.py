#!/usr/bin/env python3

import argparse
import re
import sys


def check_notebook_naming(filename):
    # This regex allows any subdirectories within 'src/notebooks/'
    dev_notebook_regex = r"^src/notebooks/(.*/)?dev_.*\.ipynb$"
    numbered_notebook_regex = r"^src/notebooks/(.*/)?\d{2}_.*\.ipynb$"
    dated_notebook_regex = (
        r"^src/notebooks/(.*/)?\d{2}_.*_[a-z]+_\d{4}-\d{2}-\d{2}\.ipynb$"
    )

    # Check for developing notebooks
    if re.match(dev_notebook_regex, filename):
        return True, ""
    # Check for numbered deliverable notebooks
    elif re.match(numbered_notebook_regex, filename):
        return True, ""
    # Check for dated deliverable notebooks
    elif re.match(dated_notebook_regex, filename):
        return True, ""

    # Verbose error messages
    if not filename.startswith("src/notebooks/"):
        return False, "Notebook is not in the 'src/notebooks/' directory."
    if "/dev_" in filename:
        return (
            False,
            "Developing notebook naming is incorrect. Expected format: 'dev_description.ipynb' or within a subdirectory.",
        )
    if re.search(r"/\d{2}_", filename):
        return (
            False,
            "Deliverable notebook naming is incorrect. Expected format: '01_description.ipynb' or within a subdirectory.",
        )
    if re.search(r"/\d{2}_.*_[a-z]+_\d{4}-\d{2}-\d{2}", filename):
        return (
            False,
            "Deliverable notebook with date and initials is incorrect. Expected format: '01_description_initials_YYYY-MM-DD.ipynb' or within a subdirectory.",
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
