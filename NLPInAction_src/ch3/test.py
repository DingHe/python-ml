#coding=utf-8
'''
Created on 2016年9月27日

@author: Administrator
'''
from __future__ import division
import nltk,re,pprint

from urllib import urlopen
url="http://www.gutenberg.org/files/2554/2554.txt"
raw=urlopen(url).read()
type(raw)

tokens=nltk.word_tokenize(raw)


url = "http://news.bbc.co.uk/2/hi/health/2284783.stm"
html=urlopen(url).read()
html[:60]

raw=nltk.clean_html(html)
tokens=nltk.word_tokenize(raw)
tokens

def stem(word):
    for suffix in ['ing','ly','ed','ious','ies','ive','es','s','ment']:
        if word.endswith(suffix):
            return word[:-len(suffix)]
    return word


porter=nltk.PorterStemmer()
lancaster=nltk.LancasterStemmer()
[porter.stem(t) for t in tokens]
[lancaster.stem(t) for t in tokens]










