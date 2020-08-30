#!/usr/local/bin/python3
import subprocess
cmd=["java","-version"]
sp=subprocess.Popen(cmd,shell=False,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
rc=sp.wait()
out,err=sp.communicate()
#print(f"output is: {out}")
#print(f"error is: {err}")
if rc==0:
  #print(f"error is: {err}")
  print(err.splitlines()[0].split()[2].strip("\""))
else:
  print(f"output is: {out}")

"""
if rc==0:
  if bool(out)==False and bool(err)==True:
    print(f"error is: {err}")
  else:
    print(f"output is: {out}")
"""

