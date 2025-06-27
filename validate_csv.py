import csv

EXPECTED_ROW_LENGTH = 7

with open("hanzi.csv") as f:
    reader = csv.reader(f)
    rows = [row for row in reader]
    lengths = [len(row) for row in rows]

printed_row_length_errors = False

for (i, length) in enumerate(lengths):
    if length < EXPECTED_ROW_LENGTH:
        print(f"Line {i + 1} is {EXPECTED_ROW_LENGTH - length} column(s) too short.")
        printed_row_length_errors = True
    elif length > EXPECTED_ROW_LENGTH:
        print(f"Line {i + 1} is {length - EXPECTED_ROW_LENGTH} column(s) too long.")
        printed_row_length_errors = True

for row in rows:
    while row[-1] == "":
        row.pop()

by_length = sorted(rows, key=len)


longest_rows = [row for row in by_length if len(row) == EXPECTED_ROW_LENGTH]

if (longest_rows):
    if printed_row_length_errors:
        print()
    print(f"{len(longest_rows)} row(s) that match EXPECTED_ROW_LENGTH of {EXPECTED_ROW_LENGTH} columns:")
    for row in longest_rows:
        print(row)
