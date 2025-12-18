#tuples are a container used to store multiple values in a single variable
#tuples are ordered, unchangeable, and allow duplicate values
#tuples are defined by enclosing the values in parentheses ()   

coordinates = (4,5)
print(coordinates)
print(coordinates[0])
#coordinates[0] = 10  #this will give error as tuples are immutable
print(coordinates[1])

#list [] is used to store multiple values in a single variablewhile in tuples () is used.
#lists are mutable while tuples are immutable
#tuples are faster than lists   

coordinates2 = [(4,5), (6,7), (8,9)]  #list of tuples
print(coordinates2)
print(coordinates2[0])



mytuple = ("Sneha")
print(type(mytuple))  #this will give class 'str' as its not a tuple
a = tuple(["Sneha", 20, "Punjab"])
print(a)
print(type(a))  #this will give class 'tuple' as we have used tuple() function

b = ('a','p','p','l','e')
print(b.count('p'))  #counts occurrences of item
print(b.index('p'))  #gives index of item
#tuples can be unpacked like lists
print(b.index('l'))  #gives index of item

c = (1,2,3,4,5,6,7,8,9,10)
d = c[2:5]  #slicing
print(d)

import timeit
print(timeit.timeit(stmt="[0,1,2,3,4,5]", number =1000000))
print(timeit.timeit(stmt="(1,2,3,4,5,6)", number =1000000)) 
#the second one is faster as tuples are immutable