import argparse
import csv
import os
import random
import string

BASE = os.path.dirname(__file__)


def main(filename, num_rows, chunk_size):
    with open(os.path.join(BASE, filename), "w", encoding="utf-8") as file_open:
        csv_file = csv.writer(file_open)
        for row in range(0, num_rows, chunk_size):
            rows = []
            for _ in range(row, min(row + chunk_size, num_rows)):
                rand_num = random.randint(1000, 9999)
                rand_string = "".join(random.choices(string.ascii_letters, k=10))
                rows.append([rand_num, rand_string])
            csv_file.writerows(rows)
        print(
            f"The {filename} with {num_rows} lines generated from {chunk_size} to {chunk_size}"
            f" was successfully generated"
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--num_rows", type=int, default=100, help="number of rows to generate")
    parser.add_argument("--filename", type=str, default="data.csv", help="name of the CSV file to write")
    parser.add_argument(
        "--chunk_size", type=int, default=10000, help="number of rows to write to the CSV file in one chunk"
    )
    args = parser.parse_args()
    main(args.filename, args.num_rows, args.chunk_size)
