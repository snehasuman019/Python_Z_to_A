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