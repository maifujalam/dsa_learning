import collections,sys
from operator import le

sys.stdin=open('input.txt')

if __name__=="__main__":
    n=int(input().strip())
    columns=input()
    Student=collections.namedtuple('Student',columns)
    a=[]
    for i in range(n):
        x=[j for j in input().strip().split()]
        l=Student._make(x)
        a.append(l)
    sum=0
    for i in a:
        sum+=(int(i.MARKS))
    print(sum/len(a))
    