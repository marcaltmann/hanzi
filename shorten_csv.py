import csv

with open("hanzi.csv") as f:
    reader = csv.reader(f)
    rows = [row for row in reader]

# Check first
for row in rows:
    if row[-1] != "":
        print("Cannot shorten the csv, last column not empty.")
        exit()

# Shorten
for row in rows:
    row.pop()

with open("hanzi_shortened.csv", "w") as f:
    writer = csv.writer(f, lineterminator="\n")
    writer.writerows(rows)
