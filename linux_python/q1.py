import subprocess
aa=subprocess.run(" ls ~",shell=True,capture_output=True,text=True)
for i in aa.stdout.splitlines():
    print(i)