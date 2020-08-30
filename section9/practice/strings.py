#!/usr/local/bin/python3
"""
usr_str=input("Enter your string: ")
usr_choice=input("Enter valid action: lower upper title: ")

if usr_choice=="lower":
	print(usr_str.lower())
elif usr_choice=="upper":
	print(usr_str.upper())
elif usr_choice=="title":
	print(usr_str.title())
else:
	print("Entered invalid option: please select valid options: lower upper title: ")
"""
import sys
#print(sys.argv)
if len(sys.argv) != 3:
	print("usage:")
	print(f"{sys.argv[0]} <user string> <lower|upper|title>")
	sys.exit()
usr_str=sys.argv[1]
usr_choice=sys.argv[2]
if usr_choice=="lower":
        print(usr_str.lower())
elif usr_choice=="upper":
        print(usr_str.upper())
elif usr_choice=="title":
        print(usr_str.title())
else:
        print("Entered invalid option: please select valid options: lower upper title: ")
