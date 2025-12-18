print("Hello everybody! \nHow are you all.")
a = "So i thought of learning Python."
print(a)
print(a.lower())
print(a[0])
print(a.index("t"))
print(a.replace("Python", "Java"))


#strings: ordered, immutable, text representation

my_striing = "I'am a programmer"
print(my_striing)
char = my_striing[7]
print(char)

# substring = my_striing[2:9]
substring = my_striing[::-1]  #reverses the string
print(substring)

greeting = "Hello"
for i in greeting:
    print(i)

if 'e' in greeting:
    print("found")
else:
    print("not found")

a = "           Hello World        "
print(a.strip())  #removes whitespace from start and end
print(a)
print(a.lstrip())  #removes whitespace from start
print(a.rstrip())  #removes whitespace from end
print(a.upper())  #converts to uppercase
print(a.lower())  #converts to lowercase
print(a.endswith("   "))  #checks if string ends with given substring
print(a.count("l"))  #counts occurrences of substring
print(a.find("o"))  #gives index of first occurrence of substring
print(a.replace("World", "Everyone"))  #replaces substring with another substring
# print(a.split(" "))  #splits string into list of substrings based on delimiter
print(len(a))  #gives length of string  
print(a.capitalize())  #capitalizes first character of string
print(a.title())  #capitalizes first character of each word
# print(a.center(50))  #centers the string within given width

print("**************")
from timeit import default_timer as timer

# mylist = ['a']*6
# print(mylist)
# #bad
# mystring = ''
# for i in mylist:
#     mystring += i
# print(mystring)

# #good
# mystring = ''.join(mylist)  
# print(mystring)


'''
mylist = ['a']*1000000
print(mylist)
#bad
start = timer()
mystring = ''
for i in mylist:
    mystring += i
stop = timer()
print(stop - start)
# print(mystring)

#good
start = timer()
mystring = ''.join(mylist)  
stop = timer()
print(stop - start)
# print(mystring)
'''


print("**************")


#formatted strings
#%, .format, f-strings

name = "Sneha"
mystring = "The name is %s" %name
print(mystring)

var = 3
mystring2 = "The variable is %d" %var
print(mystring2)

float_var = 3.14159
mystring3 = "The float variable is %.2f" %float_var  #.
print(mystring3)

var1 = 3
var2 = 5.4
mystring4 = "The variable are %d and %.1f" %(var1, var2)
print(mystring4)