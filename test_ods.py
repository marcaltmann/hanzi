from pyexcel_ods3 import get_data
import json
from character import Character

data = get_data('characters.ods')
rows = data['Sheet1']

def create_characters(rows):
    characters = []

    for index, row in enumerate(rows):
        keyword = row.pop(0)
        characters.append(Character(index + 1, keyword, row))

    return characters

characters = create_characters(rows)

print('Unequivocal translations:')

for c in characters:
    if c.is_unequivocal():
        print(f"{c.keyword}: {c.possible_translations[0]}")
