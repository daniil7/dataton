from data import authors_cnt
from data import data
import pymorphy2

def get_authors_genders():

    morph = pymorphy2.MorphAnalyzer()
    authors = list(authors_cnt.keys())
    author_gender = {}
    for author in authors:
        parsed_word = morph.parse(author.split(" ")[0])[0]
        author_gender[author] = True if parsed_word.tag.gender == 'masc' else False

    question_gender = []
    for row in data:
        i = 0
        for author in row[1]:
            if(author_gender[author]):
                i += 1
            else:
                i -= 1
        if i > 0:
            question_gender.append((row[0], True))
        if i < 0:
            question_gender.append((row[0], False))

    return question_gender
