#!/usr/local/bin/python3
my_even_no=[0,2,4,6,8,10,12,14,16,18,20,22,24]
usr_choice=eval(input("Enter the number of your choice: "))

if usr_choice in my_even_no:
	print("your number is present in my_even_number_list")
else:
	print("your number is not present in my_even_number_list")
