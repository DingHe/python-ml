#coding=utf-8
'''
Created on 2016年9月26日

@author: Administrator
'''
#文本语料库是一大段文本
import nltk
nltk.corpus.gutenberg.fileids()
emma=nltk.corpus.gutenberg.words('austen-emma.txt')
emma=nltk.Text(nltk.corpus.gutenberg.words('austen-emma.txt'))
emma.concordance("surprize")

from nltk.corpus import gutenberg
for fileid in gutenberg.fileids():
    num_chars=len(gutenberg.raw(fileid))
    num_words=len(gutenberg.words(fileid))
    num_sents=len(gutenberg.sents(fileid))
    num_vocab=len(set([w.lower() for w in gutenberg.words(fileid)]))
    print int(num_chars/num_words),int(num_words/num_sents),int(num_words/num_vocab),fileid
    
print gutenberg.raw('austen-emma.txt')
print gutenberg.sents('austen-emma.txt')


from nltk.corpus import webtext
for fileid in webtext.fileids():
    print fileid,webtext.raw(fileid)[:65],'...'


from nltk.corpus import nps_chat
chatroom=nps_chat.posts('10-19-20s_706posts.xml')

from nltk.corpus import brown
brown.categories()
brown.words(categories='news')

news_text=brown.words(categories='news')
fdist=nltk.FreqDist([w.lower() for w in news_text])
modals=['can','could','may','might','must','will']
for m in modals:
    print m + ':',fdist[m],


from nltk.corpus import reuters
reuters.fileids()
reuters.categories()


from nltk.corpus import inaugural
inaugural.fileids()

from nltk.corpus import PlaintextCorpusReader
corpus_root='/usr/share/dict'
wordlists=PlaintextCorpusReader(corpus_root,'.*')
wordlists.fileids()



from nltk.corpus import brown
cfd=nltk.ConditionalFreqDist(
    (genre,word)
    for genre in brown.categories()
    for word in brown.words(categories=genre))


from nltk.corpus import inaugural
cfd=nltk.ConditionalFreqDist(
    (target,fileid[:4])
    for fileid in inaugural.fileids()
    for w in inaugural.words(fileid)
    for target in ['america','citizen']
    if w.lower().startswith(target))


def unusual_words(text):
    text_vocab=set(w.lower() for w in text if w.isalpha())
    english_vocab=set(w.lower() for w in nltk.corpus.words.words())
    unusal=text_vocab.difference(english_vocab)
    return sorted(unusal)

from nltk.corpus import stopwords
stopwords.words('english')



entries=nltk.corpus.cmudict.entries()
from nltk.corpus import toolbox
toolbox.entries('rotokas.dic')

from nltk.corpus import wordnet as wn
wn.synsets('motorcar')


