#!/usr/local/bin/python3
import os
given_string=input("Enter the string: ")
print(given_string)
"""
print(given_string.center(80))
print(given_string.ljust(80))
print(given_string.rjust(80))
"""
terminal=os.get_terminal_size().columns
print(given_string.center(terminal).title())
print(given_string.ljust(terminal).title())
print(given_string.rjust(terminal).title())
