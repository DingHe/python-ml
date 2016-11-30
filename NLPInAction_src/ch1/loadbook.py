#coding=utf-8
from __future__ import division
'''
Created on 2016年9月25日

@author: Administrator
'''
from nltk.book import *
from nltk.util import bigrams

#text1.concordance("monstrous")
#print "========================"
#text1.similar("monstrous")

#text4.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"])

print len(text3)
print sorted(set(text3))
print len(set(text3))
print len(text3)/len(set(text3))
print text3.count("smote")
print 100 * text4.count('a') / len(text4)

def lexical_diversity(text):
    return len(text) / len(set(text))

def percentage(count,total):
    return 100 * count / total

#print sent1
#print sent2
#print sent3

fdist1=FreqDist(text1)
print fdist1
vocabulary1=fdist1.keys()
print vocabulary1[:50]
print fdist1['whale']
#fdist1.plot(50,cumulative=True)

V=set(text1)
long_word=[w for w in V if len(w) > 15]
print sorted(long_word)

#除非我们更加注重包含不常见词的情况，搭配基本上就是频繁的双连词
bigrams(['more','is','said','than','done'])
text4.collocations()
text8.collocations()

fdist=FreqDist([len(w) for w in text1])
print fdist.keys()
print fdist.items()



