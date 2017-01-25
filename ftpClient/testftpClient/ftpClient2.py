#!/usr/bin/python
import socket
import ftplib
from ftplib import FTP
import subprocess
from time import sleep
import re

timeout=30
HOST=""
PORT=21
USER=''
PASSWD=''
DISTPATH="/usr1/data4g"   #flume spooling directory
SUBPROC="/usr1/xdr/putdata117.sh"

def matchfilename(filename):
    return re.match('.*http.*.gz$', filename)

def ftpget(remotepath,localpath):
    ftp=FTP()
    try:
        ftp.connect(HOST, PORT, timeout)
    except(socket.error,socket.gaierror):
        print 'ERROR:cannot reach "%s"' % HOST
        return
    try:
        ftp.login(USER, PASSWD)
    except ftplib.error_perm:
        print 'ERROR:cannot login '
        ftp.close()
        return
    
    ftp.cwd(remotepath)
    files=ftp.nlst()
    if len(files) < 1:
        sleep(10)
    else:
        for f in files:
            if not matchfilename(f):
                print 'filename=%s' % f
                continue
            localfile=localpath+'/'+f
            ftp.retrbinary('RETR ' + f,open(localfile,'wb').write)
            subprocess.Popen([SUBPROC,localfile])     
            ftp.delete(f)

if __name__ == '__main__':
    remotepath='/'
    localpath='/usr1/xdr'   
    while True:
        try:
            ftpget(remotepath, localpath)
        except Exception:
            print 'hapen error,get files error'


