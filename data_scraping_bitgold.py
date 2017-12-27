#!/usr/bin/env python
# -*- coding: utf-8 -*-


from newspaper import Article


url = "http://nakamotoinstitute.org/bit-gold/"

article = Article(url)
article.download()
article.parse()
with open('nick_szabo_bitgold.txt', 'w') as f:
	f.write(article.text)