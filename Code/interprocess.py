
# -*- coding:utf-8 -*-

# from random import randint
# from time import time,sleep


# def download_task(filename):
#     print('开始下载%s...' %filename)

#     time_to_download  = randint(5,10)

#     sleep(time_to_download)

#     print('%s下载完成！耗费%d秒' % (filename,time_to_download))


# def main():
#     start = time()
#     download_task('python从入门到放弃.pdf')
#     download_task('peking Hot.rmvb')
#     end = time()

#     print('一共花费了%.2f秒' %(end - start))

# if __name__ == "__main__":
#     main()


#开启多进程方式去下载

# from multiprocessing import process
# from os import getpid
# from random import randint
# from time import time ,sleep

# def download_task(filename):
#     print('启动下载进程，进程号【%d】' % getpid())
#     print('开始下载%s...' %filename)

#     time_to_download = randint(5,10)
#     sleep(time_to_download)
#     print('%s下载完成！耗费%d秒' %(filename, time_to_download))

# def main():
#     start = time()
#     p1 = Process(target = download_task,args=('python从入门到放弃',))
#     p1.start()
#     p2 = Process(target = download_task,args = ('如来神掌。avi',))
#     p2.start()
#     p1.join()
#     p2.join()
#     end  = time()

#     print('一共花费时间%.2f秒' % (end - start))

# if __name__ == "__main__":
#     main()

#两个进程间的通信

# from multiprocessing import Process
# from time import sleep

# counter = 0 
# def sub_task(string):
#     global counter
#     while counter < 10:
#         print(string,end='',flush = True)
#         counter += 1
#         sleep(0.01)

# def main():
#     Process(target = sub_task, args = ('Ping'),).start()
#     Process(target = sub_task,args = ('Pong',)).start()

# if __name__ == "__main__":
#     main()

#-------------------------------python中的多线程----------------------------------------------------

# from random import randint
# from threading import Thread
# from time import time, sleep

# def download(filename):
#     print('开始下载%s...' % filename)
#     time_to_download = randint(5,10)
#     sleep(time_to_download)
#     print('%s下载完成！耗费%d秒' % (filename,time_to_download))


# def main():
#     start = time()
#     t1 = Thread(target = download,args = ('Python从入门到放弃',))
#     t1.start()
#     t2 = Thread(target  =download,args=('如来神掌。txt',))
#     t2.start()
#     t1.join()
#     t2.join()
#     end = time()

#     print('总共花费%.3f秒' %(end - start))


# if __name__ == "__main__":
#     main()

#-------------------------------通过继承实现python中的多线程----------------------------------------------------、
# from random import randint
# from threading import Thread
# from time import sleep,time

# class DownloadTask(Thread):
#     def __init__(self, filename):
#         super().__init__()
#         self._filename = filename

#     def run(self):
#         print('开始下载%s。。。。' % self._filename)
#         time_to_download = randint(5,10)
#         sleep(time_to_download)
#         print('%s下载完成。耗费%d秒' %(self._filename,time_to_download))


# def main():
#     start = time()
#     t1 = DownloadTask('从入门到删库跑路')
#     t1.start()
#     t2 = DownloadTask('如来神掌。rmvb')
#     t2.start()
#     t1.join()
#     t2.join()
#     end = time()
#     print('总共耗费了%.2f秒' % (end - start))

# if __name__ == "__main__":
#     main()


# #---------------在这个例子中，银行账户就是一个临界资源，在没有保护的情况下我们很有可能会得到错误的结果和加锁之后---------

# from time import sleep
# from threading import Thread, Lock

# class Account(object):
#     def __init__(self):
#         self._balance = 0
#         self._lock = Lock()
    
#     def deposit(self, money):
#         #先取锁才能执行后续的代码
#         self._lock.acquire()
        
#         try:
#             #计算存款后的余额
#             new_balance = self._balance + money
#         #模拟受力存款业务需要0.01秒
#             sleep(0.01)
#         #修改账户余额
#             self._balance = new_balance
#         finally:
#             #在finally中执行释放锁的操作保证异常锁都能释放
#             self._lock.release()

        

#     @property
#     def balance(self):
#         return self._balance


# class AddMoneyThread(Thread):

#     def __init__(self, account, money):
#         super().__init__()
#         self._account = account
#         self._money = money
    
#     def run(self):
#         self._account.deposit(self._money)


# def main():
#     account = Account()
#     threads = []

#     #创建100个存款的线程向同一个账户中存钱
#     for _ in range(100):
#         t = AddMoneyThread(account, 1)
#         threads.append(t)
#         t.start()
#     #等所有存款的线程都执行完毕
#     for t in threads:
#         t.join()
#     print('账户余额为：%d元'% account.balance)

# if __name__ == "__main__":
#     main()
        
#------------------------------------将耗时间的任务放到线程中以获得更好的用户体验---------------------------------------------
# import time
# import tkinter
# import tkinter.messagebox

# def download():
#     #模拟下载任务需要花费的10秒时间
#     time.sleep(10)
#     tkinter.messagebox.showinfo('提示', '下载完成')

# def show_about():
#     tkinter.messagebox.showinfo('关于', 'Python的官网')

# def main():
#     top = tkinter.Tk()
#     top.title('单线程')
#     top.wm_attributes('-topmost', True)

#     panel = tkinter.Frame(top)
#     button1 = tkinter.Button(panel,text = '下载', command = download)
#     button1.pack(side = 'left')
#     button2 = tkinter.Button(panel, text = '关于', command = show_about)
#     button2.pack(side = 'right')

#     panel.pack(side = 'bottom')

#     tkinter.mainloop()
# if __name__ == "__main__":
#     main()

#---------如果使用多线程将耗时间的任务放到一个独立的线程中执行，这样就不会因为执行耗时间的任务而阻塞了主线程-------

# import time
# import tkinter
# import tkinter.messagebox
# from threading import Thread

# def main():
#     class DownloadTaskHandler(Thread):

#         def run(self):
#             time.sleep(5)
#             tkinter.messagebox.showinfo('提示','下载完成')
#             #启用下载按钮
#             button1.config(state = tkinter.NORMAL)

    
#     def download():
#         #禁用下载按钮
#         button1.config(state = tkinter.DISABLED)

#         #通过dameon参数将线程设置为守护线程（主线程退出就不再保留执行）
#         #在线程中处理耗时的下载任务
#         DownloadTaskHandler(daemon=True).start()

#     def show_about():
#         tkinter.messagebox.showinfo('关于','Python官方网站')


#     top = tkinter.Tk()
#     top.title('单线程')
#     top.geometry('300x500')
#     top.wm_attributes('-topmost',1)

#     panel = tkinter.Frame(top)
#     button1 = tkinter.Button(panel,text='下载',command = download)
#     button1.pack(side = 'left')
#     button2 = tkinter.Button(panel, text = '关于', command = show_about)
#     button2.pack(side = 'right')
#     panel.pack(side = 'bottom')

#     tkinter.mainloop()

# if __name__ == "__main__":
#     main()

#--------使用多线程对复杂任务进行‘分而治之’，1~100000000求和的计算密集型任务-------

# from time import time

# def main():
#     total = 0
#     number_list = [x for x in range(1,100000001)]
#     start = time()
#     for number in number_list:
#         total = total + number
#     print('total=%d' % total)
#     end = time()

#     print('一共耗时%.2f秒' % (end - start))

# if __name__ == "__main__":
#     main()

#使用多线程处理之后如下

from multiprocessing import Process, Queue
from random import randint
from time import time

def task_handler(curr_list, result_queue):
    total = 0
    for nummber in curr_list:
        total += nummber
    result_queue.put(total)

def main():
    processes = []
    number_list = [x for x in range(1, 100000001)]
    result_queue = Queue()
    index = 0
    #启动8个进程将数据切片后进行计算
    for _ in range(8):
        p = Process(target = task_handler,args = (number_list[index:index + 12500000],result_queue))
        index += 12500000
        processes.append(p)
        p.start()
    
    #开始记录所有进程执行完之后花费的时间
    start = time()
    for p in processes:
        p.join()
    #合并执行的结果
    total = 0

    while not result_queue.empty():
        total += result_queue.get()
    print('total=%d',total)

    end = time()
    print('一共耗时%.2f秒' % (end - start))

if __name__ == "__main__":
    main()

