import argparse
import csv
import os

BASE = os.path.dirname(__file__)


def main(file_name, delimiter=None, quote_char=None):
    normalize = ","

    with open(os.path.join(BASE, file_name), "r", encoding="utf-8") as file_open:
        lines = file_open.readlines()
    if not delimiter or not quote_char:
        try:
            dialect = csv.Sniffer().sniff("".join(lines))
            delimiter = delimiter if delimiter else dialect.delimiter
            quote_char = quote_char if quote_char else dialect.quotechar
        except csv.Error:
            delimiter = "|"
            quote_char = '"'
    new_lines = []
    for line in lines:
        fields = line.strip().split(delimiter)
        new_fields = []
        for field in fields:
            if normalize in field or '"' in field:
                field = quote_char + field.replace('"', quote_char * 2) + quote_char
            new_fields.append(field)
        new_line = normalize.join(new_fields)
        new_lines.append(new_line)
    with open(os.path.join(BASE, "output.csv"), "w", encoding="utf-8") as file_open:
        file_open.write("\n".join(new_lines))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file_name", help="The file name to be processed")
    parser.add_argument("--delimiter", help='The input delimiter to use (default: "|")')
    parser.add_argument("--quote_char", help='The quote character to use (default: ")')
    parser.add_argument("--normalize", help='The input normalize to use (default: ",")')
    args = parser.parse_args()
    main(args.file_name, args.delimiter, args.quote_char)
