import sys

sys.stdin = open('input.txt', 'r')


def arithmetic(x, y):
    return x + y, x - y, x * y


if __name__ == '__main__':
    a = int(input().strip())
    b = int(input().strip())
    a1, b1, c1 = arithmetic(a, b)
    print(a1)
    print(b1)
    print(c1)
