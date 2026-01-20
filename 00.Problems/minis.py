# Problem 1: Check Largest of 3 Numbers
a,b,c = 10,30,20
if a>= b and a >= c:
    print(a, "is largest")
elif b>= a and b >= c:
    print(b, "is largest")
else:
    print(c, "is largest")



# Problem 2: Check Even or Odd
# a,b = 10 , 23
a = int(input("Enter a number: "))
if a%2 == 0:
    print(a, "is even")
else:
    print(a, "is odd")


# Problem 3: Check Prime Number
num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, int(num**0.5) + 1):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")


# Check positive, negative or zero
s = int(input("Enter a number:"))
if s>0:
    print(s,"is positive")
elif s<0:
    print(s,"is negative")
else:
    print(s, "is zero")

# Check Leap Year
year = int(input("Enter a year: "))
if (year%4==0 and year %100 != 0):
    print(year, " is a leap year")
else:
    print(year, " is not a leap year")
