class Translations:
    """ Represents all translations. """

    def __init__(self):
        self.translations = {}

    def add_character(self, translation, character):
        if translation in self.translations:
            self.translations[translation].append(character)
        else:
            self.translations[translation] = [character]

    def print_one(self):
        keys = self.sorted_keys()
        filtered_keys = [key for key in keys if len(self.translations[key]) == 1]
        self.print(filtered_keys)

    def print_more_than_one(self):
        keys = self.sorted_keys()
        filtered_keys = [key for key in keys if len(self.translations[key]) > 1]
        self.print(filtered_keys)

    def print_all(self):
        keys = self.sorted_keys()
        self.print(keys)

    def sorted_keys(self):
        keys = list(self.translations.keys())
        keys.sort(key=str.lower)
        return keys

    def print(self, keys):
        for key in keys:
            print(f"{key}: {self.translations[key]}")
