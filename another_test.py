#!/usr/bin/env python
# -*- coding: utf-8 -*-


import spacy
import os


# getting path
nlp = spacy.load('en_core_web_lg')
path = os.getcwd()
full_satoshi = path + '/data/satoshi_nakamoto.txt'

# reading the file
satoshi_nakamoto = open(full_satoshi, 'r')
satoshi_nakamoto_text = satoshi_nakamoto.read()
satoshi_nakamoto_tokens = satoshi_nakamoto_text.strip().split()

# spacy
doc = nlp(satoshi_nakamoto_text)

print(doc.similarity(doc))