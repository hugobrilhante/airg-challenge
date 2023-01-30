import csv
import os
import unittest

from .script import main

BASE = os.path.dirname(__file__)


class ScriptTestCase(unittest.TestCase):
    def setUp(self):
        self.input = "input.csv"
        self.output = "output.csv"
        with open(os.path.join(BASE, self.input), "w", encoding="utf-8") as file_open:
            file_open.write("Planet|Manufacturer|Model|Type|Passengers\n")
            file_open.write('Yavin|Ubrikkian" Industries|Sail Barge|sailbarge|500\n')
            file_open.write("Bespin|Bespin Motors|Storm IV, Twin-Pod|repulsorcraft|0\n")
            file_open.write("Kuat|Kuat Drive Yards|AT-ST|walker|0\n")

    def test_normalize_csv(self):
        main(self.input)
        with open(os.path.join(BASE, self.output), "r", encoding="utf-8") as file_open:
            reader = csv.reader(file_open)
            self.assertEqual(next(reader), ["Planet", "Manufacturer", "Model", "Type", "Passengers"])
            self.assertEqual(next(reader), ["Yavin", 'Ubrikkian" Industries', "Sail Barge", "sailbarge", "500"])
            self.assertEqual(next(reader), ["Bespin", "Bespin Motors", "Storm IV, Twin-Pod", "repulsorcraft", "0"])
            self.assertEqual(next(reader), ["Kuat", "Kuat Drive Yards", "AT-ST", "walker", "0"])

    def test_normalize_csv_with_delimiter(self):
        main(self.input, delimiter="|")
        with open(os.path.join(BASE, self.output), "r", encoding="utf-8") as file_open:
            reader = csv.reader(file_open, delimiter=",")
            self.assertEqual(next(reader), ["Planet", "Manufacturer", "Model", "Type", "Passengers"])
            self.assertEqual(next(reader), ["Yavin", 'Ubrikkian" Industries', "Sail Barge", "sailbarge", "500"])
            self.assertEqual(next(reader), ["Bespin", "Bespin Motors", "Storm IV, Twin-Pod", "repulsorcraft", "0"])
            self.assertEqual(next(reader), ["Kuat", "Kuat Drive Yards", "AT-ST", "walker", "0"])

    def test_normalize_csv_with_quote_char(self):
        main(self.input, quote_char="'")
        with open(os.path.join(BASE, self.output), "r", encoding="utf-8") as file_open:
            reader = csv.reader(file_open, quotechar="'")
            self.assertEqual(next(reader), ["Planet", "Manufacturer", "Model", "Type", "Passengers"])
            self.assertEqual(next(reader), ["Yavin", "Ubrikkian' Industries", "Sail Barge", "sailbarge", "500"])


if __name__ == "__main__":
    unittest.main()
