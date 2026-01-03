
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
    '''This func is doing nothing except printing a message
    that message is hellow'''
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