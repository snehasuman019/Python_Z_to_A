# try:
#     x = int(input())
#     print(10 / x)
# except ZeroDivisionError:
#     print("Cannot divide by zero")
# except ValueError:
#     print("Invalid input")

try:
    print("Try block")
except:
    print("Error")
else:
    print("No error")
finally:
    print("Always runs")
print("H")