monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April", 
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
    1: "January"
}

print(monthConversions["Nov"])
print(monthConversions.get("Dec"))
print(monthConversions.get(1))

#get method to avoid error if key not found and act as a default value
print(monthConversions.get("Luv", "Not a valid month")) 


mydict = {"name":"Sneha", "age":20, "city":"Punjab "}
print(mydict)

value = mydict["name"]
print(value)

mydict["email"] = "snehasuman1901@gmail.com"
print(mydict)

del mydict["age"] #deletes key-value pair
print(mydict)

mydict.pop("city") #removes key-value pair and returns value
print(mydict)

if "lastname" in mydict:
    print(mydict["lastname"])  #this will give error if key not found

try: 
    print(mydict["lastname"])
except:
    print("Key not found")


my_dict = {3:9, 6:36, 9:81, 12:144}
print(my_dict)
#[0] will not give any output so index you will have to use [3] so you will get the valuse as 9.
#squares = {k:v*v for k,v in my_dict.items()}  #dictionary comprehension


# mytuple = [8,7]
# mydict2 = {mytuple: 15} 
#  #tuples can be used as keys as they are immutable
# print(mydict2)
## unhashable type: 'list'