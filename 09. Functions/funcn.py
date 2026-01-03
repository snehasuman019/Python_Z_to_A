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