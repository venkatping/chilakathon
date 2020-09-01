#!/usr/local/bin/python3
"""
#NameError
print(a)
"""
"""
#TypeError
print(4+"some string")
"""
"""
#FileNotFoundError
open("demo.txt")
"""
"""
#ZeroDivisionError
print(4/0)
"""
try:
  print("This is try block")
  #print(a)
  #print(4+"hi")
  #open('demo.txt')
  #print(4/0)
  import fabric
except FileNotFoundError:
  print("File is not present to open it")
except NameError:
  print("Variable a is not defined")
except TypeError:
  print("Adding number and string is not possible")
except ZeroDivisionError:
  print("Division with zero is not possible")
except Exception as err:
  print(err)
finally:
  print("This will execute at last")
