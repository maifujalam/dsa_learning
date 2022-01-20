import sys
sys.stdin = open('input.txt', 'r')

for _ in range(int(input().strip())):
    cg,cp=map(int,input().strip().split())
    n=int(input().strip())
    cost1=cost2=0
    for i in range(n):
        b1,b2=map(int,input().strip().split())
        cost1+=b1*cg+b2*cp
        cost2+=b2*cg+b1*cp
    print(min(cost1,cost2))
