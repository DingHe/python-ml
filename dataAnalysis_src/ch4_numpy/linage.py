'''
Created on

@author: Administrator
'''
import numpy as np
x=np.array([[1,2,3],[4,5,6]])
y=np.array([[6,23],[-1,7],[8,9]])
print x
print y
print x.dot(y)

one=np.ones(3)
print one
print x.dot(one.T)

x=np.random.randn(5,5)
print x
mat=x.T.dot(x)
print np.linalg.inv(mat)