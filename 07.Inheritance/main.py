from chef import Chef
from ChineseChef import ChineseChef

my_chef = Chef()
my_chef.make_special_dish()

my_chinese_chef = ChineseChef()
my_chinese_chef.make_special_dish()

# inheritance.py

class Person:
    def speak(self):
        print("Person can speak")

class Student(Person):
    def study(self):
        print("Student can study")

s = Student()
s.speak()
s.study()
