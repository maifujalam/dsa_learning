import re

def validate(txt):
    pattern=re.compile(r"^\w+@\w+\.([a-zA-Z]){2,}$")
    return pattern.match(txt)

if __name__ == '__main__':
    print(validate("sss@gmail.com"))
    print(validate("fff@example.in"))
    print(validate("invalid-email@.c"))
    print(validate("invalid-email@com"))
    print(validate("validemail@gma.co"))
    print(validate("validemail@gma.c_"))