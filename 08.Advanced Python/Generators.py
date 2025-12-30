def mygenerator():
    yield 1
    yield 2
    yield 3
g = mygenerator()
value = next(g)
print(value)

value = next(g)
print(value)

value = next(g)
print(value)


g = mygenerator()
print(sorted(g))
print(sum(g))

# for i in g:
#     print(i)

def countdown(num):
    print("Starting")
    while num > 0:
        yield num 
        num -= 1
cd = countdown(4)
value = next(cd)
print(value)
print(next(cd))
print(next(cd))
print(next(cd))


# value = next(g)
# print(value)

def first(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums
def first_generator(n):
    num = 0
    while num < n:
        yield num
        num += 1
# print(first(10))
# print(sys.getsizeof(first(1000000))) # size in bytes


#Fibonacci
def fibonacci(limit):
    a, b = 0, 1
    # for _ in range(n):
    while a < limit:
        yield a
        a, b = b, a + b
fib = fibonacci(10)
for i in fib:
    print(i)
