# -*- coding: UTF-8 -*-

#子类不会继承父类的私有变量
#创建子类实例时，如果子类定义了构造函数，则只调用子类的构造函数；如果子类未定义构造函数，则执行父类构造函数

class Animal(object):
    def __init__(self, name):
        print 'zhi xing Animal init'
        self.__name = name

    def call(self):
        print "Animal call."

    def __getName(self):
        print "Animal getName method."
        return self.__name
    def me(self):
        return self.__getName()

class Dog(Animal):
    def __init__(self):
        self.__name = 'dogname'
        print 'zhi xing Dog init'
    def call(self):
        print "Dog call 'wang wang'."
    def __getName(self):
        print "Dog getName method."
        return self.__name
    # def me(self):
    #     return self.__getName()

pet = Animal('mypet')
print pet.me()
dog = Dog()
print dog.me()
'''commit one 提到远端'''