import csv
import locale

def prepare_reader():
    tsv_file_path = 'characters.tsv'
    file = open(tsv_file_path)
    reader = csv.reader(file, delimiter='\t')
    next(reader)  # Skip the header row
    return reader

def create_words_dict(reader):
    words = {}

    for row in reader:
        for cell in row[2:]:
            word = cell.strip()
            if not word: continue
            if word in words:
                words[word] += 1
            else:
                words[word] = 1

    return words


# Example usage
locale.setlocale(locale.LC_ALL, '')

reader = prepare_reader()
words = create_words_dict(reader)

duplicates = [(word, count) for (word, count) in words.items() if count > 1]

sorted_duplicates = sorted(duplicates, key=lambda w: locale.strxfrm(w[0].lower()), reverse=False)

for (word, count) in sorted_duplicates:
    print(word, count)
