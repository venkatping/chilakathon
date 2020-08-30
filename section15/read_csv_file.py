#!/usr/local/bin/python3
"""
import csv
req_file="/python/section15/data.csv"
fo=open(req_file,'r')
content=fo.readlines()
fo.close()
for each in content:
  print(each.strip("\n"))
"""
"""
#by default CSV consider , as seprator
import csv
req_file="/python/section15/data.csv"
fo=open(req_file,'r')
data=csv.reader(fo,delimiter="|")
#print(data)
for each in data:
 print(each)
fo.close()
"""
"""
import csv
req_file="/python/section15/data.csv"
fo=open(req_file,'r')
content=fo.readlines()
fo.close()
for each in content:
  print(each.strip("\n").split(","))
"""
import csv
req_file="/python/section15/data.csv"
fo=open(req_file,'r')
content=csv.reader(fo)
#print(list(content))
#print(f'The header is:\n {list(content)[0]}')
#print("The number of lines apart form header are: ", len(list(content))-1)
header=next(content)
print("The header is: ",header)
print("The number of lines apart from header are: ",len(list(content)))
"""
for each in content:
  print(each)
"""
fo.close()
