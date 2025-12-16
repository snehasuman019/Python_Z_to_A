number = int(input("Enter a number: "))
print(number)

#valueerror = if user enters string instead of integer
#try except block to handle errors
#it blocks the code from crashing

try:
    number = int(input("Enter a number: "))
    print(number)
except:
    print("Invalid Input")
