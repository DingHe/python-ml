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
    
file_object = open('./chengmai')
while True:
    line=file_object.readline()
    if not line:
        break
    field_data=line.split()
    logAndlat=field_data[2].split(',')
    log=logAndlat[0]
    lat=logAndlat[1]
    para="&x="+log+"&y="+lat
    full_URL=URL+para
    req=urllib2.Request(full_URL)
    res_data=urllib2.urlopen(req)
    baiduGPS=parseBaiDuGPS(res_data.read())
    result=field_data[0]+'|'+field_data[1]+'|'+field_data[2]+'|'+baiduGPS
    print result
    
    
    
    
    