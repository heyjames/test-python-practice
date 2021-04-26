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

print(1 == "0") # False
print(True == "True") # False
print(1 == True) # True
print(0 == False) # True
print(-1 == True) # False (Interesting...)
print(-1 == False) # False (Interesting...)
print("" == None) # False
print(False == None) # False
print([] == None) # False
iAmNothing = None
print(iAmNothing == None) # True
print("lem" in "element") # True
print("LEM" in "element") # False
print("lem" not in "element") # False