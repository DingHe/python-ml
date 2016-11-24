import numpy as np
from numpy.matlib import randn
from __builtin__ import range
data1=[6,7.5,8,0,1]
arr1=np.array(data1)


data2=[[1,2,3,4],[5,6,7,8]]
arr2=np.array(data2)

print arr2.ndim
print arr2.shape

print np.zeros(10)
print np.zeros((3,6))
print np.empty((2,3,2))
print np.ones((2,2), float)
print np.arange(15)

arr1=np.array([1,2,3],dtype=np.float64)
print arr1.dtype
arr1=np.array([1,2,3],dtype=np.int32)
print arr1.dtype




arr=np.array([1,2,3,4,5])
print arr.dtype
float_arr=arr.astype(np.float64)
print float_arr.dtype


arr=np.array([[1,2,3],[4,5,6]])
print arr
print arr * arr
print 1 / arr.astype(np.float32)
print arr ** 0.5

arr=np.arange(10)
print arr
print arr[5]
print arr[5:8]
arr[5:8] = 12
print arr[5:9]
print arr
arr_slice=arr[5:8]
print arr_slice
arr_slice[1]=12345
print arr_slice
print arr
arr_slice[:] = 64
print arr


arr2d=np.array([[1,2,3],[4,5,6],[7,8,9]])
print arr2d[2]

print arr2d[0][2]
print arr2d[0,2]


arr3d=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print arr3d
print arr3d[0]

old_values=arr3d[0].copy()
arr3d[0]=42
print arr3d

arr3d[0] = old_values
print arr3d

print arr2d
print arr2d[:2]

print arr2d[:2,1:]


names=np.array(['Bob','Joe','Will','Bob','Will','Joe','Joe'])
print names
data=randn(7,4)
print data
print names == 'Bob'
print data[names == 'Bob']

arr=np.empty((8,4))
print arr
for i in range(8):
    arr[i]=i

print arr

print arr[[4,3,0,6]]




