#decorators is a function that takes function as input adds extra behavior without changing the original function code
#heavily used for logging, authentication , timing functions, access control, caching, validation, api rate limiting...... flask, django, fastAPI
'''
#Function inside function
def hello():
    print("Hello")

x = hello
x()


#Function returning another function
def outer():
    def inner():
        print("Hello from inner")
    return inner

func = outer()
func()



def my_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

def greet():
    print("Hello")

greet = my_decorator(greet)
greet()


#Decorators with Arguments
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before")
        func(*args, **kwargs)
        print("After")
    return wrapper

@my_decorator
def add(a, b):
    print(a + b)

add(3, 5)

'''
import functools
'''
#2 decorators  . !function decorator and 2 class decorator
def start_end_decorator(func):
    def wrapper():
        print('start')
        func()
        print("End")
    return wrapper
@start_end_decorator
def print_name():
    print("Sneha")

# print_name = start_end_decorator(print_name)
print_name()

# @my_decorator
# def dosomething():
#     pass

#*args collects positional arguments (stored as a tuple)
# **kwargs collects keyword arguments stored as a dictionary. 
#applying arguments

def start_end_decorator(func):
   
    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print("End")
        return result
    return wrapper
@start_end_decorator
def add5(x):
    return x+5
result = add5(10)
print(result)

'''
'''

def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat
@repeat(num_times = 4)

def greet(name):
    print(f"Hello {name}")
greet("sneha")
'''
#countcalls

class CountCalls:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0
    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f'This is excuted {self.num_calls} times')
        return self.func(*args, **kwargs)
        # print("Hiii")

# cc = CountCalls(None)
# cc()

@CountCalls
def say_hello():
    print("Hello")

say_hello() #1time
say_hello() #2time
