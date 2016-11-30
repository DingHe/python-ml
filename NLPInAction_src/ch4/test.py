#coding=utf-8
'''
Created on 2016年10月8日

@author: Administrator
'''
import nltk
text=nltk.word_tokenize("And now for something completely different")
nltk.pos_tag(text)
nltk.help.upenn_tagset('RB')