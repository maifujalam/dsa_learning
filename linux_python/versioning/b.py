import subprocess
import yaml

std_out=subprocess.run("ls *.yaml ",shell=True,capture_output=True)
my_file=std_out.stdout.decode().strip()

with open(my_file,"r") as f:
    data=yaml.safe_load(f)
print(data["version"])
a,b,c=map(int,data["version"].split("."))
print(a,b,c)
