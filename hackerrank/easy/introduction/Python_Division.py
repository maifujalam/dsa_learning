import sys

sys.stdin = open("input.txt")


def div(a, b):
    print(a // b)
    c = a / b
    print(c)
    print("%f"%c)


if __name__ == "__main__":
    a = int(input().strip())
    b = int(input().strip())
    div(a, b)
