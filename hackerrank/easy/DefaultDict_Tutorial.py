from operator import ge
import sys
import collections

sys.stdin = open("input.txt", 'r')


def counters(A, B):
    ans=collections.defaultdict(list)
    for i in range(len(A)):
        ans[A[i]].append(i)
    for j in B:
        get_item=ans[j]
        for k in get_item:
            print(k+1,end=' ')
        if get_item==[]:
            print('-1',end=' ')
        print()


if __name__ == '__main__':
    n, m = map(int, input().strip().split())
    A=[]
    B=[]
    for i in range(n):
        A.append(input())
    for i in range(m):
        B.append(input())
    counters(A,B)
