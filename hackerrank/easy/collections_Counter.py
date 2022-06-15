import collections
import sys

sys.stdin = open('input.txt', 'r')


def shop(no_of_shoe, shoes, no_of_customers, shoe_want):
    shoe_available = collections.Counter(shoes)
    sum=0
    for i in shoe_want:
        shoe_size=i[0]
        shoe_price=i[1]
        if shoe_size in shoe_available.keys():
            if shoe_available.get(shoe_size) == 0:
                shoe_available.pop(shoe_size)
            else:
                shoe_available.update({shoe_size:-1})
                sum += shoe_price
    print(sum)

if __name__ == '__main__':
    no_of_shoe = int(input().strip())
    shoes = [int(i) for i in input().strip().split()]
    no_of_customers = int(input().strip())
    shoe_want = []
    for i in range(no_of_customers):
        a, b = map(int, input().strip().split())
        shoe_want.append((a, b))
    shop(no_of_shoe, shoes, no_of_customers, shoe_want)
