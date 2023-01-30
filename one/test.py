import io
import json
import os
import unittest
from contextlib import redirect_stdout

import requests_mock

from .script import main

BASE = os.path.dirname(__file__)


class ScriptTestCase(unittest.TestCase):
    @requests_mock.Mocker()
    def test_five_first_manufacturers(self, request_mock):
        with open(os.path.join(BASE, "data.json"), encoding="utf-8") as data:
            request_mock.get("https://swapi.dev/api/vehicles/", json=json.load(data))
        with redirect_stdout(io.StringIO()) as stdout:
            main()
        output = stdout.getvalue()
        self.assertIn("1. Corellia Mining Corporation", output)
        self.assertIn("2. Incom Corporation", output)
        self.assertIn("3. SoroSuub Corporation", output)
        self.assertIn("4. Sienar Fleet Systems", output)
        self.assertIn("5. Kuat Drive Yards, Imperial Department of Military Research", output)


if __name__ == "__main__":
    unittest.main()
