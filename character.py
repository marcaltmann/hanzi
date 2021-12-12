class Character:
    """Represents a Chinese character."""

    def __init__(self, index, keyword, possible_translations):
        self.index = index
        self.keyword = keyword
        self.possible_translations = possible_translations

    def num_possible_translations(self):
        return len(self.possible_translations)

    def is_unequivocal(self):
        return self.num_possible_translations() == 1
