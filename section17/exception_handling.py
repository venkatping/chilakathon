#!/usr/local/bin/python3
"""
print("welcome to exceptions handling")
try:
    print(4/0)
except:
    print("zero division errors")
"""
"""
#with this script we will get an error
fo=open("demo.txt")
print(fo.read())
fo.close()
"""
"""
#This script is the solution for above script
try:
  fo=open("demo.txt")
  print(fo.read())
  fo.close()
except:
  print("There is no such file")
"""
"""
#This script we will get an error
my_list=[3,4,5]
print(my_list[4])
"""
"""
#This script is a solution for above script
try:
  print(my_list[4])
except Exception as err:
  print(err)
print("Script will not terminate and exceuted this print statement")
"""
#There is no such fabric module and we are handling with exceptions
try:
  import fabric
except Exception as err:
  print(err)
