import platform
import socket
import os
print(platform.system())
print(platform.release())
print(platform.version())


print(socket.gethostname())
print(socket.gethostbyname(socket.gethostname()))

import os

# Create a new directory
try:
    os.mkdir("new_directory")
    print("Directory created successfully.")
except OSError as error:
    print(error)

# List contents of the current directory
print("Current directory contents:", os.listdir())

# Execute a shell command
# os.system("ls -l")  # For Unix-like systems
os.system("dir")  # For Windows
