import math
import sys

sys.stdin = open("input.txt")

a = [int(i) for i in input().strip().split()]


def merge(a):
    if len(a) > 1:
        mid = math.ceil(len(a) / 2)
        print(mid)
        L = a[:mid]
        print(L)
        R = a[mid:]
        merge(L)
        merge(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                a[k] = L[i]
                i += 1
            else:
                a[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            a[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            a[k] = R[j]
            j += 1
            k += 1
        print("A"+''.join([str(i) for i in a]))


merge(a)
print(a)