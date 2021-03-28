import re


class FilterBadWords:

    def __init__(self):
        self._bad_words = None

    def get_regexp(self):
        words = '|'.join(self.bad_words)
        return re.compile(f'({words})', flags=re.IGNORECASE)

    def filter_bad_words(self, phrase: str) -> str:
        regexp = self.get_regexp()
        return regexp.sub(lambda x: '*' * len(x.group(0)), phrase)

    def get_bad_words(self):
        raise NotImplementedError

    @property
    def bad_words(self):
        if self._bad_words is None:
            self._bad_words = self.get_bad_words()

        return self._bad_words
