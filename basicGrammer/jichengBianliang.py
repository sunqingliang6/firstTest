# -*- coding: UTF-8 -*-

#子类不会继承父类的私有变量
#创建子类实例时，如果子类定义了构造函数，则只调用子类的构造函数；如果子类未定义构造函数，则执行父类构造函数

class Animal(object):
    __privateSun = 'privateSun'
    publicQing = 'publicQing'
    def __init__(self, name):
        print 'zhi xing Animal init'
        self.__name = name;

    def call(self):
        print "Animal call."

    def getName(self):
        return self.__name

    def getPrivateSun(self):
        return self.__privateSun

    def getPublicQing(self):
        return self.publicQing

class Dog(Animal):
    def __init__(self):
        print 'zhi xing Dog init'
        self.__name = 'aaaa';
    def call(self):
        print "Dog call 'wang wang'."

class Cat(Animal):
    def call(self):
        print "Cat call 'miao miao'."

pet = Animal('mypet')
print pet.getName()
dog = Dog()
print dog.getName()
print '0 ' + dog.getPrivateSun()
print '1 ' + dog.getPublicQing()
print '2 ' + dog.publicQing
# print dog.__privateSun  报错