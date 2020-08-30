#!/usr/local/bin/python3
import os
req_path=input("Enter the path: ")
#req_ext=input("Enter the extension: ")
if os.path.isfile(req_path):
  print(f"The Entered path {req_path} is a file")
else:
  list_of_files_in_dirs=os.listdir(req_path)
  #print(list_of_files_in_dirs)
  if len(list_of_files_in_dirs)==0:
    print(f"There are no files in Entered directory path: {req_path}")
  else:
    req_ext=input("Enter the extension: ")
    req_files=[]
    for each in list_of_files_in_dirs:
      if each.endswith(req_ext):
        req_files.append(each)
    if len(req_files)==0:
      print(f"There are no files with given extension: {req_ext}")
    else:
      print(f"These are the files in given path with given extension: {req_files}")
