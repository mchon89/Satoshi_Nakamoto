#!/usr/bin/env python
# -*- coding: utf-8 -*-


import nltk
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords

import spacy
import os
import string
import codecs


def main():
	path = os.getcwd() + '/data/'
	data_list = os.listdir(path)
	data_list = sorted(data_list)

	if '.DS_Store' in data_list:
		data_list.remove('.DS_Store')
	else:
		pass

	for i in range(len(data_list)):
		fullpath = path + data_list[i]

		data = codecs.open(fullpath, 'r', 'utf-8')
		data_text = data.read()
		data_tokens = data_text.strip().split()

		apostrophe = data_text.count("'")

		counter = 0
		for token in data_tokens:
			if token.isupper():
				counter += 1

		counter_1 = 0 
		puncts = list(string.punctuation)
		for token in data_tokens:
			for punct in puncts:
				if punct in token:
					counter_1 += 1

		counter_2 = 0
		for token in data_tokens:
			counter_2 = counter_2 + len(list(token))

		counter_3 = 0
		pronouns = ['i', 'we', 'she', 'he', 'our', 'my', 'us', 'they', 'it', 'its', 'them', 'his', 'her', 'me']
		for token in data_tokens:
			if token.lower() in pronouns:
				counter_3 += 1

		counter_4 = 0
		for token in data_tokens:
			temp = list(token)
			for j in range(len(temp)):
				if temp[j].isupper():
					counter_4 += 1

		counter_5 = 0 
		stop = nltk.corpus.stopwords.words('english')
		for token in data_tokens:
			if token in stop:
				counter_5 += 1

		sentence = sent_tokenize(data_text)

		print('-----------------------{}-----------------------'.format(data_list[i]))
		print('#unique words/#words: {}'.format(round(len(set(data_tokens))/len(data_tokens),4)))
		print('#apostrophe/#words: {}'.format(round(apostrophe/len(data_tokens),4)))
		print("#uppercase word/#words: {}".format(round(counter/len(data_tokens),4)))
		print("#characters/#words: {}".format(round(counter_2/len(data_tokens),4)))
		print("#pronouns/#words: {}".format(round(counter_3/len(data_tokens),4)))
		print("#whitespace/#words: {}".format(round(data_text.count(r' ')/len(data_tokens),4)))
		print("#stop/#words: {}".format(round(counter_5/len(data_tokens),4)))
		print("#punct/#characters: {}".format(round(counter_1/counter_2,4)))
		print("#uppercase letter/#characters: {}".format(round(counter_4/counter_2,4)))
		print("#words/#sentence: {}".format(round(len(data_tokens)/len(sentence),4)))


main()