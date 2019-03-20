# -*- coding: utf-8 -*-

# -------------**-----------------水仙花数-----------------------**-----------------------------

#方法一；

# for x in range(100,1000):
    
#     one =  int(str(x)[0])
#     two =  int(str(x)[1])
#     three = int(str(x)[2])
#     a = one ** 3 + two ** 3 + three ** 3
#     if a == x:
#         print(x)
    
# 方法二

# def narcissistic_number_2(num): 
    
#     original_num = num 
     
#     s = str(original_num)    
     
#     length = len(s)    
     
#     count = length    
     
#     sum_num = 0    
     
#     while count:        
         
#         sum_num += int(s[count - 1]) ** length        
         
#         count -= 1    
#     else:       
         
#         if sum_num == num:           
            
#             print("%d is a %d bit narcissistic_number" % (num, length))
         
#         else:            
#              pass
#             # print("%d is not a narcissistic_number" % num)
             
# max_num = int(input('请输入最大范围'))
 
# # 获取小于指定数的阿姆斯特朗数
 
# for num in range(0, max_num):
 
#     narcissistic_number_2(num)        #调用方法一,方法二均可



# -------------**-----------------寻找“完美数”。-----------------------**-----------------------------

# import math
# import time
# # def search_perfect_num(nums):

# start = time.clock()
# for num in range(1,10000):
#     sum = 0
#     # print('num %s'% num)
#     for factor in range(1,int(math.sqrt(num)) + 1):
#         # print(factor)
#             if num %factor == 0:
#                 sum += factor
#                 if factor > 1 and num /factor != factor:
#                     sum += num/factor
#     if sum == num:
#         print(num)
# end = time.clock()
# print('执行时间：',(end - start),"秒")

# -------------**-----------------百钱百🐔问题-----------------------**-----------------------------
import math

# for i in range(0,20):
#     for x in range(0,100-i):
#         z = (100 - i - x)/3
#         if z%2 == 0:
#             j = i * 5 + x*3 + (100 - i - x)/3
#             if j == 100:
#                   print i ,x , 100 - i - x
           
# for x in range(1,20):
#     for y in range(1,33):
#         z = 100 - x - y
#         if x*5 + y*3 + z/3 == 100:
#             print '公鸡 %d ,母鸡 %d 小鸡%d' %(x,y,z)

# for x in range(0, 20):
# 	for y in range(0, 33):
# 		z = 100 - x - y
# 		if 5 * x + 3 * y + z / 3 == 100:
# 			print('公鸡: %d只, 母鸡: %d只, 小鸡: %d只' % (x, y, z))

# -------------**-----------------斐波那切数列-----------------------**-----------------------------


# a = 0
# b = 1
# for _ in range(5):
# 	(a, b) = (b, a + b)
# 	# print((a, b))


# -------------**-----------------Craps赌博游戏-----------------------**-----------------------------

 
# Craps赌博游戏
# 玩家摇两颗色子 如果第一次摇出7点或11点 玩家胜
# 如果摇出2点 3点 12点 庄家胜 其他情况游戏继续
# 玩家再次要色子 如果摇出7点 庄家胜
# 如果摇出第一次摇的点数 玩家胜
# 否则游戏继续 玩家继续摇色子
# 玩家进入游戏时有1000元的赌注 全部输光游戏结束


# from random import randint

# money = 10
# while money > 0:
# 	print('你的总资产为:', money)
# 	needs_go_on = False
# 	while True:
# 		debt = int(input('请下注: '))
# 		if debt > 0 and debt <= money:
# 			break
# 	first = randint(1, 6) + randint(1, 6)
# 	print('玩家摇出了%d点' % first)
# 	if first == 7 or first == 11:
# 		print('玩家胜!')
# 		money += debt
# 	elif first == 2 or first == 3 or first == 12:
# 		print('庄家胜!')
# 		money -= debt
# 	else:
# 		needs_go_on = True

# 	while needs_go_on:
# 		current = randint(1, 6) + randint(1, 6)
# 		print('玩家摇出了%d点' % current)
# 		if current == 7:
# 			print('庄家胜')
# 			money -= debt
# 			needs_go_on = False
# 		elif current == first:
# 			print('玩家胜')
# 			money += debt
# 			needs_go_on = False

# print('你破产了, 游戏结束!')

# -------------**----------------将8个苹果分成四组每组至少一个苹果有多少种方案--------------------**----------------------

# m = int(input('m='))
# n = int(input('n = '))
# fm = 1
# for num in range(1, m+1):
#     fm *= num
# fn = 1

# for num in range(1,n+1):
#     fn *= num
# fmn = 1
# for num in range(1,m - n +1):
#     fmn *= num

# print(fm // fn // fmn)

# def factorial(num):
#     """
#     求阶乘
    
#     :param num: 非负整数
#     :return: num的阶乘
#     """
#     result = 1
#     for n in range(1, num + 1):
#         result *= n
#     return result


# m = int(input('m = '))
# n = int(input('n = '))
# # 当需要计算阶乘的时候不用再写循环求阶乘而是直接调用已经定义好的函数
# print(factorial(m) // factorial(n) // factorial(m - n))

# -------------**----------------最大公约数和最小公倍数--------------------**----------------

# -*- coding:utf-8 -*-

#最大公约数
# def gcd(x,y):
#     (x,y) = (y,x) if x > y else (x,y) #这一句是可以去掉的
#     for factor in range(x, 0,-1):
#         print ('==%s'%range(x, 0,-1))
#         print ('factor=%s' %factor)
#         if x %factor == 0 and y % factor == 0:
#             return factor

# print gcd(12,18)

# #最小公倍数

# def  lcm(x,y):
#     return x*y //gcd(x,y)

# print ('最小公倍数：%s',lcm(12,18))


# -------------**----------------回文数--------------------**----------------

# def is_palindrome(num):
#     temp = num
#     total = 0
#     while temp > 0:
#         total = total *10 + temp%10
       
#         temp = temp // 10
#         print total*10,temp%10,total,temp
#     return total == num

# print('is  %s' % is_palindrome(11))

# -------------**----------------素数--------------------**----------------

def is_prime(num):
    for factor in range(1,num):
        if num %factor == 0:
            return False
    
    return True if num != 1 else False

if __name__ == "__main__":
    print (is_prime(3))


