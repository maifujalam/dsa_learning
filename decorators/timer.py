import time

def decorator(fun):
    def wrapper(*args,**kwargs):
        print("Start")
        before=time.time()
        fun(*args,**kwargs)
        print("Time to run:",time.time()-before)
        print("stop")
    return wrapper

@decorator
def run(a):
    print("I am called")
    time.sleep(a)
    print("I am called stopped")

run(3)