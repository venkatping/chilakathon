#!/usr/local/bin/python3
import os
cmd="date"
os.system(cmd)
rt=os.system(cmd)
if rt==0:
	print("your command is successfully executed")
else:
	print("your command is not correct")
