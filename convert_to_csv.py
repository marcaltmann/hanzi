import csv
from csv import Sniffer


with open("characters.tsv") as f:
    text = f.read()
    s = Sniffer()
    dialect = s.sniff(text)
    print(dialect)

    #reader = csv.reader(f, delimiter="\t")

    #for row in reader:
    #    print(row)
