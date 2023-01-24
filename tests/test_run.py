import os

from linter.cli import run


def test_run_script():
    path = os.getcwd()
    result = run(os.path.join(path, "testscript.py"), 'main')
    assert result == 42
