#!/usr/local/bin/python3
"""
fo=open('newdemo.txt','w')
print(fo.mode)
print(fo.readable())
print(fo.writable())
fo.close()
"""
"""
#if we don't have any file and then we have to open it on write mode
my_content=["This is a data\n""This is a data\n"]
fo=open('newdemo1.txt','w')
#fo.write("This is first line and iam still on training\n")
#print(fo.mode)
fo.writelines(my_content)
fo.close()
"""
"""
my_content=["This is first line","This is second line","This is third line"]
fo=open("with_loop.txt",'a')
for each_line in my_content:
  fo.write(each_line+"\n")
"""
"""
#reading a text file
fo=open("with_loop.txt",'r')
data=fo.read()
print(data)
fo.close()
"""
"""
#reading atext file with line by line
fo=open("with_loop.txt",'r')
print(fo.readline())
fo.close()
"""
"""
#printing the type of data
fo=open("with_loop.txt",'r')
data=fo.read()
fo.close()
print(type(data))
"""
"""
#reading the file in list which the output in a file is print in list
fo=open("with_loop.txt",'r')
data=fo.readlines()
fo.close()
#print(data)

for each in range(3):
  print(data[each])
"""
#reading teh last line in a file
fo=open("with_loop.txt",'r')
data=fo.readlines()
fo.close()
print(data[-1])
