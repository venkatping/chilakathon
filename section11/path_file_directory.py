#!/usr/local/bin/python3
"""
import os
path=input("Enter your path: ")
if os.path.isfile(path):
	print(f"The given path is: {path} is a file")
else:
	print(f"The given path is: {path} is a directory")
"""

import os
path=input("Enter your path: ")
if os.path.exists(path):
  print(f"Given path: {path} is valid")
  if os.path.isfile(path):
     print(f"The Givn path {path} is a file")
  else:
     print(f"The Given path {path} is a directory")
else:
  print(f"Given path: {path} is not existing in host")

