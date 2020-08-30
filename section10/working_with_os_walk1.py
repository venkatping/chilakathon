#!/usr/local/bin/python3
import os
req_file=input("Enter your filename to search: ")
for r,d,f in os.walk("/"):
  for each_file in f:
    if each_file==req_file:
      print(os.path.join(r,each_file))
