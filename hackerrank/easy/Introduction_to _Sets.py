import sys

sys.stdin=open('input.txt','r')


def plant(a):
    x=set(a)
    print(sum(x)/len(x))


if __name__ == '__main__':
    N=int(input().strip())
    a=[int(i) for i in input().strip().split()]
    plant(a)