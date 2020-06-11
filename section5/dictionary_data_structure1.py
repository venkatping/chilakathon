#!/usr/local/bin/python3
my_dict={'fruit':'apple','animal':'fox',1:'one'}
#print(dir(my_dict))
'''
my_new_dict={'four':'4'}
my_dict.update(my_new_dict)
print(my_dict)
'''
'''
#pop is used to remove based on key and here we are removing four 
my_dict.pop('four')
print(my_dict)
'''
'''
#popitem will remove the keys randomly
print(my_dict)
#my_dict.popitem()
removed_item=my_dict.popitem()
print(removed_item)
print(my_dict)
'''
'''
keys=['a','e','i','o','u']
new_dict=dict.fromkeys(keys)
print(new_dict)
new_dict['a']="First Apple"
#print(new_dict)
new_dict['e']="First Animal"
new_dict['i']="First place"
new_dict['o']="First legend"
new_dict['u']="First Tech"
print(new_dict)
'''
dict={}
dict.setdefault('k',45)
print(dict)
#by using setdefault if key is not there it will create it else if key is there it won't update/create
dict={'fruit':'apple'}
print(dict)
dict.setdefault('fruit','orange')
print(dict)
