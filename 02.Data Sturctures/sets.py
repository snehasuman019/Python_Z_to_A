#sets: unordered, mutuable, no duplicate elements
#sets are defined by enclosing the values in curly braces {} or by using the set() function
myset = set()
myset.add(1)
myset.add(2)    
myset.add(3)
print(myset)
if 1 in myset:
    print("Found")

print(type(myset))  #this will give class 'dict' as its not a set


#union 

odds = {1,3,5,7,9}
evens = {0,2,4,6,8}
primes = {2,3,5,7}

u = odds.union(evens)
print(u)

i = evens.intersection(primes)
print(i)

# setA = {1,2,3,4,5,6,7,8,9}
# setB = {1,2,3,10,11,12}

setA = {1,2,3,4,5,6}
setB = {1,2,3}

# diff = setA.difference(setB)
# print(diff)  #elements in setA but not in setB
diff = setA.symmetric_difference(setB)
print(diff)  #elements in setA and setB but not in both

setA.update(setB)
print(setA)  #adds elements of setB to setA

setA.intersection_update(setB)
print(setA)  #keeps only elements present in both sets

setA.difference_update(setB)
print(setA)  #removes elements of setB from setA

setA.symmetric_difference_update(setB)
print(setA)  #keeps elements in setA and setB but not in both

print(setA.issubset(setB))  #checks if setA is subset of setB
print(setA.issuperset(setB))  #checks if setA is superset
print(setB.issubset(setA))  #checks if setB is subset of setA
print(setB.issuperset(setA))  #checks if setB is superset

print(setA.isdisjoint(setB))  #checks if sets have no elements in common

setC = {1,2,3,4,5,6}
setD = set(setC)  #creates a copy of setC
setD.add(7)
print(setC)
print(setD)


a = frozenset([1,2,3,4,5])  #immutable set
#a.add(6)  #this will give error as frozenset is immutable
#a.remove(3)  #this will give error as frozenset is immutable
#but union and intersection methods work
b = a.union({6,7,8})
print(b)
print(a)