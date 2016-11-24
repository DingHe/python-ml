#coding=utf-8
'''
Created on 2016年8月31日

@author: Administrator
'''

from numpy import *
U,Sigma,VT=linalg.svd([[1,1],[7,7]])
print U
print Sigma
print VT


def loadExData():
    return[[0, 0, 0, 2, 2],
           [0, 0, 0, 3, 3],
           [0, 0, 0, 1, 1],
           [1, 1, 1, 0, 0],
           [2, 2, 2, 0, 0],
           [5, 5, 5, 0, 0],
           [1, 1, 1, 0, 0]]
    
    
Data=loadExData()
print shape(Data)
U,Sigma,VT=linalg.svd(Data)
print Sigma

Sig3=mat([[Sigma[0],0,0],[0,Sigma[1],0],[0,0,Sigma[2]]])
print "==============================================="
LowData= U[:,:3]*Sig3*VT[:3,:]
print shape(LowData)



def ecludSim(inA,inB):
    return 1.0/(1.0 + linalg.norm(inA - inB))

def pearsSim(inA,inB):
    if len(inA) < 3:
        return 1.0
    return 0.5 + 0.5 * corrcoef(inA, inB, rowvar=0)[0][1]

def cosSim(inA,inB):
    num=float(inA.T * inB)
    denom=linalg.norm(inA) * linalg.norm(inB)
    return 0.5 + 0.5*(num/denom)



myMat=mat(loadExData())
print ecludSim(myMat[:,0], myMat[:,4])
print ecludSim(myMat[:,0], myMat[:,0])

print cosSim(myMat[:,0], myMat[:,4])
print cosSim(myMat[:,0], myMat[:,0])

print pearsSim(myMat[:,0], myMat[:,4])
print pearsSim(myMat[:,0], myMat[:,0])

'''
dataMat :数据矩阵
user    :用户编号
simMeans:相似度计算方法
item    :物品编号

'''
def standEst(dataMat, user, simMeas, item):
    n = shape(dataMat)[1]
    simTotal = 0.0; ratSimTotal = 0.0
    for j in range(n):
        userRating = dataMat[user,j]
        if userRating == 0: continue
        overLap = nonzero(logical_and(dataMat[:,item].A>0, \
                                      dataMat[:,j].A>0))[0]
        if len(overLap) == 0: similarity = 0
        else: similarity = simMeas(dataMat[overLap,item], \
                                   dataMat[overLap,j])
        print 'the %d and %d similarity is: %f' % (item, j, similarity)
        simTotal += similarity
        ratSimTotal += similarity * userRating
    if simTotal == 0: return 0
    else: return ratSimTotal/simTotal
    
    
    

def recommend(dataMat, user, N=3, simMeas=cosSim, estMethod=standEst):
    unratedItems = nonzero(dataMat[user,:].A==0)[1]#find unrated items 
    if len(unratedItems) == 0: return 'you rated everything'
    itemScores = []
    for item in unratedItems:
        estimatedScore = estMethod(dataMat, user, simMeas, item)
        itemScores.append((item, estimatedScore))
    return sorted(itemScores, key=lambda jj: jj[1], reverse=True)[:N]





def loadExData2():
    return[[0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 5],
           [0, 0, 0, 3, 0, 4, 0, 0, 0, 0, 3],
           [0, 0, 0, 0, 4, 0, 0, 1, 0, 4, 0],
           [3, 3, 4, 0, 0, 0, 0, 2, 2, 0, 0],
           [5, 4, 5, 0, 0, 0, 0, 5, 5, 0, 0],
           [0, 0, 0, 0, 5, 0, 1, 0, 0, 5, 0],
           [4, 3, 4, 0, 0, 0, 0, 5, 5, 0, 1],
           [0, 0, 0, 4, 0, 4, 0, 0, 0, 0, 4],
           [0, 0, 0, 2, 0, 2, 5, 0, 0, 1, 2],
           [0, 0, 0, 0, 5, 0, 0, 0, 0, 4, 0],
           [1, 0, 0, 0, 0, 0, 0, 1, 2, 0, 0]]
    
    
U,Sigma,VT=linalg.svd(mat(loadExData2()))
print Sigma
Sig2=Sigma ** 2
print Sig2
print sum(Sig2)
print sum(Sig2) * 0.9
print sum(Sig2[:2])
print sum(Sig2[:3])


'''
dataMat :数据矩阵
user    :用户编号
simMeans:相似度计算方法
item    :物品编号

'''
def svdEst(dataMat, user, simMeas, item):
    n = shape(dataMat)[1]
    simTotal = 0.0; ratSimTotal = 0.0
    U,Sigma,VT = linalg.svd(dataMat)
    Sig4 = mat(eye(4)*Sigma[:4]) 
    xformedItems = dataMat.T * U[:,:4] * Sig4.I  
    for j in range(n):
        userRating = dataMat[user,j]
        if userRating == 0 or j==item: continue
        similarity = simMeas(xformedItems[item,:].T,\
                             xformedItems[j,:].T)
        print 'the %d and %d similarity is: %f' % (item, j, similarity)
        simTotal += similarity
        ratSimTotal += similarity * userRating
    if simTotal == 0: return 0
    else: return ratSimTotal/simTotal
