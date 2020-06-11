#!/usr/local/bin/python3
'''num=eval(input("Enter your number: "))
if num==1:
	print("one")
elif num==2:
	print("two")
elif num==3:
	print("three")
elif num not in [1,2,3]:
	print("your number is not there in list")
'''
'''num=eval(input("Enter your number: "))

if num==1:
       print("one")
elif num==2:
       print("two")
elif num==3:
       print("three")
else:
       print("your number is not there in list")
'''
'''
num=eval(input("Enter any number between 1 to 10: "))
if num in [1,2,3,4]:
	if num==1:
		print('one')
	elif num==2:
		print('two')
	elif num==3:
		print('three')
	elif num==4:
		print('four')
else:
       print("your number is not there in the list")
'''
num=eval(input("Enter any number between 1 to 10: "))
num_word={1:'one',2:'two',3:'three',4:'four'}
if num in [1,2,3,4]:
	print(num_word.get(num))	
else:
	print("your number is not there in the list")






