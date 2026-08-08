import subprocess

uptime=subprocess.run("uptime",shell=True,capture_output="True")
a=uptime.stdout.decode()
aa=[i for i in a.split()]
print("Uptime",aa[0])
print("Load",aa[-3:])