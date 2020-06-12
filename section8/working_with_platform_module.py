#!/usr/local/bin/python3
'''
import platform
print(dir(platform))
print(help(platform))
'''
import platform
print(platform.system())
print(f"This is {platform.system()}")
print(f"python version is: {platform.python_version()}")
print(platform.python_version_tuple())
