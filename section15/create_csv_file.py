#!/usr/local/bin/python3
"""
import csv
req_file="/python/section15/file.csv"
fo=open(req_file,'r')
csv_reader=csv.reader(fo,delimiter=",")
for each_row in csv_reader:
  print(each_row)
fo.close()
"""
import csv
req_file="/python/section15/file1.csv"
fo=open(req_file,'w')
csv_writer=csv.writer(fo,delimiter=",")
csv_writer.writerow(['S.No','Name','age','skill'])

fo.close()
