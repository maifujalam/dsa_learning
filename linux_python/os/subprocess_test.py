import subprocess
try:
    ans = subprocess.check_output(["python", "--version"], text=True)
    print(ans)
    a1=subprocess.run("ps aux | head -n 3", shell=True, capture_output=True, text=True)
    for i in a1.stdout.splitlines():
        print(i)

except subprocess.CalledProcessError as e:
    print(f"Command failed with return code {e.returncode}")


import subprocess
aa=subprocess.run(" ls ~",shell=True,capture_output=True,text=True)
for i in aa.stdout.splitlines():
    print(i)