#!/usr/local/bin/python3
"""
try:
  a=10
  print(a)
except NameError:
  print("Variable a is no defind")
except Exception as err:
  print(f"Exception occured: {err}")
else:
  print("This will execute if there is no exceptions in try block")
"""
#if try block has exceptions then else won't print
try:
  print(a)
except NameError:
  print("Variable a is not defind")
except Exception as err:
  print(f"Exception occured: {err}")
else:
  print("This will execute if there is no exceptions in try block")
finally:
  print("This will execute always")

