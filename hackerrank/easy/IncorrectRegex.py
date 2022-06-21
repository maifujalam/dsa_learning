import sys
import re 
sys.stdin = open('input.txt')

def validate_regex(l):
    for i in l:
        try:
            re.compile(i)
            print("True")
        except:
            print("False")


if __name__ == '__main__':
    a=int(input())
    l=[]
    for i in range(a):
        x=input().strip()
        l.append(x)
    validate_regex(l)
