#!/usr/local/bin/python3
"""
num=eval(input("Enter the number: "))
if num==1:
	print("one")
if num==2:
	print("two")
if num==3:
	print("three")
if num==4:
	print("four")
if num not in [1,2,3,4,5,6,7,8,9,10]:
	print(f"your number is not there in 1-10 range: {num}")
"""
"""
num=eval(input("Enter your number: "))
if num in [1,2,3,4]:
    if num==1:
      print("one")
    elif num==2:
      print("two")
    elif num==3:
      print("three")
    elif num==4:
      print("four")
else:
    print("your number is not there in list")
"""
num=eval(input("Enter your number: "))

num_word={1:'one',2:'two',3:'three',4:'four'}

if num in [1,2,3,4]:
	print(num_word.get(num))
else:
	print("enter in 1-4 range:")
