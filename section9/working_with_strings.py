#!/usr/local/bin/python3
'''
usr_str=input("Enter your string: ")
usr_action=input("Enter your action on your string,valid actions: lower:upper:title: ")
if usr_action=="lower":
	print(usr_str.lower())
elif usr_action=="upper":
	print(usr_str.upper())
elif usr_action=="title":
	print(usr_str.title())
else:
	print("you entered invalid number:please enter lower:upper:title")
'''

#run this script like ./working_with_strings.py "python scripting" title

import sys
#print("The number of command line arguments: ", len(sys.argv))
if len(sys.argv) != 3:
	print("usage:")
	print(f"{sys.argv[0]} <your string> <lower|upper|title>")
	sys.exit()
usr_str=sys.argv[1]
usr_action=sys.argv[2]
if usr_action=="lower":
        print(usr_str.lower())
elif usr_action=="upper":
        print(usr_str.upper())
elif usr_action=="title":
        print(usr_str.title())
else:
	print("you entered invalid number: please enter lower: upper: title: ")



