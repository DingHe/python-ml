#!/usr/bin/python
import socket
import ftplib
from ftplib import FTP
import subprocess
from time import sleep
import os
from unzipandmv import gunzip
from unzipandmv import mvfile

timeout=30
HOST="135.112.74.239"
PORT=21
USER=''
PASSWD=''
DISTPATH=""   #flume spooling directory
SUBPROC="/usr1/xdr/unzipandmv.py"
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
            print 'filename=%s' % f
            localfile=localpath+'/'+f
            ftp.retrbinary('RETR ' + f,open(localfile,'wb').write)
            subprocess.Popen([SUBPROC,localfile,DISTPATH])
            #ftp.delete(f)

def unzipAndMoveLocalfile(localpath,distdir):
    localfiles=os.listdir(localpath)
    for f in localfiles:
        localfile=localpath+'/'+f
        print "localfilename=%s" % localfile
        if os.path.isdir(localfile):
            pass
        elif f[-4:] == '.txt':
            mvfile(localfile,"/usr1/data4g")
        elif f[-3:] == '.gz':
            try:
                gunzip(localfile)
            except Exception:
                print 'gunzip failed,deleted'
                os.remove(localfile)

if __name__ == '__main__':
    remotepath='/data/xdr/hnbak'
    localpath='/usr1/xdr'
    unzipAndMoveLocalfile(localpath,DISTPATH)      
    while True:
        ftpget(remotepath, localpath)

