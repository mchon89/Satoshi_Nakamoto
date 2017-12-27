#!/usr/bin/env python
# -*- coding: utf-8 -*-


import spacy
import os
import codecs

from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer

import nltk


def main():
	nlp = spacy.load('en_core_web_lg')
	path = os.getcwd() + '/data/'
	data_list = os.listdir(path)
	data_list = sorted(data_list)

	if '.DS_Store' in data_list:
		data_list.remove('.DS_Store')
	else:
		pass

	stopwords = nltk.corpus.stopwords.words('english')
	stopwords.extend(['–', '=', '>', '↩'])
	lemma = WordNetLemmatizer()
	holder = []
	for i in range(len(data_list)):
		fullpath = path + data_list[i]

		data = codecs.open(fullpath, 'r', 'utf-8')
		data_text = data.read()
		data_tokens = data_text.strip().split()
		lemma_data_tokens = [lemma.lemmatize(word.lower()) for word in data_tokens]

		content = [lemma.lemmatize(word.lower()) for word in data_tokens if word.lower() not in stopwords]
		fdist_nostop = nltk.FreqDist(content)
		fdist_stop = nltk.FreqDist(lemma_data_tokens)
		holder.append(data_text)

		print('-----------------------{}-----------------------'.format(data_list[i]))
		print('1 gram with stopwords: {}'.format(fdist_stop.most_common(10)))
		print('1 gram without stopwords: {}'.format(fdist_nostop.most_common(10)))

		for i in range(2,6):
			bgs = nltk.ngrams(data_tokens, i)
			fdist = nltk.FreqDist(bgs)
			print('{} gram: {}'.format(i, fdist.most_common(10)))

	for k in range(len(holder)):
		nlp_doc = nlp(holder[k])
		for y in range(len(holder)):
			nlp_other_doc = nlp(holder[y])
			print("{} {}: {}".format(data_list[k], data_list[y], round(nlp_doc.similarity(nlp_other_doc),4)))


main()