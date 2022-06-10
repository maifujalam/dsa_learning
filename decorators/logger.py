import datetime
import time
import glog

def loger(fun):
    def wrapper(*args, **kwargs):
        with open("log.log", "a+") as f:
            time_start = time.time()
            f.write(
                "Start Function:" + fun.__name__ + " at: " + str(datetime.datetime.now()) + "\n")
            fun(*args, **kwargs)
            f.write("Ended Function:" + fun.__name__ + " at:" + str(datetime.datetime.now()) +
                    " took:" + str(round(time.time() - time_start, 3)) + " Seconds \n")
            glog.info("completed")

    return wrapper


@loger
def run(a, b, c):
    time.sleep(0.2)
    print(a, b, c)


run(1, 2, 3)
