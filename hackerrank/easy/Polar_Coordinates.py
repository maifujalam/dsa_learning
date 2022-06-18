import math
import sys
import cmath

sys.stdin=open('input.txt','r')


def polar_coordinate(z):
    print(math.sqrt(math.pow(z.real,2)+math.pow(z.imag,2)))
    print(cmath.phase(z))

if __name__ == '__main__':
    z=complex(input())
    polar_coordinate(z)