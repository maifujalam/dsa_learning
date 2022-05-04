import sys

sys.stdin = open('input.txt', 'r')


def zoo(x):
    # z=o=0
    z = x.count('z')
    o = x.count('o')
    # z = o = 0
    # for i in x:
    #     if i == 'z':
    #         z += 1
    #     else:
    #         break
    # for i in x:
    #     if i == 'o':
    #         o += 1
    #     else:
    #         break ceil
    if z != 0 and o != 0:
        return "Yes" if o / z == 2 else "No"
    else:
        return "No"


if __name__ == '__main__':
    x = input().strip().strip()
    print(zoo(x))
