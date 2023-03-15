import time

def timestamp(my_func):
    def wrapper_function():
        print(time.ctime())
        my_func()
    return wrapper_function
