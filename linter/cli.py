import argparse

from py._builtin import execfile

from linter import *


def main():
    parser = argparse.ArgumentParser(prog=SHELL_NAME, description=APP_DESCRIPTION)

    parser.add_argument("-v", "--version", action="version", version=APP_VERSION)

    config_group = parser.add_mutually_exclusive_group()
    config_group.add_argument(
        "--function",
        "-f",
        dest="file_path",
        action="store",
        help="python file path to run",
    )
    config_group.add_argument(
        "--name",
        "-n",
        dest="function_name",
        action="store",
        help="function name to invoke in file",
    )
    args = parser.parse_args()
    return run(args.file_path, args.function_name)


def run(file_path: str, function_name: str):
    loc = {}
    config = dict()
    execfile(file_path, config, loc)
    return loc.get(function_name)()
