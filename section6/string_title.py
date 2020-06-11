#!/usr/local/bin/python3
import os
terminal_size=os.get_terminal_size().columns
given_string=input("Enter the value of string: ")
print(given_string)
user_conf=input("Do you want to allign text: say yes or no: ")
if user_conf=="yes":
	print(given_string.center(terminal_size).title())
	print(given_string.ljust(terminal_size).title())
	print(given_string.rjust(terminal_size).title())

