#coding=utf-8
'''
Created on 2016年11月29日

@author: Administrator
'''
class Number:
    def __init__(self,start):
        self.data=start
    def __sub__(self,other):
        return Number(self.data-other)
    
X=Number(5)
Y=X-2
print Y.data



class Indexer:
    def __getitem__(self,index):
        return index**2
    
X=Indexer()
print(X[2])
        
        
        
        
        
        
        
        
        
        
        