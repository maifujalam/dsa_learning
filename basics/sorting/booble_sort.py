import sys

sys.stdin = open('input.txt', 'r')

a = [int(i) for i in input().strip().split()]

for i in range(len(a) - 1):
    for j in range(len(a) - 1 - i):
        if a[j + 1] < a[j] :
            a[j], a[j + 1] = a[j + 1], a[j]

print(a)