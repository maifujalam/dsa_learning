import collections
import sys 

sys.stdin=open('input.txt')

if __name__=='__main__':
    a=collections.OrderedDict()
    n=int(input().strip())
    for i in range(n):
        x=[i for i in input().strip().split()]
        price=int(x[-1])
        item=' '.join(x[:-1])
        if item in a:
            a[item]=a[item]+price
        else:
            a[item]=price
    #print(a)
    for i in a.items():
        print(i[0],i[1])
