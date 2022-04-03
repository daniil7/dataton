import csv
from collections import Counter


# text, author
data = []
authors_cnt = Counter()

with open('dataset.csv', 'r', encoding="utf-8") as f:
    reader = csv.DictReader(f, delimiter='\t')
    for row in reader:
        authors = [a.strip() for a in row["Author Full Name"].split(',')]
        data.append((row["QuestionText"], authors))
        authors_cnt.update(authors)
