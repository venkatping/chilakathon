#!/usr/local/bin/python3
a=eval(input("Enter the first number: "))
b=eval(input("Enter the second number: "))
if a > b:
	print(f"{a} is greater than {b}")
elif a < b:
	print(f"{b} is greater than {a}")
elif a == b:
	print(f"{a} is equal to {b}")
else:
	print("give only numbers")

