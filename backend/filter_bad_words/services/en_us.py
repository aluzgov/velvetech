import os

import requests

from filter_bad_words.config import WORDS_DIR, EN_WORDS_URL
from filter_bad_words.services.filter_bad_words import FilterBadWords


class EnUsFilterBadWords(FilterBadWords):

    def get_bad_words(self):
        words_from_github = self._get_bad_words_from_github()
        if words_from_github is not None:
            return words_from_github

        return self.get_bad_words_from_file()

    def _get_bad_words_from_github(self):
        try:
            response = requests.get(EN_WORDS_URL)
            return tuple(bad_word.strip().lower() for bad_word in response.text.split('\n'))
        except (requests.exceptions.HTTPError, AttributeError):
            return None

    def get_bad_words_from_file(self):
        filename = os.path.join(WORDS_DIR, 'en.txt')
        with open(filename) as bad_words_file:
            return tuple(bad_word.strip().lower() for bad_word in bad_words_file.readlines())
