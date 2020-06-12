#!/usr/local/bin/python3
#db_pass=input("Enter your password: ")
import getpass
#db_pass=getpass.getpass()
db_pass=getpass.getpass(prompt="Enter your db password: ")
print(f"The entered password is: {db_pass}")

