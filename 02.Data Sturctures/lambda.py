#lambda arguments: expression
add10 = lambda x: x + 10
print(add10(5))

def add10_func(x):
    return x + 10

mult = lambda x, y: x * y
print(mult(2,3))

# list = [(1,2), (15,1), (5,-1), (10,4)]

# # def sort_by_y(x):
# #     return x[1]
# # list_sorted = sorted(list, key=sort_by_y)

# list_sorted = sorted(list, key=lambda x: x[0] + x[1])
# print(list)
# print(list_sorted)

#map(fun, seq)
a = [1,2,3,4,5]
b = map(lambda x: x*2, a)
print(list(b))

#filter(fun, seq)
d = [1,2,3,4,5,6,7,8,9,10]
c = filter(lambda x: x%2==0, a)
# c=[x*2 for x in a]  #using list comprehension
print(c)
e=[x for x in a if x%2==0] #using list comprehension
print(e)


from functools import reduce
#reduce(fun, seq)
f = [1,2,3,4]
product_a = reduce(lambda x,y: x*y, f)
print(product_a)
