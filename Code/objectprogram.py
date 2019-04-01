# -*- coding: utf-8 -*-

""" 面向对象编程，封装，继承，多态 """

# #工资计算系统

# from abc import ABCMeta,abstractmethod

# class Employee(metaclass = ABCMeta):
#     #员工抽象类
#     def __init__(self, name):
#         self.name = name
    
#     @abstractmethod
#     def get_salary(self):
#         #结算月薪抽象方法
#         pass

# class Manager(Employee):

#     def get_salary(self):
#         return 15000.0

# class Programmer(Employee):

#     def __init__(self, name, working_hour = 0):
#         self.working_hour = working_hour
#         super().__init__(name)
    
#     def get_salary(self):
#         return 200* self.working_hour
    
# class Saleman(Employee):
#     #销售员
#     def __init__(self, name,sales = 0.0):
#         self.sales = sales
#         super().__init__(name)

    
#     def get_salary(self):
#         return 1800.0 + self.sales *0.05

# class EmployeeFactory():
#     """创建员工的工厂（工厂模式--通过工厂实现对象使用者和对象之间的解耦合）"""
#     @staticmethod
#     def create(emp_type, *args , **kwargs):
#         emp_type = emp_type.upper()
#         emp = None
#         if emp_type == 'M':
#             emp = Manager(*args, **kwargs)
#         elif emp_type == 'P':
#             emp = Programmer(*args, **kwargs)
#         elif emp_type == 'S':
#             emp = Saleman(*args , **kwargs)
#         return emp

# def main():
#     #主函数
#     emps = [
#         EmployeeFactory.create('M','Qun'),
#         EmployeeFactory.create('P','Wan',120),
#         EmployeeFactory.create('P','Niu', 85),
#         EmployeeFactory.create('S','Song',123000),
#     ]
#     for emp in emps:
#         print('%s:%.2f元' % (emp.name,emp.get_salary()))

# if __name__ == "__main__":
#     main()

# 混入（Mixin）
# 示例：自定义字典限制只有在指定的key不存在时才能在字典中设置键值对

# class SetOnceMappingMixin():
#     #自定义混入类
#     __slots__ = ()

#     def __setitem__(self, key, value):
#         if key in self:
#             raise KeyError(str(key) + ' already set')
#         return super().__setitem__(key,value)

# class SetOnceDict(SetOnceMappingMixin, dict):
#     #自定义字典
#     pass

# my_dict = SetOnceDict()
# try:
#     my_dict['username'] = 'Jason'
#     my_dict['username'] = 'Bron'
# except KeyError:
#     pass
# print(my_dict)

#------元编程和元类-------------

#用元类实现单例模式
import threading

class SingletonMeta(type):
    #自定义元类
    def __init__(cls, *args, **kwargs):
        cls.__instance = None
        cls.__lock  =threading.Lock()
        super().__init__(*args, **kwargs)
    
    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            with cls.__lock:
                if cls.__instance is None:
                    cls.__instance = super().__call__(*args, **kwargs)
        return cls.__instance

class Present(metaclass = SingletonMeta):
    pass