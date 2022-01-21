import sys

sys.stdin = open('input.txt', 'r')

n=int(input())
a=[int(i) for i in input().strip().split()]
print("Yes") if a[-1]%10==0 else print("No")