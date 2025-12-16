num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
sum = float(num1) + float(num2)
print(sum)

diff = float(num1) - float(num2)
print(diff)

prod = float(num1) * float(num2)
print(prod)

quot = float(num1) / float(num2)
print(quot)

# Modulus
mod = float(num1) % float(num2)
print(mod)

# Exponentiation
exp = float(num1) ** float(num2)
print(exp)

# Floor Division
floor_div = float(num1) // float(num2)
print(floor_div)

# Using parentheses to change order of operations
complex_calc = (float(num1) + float(num2)) * (float(num1) - float(num2))
print(complex_calc)

from math import *
print(floor(float(num1)))  # Rounding down
print(ceil(float(num2)))   # Rounding up
print(sqrt(float(num1)))    # Square root
print(sqrt(float(num2)))    # Square root
print(pow(float(num1), float(num2)))  # num1 to the power of num2
print(max(float(num1), float(num2)))  # Maximum of two numbers
print(min(float(num1), float(num2)))  # Minimum of two numbers
print(round(float(num1)))  # Rounding off num1
print(round(float(num2)))  # Rounding off num2


