# -*- coding:utf-8 -*-

#--------------------------定义类-----------------------------
# class Student:
#     #__int__是一个特殊犯法用于创建对象时进行初始化操作
#     #通过这个方法我们可以为学生绑定name和age两个属性
    
#     def __init__(self,name, age):
#         self.name = name
#         self.age = age

#     def study(self,course_name):
#         print('%s正在通过学习%s之后' %(self.name, course_name))

#     #PEP 8要求标识符名字用全小雪多个下划线连接
#     #但是很多程序员和公司更倾向于使用驼峰命名法（驼峰标识）

#     def watch_av(self):
#         if self.age < 18:
#             print('%s只能看熊出没' %self.name)

#         else:
#             print('%s正在看爱情动作片' %self.name)




#--------------------------创建和使用对象-----------------------------

#当我们定义好一个类之后，可以通过下面的创建对象并给对象发消息

# def main():
#     test = Student('陈波',32)
#     test.study('数学')
#     test.watch_av()


# if __name__ == "__main__":
#     main()



# #--------------------------访问可见性-----------------------------
# """
# python中，属性和方法的访问权限只有两种，也就是公开的和私有的，如果向往属性是私有的
# 在给属性命名的时候可以用两个下划线（__xx__）作为开头
# """
# class Test:
#     def __init__(self, foo):
#         self.__foo = foo
#     def __bar(self):
#         print(self.__foo)
#         print('__bar')

# def main():
#     test = Test('hello')
#     test.__bar()
#     print(test.__foo)
#     """
#     Traceback (most recent call last):
#   File "object.py", line 61, in <module>
#     main()
#   File "object.py", line 57, in main
#     test.__bar()
#     AttributeError: Test instance has no attribute '__bar'
#     """

# if __name__ == "__main__":
#     main()

# """
# Python并没有从语法上严格保证私有属性或方法的私密性
# 它只是给私有的属性和方法换了一个名字来“妨碍”对它们的访问
# 事实上如果你知道更换名字的规则仍然可以访问到它们
# 下面的代码就可以验证这一点。之所以这样设定，可以用这样一句名言加以解释
# 就是“We are all consenting adults here”。因为绝大多数程序员都认为开放比封闭要好，而且程序员要自己为自己的行为负责。
# """

# class Test:
#     def __init__(self,foo):
#         self.__foo = foo

#     def __bar(self):
#         print(self.__foo)
#         print('__bar')

# def main():
#     test = Test('hello')
#     test._Test__bar()
#     print(test._Test__foo)

# if __name__ == "__main__":
#     main()


#--------------------------Practice-----------------------------

#--------------------------时钟-----------------------------
# import time

# class Clock(object):
#     """
#     数字时钟
#     """
#     def __init__(self, hour=0,minute = 0, second = 0):
#         """
#         构造器
#         """
#         self._hour = hour
#         self._minute = minute
#         self._second = second

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

#     def __str__(self):
#         """显示时间"""
#         return '%02d:%02d:%02d' % (self._hour,self._minute,self._second)

# def main():
#     clock = Clock(23,59,58)
#     while True:
#         print(clock)
#         time.sleep(1)
#         clock.run()

# if __name__ == "__main__":
#     main()

#--------------------------点与点之间的距离计算----------------------------

from math import sqrt

class Point(object):
    def __init__(self, x= 0, y=0):
        """
        构造器
        
        :param x: 横坐标
        :param y: 纵坐标
        """
        self.x = x
        self.y = y
    
    def move_to(self, x, y):
        #移动到指定位子
        self.x = x
        self.y = y

    def move_by(self, dx, dy):
        """
        移动指定的增量
        ：Parma dx : 横坐标的增量
        ：Parma dy : 纵坐标的增量n
        """
        self.x += dy
        self.y += dy

    def distance_to(self, other):
        """
        计算与另一个点的距离
        ：Parma other：另一个点
        """
        dx = self.x - other.x
        dy = self.y - other.y
        return sqrt(dx**2 + dy **2)
    def __str__(self):
        return '(%s,%s) ' % (str(self.x), str(self.y))


def main():
    p1 = Point(3,5)
    p2 = Point()
    print('p1==%s'% p1)
    print('p2==%s' %p2)

    p2.move_by(-1,2)
    print('p2move=%s',p2)
    print(p1.distance_to(p2))
if __name__ == "__main__":
    main()
