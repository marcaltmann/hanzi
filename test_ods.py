from pyexcel_ods3 import get_data
import json
from character import Character

data = get_data('characters.ods')
rows = data['Sheet1']

characters = []

for index, row in enumerate(rows):
    keyword = row.pop(0)
    characters.append(Character(index + 1, keyword, row))

for c in characters:
    print(c.index, c.keyword, c.num_translations())


for row in rows:
    row.pop(0)

flat_list = [item for sublist in rows for item in sublist]

word_dict = {}

for word in flat_list:
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1

sort_orders = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)

for i in sort_orders:
    print(i[0], i[1])
