import re

MYINPUT = "adcvfADD12d"

pattern = re.compile(r'^[a-z]$')

print(pattern.findall(MYINPUT))