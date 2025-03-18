import csv
import pprint

with open("hanzi.csv") as csvfile:
    reader = csv.reader(csvfile)
    csv_all = [row for row in reader]

first_row_words = [row[0] for row in csv_all]

pprint.pp(first_row_words)
