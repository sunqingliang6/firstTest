# -*- coding: UTF-8 -*-

class Animal(object):
    def call(self):
        print "Animal call."

class Dog(Animal):
    def call(self):
        print "Dog call 'wang wang'."

class Cat(Animal):
    def call(self):
        print "Cat call 'miao miao'."

class Bee(Animal):
    pass

def call_twice(dd):
    dd.call()
    dd.call()

call_twice(Animal())
call_twice(Dog())
call_twice(Cat())
call_twice(Bee())