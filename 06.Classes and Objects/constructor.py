# Constructor runs automatically when object is created.
# __init__ method
# Initializing object data
# Instance variables

# constructor.py

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name, self.age)

s1 = Student("Sneha", 21)
s2 = Student("Amit", 22)

s1.display()
s2.display()
