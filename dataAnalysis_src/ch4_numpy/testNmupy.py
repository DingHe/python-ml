#coding=utf-8
import numpy as np
data1=[6,7.5,8,0,1]
arr1=np.array(data1)
print(arr1)
print(arr1.shape)
print(arr1.dtype)
print(arr1.ndim)

print("===test arr2====")
data2=[[1,2,3,4],[5,6,7,8]]
arr2=np.array(data2)
print(arr2)
print(arr2.shape)
print(arr2.dtype)
print(arr2.ndim)       #ndim表示数组的维度

a=np.arange(15)
print(a)

#数组和标量之间的运算
arr=np.array([[1,2,3],[4,5,6]])
print arr
print arr * arr
print arr-arr
print 1 / arr.astype(np.float32)
print arr ** 0.5




#数组转置和轴对换
print("=======数组转置和轴对换=========")
arr=np.arange(15).reshape((3,5))
#print arr
#print arr.T

arr=np.arange(16).reshape((2,2,4))
print arr
print arr.shape
b=arr.transpose((1,0,2))
print b 
print b.shape





