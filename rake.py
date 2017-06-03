#!/usr/bin/python3

import nltk,string,re
from nltk.corpus import stopwords
from nltk import word_tokenize

text = """
Compatibility of systems of linear constraints over the set of natural numbers.
Criteria of compatibility of a system of linear Diophantine equations, strict inequations,
and nonstrict inequations are considered. Upper bounds for components of a minimal set
of solutions and algorithms of construction of minimal generating sets of solutions for all
types of systems are given. These criteria and the corresponding algorithms for
constructing a minimal supporting set of solutions can be used in solving all the
considered types of systems and systems of mixed types."""

stopwords = set(stopwords.words('english'))
allwords = [x.lower() for x in word_tokenize(text)]
idx = [i for i in range(len(allwords)) if not(allwords[i] in stopwords) and not(allwords[i] in string.punctuation)]
content_words = {allwords[i]:i for i in idx}
keywords = [[]]
tmp = [keywords[-1].append(content_words[allwords[idx[i]]]) if (i==0 or idx[i]==idx[i-1]+1) else keywords.append([content_words[allwords[idx[i]]]]) for i in range(len(idx))]
un_key = []
tmp = [un_key.append(x) for x in keywords if not x in un_key]
pairs = [(i,j) for i in content_words.values() for j in content_words.values()]
graph = {(p[0],p[1]):sum([(p[0] in k and p[1] in k) for k in un_key]) for p in pairs}
freq = {i:graph[(i,i)] for i in content_words.values()}
deg = {i:sum([graph[(i,j)] for j in content_words.values() if (i,j) in graph]) for i in content_words.values()}
scores = [sum([deg[k[i]]/freq[k[i]] for i in range(len(k))]) for k in un_key]
sorted_idx = sorted(range(len(scores)), key=scores.__getitem__, reverse=True)
results = [(' '.join([allwords[i] for i in un_key[j]]),scores[j]) for j in sorted_idx]

tmp = [print(r) for r in results]
