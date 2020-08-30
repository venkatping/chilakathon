#!/usr/local/bin/python3
x="python"
y="-".join(x)
z="scripting"
print(x)
print(y)
print("_".join(x))
print("\n".join(x))
print("\t".join(x))
print(x.center(20))
print(z.center(20))
print(f"{x.center(20)}\n{z.center(20)}")
#assigning 0s on the left is something like padding we are using zfill
print(x.zfill(10))
