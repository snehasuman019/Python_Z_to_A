# args_kwargs.py
# Learn flexible functions that accept any number of arguments.
# args_kwargs.py

def add_numbers(*args):
    print("Args:", args)
    return sum(args)

def student_info(**kwargs):
    print("Student Info:", kwargs)

def mixed(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

print(add_numbers(1, 2, 3, 4))

student_info(name="Sneha", age=21, course="Python")

mixed(10, 20, city="Ranchi", country="India")
