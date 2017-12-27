#!/usr/bin/env python
# -*- coding: utf-8 -*-


import pandas as pd
import os
import codecs
import matplotlib.pyplot as plt

from sklearn.feature_extraction.text import CountVectorizer 
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import euclidean_distances 
from sklearn.metrics.pairwise import cosine_similarity 
from sklearn.manifold import MDS



path = os.getcwd() + '/data/'
data_list = os.listdir(path)
data_list = sorted(data_list)

if '.DS_Store' in data_list:
    data_list.remove('.DS_Store')
else:
    pass

documents = [] 
for i in range(len(data_list)):
    fullpath = path + data_list[i]
    documents.append(fullpath)

vectorizer = CountVectorizer(input='filename')
dtm = vectorizer.fit_transform(documents)
vocab = vectorizer.get_feature_names()

dtm = dtm.toarray()
dist = euclidean_distances(dtm)
cosdist = 1 - cosine_similarity(dtm)

mds = MDS(n_components=2, dissimilarity="precomputed", random_state=1)
pos = mds.fit_transform(cosdist)
xs, ys = pos[:, 0], pos[:, 1]

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)
ax.set_xlim([min(xs)-.05, max(xs)+.05])
ax.set_ylim([min(ys)-.05, max(ys)+.05])

for x, y, name in zip(xs, ys, data_list): 
    name = name.replace('.txt', '')
    plt.scatter(x, y)
    plt.text(x, y, name, fontsize=7)

plt.show()
fig.savefig('2d')