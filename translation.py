class Translation:
    """Represents a keyword translation."""

    def __init__(self, name):
        self.name = name
        self.characters = []

    def add_character(self, character):
        self.characters.append(character)

    def num_characters(self):
        return len(self.characters)
