#!/usr/local/bin/python3
import os
req_path=input("Enter your directory path: ")
req_ext=input("Enter the required extension: ")
if os.path.isfile(req_path):
    print(f"The Given path: {path} is a file")
else:
    all_files_dirs=os.listdir(req_path)
    if len(all_files_dirs)==0:
        print(f"The Given path is empty")
