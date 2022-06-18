import itertools
import sys

sys.stdin=open("input.txt","r")


def string_permutation(a, b):
    k=[str(i) for i in a]
    k.sort()
    k=''.join(k)
    ans=list(itertools.permutations(k,b))
    for i in ans:
        tmp=''
        for j in i:
            tmp+=j
        print(tmp)


if __name__ == '__main__':
    a,b=input().strip().split()
    b=int(b)
    string_permutation(a,b)