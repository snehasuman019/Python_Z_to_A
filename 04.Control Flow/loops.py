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
for letter in "Sneha":
    print(letter)


# Nested loops
# A loop inside another loop.

for i in range(3):
    for j in range(2):
        print(i, j)
