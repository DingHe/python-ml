#!/usr/bin/env python
# -*- coding: utf-8 -*-
#左下 108.524636,18.022228
#右上 111.252035,20.108245
#对于两个点，在纬度相等的情况下：
#经度每隔0.00001度，距离相差约1米；每隔0.0001度，距离相差约10米；每隔0.001度，距离相差约100米；每隔0.01度，距离相差约1000米；每隔0.1度，距离相差约10000米。
#对于两个点，在经度相等的情况下：
#纬度每隔0.00001度，距离相差约1.1米；每隔0.0001度，距离相差约11米；每隔0.001度，距离相差约111米；每隔0.01度，距离相差约1113米；每隔0.1度，距离相差约11132米。
import uuid
DISTINCE=0.02
leftdownlng=108.524636
leftdownlat=18.022228
righttoplng=111.252035
righttoplat=20.108245
class Poin(object):
    def __init__(self,lng,lat):
        self.lng=lng 
        self.lat=lat 
    def toString(self):
        return str(self.lng)+','+str(self.lat)
    
class Region(object):
    def __init__(self,leftdown,righttop):
        self.leftdown=leftdown
        self.righttop=righttop
    def ciIsIn(self,ciLng,ciLat):
        if self.leftdown.lng < ciLng and self.righttop.lng >= ciLng and self.leftdown.lat < ciLat and self.righttop.lat >= ciLat:
            return True
        else:
            return False

    
region_file_object=open('./region_ci2.txt','wb')
for i in range(1,int((righttoplng-leftdownlng)/DISTINCE)+2):   #range的范围是左闭右开
    for j in range(1,int((righttoplat-leftdownlat)/DISTINCE)+2):   #range的范围是左闭右开
        leftdown=Poin(leftdownlng+(i-1)*DISTINCE,leftdownlat+(j-1)*DISTINCE)
        righttop=Poin(leftdownlng+i*DISTINCE,leftdownlat+j*DISTINCE)
        region=Region(leftdown,righttop)
        regionuuid=uuid.uuid1()
        file_object = open('./ci_info.txt') 
        while True:
            line=file_object.readline()
            if not line:
                file_object.close()
                break
            field_data=line.split(',')
            #print field_data[0],',',field_data[2],',',field_data[3]
            cilng=float(field_data[2])
            cilat=float(field_data[3])
            if region.ciIsIn(cilng, cilat):
                result=str(regionuuid)+','+line.replace('\n','')+','+region.leftdown.toString()+','+region.righttop.toString()+'\n'
                region_file_object.writelines(result)
                print result
            else:
                #print cilng,',',cilat,'not in region:',region.leftdown.toString(),region.righttop.toString()
                pass
            
    
    
    