# -*- coding:utf-8 -*-

# """
# 之前我们讨论过Python中属性和方法访问权限的问题，虽然我们不建议将属性设置为私有的，
# 但是如果直接将属性暴露给外界也是有问题的，比如我们没有办法检查赋给属性的值是否有效。
# 我们之前的建议是将属性命名以单下划线开头，通过这种方式来暗示属性是受保护的，不建议外界直接访问
# 那么如果想访问属性可以通过属性的getter（访问器）和setter（修改器）方法进行对应的操作。
# 如果要做到这点，就可以考虑使用@property包装器来包装getter和setter方法，使得对属性的访问既安全又方便，代码如下所示。
# """
# class Person(object):
#     def __init__(self, name, age):
#         self._name = name
#         self._age = age

#     #访问器 ----getter方法
#     @property
#     def name(self):
#         return self._name

#     #访问器 ----getter方法
#     @property
#     def age(self):
#         return self._age

#     #修改器 ---settter方法
#     @age.setter
#     def age(self, age):
#         self._age = age

#     def play(self):
#         if self._age  <= 16:
#             print('%s在玩斗地主。%ld ,%ld' % (self._name, self.age, self._age))
#         else:
#             print('%s正在打游戏%ld ,%ld' % (self._name,self.age,self._age))


# def main():
#     person = Person('Lisa',18)
#     person.play()
#     person.age = 14
#     person.play()

# if __name__ == "__main__":
#     main()
    

# # ---------------------------------————__slots__魔法--------------------------

# class Person(object):
#     #限定person对象只能绑定_name,_age和_gender属性
#     __slots__ = ('_name','_age','_gender')

#     def __init__ (self, name, age):
#         self._name = name
#         self._age = age

#     @property
#     def name(self):
#         return self._name

#     @property
#     def age(self):
#         return self._age

#     @age.setter
#     def age(self, age):
#         self._age = age

#     def play(self):
#         if self._age <= 16:
#             print('%s 正在玩王者荣耀' % self._name)
#         else:
#             print('%s 正在玩LOL' % self._name)

# def main():
#     person = Person('Jason',22)
#     person.play()
#     person._gender =  'Man'
#     person.age = 12
#     person.play()


# if __name__ == "__main__":
#     main()

# ---------------------------------————静态方法和类方法--------------------------

# from math import sqrt

# class Triangle(object):
#     def __init__(self, a, b, c):
#         self._a = a
#         self._b = b
#         self._c = c
    
#     @staticmethod
#     def is_vaild(a, b, c):
#         return a + b > c and b + c > a and a + c > b

#     def perimeter(self):
#         return self._a + self._b + self._c

#     def area(self):
#         half = self.perimeter() / 2
#         return sqrt(half * (half - self._a) * (half - self._b) * (half - self._c))

# def main():
#     a ,b ,c  = 3,4,5

#     #静态方法和类方法都是通过给类发消息来调用的

#     if Triangle.is_vaild(a,b,c):
#         t = Triangle(a,b,c)
#         print(t.perimeter())
#         print(t.area())
#     else:
#         print('无法构成三角形')

# if __name__ == "__main__":
#     main()

# ---------------------------------————类方法--------------------------

# """
# 和静态方法比较，Python还可以在类中定义方法，类方法的第一个参数约定名为cls
# 他代表的是当前类相关的信息的对象（类本事也是一个对象，有的地方成为类为元数据对象）
# 通过这个参数我们可以获取和类相关的信息并且可以创建出类的对象
# """

# from time import time, localtime, sleep 

# class Clock(object):
#     #数字时钟
#     def __init__(self, hour = 0, minute = 0, second = 0):
#         self._hour = hour
#         self._minute = minute
#         self._second = second
    
#     @classmethod
#     def now(cls):
#         ctime = localtime(time())
#         return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)
    
#     def run(self):

#         self._second += 1
#         if self._second == 60:
#             self._second = 0
#             self._minute += 1
#             if self._minute == 60:
#                 self._minute = 0
#                 self._hour += 1
#                 if self._hour == 24:
#                     self._hour = 0
    
#     def show(self):
#         return '%02d:%02d:%02d' % (self._hour, self._minute, self._second)


# def main():
#     #通过类方法创建对象并获取系统时间
#     clock = Clock.now()
#     while True:
#         print(clock.show())
#         sleep(1)
#         clock.run()

# if __name__ == "__main__":
#     main()
    
 # ---------------------------------————继承和多态--------------------------
 
# class Person(object):
#     def  __init__(self, name, age):
#         self._name = name
#         self._age = age

#     @property
#     def name(self):
#         return self._name

#     @property
#     def age(self):
#         return self._age

#     @age.setter
#     def age(self,age):
#         self._age = age

#     def play(self):
#         print('%s正在玩LOL' % self._name)

#     def move(self):
#         if self._age >= 18:
#             print('%s可以自己出国旅游了' % self._name)
#         else:
#             print('%s 只能自己在家玩耍' % self._name)
    

# class Student(Person):
#     def __init__(self,name,age,grade):
#         super(Student,self).__init__(name,age)
#         self._grade = grade
    
#     @property 
#     def grade(self):
#         return self._grade

#     @grade.setter
#     def grade(self, grade):
#         self._grade = grade
    
#     def study(self, course):
#         print('%s的%s正在学习%s.' % (self._grade,self._name,course))

# class Teacher(Person):
#     def __init__(self,name,age,title):
#         super(Teacher,self).__init__(name, age)
#         self._title = title

#     @property
#     def title(self):
#         def title(self):
#             return self._title
#     @title.setter

#     def title(self,title):
#         self._title = title
    
#     def teach(self,course):
#         print('%s%s正在讲%s' % (self._name,self._title,course))

# def main():
#     stu  = Student('Jason',19,'三年级')
#     stu.study('数学')
#     stu.move()
#     t = Teacher('Jim',40,'开车')
#     t.teach('倒车入库')
#     t.move()



# if __name__ == "__main__":
#     main()

# ---------------------------------————子类继承父类方法后，可以改写父类，在不同的版本中实现--------------------------


# import six
# from abc import ABCMeta, abstractmethod
# @six.add_metaclass(ABCMeta)

# class Pet(object):
    
#     #宠物
#     def __init__(self,nickname):
#         self._nickname = self.nickname

#     @abstractmethod
#     def make_voice(self):
#         pass


# class Dog(Pet):
#     def make_voice(self):
#         print('%s :汪汪汪。。。' % self._nickname)

# class Cat(Pet):
#     def make_voice(self):
#         print('%s:喵喵喵。。。。' % self._nickname)

# def main():
#     pets = [Dog('旺财'), Cat('凯迪'), Dog('小黄')]
#     for pet in pets:
#         pet.make_voice()


# if __name__ == "__main__":
#     main()

#  ---------------------------------————综合练习，案例扑克游戏--------------------------

# import random

# class Card(object):
#     #一张牌
#     def __init__(self, suite, face):
#         self._suite = suite
#         self._face = face

#     @property 
#     def face(self):
#         return self._face
#     @property 
#     def suite(self):
#         return self._suite

#     def __str__(self):
#         if self._face == 1:
#             face_str = 'A'
#         elif self._face == 11:
#             face_str = 'J'
#         elif self._face == 12:
#             face_str  = 'Q'
#         elif self._face == 13:
#             face_str = 'K'
#         else:
#             face_str = str(self._face)
        
#         return '%s%s' % (self._suite, face_str)

#     def __repr__(self):
#         return self.__str__()

# class Poker(object):
#     #一副牌
#     def __init__(self):
#         self._cards = [Card(suite,face)
#                        for suite in '♠♥♣♦'
#                        for face in  range(1, 14) ]
#         self._current = 0

    
#     @property
#     def cards(self):
#         return self._cards

#     def shuffle(self):
#         #洗牌
#         self._current  =0
#         random.shuffle(self._cards)
    
#     @property
#     def next(self):
#         #发牌
#         card = self._cards[self._current]
#         self._current += 1
#         return card

#     @property
#     def has_next(self):
#         #还没有牌
#         return self._current < len(self._cards)


# class Player(object):
#     #玩家
#     def __init__(self, name):
#         self._name = name
#         self._cards_on_hand = []
    
#     @property
#     def name(self):
#         return self._name

#     @property
#     def cards_on_hand(self):
#         return self._cards_on_hand
    
#     def get(self, card):
#         #摸牌
#         self._cards_on_hand.append(card)
    
#     def arrange(self, card_key):
#         #玩家整理手上牌
#         self._cards_on_hand.sort(key=card_key)

# #排序规则--先按照花色再根据点数进行排序
# def get_key(card):
#     return (card.suite, card.face)

# def main():
#     p  = Poker()
#     p.shuffle()
#     players = [Player('东邪') ,Player('吸毒'), Player('南帝'), Player('北丐')]
#     for _ in range(3):
#         for player in players:
#             print('%s:' %player.name)
#             player.arrange(get_key)
#             print(player.cards_on_hand)

# if __name__ == "__main__":
#     main()

#------------------------------------------------工作结算系统---------------------------------------------------------
"""
某公司有三种类型的员工 分别是部门经理、程序员和销售员
需要设计一个工资结算系统 根据提供的员工信息来计算月薪
部门经理的月薪是每月固定15000元
程序员的月薪按本月工作时间计算 每小时150元
销售员的月薪是1200元的底薪加上销售额5%的提成
"""

from abc import ABCMeta, abstractmethod
import six

class Employee(six.with_metaclass(ABCMeta,object)):
    #员工
    def __init__(self, name):
        #初始化方法
        self._name = name

    @property
    def name(self):
        return self._name

    @abstractmethod
    def get_salary(self):
        #获得月薪
        pass

class Manager(Employee):
    #部门经理
    def get_salary(self):
        return 15000.00


class Programmmer(Employee):
    def __init__(self,name,working_hour = 0):
        super(Programmmer ,self).__init__(name)
        self._working_hour = working_hour
    
    @property
    def working_hour(self):
        return self._working_hour
    
    @working_hour.setter
    def working_hour(self, working_hour):
        self._working_hour = working_hour if working_hour > 0 else 0
    
    def get_salary(self):
        return 150.0* self._working_hour

class SalesMan(Employee):
    #销售员
    def __init__(self,name,sales=0):
        super(SalesMan, self).__init__(name)
        self._sales = sales

    @property
    def sales(self):
         return self._sales

    @sales.setter
    def sales(self, sales):
        self._sales = sales if sales > 0 else 0

    def get_salary(self):
        return 1200.0 + self._sales*0.05


def main():
    emps = [Manager('刘备'), Programmmer('张飞'), Manager('关羽'), SalesMan('荀彧'), SalesMan('吕布'), Programmmer('张辽'), Programmmer('赵云')]

    for emp in emps:
        if isinstance(emp,Programmmer):
            emp.working_hour = int(input('请输入%s本月工作的时间：' %emp.name))
        elif isinstance(emp,SalesMan):
            emp.sales = float(input('请输入%s本月销售额'% emp.name))
        
        #同样是接受get_salary这个消息但是不同的员工表现出了不同行为（多态）
        print('%s本月工资为¥：%s 元' % (emp.name, emp.get_salary()))

if __name__ == "__main__":
    main()


    
