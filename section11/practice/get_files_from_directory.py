#!/usr/local/bin/python3
import os
import sys
path=input("Enter your directory path: ")
if os.path.exists(path):
  df_l=os.listdir(path)
else:
  print("Please provide valid path: ")
  sys.exit()
"""
p1=os.path.join(path,df_l[0])
p2=os.path.join(path,df_l[1])
#print(os.path.join(path,p1))
if os.path.isfile(p2):
  print("P2 is a file")
else:
  print("P2 is a directory")
"""
list_of_files_dirs=os.listdir(path)
for each_file in list_of_files_dirs:
    f_d_p=os.path.join(path,each_file)
    if os.path.isfile(f_d_p):
      print(f"Given path is: {f_d_p} and it is a file")
    else:
      print(f"Given path is: {f_d_p} and it is a directory")
