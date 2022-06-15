import itertools, sys

sys.stdin=open('input.txt','r')

def prod(a, b):
    ans=list(itertools.product(a,b))
    for i in ans:
        print(i,end=' ')


if __name__ == '__main__':
    a = [int(i) for i in input().strip().split()]
    b = [int(i) for i in input().strip().split()]
    prod(a, b)
