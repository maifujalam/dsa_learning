import re

def validate(txt):
    pattern=re.compile(r"\+(\d){2,4}(\d){10,12}")
    return pattern.match(txt)

if __name__ == '__main__':
    print(validate("+911234567890"))
    print(validate("+961234556890"))
    print(validate("+1234567890"))
    print(validate("+1234567890rr"))
    print(validate("+1234567890"))
    print(validate("+1234567890"))
    print(validate("+1234567890"))
    print(validate("+1234567890"))