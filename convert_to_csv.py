import csv

with open("hanzi.tsv") as csvfile:
    reader = csv.reader(csvfile, delimiter="\t")
    csv_all = [row for row in reader]


LONGEST_ROW = 11

for row in csv_all:
    # Make first column consistent.
    if row[0] == "":
        row[0] = "None"

    # Switch first and second columns.
    tmp = row[1]
    row[1] = row[0]
    row[0] = tmp

    # Add column for cards.
    row.insert(2, "False")

    # Fill up row if necessary.
    length_to_fill = LONGEST_ROW - len(row)
    fill_list = [""] * length_to_fill
    row.extend(fill_list)


with open("hanzi.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile, delimiter=",")
    for row in csv_all:
        writer.writerow(row)
