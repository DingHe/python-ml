#!/usr/bin/env python
# -*- coding: utf-8 -*-
import paramiko
import re
import subprocess
from time import sleep
HOST=''
PORT=21
USER=''
passwd=''
DISTPATH="/usr1/data4g"   #flume spooling directory
SUBPROC="/usr1/xdr/unzipandmv.py"

def matchfilename(filename):
    return re.match('.*http.*.gz$', filename)

def sftpget(remotedir,localdir):
    transport=paramiko.Transport((HOST,PORT)) 
    transport.connect(username=USER, password=passwd)
    sftp=paramiko.SFTPClient.from_transport(transport)
    print sftp.listdir('/usr1/xdr/data')
    filenames=sftp.listdir(remotedir)
    if len(filenames) < 1:
        sleep(10)
    else:
        for filename in filenames:
            if not matchfilename(filename):
                print filename
            remotefilename=remotedir+'/'+filename
            localfilename=localdir+'/'+filename
            sftp.get(remotefilename,localfilename)
            subprocess.Popen([SUBPROC,localfilename,DISTPATH])
            sftp.remove(remotefilename)
            print remotefilename

if __name__ == '__main__':
    remotedir='/usr1/xdr/data'
    localdir=''
    while True:
        try:
            sftpget(remotedir,localdir)
        except Exception:
            print 'hapen error,get files error'

