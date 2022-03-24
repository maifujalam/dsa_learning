import sys

sys.stdin = open('input.txt', 'r')


def selection(x):
    for i in range(len(x)):
        min_index = i
        for j in range(i + 1, len(x)):
            if a[min_index] > a[j]:
                min_index = j
        a[i] = a[min_index]
    return x


if __name__ == '__main__':
    a = [int(i) for i in input().strip().split()]
    b = selection(a)
    print(b)
