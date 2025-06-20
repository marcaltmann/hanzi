import csv

EXPECTED_ROW_LENGTH = 8

with open("hanzi.csv") as f:
    reader = csv.reader(f)
    rows = [row for row in reader]
    lengths = [len(row) for row in rows]

for (i, length) in enumerate(lengths):
    if length < EXPECTED_ROW_LENGTH:
        print(f"Line {i + 1} is too short.")
    elif length > EXPECTED_ROW_LENGTH:
        print(f"Line {i + 1} is too long.")

for row in rows:
    while row[-1] == "":
        row.pop()

by_length = sorted(rows, key=len)

for row in by_length:
    if len(row) == EXPECTED_ROW_LENGTH:
        print(row)

longest = by_length[-1]
print(f"Longest row ({len(longest)}):")
print(longest)
