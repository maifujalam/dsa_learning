a=[1,2,3,4,5]
n=3

for i in range(n):
    last=a.pop()
    a.insert(0,last)
    print(a)
