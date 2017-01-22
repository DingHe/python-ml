#!/usr/bin/python
import gzip
import os
import sys
def in2out(fin,fout):
    Bufsize=1024*8
    while True:
        buf=fin.read(Bufsize)
        if len(buf) < 1:
            break
        fout.write(buf)
    fin.close()
    fout.close()
        
def gunzip(filename):
    fin=gzip.open(filename,'rb')
    fout=open(filename[0:-3],'wb')
    in2out(fin, fout)
    os.remove(filename)
    
def mvfile(srcfile,dsctdir):
    basefilename=os.path.basename(srcfile)
    os.rename(srcfile, dsctdir+"/"+basefilename)
    
    
if __name__ == '__main__':
    if len(sys.argv) < 3:
        print 'use %s srcfile  distdir' % sys.argv[0]
    gunzip(sys.argv[1])
    mvfile(sys.argv[1][0:-3],sys.argv[2])