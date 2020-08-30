#!/usr/local/bin/python3
import os
cmd="date"
#print(os.system("date"))
rt=os.system(cmd)
if rt==0:
	print("command succesfully executed")
else:
	print("command not successful")

