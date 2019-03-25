# -*- coding:utf-8 -*-

#-----函数的使用方式
    #将函数视为‘一等公民’
    #函数可以赋值变量
    #函数可以作为函数的参数
    #函数可以作为函数的返回值

#----高阶函数用法（filter。ma破以及他们的替代品

item1 = list(map(lambda x : x **2, filter(lambda x : x % 2, range(1,10))))
print('item1:%s' %item1)
item2 = [x ** 2 for x in range(1, 10) if x % 2]
print('item2:%s' % item2)

#-----装饰器函数（使用装饰器和取消装饰器）

#输出函数执行时间的装饰器
# import time

# def record_time(func):
#     #自定义装饰函数的装饰器

#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         start = time()
#         result  =func(*args, **kwargs)
#         print(f'{func.__name__}: {time() - start}秒')
#         return result
    
#     return wrapper

#如果装饰器不希望分print函数耦合，可以编写贷参数的装饰器

# from functools import wraps
# from time import time

# def record(output):
#     #自定义带参数的装饰器

#     def decorate(func):

#         @wraps(func)
#         def wrapper(*args, **kwargs)
#         start = time()
#         result = func(*args, **kwargs)
#         output(func.__name__, time() - start)
#         return result
    
#     return decorate


# from functools import wraps
# from time import time

# class Recod():
#     """ 自定义装饰器类（通过__call__魔术方法似的对象可以当成函数调用）"""
#     def __init__(self, output):
#         self.output =  output
    
#     def __call__(self, func):

#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             start = time()
#             result = func(*args, **kwargs)
#             self.output(func.__name__, time() - start)
#             return result
        
#         return wrapper

#用装饰器来来实现单例模式

# from functools import wraps


# def singleton(cls):
#     #装饰器类的装饰器
#     isinstances = {}
#     locker = Lock()

#     @wraps(cls)
#     def wrapper(*args, **kwargs):
#         if cls not in isinstances:
#             with locker:
#                 if cls not in isinstances:
#                     isinstances[cls] = cls(*args, **kwargs)
#             return isinstances[cls]
        
#         return wrapper

# @singleton
# class President():
#     #总统单例类
#     pass


