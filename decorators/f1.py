def f1(fun):
    def wrapper(*args, **kwargs):
        print("Started")
        fun(*args,**kwargs)
        print("Ended")

    return wrapper


@f1  # It will call function f1 with parameter as f i.e, f1(f)
def f(p,q):
    print(p,q)


f("Hi","hello")
