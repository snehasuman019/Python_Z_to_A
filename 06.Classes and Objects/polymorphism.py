# Same method name, different behavior

# Method overriding
# “One name, many forms”# polymorphism.py

class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

animals = [Dog(), Cat()]

for a in animals:
    a.sound()
