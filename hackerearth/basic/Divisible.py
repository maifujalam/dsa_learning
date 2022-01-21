import sys

sys.stdin = open('input.txt', 'r')

n = int(input().strip())
a = [i for i in input().strip().split()]
al=a[:len(a)//2]
ar=a[len(a)//2:]
gn=''
for i in al:
    gn+=i[0]
for i in ar:
    gn+=i[-1]
print('OUI') if int(gn)%11==0 else print('NON')