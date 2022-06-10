def f1(fun):
    def wrapper(*args,**kwargs):
        print("Start")
        val=fun(*args,**kwargs)
        print("Stop")
        return val
    return wrapper

@f1
def f2(a,b):
    print(a,b)

@f1
def add(a,b):
    return a+b

print(add(2,4))