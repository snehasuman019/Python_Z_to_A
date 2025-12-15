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