#!/usr/local/bin/python3
"""
import os
import sys
path=input("Enter your directory path: ")
if os.path.exists(path):
 df_l=os.listdir(path)
else:
 print("Please provide valid path")
 sys.exit()
#print(df_l)
p1=os.path.join(path,df_l[0])
p2=os.path.join(path,df_l[1])
p3=os.path.join(path,df_l[2])
if os.path.isfile(p1):
  print(f"p1 is a file")
else:
  print(f"p1 is not a file")
"""

import os
import sys
path=input("Enter your directory path: ")
if os.path.exists(path):
 df_l=os.listdir(path)
else:
 print("Please provide valid path")
 sys.exit()

list_of_files=os.listdir(path)
for each in list_of_files:
  f_d=os.path.join(path,each)
  if os.path.isfile(f_d):
   print(f"The given path: {path} is a file")
  else:
   print(f"The given path: {path} is directory")

