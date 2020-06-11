#!/usr/local/bin/python3
my_list=[2,4,6,'python scripting','learning']
print(my_list)
print((my_list)[3])
print((my_list)[4])
#it will print last value
print((my_list)[-1])
#it will print last before value
print((my_list)[-4])
#it will printthe letter number 3 in index3
print((my_list)[3][2])
#it will print all values in my_list
print((my_list)[:])
#it will print all value from index 0
print((my_list)[0:])
#it will print all values from index 1
print((my_list)[1:])
#it will print from index1 to index3
print((my_list)[1:3])
#it will print from index0 to index3
print((my_list)[:3])
#it will change the index0 value to 22
my_list[0]=22
print(my_list)

my_values=[2,4,6,8,22,46,74,4,92]
#it will give the number 22 index value
print(my_values.index(22))
print(my_values.index(4))
print(my_values.index(74))
#it will print the 4 values which are there after index2
print(my_values.index(4,2))
#it will provide how many 4 are there
print(my_values.count(4))
print(my_values.count(74))
#it will clear values in my_values
print(my_values)
my_values.clear()
print(my_values)
