#!/usr/local/bin/python3
import subprocess
cmd=["bash","--version"]
sp=subprocess.Popen(cmd,shell=False,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
rc=sp.wait()
out,err=sp.communicate()
if rc==0:
  for each in out.splitlines():
    if "version" in each and "release" in each:
      print(each.split()[3].split('(')[0])
else:
  print(f"error is: {err}")
