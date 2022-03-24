import sys

sys.stdin = open('input.txt', 'r')


def fun(a):
    for i in range(len(a) - 1):
        for j in range(len(a) - 1 - i):
            if a[j + 1] < a[j]:
                a[j + 1], a[j] = a[j], a[j + 1]
    return a


if __name__ == '__main__':
    a = [int(i) for i in input().strip().split()]
    b = fun(a)
    print(b)
