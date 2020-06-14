#!/usr/local/bin/python3
import os
path="/root/python/section10"
print(os.path.basename(path))
print(os.path.dirname(path))
path1="/home"
path2="redhat"
print(os.path.join(path1,path2))
'''
path2="/root/python/section10"
print(os.path.split(path2))
print(os.path.getsize(path2))
print(os.path.exists(path2))
if os.path.exists(path2):
	print("path exists")
else:
	print("path not exists")
'''
if os.path.isfile(path):
	print("your path is not file")
else:
	print("your path is directory")

