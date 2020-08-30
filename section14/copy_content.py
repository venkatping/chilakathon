#!/usr/local/bin/python3
"""
sfile="/python/section14/newdemo1.txt"
dfile="/python/section14/newdemo2.txt"
sfo=open(sfile,'r')
content=sfo.read()
sfo.close()

dfo=open(dfile,'w')
dfo.write(content)
dfo.close()
"""
sfile=input("Enter the source file: ")
dfile=input("Enter the destination file: ")
sfo=open(sfile,'r')
content=sfo.read()
sfo.close()

dfo=open(dfile,'w')
dfo.write(content)
dfo.close()

