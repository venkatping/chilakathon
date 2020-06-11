#!/usr/local/bin/python3
usr_str=input("Enter your string: ")
#print(usr_str.title())
usr_conf=input("Do you want to convert the string into title format say yes or no: ")
if usr_conf=="yes":
	print(usr_str.title())
else:
	print(usr_str)
