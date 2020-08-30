#!/usr/local/bin/python3
"""
import os
path=input("Enter your path: ")
if os.path.isfile(path):
  print(f"The given path: {path} is a file: ")
else:
   print(f"The given path: {path} is a directory: ")
"""
import os
path=input("Enter your path: ")
if os.path.exists(path):
  print(f"Given path is valid")
  if os.path.isfile(path):
    print(f"Given path is a file")
  else:
    print(f"Given path is a directory")
else:
  print(f"Given path is invalid")
