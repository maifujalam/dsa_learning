import collections

a=[1,1,2,3,4,5,3,2,3,2,1,2,3]
b=collections.Counter(a)
reduce_item=4
print(b)
if reduce_item in b.keys():
    print("ok")
    print(b.get(reduce_item))
    print(b.update({reduce_item:-1}))
    print(b)