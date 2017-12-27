# -*- coding: UTF-8 -*-

class Animal(object):
    aa = 'aa'
    def __init__(self):
        print "Animal init method"
    def weare(self):
        print "We are animal"
    def call(self):
        print "Animal call."

class Dog(Animal):
    def __init__(self, aa):
        #Animal.__init__(self)
        super(Dog, self).__init__()
        self.aa = aa
        print "Dog init method"
    def call(self):
        print "Dog call 'wang wang'."

mydog = Dog('fuzhi')
mydog.weare()
mydog.call()
print mydog.aa
print Animal.aa

print issubclass(Dog, Animal)
print isinstance(mydog, Dog)

'''变量'''
class JustCounter:
    __secretCount = 0  # 私有变量
    publicCount = 0    # 公开变量
    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print self.__secretCount
    def count2(self):
        print self.__secretCount
cou = JustCounter()
try:
    cou.count()
    cou.count2()
except:
    print "error!HA"
