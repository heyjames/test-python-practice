# print("Hello World")

# class MyClass:
#     x = 5

# p1 = MyClass()
# print(p1.x)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print("Hello. My name is " + self.name)

p = Person("John", 21)
p.greet()