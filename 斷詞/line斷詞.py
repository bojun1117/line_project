import jieba
from collections import Counter
import json

all_words = []
jieba.set_dictionary('dict.txt.big')
stopword_set = set()
with open('停用詞-繁體中文.txt','r', encoding='utf-8') as stopwords:
    for stopword in stopwords:
        stopword_set.add(stopword.rstrip('\n'))
with open('afterdata.txt','r', encoding='utf-8') as sentences:
    for sentence in sentences:
        sentence = sentence.strip('\n')
        words = jieba.cut(sentence, cut_all=False)
        for word in words:
            if word not in stopword_set:
                all_words.append(word)
dict_words = dict(Counter(all_words))
items=list(dict_words.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(10):
    word,count=items[i]
    print("{0:<10}{1:>5}".format(word,count))
