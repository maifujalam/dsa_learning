import sys

sys.stdin = open('input.txt', 'r')


def is_leap(x):
    flag=False
    if x%4 == 0:
        flag=True
        if x%100 !=0 and x%400==0:
            flag=False
        if x%100 ==0 and x%400 ==0:
            flag=True
    return flag


if __name__ == '__main__':
    a = int(input())
    print(is_leap(a))