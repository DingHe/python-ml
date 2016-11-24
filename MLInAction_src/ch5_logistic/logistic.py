#coding=utf-8

#用一条直线对这些点进行你和（该直线的最佳拟合直线），这个拟合的过程就称作回归）
import numpy as np
import matplotlib.pyplot as plt
import math
from numpy import shape
#x=np.random.randn(100)
x=np.array(range(-20,21))
print x
y=1.0/(1.0 + math.e ** (-x))
print y
fig=plt.figure()
ax=fig.add_subplot(1,1,1)
ax.scatter(x,y)


#==============================
'''fr=open('testSet.txt')
stringArr=[line.strip().split('\t') for line in fr.readlines()]
print stringArr
datArr=[map(float,line) for line in stringArr]
print np.mat(datArr)

fig=plt.figure()
ax=fig.add_subplot(1,1,1)
ax.scatter(np.mat(datArr)[:,0],np.mat(datArr)[:,1])'''


def loadDataSet():
    dataMat = []; labelMat = []
    fr = open('testSet.txt')
    for line in fr.readlines():
        lineArr = line.strip().split()
        dataMat.append([1.0, float(lineArr[0]), float(lineArr[1])])
        labelMat.append(int(lineArr[2]))
    return dataMat,labelMat

def sigmoid(inX):
    return 1.0/(1+np.exp(-inX))

def gradAscent(dataMatIn, classLabels):
    dataMatrix = np.mat(dataMatIn)                #convert to NumPy matrix
    labelMat = np.mat(classLabels).transpose()    #convert to NumPy matrix
    m,n = np.shape(dataMatrix)
    alpha = 0.001
    maxCycles = 50000
    weights = np.ones((n,1))
    for k in range(maxCycles):                    #heavy on matrix operations
        h = sigmoid(dataMatrix*weights)           #matrix mult
        error = (labelMat - h)                    #vector subtraction
        weights = weights + alpha * dataMatrix.transpose()* error  #matrix mult
    return weights

dataMatIn,classLabels = loadDataSet()
print gradAscent(dataMatIn,classLabels)


def plotBestFit(weights):
    import matplotlib.pyplot as plt
    dataMat,labelMat=loadDataSet()
    dataArr = np.array(dataMat)
    n = np.shape(dataArr)[0] 
    xcord1 = []; ycord1 = []
    xcord2 = []; ycord2 = []
    for i in range(n):
        if int(labelMat[i])== 1:
            xcord1.append(dataArr[i,1]); ycord1.append(dataArr[i,2])
        else:
            xcord2.append(dataArr[i,1]); ycord2.append(dataArr[i,2])
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(xcord1, ycord1, s=30, c='red', marker='s')
    ax.scatter(xcord2, ycord2, s=30, c='green')
    x = np.arange(-3.0, 3.0, 0.1)
    print shape(x)
    y = (-weights[0]-weights[1]*x)/weights[2]
    print shape(y.T)
    ax.plot(x, y.T)
    plt.xlabel('X1'); plt.ylabel('X2');
    plt.show()

#验证梯度上升
plotBestFit(gradAscent(dataMatIn,classLabels))




def stocGradAscent0(dataMatrix, classLabels):
    m,n = shape(dataMatrix)
    alpha = 0.01
    weights = np.ones(n)   #initialize to all ones
    for i in range(m):
        h = sigmoid(sum(dataMatrix[i]*weights))
        error = classLabels[i] - h
        weights = weights + alpha * error * dataMatrix[i]
    return weights

#验证随机梯度上升
#plotBestFit(stocGradAscent0(dataMatIn,classLabels))



def stocGradAscent1(dataMatrix, classLabels, numIter=150):
    m,n = shape(dataMatrix)
    weights = np.ones(n)   #initialize to all ones
    for j in range(numIter):
        dataIndex = range(m)
        for i in range(m):
            alpha = 4/(1.0+j+i)+0.0001    #apha decreases with iteration, does not 
            randIndex = int(np.random.uniform(0,len(dataIndex)))#go to 0 because of the constant
            h = sigmoid(sum(dataMatrix[randIndex]*weights))
            error = classLabels[randIndex] - h
            weights = weights + alpha * error * dataMatrix[randIndex]
            del(dataIndex[randIndex])
    return weights
