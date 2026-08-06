import re

print("Validating dob: dd/mm/yyyy")
def validate(txt):
    isValid=False
    pattern=re.compile(r"(\d){2}/(\d){2}/(\d){4}")
    if pattern.match(txt):
        dd,mm,yyyy=map(int,txt.split("/"))
        if dd <31 and dd>0:
            isValid=True
        if mm<=12 and mm>0:
            isValid=True
        if yyyy<=2026 and yyyy>1900:
            isValid=True
    if isValid:
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    validate("12/12/2020")
    validate("31/01/1999")
    validate("00/00/0000")
    validate("29/02/2020")  # Leap year
    validate("29/02/2019")  # Not a leap year
    validate("31/04/2021")  # Invalid date
    validate("15-08-1947")  # Invalid format
