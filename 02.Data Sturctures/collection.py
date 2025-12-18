#collections: Counter, namedtuple, OrderedDict, defaultdict, deque
from collections import Counter, namedtuple, OrderedDict, defaultdict, deque
a = "aaaaabbbbcccdde"
my_counter = Counter(a)
print(my_counter)
print(my_counter.items())
print(my_counter.keys())    
print(my_counter.values())
print(my_counter.most_common(2))  #gives 2 most common elements
print(my_counter.most_common(1)[0][0])  #gives the most
print(list(my_counter.elements()))  #gives all elements as per their count



print("***********namedtuple************")

Point = namedtuple('Point', 'x y')  #creates a namedtuple class Point with fields x and y
pt = Point(1, -4)
print(pt)


print("***********OrderedDict************" )
ordered_dict = OrderedDict()
ordered_dict['a'] = 3
ordered_dict['b'] = 2
ordered_dict['c'] = 5
print(ordered_dict)  #maintains the order of insertion

print("***********defaultdict************" )
d = defaultdict(int)  #default value of int is 0
d['a'] = 1
d['b'] = 2
print(d['a'])
print(d['c'])  #not present, returns default value 0


print("***********deque************" )
d = deque()
d.append(1)
d.append(2)
print(d)
d.appendleft(3)
print(d)
d.pop()
print(d)
d.popleft() #removes from left
print(d)
d.extend([4,5,6])
print(d)
d.appendleft(7)
print(d)
d.extendleft([8,9,10])  #adds to left in reverse order
print(d)
d.rotate(1)  #rotates right
print(d)
d.rotate(-2)  #rotates left
print(d)