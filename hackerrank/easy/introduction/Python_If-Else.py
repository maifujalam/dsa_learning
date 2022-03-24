import sys
import unittest

sys.stdin = open('input.txt', 'r')


def weird(x):
    flag = False
    if x % 2 != 0:
        flag = True
    else:
        if 2 <= x <= 5:
            flag = False
        if 6 <= x <= 20:
            flag = True
        if x >= 20:
            flag = False
    print("Weird") if flag else print("Not Weird")


if __name__ == '__main__':
    n = int(input().strip())
    weird(n)
