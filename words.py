from process_questions import get_authors_genders

import numpy as np
from razdel import sentenize, tokenize
from pymorphy2 import MorphAnalyzer

WORDLIST = {}
morph = MorphAnalyzer()

parsed_data = []

male_phrases = []
female_phrases = []

i = 0
for text, is_male in get_authors_genders():
    for sent in sentenize(text):
        tokens = [_.text for _ in tokenize(sent.text)]
        filtered = []

        for token in tokens:  # filter tokens
            if len(token) != 1:
                token = morph.parse(token)[0].normal_form
                filtered.append(token)
                if token not in WORDLIST:
                    WORDLIST[token] = i
                    i += 1

        if is_male:
            male_phrases.extend(filtered)
        else:
            female_phrases.extend(filtered)

        parsed_data.append(
            (filtered, is_male)
        )

TOTAL_WORDS = len(WORDLIST)


def to_vec(words):
    vec = np.zeros(TOTAL_WORDS)
    for word in words:
        if word in WORDLIST:
            vec[WORDLIST[word]] = 1


for i, row in enumerate(parsed_data):
    parsed_data[i] = (
        to_vec(parsed_data[i][0]),
        parsed_data[i][1]
    )
print(WORDLIST)
