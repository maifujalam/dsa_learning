import re
import subprocess
import yaml

try:
    std_out=subprocess.run("ls -a *.yaml | grep -i chart",shell=True,capture_output=True)
    a1=std_out.stdout.decode().strip()

    data=None
    with open(a1) as f:
        data=yaml.safe_load(f)
    print(data)
    print(data["version"])
    a,b,c=map(int,data["version"].split("."))
    print(a,b,c)
    if c<100:
        c+=1
    else:
        c=0
        b+=1
    if b>=100:
        b=0
        a+=1
    print(a,b,c)
except e:
    print(e)