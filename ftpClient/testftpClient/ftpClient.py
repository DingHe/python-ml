#!/usr/bin/python
import socket
import ftplib
from ftplib import FTP
import subprocess
from time import sleep

timeout=30
HOST="127.0.0.1"
PORT=21
USER=''
PASSWD=''
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
    try:
        ftp.cmd_CD(remotepath)
        ftp.cmd_LCD(localpath)
        files=ftp.nlst()
        if len(files) < 1:
            sleep(5)
        else:
            for f in files:
                print 'filename=%s' % f
                localfile=localpath+'/'+f
                ftp.retrbinary('RETR %S' % f,open(localfile,'wb').write)
                subprocess.call(["unzipandmv.py",localfile,"/usr1/data4g"])
                #ftp.delete(f)
    except Exception:
        return
        
if __name__ == '__main__':
    while True:
        remotepath=''
        localpath=''
        ftpget(remotepath, localpath)
    
        


