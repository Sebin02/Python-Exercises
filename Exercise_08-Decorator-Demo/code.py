#prg to measure the time taken by a function to run
import time

def time_this(func):
    def wrapper(*args,**kwargs):
        print(f"--> Running {func.__name__}")   #Shows the function name
        start_time=time.perf_counter()          #Record the start time
        result=func(*args,**kwargs)             #Call the actual function  
        end_time=time.perf_counter()            #get end time
        time_taken=end_time-start_time
        print(f"--> {func.__name__} ran in {time_taken:.6f} seconds")   #display the time taken
        return result                           # return the result of the function
    return wrapper                              # return the wrapped version of the function

@time_this                                      # apply the decorator
def sum_func(a,b):
    print("Sum is",a+b)

sum_func(3,4)                                   #call decorated function