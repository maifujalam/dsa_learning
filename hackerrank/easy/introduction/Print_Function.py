import sys

sys.stdin = open('input.txt', 'r')


def printfunction(x):
    y = ''
    for i in range(1, x + 1):
        y += str(i)
    return y


if __name__ == '__main__':
    a = int(input().strip())
    a1 = printfunction(a)
    print(a1)
