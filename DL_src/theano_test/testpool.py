#coding=utf-8
'''
Created on 2016年11月30日

@author: Administrator
'''
import numpy
import theano.tensor as T
import theano
from theano.tensor.signal import pool
input=T.dtensor4('input')
maxpool_shape=(2,2)
#pool_out=pool.pool_2d(input=input, ds=maxpool_shape, ignore_border=True)
pool_out=pool.pool_2d(input=input, ds=maxpool_shape, ignore_border=False)
f=theano.function([input],pool_out)

invals=numpy.random.RandomState(1).rand(3,2,5,5)
print 'With ignore_border set to True:'
print 'invals[0, 0, :, :] =\n', invals[0, 0, :, :]
print 'output[0, 0, :, :] =\n', f(invals)[0, 0, :, :]




