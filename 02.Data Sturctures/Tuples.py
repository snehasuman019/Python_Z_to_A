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
