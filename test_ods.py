from pyexcel_ods3 import get_data
import json
from character import Character
from translation import Translation

data = get_data('characters.ods')
rows = data['Sheet1']

def create_characters(rows):
    characters = []

    for index, row in enumerate(rows):
        keyword = row[0]
        characters.append(Character(index + 1, keyword))

    return characters

characters = create_characters(rows)

def create_translations(rows, characters):
    word_dict = {}

    for index, row in enumerate(rows):
        row.pop(0)

        for word in row:
            if word in word_dict:
                word_dict[word].add_character(characters[index])
            else:
                translation = Translation(word)
                translation.add_character(characters[index])
                word_dict[word] = translation

    return word_dict


translations = create_translations(rows, characters)

def get_keyword(character):
    return character.keyword

for translation, characters in translations.items():
    print(characters)
    #keywords = map(get_keyword, characters)
    #print(keywords)
    print(f"{translation}: ")

#sort_orders = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)

#for i in sort_orders:
#    print(i[0], i[1])
