#!/usr/bin/env python
# -*- coding: utf-8 -*-


import nltk
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords

import numpy as np
import os
import string
import codecs

import tensorflow as tf


def main():
	path = os.getcwd() + '/data/'
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

	return result

def tensor(result):
	satoshi = result.pop(4)
	satoshi_email = result.pop(4)

	X_train = result
	Y_train = [[0],[1],[2],[3],[4],[5]]

	x = tf.placeholder(tf.float32, [None, 10])
	W = tf.Variable(tf.zeros([10, 6]))
	b = tf.Variable(tf.zeros([6]))
	y = tf.nn.softmax(tf.matmul(x, W) + b)

	y_ = tf.placeholder(tf.float32, [None, 1])

	cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))
	train_step = tf.train.GradientDescentOptimizer(1.0).minimize(cross_entropy)

	sess = tf.InteractiveSession()
	tf.global_variables_initializer().run()
	for _ in range(1000):
  		sess.run(train_step, feed_dict={x: X_train, y_: Y_train})

	prediction = sess.run(tf.argmax(y, 1), feed_dict={x: np.array(satoshi).reshape(1,10)})
	print(tf.argmax(y,1))
	print(prediction)


result = main()
tensor(result)