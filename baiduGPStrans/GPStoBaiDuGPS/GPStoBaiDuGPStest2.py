#coding=utf-8
'''
Created on 2017年2月3日

@author: zzx
'''
import urllib2
import json
import base64
URL="http://api.map.baidu.com/ag/coord/convert?from=0&to=4"
def parseBaiDuGPS(result):
    data=json.loads(result)
    x=base64.b64decode(data["x"])
    y=base64.b64decode(data["y"])
    return x+','+y
    
file_object = open('./澄迈网格排名')
result_file_object=open('./澄迈网格排名baidu','wb')
while True:
    line=file_object.readline()
    if not line:
        break
    field_data=line.split()
    leftdownlng=field_data[2]
    leftdownlat=field_data[3]
    righttoplng=field_data[4]
    righttoplat=field_data[5]
    para1="&x="+leftdownlng+"&y="+leftdownlat
    para2="&x="+righttoplng+"&y="+righttoplat
    full_URL1=URL+para1
    full_URL2=URL+para2
    req1=urllib2.Request(full_URL1)
    res_data1=urllib2.urlopen(req1)
    baiduGPS1=parseBaiDuGPS(res_data1.read())
    
    req2=urllib2.Request(full_URL2)
    res_data2=urllib2.urlopen(req2)
    baiduGPS2=parseBaiDuGPS(res_data2.read())
    result=line.replace('\n','') +'   '+baiduGPS1+ '   '+baiduGPS2+'\n'
    result_file_object.writelines(result)
    print result
result_file_object.close()    
    
    
    
    