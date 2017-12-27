#!/usr/bin/env python
# -*- coding: utf-8 -*-


import nltk
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords

import numpy as np
import os
import string
import codecs

from sklearn import svm
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB


def main():
	path = os.getcwd() + '/other_data/'
	data_list = os.listdir(path)
	data_list = sorted(data_list)

	if '.DS_Store' in data_list:
		data_list.remove('.DS_Store')
	else:
		pass

	result = []
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

		temp = [round(len(set(data_tokens))/len(data_tokens),4),
			round(apostrophe/len(data_tokens),4), 
			round(counter/len(data_tokens),4),
			round(counter_2/len(data_tokens),4),
			round(counter_3/len(data_tokens),4),
			round(data_text.count(r' ')/len(data_tokens),4),
			round(counter_5/len(data_tokens),4),
			round(counter_1/counter_2,4), 
			round(counter_4/counter_2,4), 
			round(len(data_tokens)/len(sentence),4)]

		result.append(temp)
	
	satoshi_pop = data_list.index('satoshi_nakamoto.txt')
	satoshi_email_pop = data_list.index('satoshi_nakamoto_email.txt')

	satoshi = result.pop(satoshi_pop)
	satoshi_email = result.pop(satoshi_email_pop)

	X = np.array(result)

	Y = []
	for k in range(len(data_list)):
		if 'hal' in data_list[k]:
			Y.append([0])
		elif 'ian' in data_list[k]:
			Y.append([1])
		elif 'nick' in data_list[k]:
			Y.append([2])
		elif 'timothy' in data_list[k]:
			Y.append([3])
		elif 'wei' in data_list[k]:
			Y.append([4])

	Y = np.ravel(Y)
	print(data_list)

	# Neural Network
	clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(10,8), random_state=1)
	clf.fit(X,Y)
	print(clf.score(X,Y))
	print(clf.predict(np.array(satoshi).reshape(1,-1)))
	print(clf.predict(np.array(satoshi_email).reshape(1,-1)))

	# Support Vector Machine
	new_clf = svm.SVC()
	new_clf.fit(X, Y)
	print(new_clf.score(X,Y))
	print(new_clf.predict(np.array(satoshi).reshape(1,-1)))
	print(new_clf.predict(np.array(satoshi_email).reshape(1,-1)))	

	# Random Forest
	rf = RandomForestClassifier(n_estimators=10, random_state=0, max_depth=None)
	rf.fit(X,Y)
	print(rf.score(X,Y))
	print(rf.predict(np.array(satoshi).reshape(1,-1)))
	print(rf.predict(np.array(satoshi_email).reshape(1,-1)))	

	# Gaussian NB
	gnb = GaussianNB()
	gnb.fit(X,Y)
	print(gnb.score(X,Y))
	print(gnb.predict(np.array(satoshi).reshape(1,-1)))
	print(gnb.predict(np.array(satoshi_email).reshape(1,-1)))	


main()
