# -*- coding:utf-8 -*-

# from socket import socket, SOCK_STREAM, AF_INET
# from datetime import datetime

# def main():
#     #1。创建套接字对象并制定是哪种传输服务
#     #family = AF_INET ---IPv4地址
#     #family = AF_INET6 ---IPv6地址
#     #type = SOCK_STREAM  -  TCP套接字
#     #type = SOCK_DGRAM  ---UDP套接字
#     #type = SCOK_RAW  ---原始套接字

#     sever = socket(family= AF_INET, type= SOCK_STREAM)
#     #2、绑定IP地址和端口（端口用于区别不同的服务）
#     #同一时间在一个端口上只能绑定一个服务器，否则报错
#     sever.bind(('192.168.1.20', 9999))

#     #3.开启监听--监听客户端连接到服务器
#     #参数可以理解为队列的大小
#     sever.listen(512)
#     print('服务器启动开始监听')

#     while True:
#         #4.通过循环接受客户端的连接并作出相应的处理（提供服务）
#         #accept方法是一个阻塞方法，如果客户端连接到服务器代码不会向下执行
#         #accept方法返回一个元组，其中的第一个元素是客户端对象
#         #第二个元素是连接到服务器的客户端地址（由IP地址和端口两部分构成）
#         client, addr = sever.accept()
#         print(str(addr) + '连接到了服务器')

#         #5、发送数据
#         client.send(str(datetime.now())).encode('utf-8')

#         #6.断开连接
#         client.close()

# if __name__ == "__main__":
#     main()

#-------通过Python来实现TCP客户端的功能-----------

# ###服务端代码
# from socket import socket
# from base64 import b64encode
# from json import dumps
# from threading import Thread

# def main():
#     #1/自定义线程类
#     class FileTransferHandler(Thread):
        
#         def __init__(self, cclient):
#             super().__init__()
#             self.cclient = cclient

#         def run(self):
#             my_dict = {}
#             my_dict['filename'] = 'av.jpj'
#             #json纯文本不能带二进制数据
#             #所以图片的二进制数据要处理成base64编码

#             my_dict['filedata'] = data
#             #通过dumps函数将字段处理成json字符串
#             json_str = dumps(my_dict)
#             #发送json字符串
#             self.cclient.send(json_str.encode('utf-8'))
#             self.cclient.close()

    
#     #1.创建套接字对象并制定使用哪种传输服务
#     server = socket()

#     #2/绑定IP地址和端口（区分不同的服务）
#     server.bind(('192.168.1.2',5566))

#     #3.开启监听--监听客户端连接到服务器
#     server.listen(512)
#     print('服务器启动开始监听。。。')
    
#     with open('av.jpg','rb') as f:
#         #将二进制数据处理成base64再解码成字符串
#         data = b64encode(f.read()).decode('utf-8')

#     while True:
#         client , addr = server.accept()
#         #启动一个线程来处理客户端的请求
#         FileTransferHandler(client).start()


# if __name__ == "__main__":
#     main()


# ####客户端代码

# from socket import socket
# from json import loads
# from base64 import b64decode

# def main():
#     client = socket()
#     client.connect(('192.168.1.1', 5566))

#     #定义一个保存二进制数据的对象
#     in_data = bytes()
#     #由于不知道服务器发送方的数据有多大每次接受1024字节
#     data = client.recv(1024)

#     while data:
#         #将受到的数据拼接起来
#         in_data += data
#         data = client.recv(1024)
    
#     #将收到的二进制数据解码成json字符串并拼接成字典
#     #loads函数的作用就是讲json字符串转换成字段对象

#     my_dict = loads(in_data.decode('utf-8'))
#     filename = my_dict['filename']
#     filedata = my_dict['filedata'].encode('utf-8')

#     with open('/Users/administrator/Desktop' + filename, 'wb') as f:
#         #讲base64格式的数据解码成二进制数据并写入文件
#         f.write(b64decode(filedata))
#     print('图片已经保存')

# if __name__ == "__main__":
#     main()

# ------------------------------发送电子邮件-------------------------------------------

# from smtplib import SMTP
# from email.header import Header
# from email.mime.text import MIMEText

# def main():
#     sender = 'mrkingyuanwang@163.com'
#     receives = ['7252643013@qq.com','yuankisstherain@163.com']
#     message = MIMEText('用Python发送邮件代码示例', 'plain', 'utf-8')
#     message['From'] = Header('Lisa', 'utf-8')
#     message['To'] = Header('Jason', 'utf-8')
#     message['Subject'] = Header('示例代码实验邮件', 'utf-8')
#     smtper = SMTP('smtp.126.com')

#     smtper.login(sender, '@loveyou66#')
#     smtper.sendmail(sender, receives, message.as_string())
#     print('邮件发送完成')

# if __name__ == "__main__":
#     main()

# # ----如果要发送带有附件的邮件--------
# from smtplib import SMTP
# from email.header  import Header
# from email.mime.text  import MIMEText
# from email.mime.image import MIMEImage
# from email.mime.multipart import MIMEMultipart
# import urllib

# def main():
#     #创建一个带附件的邮件消息对象
#     message = MIMEMultipart()

#     #创建文本内容
#     text_content = MIMEText('附件中有本月数据请查收', 'plain','utf-8')
#     message['Subject'] = Header('本月数据', 'utf-8')
#     #将文本内容添加到邮件消息对象中
#     message.attach(text_content)

#     #读取文件并将文件作为附件添加到邮件消息对象中
#     with open('/Users/administrator/Desktop/helloworld.txt', 'rb') as f:
#         txt = MIMEText(f.read(), 'base64', 'utg-8')
#         txt['Content-Type'] = 'text/plain'
#         txt['Content-Disposition'] = 'attachment; filename=helloword.txt'
#         message.attach(txt)
#     #读取文件并将文件作为附件添加到邮件消息对象中
#     with open('/Users/administrator/Desktop/历史数据.xlsx','rb') as f:
#         xls = MIMEText(f.read(),'base64','utf-8')
#         xls['Content-Type'] = 'application/vnd.ms-excel'
#         xls['Content-Disposition'] = 'attachment; filename=month-data.xlsx'
#         message.attach(xls)

#     #创建SMTP对象
#     smtper = SMTP('smtp.126.com')
#     #开启安全连接
#     smtper.starttls()
#     sender = '752643013@qq.com'
#     receivers = ['yuankisstherain@163.com']
#     #登录到SMTP服务器
#     smtper.login(sender,'secretpass')
#     #发送邮件
#     smtper.sendmail(sender, receivers,message.as_string())
#     #与邮件服务器断开连接
#     smtper.quit()
#     print('发送完成')

# if __name__ == "__main__":
#     main()


#-----------------------------------发送短信----------------------------------

import urllib.parse
import http.client
import json

def main():
    host = '106.ihuyi.com'
    sms_send_uri = '/webservice/sms.php?method=Submit'
    params = urllib.parse.urlencode({'account':'jsaon','password':'123456'})
    print('param: %s' %params)

    headers = {'Content-type' : 'application/x-www-form-urlencode','Accept':'text/plain'}
    conn = http.client.HTTPConnection(host,port=80,timeout=30)
    conn.request('POST',sms_send_uri,params,headers)
    response = conn.getresponse()
    response_str = response.read()
    jsonstr = response_str.decode('utf-8')
    print(json.loads(jsonstr))
    conn.close()

if __name__ == "__main__":
    main()