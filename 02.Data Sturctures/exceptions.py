#errors and exceptions
# a = 5 
# print(a)
#print(a)) #syntax error becasue of extra parenthesis
#print(b) #name error because b is not defined

# b = 5 + '10'
# print(b) #type error because we are trying to add int and str

# a = [1,2,3]
# a.remove(4) #value error because 4 is not in the list
# print(a)

# x = 5
# assert (x>=0), 'x is not positive' #assertion error if condition is false
# print(x)

# # try:
# #     a = 5 / 0
# # except:
# #     print("an error occurred")


# # try:
# #     a = 5 / 0
# # except Exception as e:
# #     print(e)

# try:
#     a = 5 /1
#     b = a + '10'
# except ZeroDivisionError as e:
#     print(e)
# except TypeError as e:
#      print(e)
# else:
#     print("everything is fine")
# finally:
#     print("cleaning up..")



class ValueTooHighError(Exception):
    pass

class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

def test_value(x):
    if x > 100:
        raise ValueTooHighError("value is too high")
    if x < 5:
        raise ValueTooSmallError("value is too small",x)
try:
    test_value(00)
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(e.message, e.value)