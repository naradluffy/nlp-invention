"""
created by Sri Ratna Wulan
inspired by https://machinelearningmastery.com/
Sep 16, 2020. 15:38
input: we have shakespeare.txt. it's about all shakespeare works.
output: we want to count the words. we sort it by the frequency descending. we put them to the results.txt
"""

import string
from nltk.corpus import stopwords
from collections import Counter
from itertools import starmap

# load text
filename = 'shakespeare.txt'
with open(filename, 'rt') as file:
    text = file.read()

# split into words by white space
words = text.split()

# remove punctuation from each word
# we have 3 args. the third one means remove punctuation inside string.punctuation.
table = str.maketrans('', '', string.punctuation)
stripped = [w.translate(table) for w in words]

# remove remaining tokens that are not alphabetic
words = [word for word in stripped if word.isalpha()]

# filter out stop words
stop_words = set(stopwords.words('english'))
words = [w for w in words if not w in stop_words]

# count words, sort them by values, save it into a list.
count_words = Counter(words)
results = list(starmap(lambda key, value: key + ' : ' + str(value) + '\n', count_words.most_common()))

# save the result to a .txt
with open('result.txt', 'w') as out:
    out.writelines(results)
