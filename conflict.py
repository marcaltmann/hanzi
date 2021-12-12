class Conflict:
    """ Represents a case where a translation has > 1 candidate. """

    def __init__(self, translation):
        self.translation = translation
        self.candidates = []

    def add_candidate(self, candidate):
        self.candidates.append(candidate)

    def candidate_names(self):
        return [c.keyword for c in self.candidates]
