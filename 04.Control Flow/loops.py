#while loop
#Runs as long as a condition is True

i=1
#while condition
while i<= 10:
    print(i)
    i += 1
print("Done with while loop")


#for loop
#Iterates over a sequence (list, string, range, etc.).
friends = ["Sam", "Joe", "Ria", "Tia"]
len(friends)  #gives length of list
print(len(friends))

for friend in friends:
    print(friend)

for index in range(5):  #range(n) gives numbers from 0 to n-1
    print(index)
    if index == 0:
        print("First iteration")
    else:
        print("Not first")


for letter in "Sneha":
    print(letter)


# Nested loops
# A loop inside another loop.

for i in range(3):
    for j in range(2):
        print(i, j)
