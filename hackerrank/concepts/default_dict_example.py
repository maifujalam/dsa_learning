# https://docs.python.org/3.10/library/collections.html#collections.defaultdict
import collections
a="umbrella"
x=collections.defaultdict(int)
for i in a:
    x[i]+=1
print(x)
for j in x.items():
    print(j)


