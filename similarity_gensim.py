#!/usr/bin/env python
# -*- coding: utf-8 -*-


import gensim 
import os
import codecs 

from collections import defaultdict
from gensim import corpora, models, similarities


def main():
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

		data = codecs.open(fullpath, 'r', 'utf-8')
		data_text = data.read()
		documents.append(data_text)

	stoplist = set('for a of the and to in'.split())
	texts = [[word for word in document.lower().split() if word not in stoplist] for document in documents]
	frequency = defaultdict(int)
	for text in texts:
		for token in text:
			frequency[token] += 1

	texts = [[token for token in text if frequency[token] > 1] for text in texts]
	dictionary = corpora.Dictionary(texts)
	corpus = [dictionary.doc2bow(text) for text in texts]
	lsi = models.LsiModel(corpus, id2word=dictionary, num_topics=2)
	index = similarities.MatrixSimilarity(lsi[corpus])

	for j in range(len(data_list)):
		doc = documents[j]
		vec_bow = dictionary.doc2bow(doc.lower().split())
		vec_lsi = lsi[vec_bow]
		sims = index[vec_lsi]
		for k in range(len(sims)):
			print("{} {}: {}".format(data_list[j], data_list[k], round(sims[k],5)))


main()