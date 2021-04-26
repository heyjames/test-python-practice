# print("Hello World")

# class MyClass:
#     x = 5

# p1 = MyClass()
# print(p1.x)

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def greet(self):
#         print("Hello. My name is " + self.name)

# p = Person("John", 21)
# p.greet()

# def sum(x, y):
#     return int(x) + int(y)

# answer = sum(4, "2")
# print(answer)

# print(1 == "0") # False
# print(True == "True") # False
# print(1 == True) # True
# print(0 == False) # True
# print(-1 == True) # False (Interesting...)
# print(-1 == False) # False (Interesting...)
# print("" == None) # False
# print(False == None) # False
# print([] == None) # False
# iAmNothing = None
# print(iAmNothing == None) # True
# print("lem" in "element") # True
# print("LEM" in "element") # False
# print("lem" not in "element") # False

# https://stackoverflow.com/a/3437068
# s = "This be a string"
# if s.find("is") == -1: # False and True doesn't work
#     print("No 'is' here!")
# else:
#     print("Found 'is' in the string.")

# s = "This be a string"
# if "is" not in s:
#     print("No 'is' here!")
# else:
#     print("Found 'is' in the string.")

# any_string = "This"
# start = 0
# stop = len(any_string)
# print(any_string.find('is', start, stop)) # 2. Returns start index of substring

x = -1
if x < 0:
    raise Exception("Numbers below zero are not allowed.")

myList = ["Tony Stark", "Steve Rogers"]
for element in myList:
    print(element)

for i in range(0, 4):
    print(i, "I can do this all day.")

metal = "Vibranium"
for i in range(0, len(metal)):
    print(metal[i])