import sys

sys.stdin=open('input.txt')

if __name__ == '__main__':
    n=int(input().strip())
    l=set()
    for _ in range(n):
        l.add(input())
    print(len(l))