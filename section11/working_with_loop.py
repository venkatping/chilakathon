#!/usr/local/bin/python3
#All programming languages need a way to execute block of code many times and this is possible with loops
"""
my_list=[3,4,5]
print(my_list[0])
print(my_list[1])
print(my_list[2])
"""
"""
my_list=[2,4,6,7]
for each in my_list:
	print(each)
"""
my_list=[2,3,4,5,6,7]

for each in my_list:
  rem=each%2
  if rem==0:
    print(f"The entered number {each} is even")
  else:
    print(f"The entered number {each} is odd")

