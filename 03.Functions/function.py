#functions helps to organize code into reusable blocks
def say_hi():
    print("Hello User!")
    print("Welcome to Python Functions")
say_hi()  #function call

def sayhi(name, age):
    print("Hello " + name + ", you are "+ str(age)+ "!")
sayhi("Alice", 20)


def cube(num):
    return num*num*num
#cube(3)  #function call but return value is not used
print(cube(3))  #printing the return value
result = cube(3)
print(result)

'''
def printSuccess():
    print("The task was successful")
    print("Moving to the next task")
    print("Send me the next task")
printSuccess()

def addNumbers(num1, num2):
    return num1 + num2  
result = addNumbers(5, 10)
print(result)

# Doc Strings
def printSuccess2():
    ''''''This func is doing nothing except printing a message
    that message is hellow 
    print("Hellow")
printSuccess2()
print(printSuccess2.__doc__)
help(printSuccess2)

# # input arguments
# def printMessage(msg):
#     print(msg)
# printMessage("Hello World")

def printMsg(msg):
    """The function prints the message supplied by the user or prints that msg is not in the form of string"""
    if isinstance(msg, str):
        print(msg)
    else:
        print("Your input argument is not a string")
        print("Here is the type of what you have supplied :",type(msg))
help(printMsg)
# printMsg("Hello World")
print("This is the message")
'''
'''
def mypow(a, b):
    # 'this function computes power just like builtin pow function
    c = a**b
    print(c)
    mypow(2, 3)
def myadd(x, y):
    # this function computes addition just like builtin add function
    z = x + y
    print(z)
# '''

# def calc(a, b):
#     return a + b, a - b

# x, y = calc(5, 2)
# def myadd(x, y):
#     z = x + y
#     print(z)

def calc(a, b):
    return a + b, a - b

x, y = calc(5, 2)

def myadd(x, y):
    z = x + y
    print(z)

myadd(x, y)
def square(n):
    return n * n

result = square(4)
print("The square is:", result)

# basic_functions.py

def greet():
    print("Hello, welcome to Python!")

def add(a, b):
    return a + b

def calc(a, b):
    return a + b, a - b

greet()

result = add(3, 5)
print("Sum:", result)

x, y = calc(10, 4)
print("Addition:", x)
print("Subtraction:", y)


# Binary recursionn
def func(n):
    if n == 0:
        return
    func(n-1)
    func(n-1)
    print(n)
