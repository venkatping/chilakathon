#!/usr/local/bin/python3
import os
import sys
import datetime
path=input("Enter the path: ")
age=eval(input("Enter the required age: "))
if not os.path.exists(path):
  print("Please provide valid path")
  sys.exit()
if os.path.isfile(path):
  print("Please provide directory path")
  sys.exit()
today=datetime.datetime.now()
for each_file in os.listdir(path):
  each_file_path=os.path.join(path,each_file)
  if os.path.isfile(each_file_path):
    file_creation_date=datetime.datetime.fromtimestamp(os.path.getctime(each_file_path))
    #print(dir(today-file_creation_date))
    difference_in_days=(today-file_creation_date).days
    if difference_in_days > age:
      print(each_file_path,difference_in_days)
