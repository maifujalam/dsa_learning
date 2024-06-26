import sys

sys.stdin = open("input.txt")

if __name__ == '__main__':
    A = {1, 2, 3, 4, 5}
    B = {1, 2, 3}
    C = {1, 2, 3}
    print(A.issuperset(B))
    print(B)
    print(C)
