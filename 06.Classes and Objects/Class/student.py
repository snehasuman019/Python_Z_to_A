class Student:
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

# class_object.py

class Student:
    def study(self):
        print("Student is studying")

# Creating objects
s1 = Student()
s2 = Student()

s1.study()
s2.study()
