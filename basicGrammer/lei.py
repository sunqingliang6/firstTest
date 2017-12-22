# -*- coding: UTF-8 -*-

class Dog:
    count = 1
    name = "publicname"

    def __init__(self, name, color):
        Dog.count += 1
        self.name = name
        self.color = color
        print("Dog's init method.")

    def display(self):
        print "Name: " + self.name + ", Color: " + self.color

print Dog.count
yellowDog = Dog("huang", "yellow")
yellowDog.display()
print Dog.count
redDog = Dog("hong", "red")
redDog.display()

'''getattr测试'''
if hasattr(redDog, "display"):
    print getattr(redDog, "display")
else:
    print "no can shu"

'''首次关联git'''