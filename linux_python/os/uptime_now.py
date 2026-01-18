import subprocess

def get_cpu_uptime():
    try:
        # Get system uptime
        uptime_info = subprocess.run("uptime", capture_output=True,text=True)
        print("System Uptime:")

        for i in uptime_info.stdout.splitlines():
            print(i)

    except subprocess.CalledProcessError as e:
        print(f"Command failed with return code {e.returncode}")

if __name__ == "__main__":
    get_cpu_uptime()
