def double(my_func):
    def wrapper_function():
        my_func()
        print("Let's try that again!")
        my_func()
    return wrapper_function