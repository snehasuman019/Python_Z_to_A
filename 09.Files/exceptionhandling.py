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

# practice.py

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def move(self):
        print("Vehicle moves")

class Car(Vehicle):
    def move(self):
        print(self.brand, "car drives")

c = Car("Honda")
c.move()
