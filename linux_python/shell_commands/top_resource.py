import subprocess
aa=subprocess.run("ps -eo user,uid,%cpu,%mem",shell=True,capture_output=True)
print(aa.stdout.decode())
