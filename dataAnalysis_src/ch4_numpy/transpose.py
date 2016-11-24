'''
Created on 2016829

@author: Administrator
'''

import numpy as np
from ch4_numpy.test import arr
arr=np.arange(15).reshape((3,5))
print arr
print arr.T


arr=np.random.randn(6,3)
print arr
print arr.T
print np.dot(arr.T,arr)
print np.dot(arr,arr.T)

arr=np.arange(16).reshape((2,2,4))
print '======================='
print arr
print arr.transpose((1,0,2))


arr=np.arange(10)
print arr
print np.sqrt(arr)
print np.exp(arr)

x=np.random.randn(8)
y=np.random.randn(8)
print x
print y
print np.maximum(x,y)

points=np.arange(-5,5,0.01)
xs,ys=np.meshgrid(points,points)
print xs,ys

import matplotlib.pyplot as plt
z=np.sqrt(xs ** 2 + ys ** 2)
#plt.imshow(z)
#plt.colorbar()

xarr=np.array([1.1,1.2,1.3,1.4,1.5])
yarr=np.array([2.1,2.2,2.3,2.4,2.5])
cond=np.array([True,False,True,True,False])

result=[(x if c else y) for x,y,c in zip(xarr,yarr,cond)]
print result

result = np.where(cond,xarr,yarr)
print result

arr=np.random.randn(4,4)
print arr
result = np.where(arr > 0,2,-2)
print result


arr=np.random.randn(5,4)
print arr.mean()
print arr.mean(axis=1)
print np.mean(arr)
print arr.sum()
print np.sum(arr)








