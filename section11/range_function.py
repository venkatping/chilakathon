#!/usr/local/bin/python3
print(range(5))
print(range(3))
print(list(range(5)))
print(list(range(4)))
#here start is 0 and stop is 5
print(list(range(0,5)))
#Here start is 0 and stop is 20 and step is 2
print(list(range(0,20,2)))
#print from right to left
print(list(range(10,2,-1)))
for each in range(4):
    print(each)
for each in range(0,4,2):
    print(each)

my_list=[2,4,6,"hi","python"]
print(list(range(len(my_list))))
print(my_list[0])
for each in range(len(my_list)):
    print(f"{each}---->{my_list[each]}")

