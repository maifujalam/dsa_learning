import re

def validate(txt):
    pattern=re.compile(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")
    isValid=False
    if pattern.match(txt):
        isValid=True
        a=[ i for i in txt.strip().split(".")]
        for i in a:
            if int(i)>255:
                isValid=False
        print(a)
    else:
        isValid=False
    return isValid

if __name__ == '__main__':
    print(validate("1.1.1.1"))
    print(validate("123.123.123.123"))
    print(validate("dds.dsd.dsd"))
    print(validate("333.123.123.123"))