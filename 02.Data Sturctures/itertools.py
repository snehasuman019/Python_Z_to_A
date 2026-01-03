#itertools module in Python provides a collection of tools for handling iterators.
# It includes functions that create iterators for efficient looping, combinatorial generation, and more.
#product , permutations, combinations, accumulate, groupby, infinite iterators
from itertools import product, permutations, combinations, accumulate, groupby, count, cycle, repeat, combinations_with_replacement
a = [1,2]
b = [3,4]
prod = product(a,b)
print(list(prod))  #cartesian product


print("**permutations**")
c = [1,2,3]
perm = permutations(c)
print(list(perm))  #all possible arrangements


print("**combinations**")
d = [1,2,3,4]
comb = combinations(d, 2)
print(list(comb))  #all possible combinations of length 2

#combinations with replacement
comb_wr = combinations(d, 2)    
print(list(comb_wr))  #all possible combinations of length 2 with replacement


print("**accumulate**")
#cumulative sum
e = [1,2,3,4]
acc = accumulate(e)
print(list(acc))  
print(e)
print(list(acc))

print("**groupby**")
def smaller_than_3(x):
    return x<3
f = [1,2,3,4]
group_obj = groupby(f, key= smaller_than_3)
for key, value in group_obj:
    print(key, list(value))


print("**count,cycle, repeat** ")
#infinite iterator starting from 10
#count is used to generate consecutive integers indefinitely.
#cycle is used to cycle through an iterable indefinitely.
#repeat is used to repeat a single value indefinitely or a specified number of times.   

z=[1,2,3]
for i in repeat(1,4): #infinite iterator starting from 10
    print(i)

for i in count(10):
    print(i)
    if i==15:
        break


from itertools import cycle

for i, v in zip(range(6), cycle(["A", "B"])):
    print(v)