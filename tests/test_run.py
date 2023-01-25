import os
import unittest
from argparse import Namespace

from linter.application import Application


class ScriptTest(unittest.TestCase):
    def test_run_script(self):
        path = os.getcwd()
        app = Application()
        args = Namespace(
            file_path=os.path.join(path, "testscript.py"),
            invoke_function="main",
            linter_files=["test.py"]
        )
        result = app.run(args)
        assert result == 42
