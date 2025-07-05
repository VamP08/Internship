import csv
from pathlib import Path
from typing import Dict, List

import pytest

from week1.csv_parser import read_csv


def make_sample_csv(path: Path) -> List[Dict[str, str]]:
    """
    Create a CSV with two sample rows and return the raw dict rows.
    """
    headers = [
        "Delivery Distance (km)",
        "Number of Items",
        "Time of Day",
        "Actual Delivery Time (min)",
    ]
    rows = [
        {
            "Delivery Distance (km)": "12.3",
            "Number of Items": "4",
            "Time of Day": "morning",
            "Actual Delivery Time (min)": "45",
        },
        {
            "Delivery Distance (km)": "7.8",
            "Number of Items": "2",
            "Time of Day": "evening",
            "Actual Delivery Time (min)": "30",
        },
    ]

    with path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)
    return rows


def test_read_csv_returns_correct_number_of_rows(tmp_path):
    # Arrange: Create the sample CSV on disk
    csv_file = tmp_path / "sample.csv"
    raw_rows = make_sample_csv(csv_file)
    expected_count = len(raw_rows)

    # Act: parse into Row objects
    parsed_rows = read_csv(str(csv_file))

    # Assert: number of parsed rows matches
    assert len(parsed_rows) == expected_count


def test_empty_csv_returns_empty_list(tmp_path):
    # Arrange: create an empty file
    csv_file = tmp_path / "empty.csv"
    csv_file.write_text("")

    # Act
    result = read_csv(str(csv_file))

    # Assert
    assert result == []


def test_invalid_csv_headers_raise_keyerror(tmp_path):
    # Arrange: write bad headers
    csv_file = tmp_path / "invalid_headers.csv"
    csv_file.write_text("Name,Years,E-mail\nAlice,30,alice@example.com")

    # Act & Assert
    with pytest.raises(KeyError):
        read_csv(str(csv_file))
