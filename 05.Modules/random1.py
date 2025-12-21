import random
#If you want a random integer between 1 and 10
a = random.randint(1,10)
print(a)

# If you want a random float between 1 and 10
b=random.uniform(1,10)
print(b)

#If you want a float between 0 and 1
print(random.random())

d=random.normalvariate(0,1)
print(d)

mylist = list("ABCDEFGH")
f = random.sample(mylist, 3)
print(f)
g=random.choices(mylist, k=3)
print(g)

random.shuffle(mylist)
print(mylist)
random.seed(2)
print(random.random())
print(random.randint(1,10))


import secrets
#used to import secrets like passwords,security tokens or accounts authentication .  disadvantage : is that it's it take more times for these algo but they will generate a true random no. 

z=secrets.randbelow(10)
print(z)

y=secrets.randbits(4)
print(y)

mylist1 = list("ABCDEFGH")
s=secrets.choice(mylist1)
print(s)



import numpy as np
f=np.random.randint(0,10, (3,4))
print(f)

print("*********")

arr = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(arr)
np.random.shuffle(arr)
print(arr)



np.random.seed(1)
print(np.random.rand(3,3))
# np.random.seed(1)
# print(np.random.rand(3,3))
