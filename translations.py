class Translations:
    """ Represents all translations. """

    def __init__(self):
        self.translations = {}

    def add_character(self, translation, character):
        if translation in self.translations:
            self.translations[translation].append(character)
        else:
            self.translations[translation] = [character]

    def print(self):
        for key, value in self.translations.items():
            print(f"{key}: {value}")
