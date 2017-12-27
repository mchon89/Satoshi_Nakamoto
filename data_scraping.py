#!/usr/bin/env python
# -*- coding: utf-8 -*-


from newspaper import Article


satoshi_nakamoto = ["http://nakamotoinstitute.org/bitcoin/"]

wei_dai = ["http://nakamotoinstitute.org/b-money/"]

timothy_may = ["http://nakamotoinstitute.org/crypto-anarchist-manifesto/",
				"http://nakamotoinstitute.org/virtual-communities/"]

nick_szabo = ["http://nakamotoinstitute.org/formalizing-securing-relationships/",
		"http://nakamotoinstitute.org/contract-language/",
		"http://nakamotoinstitute.org/secure-property-titles/",
		"http://nakamotoinstitute.org/trusted-third-parties/",
		"http://nakamotoinstitute.org/contracts-with-bearer/",
		"http://nakamotoinstitute.org/the-god-protocols/",
		"http://nakamotoinstitute.org/multinational-small-business/",
		"http://nakamotoinstitute.org/shelling-out/",
		"http://nakamotoinstitute.org/bit-gold/",
		"http://nakamotoinstitute.org/advances-in-distributed-security/",
		"http://nakamotoinstitute.org/the-playdough-protocols/",
		"http://nakamotoinstitute.org/measuring-value/",
		"http://nakamotoinstitute.org/intrapolynomial-cryptography/",
		"http://nakamotoinstitute.org/smart-contracts-glossary/",
		"http://nakamotoinstitute.org/scarce-objects/",
		"http://nakamotoinstitute.org/negative-reputation/"]

ian_grigg = ["http://nakamotoinstitute.org/the-ricardian-contract/",
			"http://nakamotoinstitute.org/triple-entry-accounting/"]

hal_finney = ["http://nakamotoinstitute.org/bitcoin-and-me/",
			"http://nakamotoinstitute.org/for-pay-remailers/",
			"http://nakamotoinstitute.org/politics-vs-technology/",
			"http://nakamotoinstitute.org/pgp-web-of-trust-misconceptions/",
			"http://nakamotoinstitute.org/rpow/",
			"http://nakamotoinstitute.org/digital-cash-and-privacy/"]

author = [satoshi_nakamoto, wei_dai, timothy_may, nick_szabo, ian_grigg, hal_finney]
author_name = ["satoshi_nakamoto", "wei_dai", "timothy_may", "nick_szabo", "ian_grigg", "hal_finney"]


for i in range(len(author)):
	for j in range(len(author[i])):
		article = Article(author[i][j])
		article.download()
		article.parse()
		with open('{}.txt'.format(author_name[i]), 'a') as f:
			f.write(article.text)

url = "http://satoshi.nakamotoinstitute.org/emails/cryptography/"
for k in range(2,19):
	new_url = url + str(k)
	article = Article(new_url)
	article.download()
	article.parse()
	with open('satoshi_nakamoto_email.txt', 'a') as f:
		f.write('{}'.format(article.text))


