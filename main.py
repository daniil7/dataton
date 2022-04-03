from process_questions import get_authors_genders

import pandas as pd
import matplotlib.pyplot as plt

from wordcloud import WordCloud

question_gender = get_authors_genders()

text_m = ''
text_f = ''
for question in question_gender:
    if question[1]:
        text_m = text_m + '\n' + (question[0])
    else:
        text_f = text_f + '\n' + (question[0])

# подгружаем библиотеку nltk со стоп-словами
from nltk.corpus import stopwords
# сохраняем список с русскими стоп-cловами в переменную stop_words
stop_words = stopwords.words('russian')

cloud_m = WordCloud(stopwords = stop_words).generate(text_m)
cloud_f = WordCloud(stopwords = stop_words).generate(text_f)

plt.imshow(cloud_m)
plt.axis('off')
plt.show()

plt.imshow(cloud_f)
plt.axis('off')
plt.show()

from words import parsed_data
from perceptron import Net

# random.shuffle(parsed_data)

for_train = parsed_data[:int(len(parsed_data) * (1/3))]
for_test = parsed_data[int(len(parsed_data) * (1/3)):]

perceptron = Net(len(parsed_data[0][0]), 40)

print("Переходим к тренировке")

# тренируем
for i in range(1):
    for row in for_train:
        perceptron.train(row[0], row[1])
    print(i)

good = 0

for row in for_test:
    # print(perceptron.perceptron(row[0]) == row[1])
    if perceptron.perceptron(row[0]) == row[1]:
        good += 1

print("Процент угадываний: ", good / len(for_test))
