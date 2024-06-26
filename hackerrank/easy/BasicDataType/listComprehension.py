import sys

sys.stdin = open("input.txt")

if __name__ == '__main__':
    x = int(input().strip())
    y = int(input().strip())
    z = int(input().strip())
    n = int(input().strip())
    a=[ [a,b,c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if a+b+c!=n ]
    print(a)
