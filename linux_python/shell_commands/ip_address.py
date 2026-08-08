import subprocess

txt=subprocess.run("ifconfig | grep -i 192.168",shell=True,capture_output=True)
print(txt.stdout.decode().split())