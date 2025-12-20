# import json
# print(json.__file__)


# data = {"project": "AI Mentor", "status": "active"}

# with open("data.json", "w") as f:
#     json.dump(data, f, indent=4)



#json JavaScript Object Notation
#It is a lightweight data format used to store and exchange data.

'''
import json
person = {"name":"Sneha", "age":20, "city":"New York", "hasChildren":False, "titles": ["engineer", "programmer"]}
personJSON = json.dumps(person, indent=4, sort_keys = True)
# print(personJSON)

# json_string = json.dumps(personJSON)
#json.dumps() → convert to JSON string
# print(personJSON)

# with open("person.json", 'w')as file:
#     json.dumps(person, file, indent=4)

# person = json.loads(personJSON)

with open("person.json", 'r')as file:
    person = json.load(file)
# json.dumps(person, file, indent=4)

print(person)
'''

import json
class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age

user = User("Sneha", 20)

def encode_user(o):
    if isinstance(o, User):
        return{'name': o.name, 'age': o.age, o.__class__.__name__: True}
    else:
        return TypeError("Object of type user is not JSON serializable")

from json import JSONEncoder
class UserEncoder(JSONEncoder):

    def default(self, o):
        if isinstance(o, User):
            return{'name': o.name, 'age': o.age, o.__class__.__name__: True}
        return JSONEncoder.default(self, o)
            
userJSON = json.dumps(user, default=encode_user)
print(userJSON)

def decode_user(dct):
    if User.__name__ in dct:
        return User(name=dct['name'], age=dct['age'])
    return dct

user = json.loads(userJSON, object_hook = decode_user)
print(type(user))
print(user.name)