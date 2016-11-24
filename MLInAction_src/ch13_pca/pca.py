#coding:utf-8
from numpy import *
import matplotlib 
import matplotlib.pyplot as plt

#第一行表示编码方式，可以允许中文注释，出自https://www.python.org/dev/peps/pep-0263/


def loadDataSet(fileName,delim='\t'):
    fr=open(fileName)
    stringArr=[line.strip().split(delim) for line in fr.readlines()]
    datArr=[map(float,line) for line in stringArr]
    return mat(datArr)

def pca(dataMat, topNfeat=9999999):
    meanVals = mean(dataMat, axis=0)
    meanRemoved = dataMat - meanVals #remove mean
    covMat = cov(meanRemoved, rowvar=0)
    eigVals,eigVects = linalg.eig(mat(covMat))
    eigValInd = argsort(eigVals)            #sort, sort goes smallest to largest
    eigValInd = eigValInd[:-(topNfeat+1):-1]  #cut off unwanted dimensions
    redEigVects = eigVects[:,eigValInd]       #reorganize eig vects largest to smallest
    lowDDataMat = meanRemoved * redEigVects#transform data into new dimensions
    reconMat = (lowDDataMat * redEigVects.T) + meanVals
    return lowDDataMat, reconMat


def replaceNanWithMean():
    dataMat=loadDataSet('secom.data', ' ')
    numFeat=shape(dataMat)[1]
    for i in range(numFeat):
        meanVal=mean(dataMat[nonzero(~isnan(dataMat[:,i].A))[0],i])
        dataMat[nonzero(isnan(dataMat[:,i].A))[0],i] =meanVal
    return dataMat

#example one
'''if __name__ == '__main__':
    dataMat=loadDataSet('testSet.txt', '\t')
    lowDMat,reconMat=pca(dataMat, 1)
    fig=plt.figure()
    ax=fig.add_subplot(111)
    ax.scatter(dataMat[:,0].flatten().A[0],dataMat[:,1].flatten().A[0],marker='^',s=90)
    ax.scatter(reconMat[:,0].flatten().A[0],reconMat[:,1].flatten().A[0],marker='o',s=50,c='red')'''
    
if __name__ == '__main__':
    dataMat=replaceNanWithMean()
    meanVals=mean(dataMat,axis=0)
    #print meanVals
    meanRemoved=dataMat - meanVals
    #print meanRemoved
    covMat=cov(meanRemoved,rowvar=0)
    eigVals,eigVects=linalg.eig(mat(covMat))
    print eigVals
    #print eigVects
    lowDMat,reconMat=pca(dataMat,20)
    print dataMat.shape
    print shape(lowDMat)
    




