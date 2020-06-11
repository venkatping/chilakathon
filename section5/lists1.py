#!/usr/local/bin/python3
'''
x=4
print(x)
#assigning x value to y
y=x
print(y)
'''
my_list=[2,4,6,8,74,32,92,4,47]
'''
print(my_list)
my_new_list=my_list
print(my_new_list)
'''
'''
my_new_list=my_list.copy()
print(my_new_list)
'''
'''
#id value is deifferent when we use copy
print(id(my_new_list))
my_one_list=my_list
#id value is same when we don't use copy
print(id(my_list),id(my_one_list))
'''
'''
my_values=[4,7,42,32,35,92,94,62]
print(my_values)
my_values.append(56)
print(my_values)
#inserting 47 in index1
my_values.insert(1,47)
print(my_values)
'''
'''
my_list.append(my_values)
print(my_list)
'''
'''
print(dir(my_list))
'''
'''
print(my_list,my_values)
my_list.extend(my_values)
print(my_list)
'''
'''
#remove will remove based on value
my_list.remove(8)
print(my_list)
'''

#pop will remove based on index value
'''
my_list.pop(1)
print(my_list)
'''
'''
print(my_list.pop(2))
print(my_list)
'''
print(my_list)
'''
my_list.reverse()
print(my_list)
'''
'''
#sorting in Ascending order
my_list.sort()
print(my_list)
'''
#sorting in descending order
my_list.sort(reverse=True)
print(my_list)
