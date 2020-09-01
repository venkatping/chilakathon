#!/usr/local/bin/python3
#raise Exception("This is a exception")
#raise NameError("Variable a is not defined")
"""
age=23
if age>30:
  print("valid age")
else:
  raise ValueError("age is less than 30")
"""
#assert will raise AssertionError if condition is false
#assert 4<3
"""
age=20
try:
  assert age>30
  print("valid age")
except:
  print("Exception occured")
"""
age=20
try:
  assert age>30
  print("valid age")
except AssertionError:
  print("Raised with assert because age is less than 30")
