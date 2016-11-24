'''
Created on

@author: Administrator
'''

import numpy as np
arr=np.arange(10)
np.save('some_array', arr)

print np.load('some_array.npy')

np.savez('array_archive.npz',a=arr,b=arr)
arch=np.load('array_archive.npz')

