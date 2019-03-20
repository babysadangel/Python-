# -*- coding:utf-8 -*-

# def main():
#     f = None
#     try:
#         f = open('test.txt','r',encoding='uft-8')
#         print(f.read)
#     except  FileNotFoundError:
#         print('无法打开指定文件')
#     except LookupError:
#         print('指定了未知编码')
#     finally:
#         if f:
#             f.close()


# if __name__ == "__main__":
#     main()


#--除了使用文件对象的read方法读取文件之外，还可以使用for-in循环逐行读取或者用readlines方法将文件按行读取到一个列表容器中，
# import time

# def main():
#     #一次性读取整个文件的内容
#     with open('text.txt','r',encoding='utf-8') as f:
#         # print(f.read)
#     #利用for-in 循环进行逐行读取
#     with open('text.txt',mode='r') as f:
#         for line in f:
#             print(line,end='')
#     print()

#     #读取文件按行到列表中
#     with open('text.txt') as f:
#         lines = f.readline()
#     print(lines)

# if __name__ == "__main__":
#     main()

#  写入文件
# from math import sqrt

# def is_prime(n):
#     #判断素数的函数
#     assert n > 0
#     for factor in range(2, int(sqrt(n)) + 1):
#         if n % factor == 0:
#             return False
    
#     return True if n != 1 else False

# def main():
#     filenames = ('a.txt','b.txt','c.txt')
#     fs_list = []

#     try:
#         for filename in filenames:
#             fs_list.append(open(filename,'w',encoding='utf-8'))

#         for number in range(1,10000):
#             if is_prime(number):
#                 if number < 100:
#                     fs_list[0].write(str(number) + '\n')
#                 elif number < 1000:
#                     fs_list[1].write(str(number) + '\n')
#                 else:
#                     fs_list[2].write(str(number) + '\n')

#     except IOError as ex:

#         print(ex)
#         print('写文件的时候错误')
        
#     finally:
#         for fs in fs_list:
#             fs.close()
#     print('操作完成！')

# if __name__ == "__main__":
#     main()

#------读写二进制，赋值图片功能------

# def main():
#     try:
#         with open('666.jpg','rb') as fs1:
#             data = fs1.read()
#             print(type(data))
        
#         with open('888.jpg','wb') as fs2:
#             fs2.write(data)
            
#     except FileNotFoundError   as e:

#         print('无法打开指定文件')
#     except IOError as e:
#         print('读写文件时候出现错误')
#     print('程序执行结束')

# if __name__ == "__main__":
#     main()

#-------保存二进制文件---------

# import json

# def main():
#     mydict = {
#         'name': 'Lisa',
#         'age' : 14,
#         'qq' : 14792472425,
#         'cards' :[
#             {'brand':'HIN','mac':'rw'},
#             {'brand': 'IJH','mac':'jd'}
#         ]
#     }

#     try:
#         with open('data.json','w',encoding='utf-8') as fs:
#             json.dump(mydict,fs)
#     except IOError as identifier:
#         print(identifier)
#     print('数据保存完成')

# if __name__ == "__main__":
#     main()

# import requests
# import json
# import urllib3

# def main():
#     resp = requests.get('http://api.tianapi.com/guonei/?key=APIKey&num=10')
#     data_mode = json.loads(resp.text)
#     for news  in data_mode['newslist']:
#         print(news['title'])

# if __name__ == "__main__":
#     main()

import requests
import json


def main():
    resp = requests.get('http://api.tianapi.com/guonei/?key=APIKey&num=10')
    data_model = json.loads(resp.text)
    print(data_model)
    for news in data_model['newslist']:
        print(news['title'])

if __name__ == '__main__':
    main()