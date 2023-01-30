import csv
import io
import os
import unittest
from contextlib import redirect_stdout

from .script import main

BASE = os.path.dirname(__file__)


class ScriptTestCase(unittest.TestCase):
    def setUp(self):
        self.script = os.path.join(BASE, "script.py")

    def test_command_line_arguments(self):
        with redirect_stdout(io.StringIO()) as stdout:
            main("data.csv", 100, 10)
        msg = "The data.csv with 100 lines generated from 10 to 10 was successfully generated\n"
        output = stdout.getvalue()
        self.assertEqual(msg, output)

        with redirect_stdout(io.StringIO()) as stdout:
            main("test.csv", 10, 5)
        msg = "The test.csv with 10 lines generated from 5 to 5 was successfully generated\n"
        output = stdout.getvalue()
        self.assertEqual(msg, output)

        with redirect_stdout(io.StringIO()) as stdout:
            main("data.csv", 100, 50)
        msg = "The data.csv with 100 lines generated from 50 to 50 was successfully generated\n"
        output = stdout.getvalue()
        self.assertEqual(msg, output)

    def test_file_generation(self):
        main("test.csv", 100, 10)
        with open(os.path.join(BASE, "test.csv"), encoding="utf-8") as file_open:
            reader = csv.reader(file_open)
            data = list(reader)
        assert len(data) == 100

    def test_data_validation(self):
        main("test.csv", 100, 10)
        with open(os.path.join(BASE, "test.csv"), encoding="utf-8") as file_open:
            reader = csv.reader(file_open)
            data = list(reader)
        for row in data:
            assert isinstance(int(row[0]), int)
            assert isinstance(row[1], str)


if __name__ == "__main__":
    unittest.main()
