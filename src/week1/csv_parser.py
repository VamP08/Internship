import csv
import sys
from dataclasses import dataclass


@dataclass
class Row:
    distance: float
    items_count: int
    time_of_day: str
    delivery_time: int


def read_csv(file_path: str) -> list[Row]:
    """
    Read a CSV file and return a list of rows as dictionaries.
    """
    with open(file_path, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        rows = []
        for row in reader:
            rows.append(
                Row(
                    float(row["Delivery Distance (km)"]),
                    int(row["Number of Items"]),
                    row["Time of Day"],
                    int(row["Actual Delivery Time (min)"]),
                )
            )

        return rows


def main():
    if len(sys.argv) < 2:
        print("Usage: python csv_parser.py <csv_file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    rows = read_csv(file_path)
    for row in rows:
        print(row)


if __name__ == "__main__":
    main()
