import sys, string

sys.stdin = open('input.txt', 'r')


def solve(s):
    ans=''
    for i in range(len(s)):
        if i ==0 and s[i].islower():
            ans+=s[i].upper()
        elif i==0 and not s[i].islower():
            ans+=s[i]
        elif s[i].islower() and s[i-1]==' ':
            ans+=s[i].upper()
        elif s[i].islower() and s[i-1]!=' ':
            ans+=s[i]
        else:
            ans+=s[i]
    return ans


if __name__ == '__main__':
    s = input()
    print(solve(s))
