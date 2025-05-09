#prg to measure the time taken by a function to run
import time

def time_this(func):
    def wrapper(*args,**kwargs):
        print(f"--> Running {func.__name__}")
        start_time=time.perf_counter()
        result=func(*args,**kwargs)
        end_time=time.perf_counter()
        time_taken=end_time-start_time
        print(f"--> {func.__name__} ran in {time_taken:.6f} seconds")
        return result
    return wrapper

@time_this
def sum_func(a,b):
    print("Sum is",a+b)

sum_func(3,4)