#!/usr/local/bin/python3
import os
path="/python/section10/"
for r,d,f in os.walk(path):
  if len(f) != 0:
    print(r)
    for each_file in f:
      print(os.path.join(r,each_file))
