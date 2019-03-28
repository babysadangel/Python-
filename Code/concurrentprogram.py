#-*- coding:utf-8 -*-
#------并发编程--------
""" 
python中实现并发编程三种方案：
多线程
多进程
异步I/O
并发编程的好处在于可以提升程序的执行效率以及改善用户体验
坏处在于并发的程序不容易开发和调试，同时对其他程序来说并不友好
"""

"""
多线程：python中提供了Thread类并以辅助Lock，Condition，Event，Semaphore和Barrier
Python中有GIL来防止多个线程同时执行本地字节码，这个锁对于CPython是必须的，因为CPython的内存管理并不是线程安全的。
因为GIL的存在多线程并不能发挥CPU的多核特性
"""

"""
面试进程与线程的区别和联系
进程：操作系统分配内存的基本单位-  一个进程可以包含一个或者多个线程
线程： 操作系统分配CPU的基本单位

"""
# import glob
# import os
# import threading

# from PIL import Image

# PREFIX = 'thumbnails'

# def generate_thumbanil(infile,size,format='PNG'):
#     #生成指定图片文件的缩略图
#     file, ext = os.path.splitext(infile)
#     file = file[file.rfind('/') + 1:]
#     outfile  =f'{PREFIX}/{file}_{size[0]}_{size[1]}.{ext}'
#     img = Image.open(infile)
#     img.thumbnails(size,Image.ANTIALIAS)
#     img.save(outfile, format)

# def main():
#     if not os.path.exists(PREFIX):
#         os.mkdir(PREFIX)
    
#     for infile in glob.glob('images/*.png'):
#         for size in (32, 64, 128):
#             #创建并启动线程
#             threading.Thread(
#                 target = generate_thumbanil,
#                 args= (infile,(size,size))
#             ).start()

# if __name__ == "__main__":
#     main()

#多个线程竞争资源的情况
"""
多线程程序如果没有竞争资源出来起来比较简单
当多个线程竞争临街资源的时候，如果缺乏必要的保护，就会导致数据错乱
说明：临界资源就是被多个线程竞争的资源
"""

# import time
# import threading

# from concurrent.futures import ThreadPoolExecutor

# class Account(object):
#     #银行账户
#     def __init__(self):
#         self.balance = 0.0
#         self.lock = threading.Lock()
    
#     def deposit(self, money):
#         #通过锁保护临界资源

#         with  self.lock:
#             new_balance = self.balance + money
#             time.sleep(0.001)
#             self.new_balance = new_balance

# class AddMoneyThread(threading.Thread):
#     #自定义线程类
#     def __init__(self, account, money):
#         self.account  = account
#         self.money = money
#         #自定义线程的初始化方法中必须调用父类的初始化方法
#         super().__init__()

#     def run(self):
#         #线程之后要执行的操作
#         self.account.deposit(self.money)

# def main():
#     account = Account()
#     #创建线程池
#     pool = ThreadPoolExecutor(max_workers=10)
#     futures= []
#     for _ in range(100):
#         #创建线程的第一种方式
#         # threading.Thread(
#         #     target=account.deposit,
#         #     args=(1,)
#         # ).start()

#         # #创建线程的第二种方式
#         # AddMoneyThread(account, 1).start()

#         #创建线程的第三种方式
#         #调用线程池中的线程来执行特定的任务
#         future  = pool.submit(account.deposit,1)
#         futures.append(future)
#     #关闭线程池
#     pool.shutdown()
#     for future in futures:
#         future.result()
#     print(account.balance)

# if __name__ == "__main__":
#     main()

#修改上面的程序，启动5个线程向账户中存钱，5分线程从账户中曲取钱，取钱时如果余额不足就暂停线程进行等待。
#为了达到目标，需要对存钱和取钱的线程进行调度，在余额不足时候取钱的线程暂停并释放锁，而存钱的线程将钱存入后要通知取钱的线程，从而从暂停状态被唤起
#可以使用threading模块Condition来实现线程调度，该对象也是基于锁来创建的
# """
# 多个线程竞争一个资源 --- 保护临界资源--锁（Lock/RLock）
# 多个线程竞争多个资源（线程数>资源数） --信号量（Semaphore）
# 多个线程的调度---暂停线程执行/唤醒等待中的线程--Condition

# """

# from concurrent.futures import ThreadPoolExecutor
# from random import randint
# from time import sleep
# import threading

# class Account():
#     #银行账户
#     def __init__(self, balance = 0):
#         self.balance = balance
#         lock = threading.Lock()
#         self.condition = threading.Condition(lock)

#     def withdraw(self, money):
#         #取钱
#         with self.condition:
#             while money > self.balance:
#                 self.condition.wait()
#             new_balance = self.new_balance - money
#             sleep(0.01)
#             self.balance = new_balance

#     def deposit(self, money):
#         #存钱
#         with self.condition:
#             new_balance = self.balance  + money
#             sleep(0.01)
#             self.balance =  new_balance
#             self.condition.notify_all()
    

# def add_money(account):
#     while True:
#         money = randint(5, 10)
#         account.deposit(money)
#         print(threading.current_thread().name,':' ,money, '======>',account.balance)
#         sleep(0.5)

# def sub_money(account):
#     while True:
#         money = randint(10, 30)
#         account.withdraw(money)
#         print(threading.current_thread().name, ':', money, '====>', account.balance)
#         sleep(1)

# def main():
#     account = Account()
#     with ThreadPoolExecutor(max_workers=10) as pool:
#         for _ in range(5):
#             pool.submit(add_money, account)
#             pool.submit(sub_money, account)

# if __name__ == "__main__":
#     main()


"""
多进程：
多进程可以有效解决GIL的问题，实现多进程主要的类是Process，其他辅助类跟threading模块中的类似
进程之间共享数据可以通过使用管道，套嵌字等
在multiproocess模块中有个Queue类，他基于管道和锁机制提供了多个进程共享的队列
如下官方文档示例：
"""

#多进程和进程池的使用，多线程因为GIL的存在不能够发挥CPU的多核特性，对于计算密集型应该考虑使用多进程

# import concurrent.futures
# import math

# PRIMES = [
#     1116281,
#     1297337,
#     104395303,
#     472882027,
#     533000389,
#     817504243,
#     982451653,
#     112272535095293,
#     112582705942171,
#     112272535095293,
#     115280095190773,
#     115797848077099,
#     1099726899285419
# ] * 5

# def is_prime(n):
#     #判断素数
#     if n % 2 == 0:
#         return False
    
#     sqrt_n = int(math.floor(math.sqrt(n)))
#     for i in range(3, sqrt_n + 1, 2):
#         if n % i == 0:
#             return False
#     return True

# def main():
#     with concurrent.futures.ProcessPoolExecutor() as executor:
#         for number, prime in zip(PRIMES, executor.map(is_prime,PRIMES)):
#             print('%d is prime: %s' % (number, prime))

# if __name__ == "__main__":
#     main()

"""
说明：多线程和多进程比较。
以下情况需要使用多线程：
a。程序需要维护许多共享的状态（尤其是可变状态）， Python中的列表、字典、集合都是线程安全的，所以
    使用线程而不是进程维护状态的代价相对较小
b。程序会花费大量的时间在I/O操作上，没有太多并行极端的需求且不占用太多的内存

以下情况需要使用多进程：
a。程序执行密集型人物（如：字节码操作、数据处理、科学计算）
b。程序的输入可以并行分成块，并且可以将计算结果合并。
c。程序内存使用方面没有任何限制且不强依赖I/O操作（如：读写文件，嵌套字等）

"""


#----------------------------------------------异步处理-------------------------------------------------------

# """
# 从调度程序的任务队列中挑选任务，该程序以交叉的形式执行这些任务
# 我们不能保证任务将以某种顺序去执行，因为执行顺序取决于队列中的一项任我是否愿意将CPU处理时间让位给另一项任务
# 异步任务通常通过多任务协作处理方式来实现
# 由于执行时间和顺序的不确定，因此需要通过回调试编程或者future对象来获取异步执行的结果
# Python3通过asyncio模块和await 和 async关键字来支持异步处理

# """
# #异步I/O-- async / await

# import asyncio

# def num_generator(m,n):
#     #指定范围的数字生成器
#     yield from range(m, n + 1)

# async def prime_filter(m, n):
#     #素数过滤器
#     primes = []
#     for i in num_generator(m, n):
#         flag = True
#         for j in range(2, int(i **0.5 + 1)):
#             if i % j == 0:
#                 flag = False
#                 break
            
#         if flag:
#             print('Prime ==>', i)
#             primes.append(i)
#         await asyncio.sleep(0.01)
#     return tuple(primes)

# async def square_mapper(m, n):
#     #平方映射器
#     squares = []
#     for i in num_generator(m, n):
#         print('Square =>', i * i)
#         squares.append(i * i)

#         await asyncio.sleep(0.001)
#     return squares

# def main():
#     loop  = asyncio.get_event_loop()
#     future = asyncio.gather(prime_filter(2, 100), square_mapper(1, 100))
#     future.add_done_callback(lambda x : print(x.result()))
#     loop.run_until_complete(future)
#     loop.close()

# if __name__ == "__main__":
#     main()
# # 说明：上面的代码使用get_event_loop函数获得系统默认的事件循环，通过gather函数可以获得一个
# # future对象，future对象的add_done_callback可以添加执行完成时的回调函数，loop对象的
# # run_until_complete方法可以等待通过future对象获得协程执行结果。

# Python中有一个名为aiohttp的三方库，他提供了一个异步的HTTP客户端和服务器，这三方库可以跟asyncio模块一起执行
#并提供对Future对象的支持。python3.6中引入了async和await来定义异步执行的函数以及创建异步上下文
#python3.7中他们正式成为关键字了

import asyncio
import re
import aiohttp

PATTERN = re.compile(r'\<title\>(?P<title>.*)\<\/title\>')

async def fentch_page(session,url):
    async with session.get(url, ssl=False) as resp:
        return await resp.text()

async def show_title(url):
    async with aiohttp.CalientSession() as session:
        html = await fentch_page(session, url)
        print (PATTERN.search(html).group('title'))
def main():
    urls = ('https://www.python.org/',
            'https://git-scm.com/',
            'https://www.jd.com/',
            'https://www.taobao.com/',
            'https://www.douban.com/')
    loop = asyncio.get_event_loop()
    task = [show_title(url) for url in urls]
    loop.run_until_complete(asyncio.wait(task))
    loop.close()
if __name__ == "__main__":
    main()
#说明：异步I/O与多进程比较
#当程序不需要真正的并发或者并行，而是更多依赖于异步处理和回调时，asyncico就是一种很好的选择。
#如果程序中有大量的等待和休眠时，也应该考虑asycio，他很适合编程写没有实时处理数据需求的Web应用服务器

