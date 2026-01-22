from functools import wraps
def my_decorator(func):
    def wrapper():
        print("Before function runs")
        func()
        print("After function runs")

    return wrapper

@my_decorator
def greet():
    print("hello formm decorators cheacker !!")

greet()



#Basic Structure of Decorator
def decorator(func):
    def wrapper():
        # before function
        func()
        # after function
    return wrapper
