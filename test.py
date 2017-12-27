#!/usr/bin/env python
# -*- coding: utf-8 -*-


import spacy
import os
import string
from spacy.en.word_sets import STOP_WORDS


# getting path
nlp = spacy.load('en')
path = os.getcwd()
full_satoshi = path + '/data/satoshi_nakamoto.txt'

# reading the file
satoshi_nakamoto = open(full_satoshi, 'r')
satoshi_nakamoto_text = satoshi_nakamoto.read()
satoshi_nakamoto_tokens = satoshi_nakamoto_text.strip().split()

# apostrophe count
satoshi_nakamoto_count = satoshi_nakamoto_text.count("'")

# number of uppercase letters
counter = 0
for token in satoshi_nakamoto_tokens:
	if token.isupper():
		counter += 1

# number of punctuation 
counter_1 = 0 
puncts = list(string.punctuation)
for token in satoshi_nakamoto_tokens:
	for punct in puncts:
		if punct in token:
			counter_1 += 1

# number of the letters of every word
counter_2 = 0
for token in satoshi_nakamoto_tokens:
	counter_2 = counter_2 + len(list(token))

# number of pronoun 
counter_3 = 0
pronouns = ['i', 'we', 'she', 'he', 'our', 'my', 'us', 'they', 'it', 'its', 'them', 'his', 'her', 'me']
for token in satoshi_nakamoto_tokens:
	if token.lower() in pronouns:
		counter_3 += 1

# number of uppercase letter in every letter
counter_4 = 0
for token in satoshi_nakamoto_tokens:
	temp = list(token)
	for i in range(len(temp)):
		if temp[i].isupper():
			counter_4 += 1

# number of stop words
counter_5 = 0 
stop = list(STOP_WORDS)
for token in satoshi_nakamoto_tokens:
	if token in stop:
		counter_5 += 1

# number of sentence 
from nltk.tokenize import sent_tokenize

sentence = sent_tokenize(satoshi_nakamoto_text)

# printing
print('#complexity: {}'.format(len(set(satoshi_nakamoto_tokens))/len(satoshi_nakamoto_tokens)))
print('#apostrophe/#words: {}'.format(satoshi_nakamoto_count/len(satoshi_nakamoto_tokens)))
print("#uppercase word/#words: {}".format(counter/len(satoshi_nakamoto_tokens)))
print("#characters/#words: {}".format(counter_2/len(satoshi_nakamoto_tokens)))
print("#pronouns/#words: {}".format(counter_3/len(satoshi_nakamoto_tokens)))
print("#whitespace/#words: {}".format(satoshi_nakamoto_text.count(r' ')/len(satoshi_nakamoto_tokens)))
print("#stop/#words: {}".format(counter_5/len(satoshi_nakamoto_tokens)))
print("#punct/#characters: {}".format(counter_1/counter_2))
print("#uppercase letter/#characters: {}".format(counter_4/counter_2))
print("#words/#sentence: {}".format(len(satoshi_nakamoto_tokens)/len(sentence)))

# entity extraction
satoshi = nlp(satoshi_nakamoto_text)
entity_list = ['PERSON', 'NORP', 'FACILITY', 'ORG', 
              'GPE', 'LOC', 'PRODUCT', 'EVENT', 'WORK_OF_ART', 'LANGUAGE', 'LAW']

satoshi_list = []
for i in range(len(satoshi)):
	if satoshi[i].ent_type_ in entity_list:
		satoshi_list.append(satoshi[i].text)

print("entity extration: {}".format(satoshi_list))

# noun chunk
noun_chunk = []
for chunk in satoshi.noun_chunks:
	noun_chunk.append(chunk.text)

print("noun_chunk: {}".format(noun_chunk))

# n gram
import nltk

tokens = nltk.tokenize.word_tokenize(satoshi_nakamoto_text)
bgs = nltk.ngrams(tokens, 3)
fdist = nltk.FreqDist(bgs)
print(fdist.most_common(30))


