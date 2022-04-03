from process_questions import get_authors_genders

import numpy as np
from razdel import sentenize, tokenize
from pymorphy2 import MorphAnalyzer

WORDLIST = set()
morph = MorphAnalyzer()

parsed_data = []

male_phrases = []
female_phrases = []

def to_vec(words):
    pass


for text, is_male in get_authors_genders():
    for sent in sentenize(text):
        tokens = [_.text for _ in tokenize(sent.text)]
        filtered = []

        for token in tokens:  # filter tokens
            if len(token) != 1:
                token = morph.parse(token)[0].normal_form
                filtered.append(token)

        if is_male:
            male_phrases.extend(filtered)
        else:
            female_phrases.extend(filtered)

        WORDLIST.update(filtered)
        parsed_data.append(
            (filtered, is_male)
        )
