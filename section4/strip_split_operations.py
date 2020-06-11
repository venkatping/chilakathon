#!/usr/local/bin/python3
x="   python "
#it will remove the spaces right and left side of the word
print(x.strip())
y="python"
print(y.strip('p'))
print(y.strip('n'))
print(y.strip('t'))
a="python scripting is easy"
print(a.strip('easy'))
a="python scripting is easy"
print(a.strip('python'))
b="python scripting is python"
print(b.lstrip('python'))
b="python scripting is python"
print(b.rstrip('python'))
b="python scripting is python"
print(b.strip('python'))
x="python./i"
print(x.strip('./i'))
x="pythonyy"
print(x.strip('p').strip('y'))
x="pythonyy"
print(x.strip('p').lstrip('y').rstrip('y'))
x="python is easy"
print(x.split())
x="python is easy"
print(x.split('is'))
x="python is easy and it is scripting"
print(x.split('is'))
x="python is easy and it is scripting"
print(x.find('p',1))
print(x.find('p',30))
java_version="Error when finding"
print(java_version.find('java'))
