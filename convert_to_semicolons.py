import csv

with open('characters.tsv', encoding='utf-8') as csv_file:
    reader = csv.reader(csv_file, delimiter='\t')

    with open('characters_new.csv', 'w', encoding='utf-8') as new_file:
        writer = csv.writer(new_file, delimiter=';', quoting=csv.QUOTE_MINIMAL, escapechar='\\')
        for row in reader:
            writer.writerow(row)
