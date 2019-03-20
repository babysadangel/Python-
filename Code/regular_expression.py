# -*- coding:utf-8 -*- 

#-----------------------------------验证输入用户名和QQ号是否有效 并给出对应的提示------------------------------------------------

# """
# 要求：
# 用户名必须由字幕和数字，或者下划线构成且长度在6~20个字符之间
# QQ号是5~12的数字且首位不能为0
# """
# import re

# def main():
#     username = input('请输入用户名：')
#     qq = input('请输入QQ号')
#     #match函数的第一个参数是正则表达式字符串或者正则表达式对象
#     #第二个参数是要跟正则表达式做匹配的字符串对象
#     m1 = re.match(r'^[0-9a-zA-Z_]{6,20}$',username)

#     if not m1:
#         print('请输入有效用户名')
    
#     m2 = re.match(r'^[1-9]\d{4,11}$',qq)
    
#     if not m2:
#         print('请输入有效QQ号')
    
#     if m1 and m2:
#         print('登录成功')

# if __name__ == "__main__":
#     main()



#-----------------------------------从一段文字提取国内手机号码------------------------------------------------

# import re

# def main():
#     #创建正则表达式对象， 使用前瞻和回顾来保证手机号前后不应该出现数字

#     pattern = re.compile(r'(?<=\D)1[34578]\d{9}(?=\D)')
#     sentence = '''
#     重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，
#     不是15600998765，也是110或119，王大锤的手机号才是15600998765。
#     '''

#     #查找所有匹配并保存到一个列表中
    
#     mylist = re.findall(pattern,sentence)

#     print(mylist)

#     print('---------------------')

#     #通过迭代器取出匹配对象并获得匹配的内容

#     for temp in pattern.findall(sentence):
#         print(temp)

#     print('--------------------')

#     #通过search函数指定搜索位子找出多有匹配

#     m = pattern.search(sentence)

#     while m:
#         print(m)
#         m = pattern.search(sentence, m.end())

# if __name__ == "__main__":
#     main()

#-----------------------------------替换字符串中的不良内容------------------------------------------------

# import re

# def main():

#     sentence = '你丫是傻叉吗? 我操你大爷的. Fuck you.'
#     purified = re.sub('[操艹草曹]|fuck|shit|傻[比逼叉缺吊屌]|煞笔','*',sentence, flags = re.IGNORECASE)
#     print(purified)

# if __name__ == "__main__":
#     main()

#-----------------------------------拆分长字符串------------------------------------------------

import re

def main():
    poem = '窗前明月光，疑是地上霜。举头望明月，低头思故乡。'

    sentence_list = re.split(r'[,。，.]',poem)
    while '*' in sentence_list:
        sentence_list.remove('*')
    print(sentence_list)

if __name__ == "__main__":
    main()