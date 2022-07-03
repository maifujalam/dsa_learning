import sys

sys.stdin=open('input.txt')

def sym_dif(ma,na):
    a=list(ma.difference(na))
    b=list(na.difference(ma))
    s=a+b
    s.sort()
    print(s)

if __name__ == '__main__':
    m=int(input())
    ma=set(map(int,input().strip().split()))
    n=int(input())
    na=set(map(int,input().strip().split()))
    sym_dif(ma,na)