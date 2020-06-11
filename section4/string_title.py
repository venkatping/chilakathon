#!/usr/local/bin/python3
import os
terminal_size=os.get_terminal_size().columns
given_string=input("Enter the value of string: ")
print(given_string)
print(given_string.center(terminal_size).title())
print(given_string.ljust(terminal_size).title())
print(given_string.rjust(terminal_size).title())
