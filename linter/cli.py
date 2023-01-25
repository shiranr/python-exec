import argparse
from typing import List

from linter import *
from linter.application import Application


def main():
    parser = argparse.ArgumentParser(prog=SHELL_NAME, description=APP_DESCRIPTION)

    parser.add_argument("-v", "--version", action="version", version=APP_VERSION)

    parser.add_argument(
        "-f",
        "--file",
        dest="file_path",
        action="store",
        help="python file path to run",
    )
    parser.add_argument(
        "-i",
        "--invoke",
        dest="invoke_function",
        action="store",
        help="function name to invoke in file",
    )

    parser.add_argument(
        "linter_files",
        help="files to check",
        type=str,
        nargs="+"
    )

    args = parser.parse_args()

    return Application().run(args)
