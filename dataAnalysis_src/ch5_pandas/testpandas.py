#coding=utf-8
'''
Created on 2016年11月29日

@author: Administrator
'''
from pandas import Series,DataFrame
import pandas as pd
obj=Series([4,7,-5,3])
print obj
print obj.values
print obj.index

obj2=Series([4,7,-5,3],index=['a','b','c','d'])
print obj2
print obj2.index

data={'state':['Ohio','Ohio','Ohio','Nevada','Nevada'],
      'year':[2000,2001,2002,2001,2002],
      'pop':[1.5,1.7,3.6,2.4,2.9]}
frame=DataFrame(data)
print frame

print frame['state']
print frame.year
print frame.columns












