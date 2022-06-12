import sys
import string

sys.stdin = open("input.txt", "r")


def num_to_letter(a):
    alphabets = [i for i in string.ascii_lowercase]
    return alphabets[a - 1]


def alphabet_rangoli(n):
    x = 0
    is_reversing = False
    for i in range(2 * n - 1):
        if x < n and not is_reversing:
            x += 1
        else:
            x -= 1
            is_reversing = True
        print("-"*2*(n-x),end="")
        bx=[]
        d=[]
        for j in range(x):
            bx.append(num_to_letter(n-j))
        for k in range(x-1):
           d.append(num_to_letter(n-k))
        d.reverse()
        bx=bx+d
        bx='-'.join(bx)
        print(bx,end='')
        print('-' * (2 * (n - x)), end='')
        print('')


if __name__ == '__main__':
    n = int(input().strip())
    alphabet_rangoli(n)
