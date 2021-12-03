class Character:
    """Represents a Chinese character."""

    def __init__(self, index, keyword, translations):
        self.index = index
        self.keyword = keyword
        self.translations = translations

    def num_translations(self):
        return len(self.translations)
