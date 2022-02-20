from pyexcel_ods3 import get_data
import json
from character import Character
from translations import Translations

data = get_data('zeichen.ods')
rows = data['Schlüsselwörter']

def create_characters(rows):
    characters = []

    for index, row in enumerate(rows):
        keyword = row.pop(0)
        characters.append(Character(index + 1, keyword, row))

    return characters

def create_translations(rows):
    translations = Translations()

    for index, row in enumerate(rows):
        if not row:
            continue

        keyword = row.pop(0)

        for t in row:
            translations.add_character(t, keyword)

    return translations

#characters = create_characters(rows)

translations = create_translations(rows)
translations.print_more_than_one()
