import re

MYINPUT = "a"

pattern = re.compile(r'^[a-z]$')

print(pattern.match(MYINPUT))



if __name__ == '__main__':
    print("")