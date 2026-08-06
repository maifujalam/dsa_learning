import re

print("Password Validate.Atlest 8 characters,1 Capital,1 small and 1 special character and a number")

def validate(txt):
    pattern=re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[^a-zA-Z0-9]){8,}")
    if pattern.match(txt):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    validate("Password@123")
    validate("password")
    validate("PASSWORD")
    validate("Pass@1")
    validate("Passw0rd!")
    validate("P@ssw0rd")
    validate("12345678")
    validate("Password123")
    validate("Aa1.")