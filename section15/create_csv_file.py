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
"""
import csv
req_file="/python/section15/file1.csv"
#fo=open(req_file,'wb') #python2
fo=open(req_file,'w',newline="")
csv_writer=csv.writer(fo,delimiter=",")
csv_writer.writerow(['S.No','Name','age','skill'])
csv_writer.writerow(['1','jhon','28','python'])
fo.close()
"""
import csv
req_file="/python/section15/file2.csv"
fo=open(req_file,'w',newline="")
csv_writer=csv.writer(fo,delimiter=",")
my_data=[['S.No',"Name",'age',"skill"],['1','jhon','32','python'],['2','charles','37','bash']]
csv_writer.writerows(my_data)
fo.close()
