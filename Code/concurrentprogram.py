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
import glob
import os
import threading

from PIL import Image

PREFIX = 'thumbnails'

def generate_thumbanil(infile,size,format='PNG'):
    #生成指定图片文件的缩略图
    file, ext = os.path.splitext(infile)
    file = file[file.rfind('/') + 1:]
    outfile  =f'{PREFIX}/{file}_{size[0]}_{size[1]}.{ext}'
    img = Image.open(infile)
    img.thumbnails(size,Image.ANTIALIAS)
    img.save(outfile, format)

def main():
    if not os.path.exists(PREFIX):
        os.mkdir(PREFIX)
    
    for infile in glob.glob('images/*.png'):
        for size in (32, 64, 128):
            #创建并启动线程
            threading.Thread(
                target = generate_thumbanil,
                args= (infile,(size,size))
            ).start()

if __name__ == "__main__":
    main()