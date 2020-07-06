#!/usr/local/bin/python3
import os
req_path=input("Enter your directory path: ")
#req_ext=input("Enter the required extension: ")
if os.path.isfile(req_path):
    print(f"The Given path: {path} is a file")
else:
    all_files_dirs=os.listdir(req_path)
    if len(all_files_dirs)==0:
        print(f"The required path is empty")
    else:
        req_ext=input("Enter the required files extension: ")
        req_files=[]
        for each in all_files_dirs:
            if each.endswith(req_ext):
                req_files.append(each)
        if len(req_files)==0:
            print(f"Ther is no files with required extension {req_ext}")
        else:
            print(f"The required files are {req_files}")
