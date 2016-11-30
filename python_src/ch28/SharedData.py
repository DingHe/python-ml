#coding=utf-8
'''
Created on 2016年11月28日

@author: Administrator
'''
class SharedData:
    spam=42

#所有的实例共享spam值    
x=SharedData()
y=SharedData()
print x.spam,y.spam
#通过类修改会影响所有实例
SharedData.spam=99
print x.spam,y.spam,SharedData.spam
#通过实例修改，只影响本实例
x.spam=88
print x.spam,y.spam,SharedData.spam
