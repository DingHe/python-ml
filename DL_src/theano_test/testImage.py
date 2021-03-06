#coding=utf-8
'''
Created on 2016年11月30日

@author: Administrator
'''
import numpy
import pylab
from PIL import Image 
import theano
from theano import tensor as T
from theano.tensor.nnet import conv2d
rng=numpy.random.RandomState(23455)
#定义输入张量
input=T.tensor4(name='input')
#w_shp=(2,3,9,9)
w_shp=(3,3,9,9)

w_bound=numpy.sqrt(3*9*9)
W=theano.shared(numpy.asarray(rng.uniform(
    low=-1.0/w_bound,
    high=1.0/w_bound,
    size=w_shp),dtype=input.dtype),name='W')

#b_shp=(2,)
b_shp=(3,)
b=theano.shared(numpy.asarray(rng.uniform(low=-.5,
                                          high=.5,
                                          size=b_shp),dtype=input.dtype),name='b')

conv_out=conv2d(input,W)
output=T.nnet.sigmoid(conv_out+b.dimshuffle('x',0,'x','x'))
f=theano.function([input],output)



img=Image.open('3wolfmoon.jpg')
# dimensions are (height, width, channel)
img=numpy.asarray(img, dtype='float64')/256
print img.shape
img_=img.transpose(2,0,1).reshape(1,3,639,516)
filtered_img=f(img_)

pylab.subplot(2,2,1)
pylab.axis('off')
pylab.imshow(img)
pylab.gray();
pylab.subplot(2, 2, 2); pylab.axis('off'); pylab.imshow(filtered_img[0, 0, :, :])
pylab.subplot(2, 2, 3); pylab.axis('off'); pylab.imshow(filtered_img[0, 1, :, :])
pylab.subplot(2, 2, 4); pylab.axis('off'); pylab.imshow(filtered_img[0, 2, :, :])
pylab.show()





