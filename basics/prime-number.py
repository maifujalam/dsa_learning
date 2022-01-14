n = int(input())
flag = False
for i in range(2, n):
    if n % i == 0:
        print("This no divisible by",i)
        flag = True
        break
print("Prime") if not flag else print("Not Prime")

if __name__ == '__main__':
    pass
