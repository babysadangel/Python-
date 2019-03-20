# -*- coding:utf-8 -*-

#------这个在python3下运行----------
# import tkinter
# import tkinter.messagebox


# def main():
# 	flag = True

# 	# 修改标签上的文字
# 	def change_label_text():
# 		nonlocal flag
# 		flag = not flag
# 		color, msg = ('red', 'Hello, world!')\
# 			if flag else ('blue', 'Goodbye, world!')
# 		label.config(text=msg, fg=color)

# 	# 确认退出
# 	def confirm_to_quit():
# 		if tkinter.messagebox.askokcancel('温馨提示', '确定要退出吗?'):
# 			top.quit()

# 	# 创建顶层窗口
# 	top = tkinter.Tk()
# 	# 设置窗口大小
# 	top.geometry('240x160')
# 	# 设置窗口标题
# 	top.title('小游戏')
# 	# 创建标签对象并添加到顶层窗口
# 	label = tkinter.Label(top, text='Hello, world!', font='Arial -32', fg='red')
# 	label.pack(expand=1)
# 	# 创建一个装按钮的容器
# 	panel = tkinter.Frame(top)
# 	# 创建按钮对象 指定添加到哪个容器中 通过command参数绑定事件回调函数
# 	button1 = tkinter.Button(panel, text='修改', command=change_label_text)
# 	button1.pack(side='left')
# 	button2 = tkinter.Button(panel, text='退出', command=confirm_to_quit)
# 	button2.pack(side='right')
# 	panel.pack(side='bottom')
# 	# 开启主事件循环
# 	tkinter.mainloop()


# if __name__ == '__main__':
# 	main()


# ------可以在python2下运行--------
# from Tkinter import *

# class Application(Frame):
#     def say_hi(self):
#         print "hi there, everyone!"

#     def createWidgets(self):
#         self.QUIT = Button(self)
#         self.QUIT["text"] = "QUIT"
#         self.QUIT["fg"]   = "red"
#         self.QUIT["command"] =  self.quit

#         self.QUIT.pack({"side": "left"})

#         self.hi_there = Button(self)
#         self.hi_there["text"] = "Hello",
#         self.hi_there["command"] = self.say_hi

#         self.hi_there.pack({"side": "left"})

#     def __init__(self, master=None):
#         Frame.__init__(self, master)
#         self.pack()
#         self.createWidgets()

# root = Tk()
# app = Application(master=root)
# app.mainloop()
# root.destroy()


#------------------------------------使用pygame进行游戏开发---------------

#制作游戏窗口

import pygame
import sys

def main():
    #初始化导入pygame中的模块
    pygame.init()
    #初始化用于显示的窗口并设置窗口尺寸的大小
    screen = pygame.display.set_mode((800, 600))
    #设置当前窗口的标题
    pygame.display.set_caption('大球吃小球')
    running = 1
    #开启一个时间循环处理发生的事件
    while running < 10:
        for event in pygame.event.get():
            if event.type == pygame.quit():
                # pygame.quit()
                running += 1       

if __name__ == "__main__":
    main()