friends = ["Sam", "Joe", "Ria", "Tia"]
print(friends)
print(friends[0])
print(friends[1])
print(friends[-1])
print(friends[1:3])
friends[1] = "Sneha"
print(friends)


#functions to modify list

friends.append("Lia") #adds at last
print(friends)
friends.insert(1, "Mia")  #adds at index 1
print(friends)
friends.remove("Ria")  #removes specific item
print(friends)
friends.pop()   #removes last item
print(friends)

lucky_numbers = [4, 8, 15, 16, 23, 42]
friends.extend(lucky_numbers)  #adds another list at end
print(friends)


friends.index("Sam")  #gives index of item
print(friends)
friends.count("Sam")  #counts occurrences of item
print(friends)
friends.reverse()  #reverses the list
print(friends)

# friends.sort()  #sorts the list
# print(friends)
# friends.sort(reverse=True)  #sorts in descending order
# print(friends)

friends.clear()  #clears the list
print(friends)

mylist = ["banana", "cherry", "apple"]
print(mylist)
for i in mylist:
    print(i)

l=[4,3,1,5,2]
print(l)
l.sort()
m=sorted(l)
print(l)
print(m)