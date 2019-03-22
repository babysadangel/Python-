# -*- coding:utf-8 -*-

# 排序算法（选择，冒泡和归并） 和查找算法

# ----------------------#简单的排序算法-------------------

# def select_sort(origin_items, comp = lambda x ,y : x < y):
#     #简单的排序算法
#     items = origin_items[:]
#     for i in range(len(items) - 1):
#         mix_index = i
#         for j in range(i + 1, len(items)):
#             if comp(items[j], items[mix_index]):
#                 mix_index = j

#         items[i], items[mix_index] = items[mix_index], items[i]

#         return items

# def main():
#     x = [1,9,4,7,3,8,0]
#     y  = select_sort(x)
#     print('items :%s' % y)

# if __name__ == "__main__":
#     main()


# #-------------------------------高质量冒泡排序（搅拌顺序）------------------------------------

# def bubble_sort(origin_items,comp = lambda x ,y :x >y):
#     items = origin_items[:]
#     for i in range(len(items) - 1):
#         swapped = False
#         for j in range(i ,len(items) - 1 - i):
#             if comp(items[j], items[j + 1]):
#                 items[j], items[j+1]  = items[j +1], items[j]
#                 swapped = True

#         if swapped:
#             swapped = False
#             for j in range(len(items) - 2 - i, i, -1):
#                 if comp(items[j-1],items[j]):
#                     items[j], items[j - 1] = items[j  -1], items[j]
#                     swapped  = True
#         if not swapped:
#             break

#     return items

# def main():

#     x = [0,2,9,3,7,5,4]
#     y = bubble_sort(x)
#     print('bubble_sort:%s' % y)

# if __name__ == "__main__":
#     main()


# #-------------------------------归并排序（分治法）------------------------------------

# def merge_sort(items, comp = lambda x,y : x <= y):
#     if len(items) < 2:
#         return items[:]
#     mid = len(items) // 2
#     left = merge_sort(items[:mid],comp)
#     print('left:%s' % left)
#     right = merge_sort(items[mid:],comp)
#     print('right:%s' % right)

#     return merge(left, right, comp)

# def merge(items1, items2, comp):
#     #合并（将两个有序的列表合并成一个有序的列表）
#     items = []
#     index1, index2 = 0, 0
#     while index1 < len(items1) and index2 < len(items2):
#         if comp(items1[index1], items2[index2]):
#             items.append(items1[index1])
#             index1 +=  1
#             print('items1:%s' % items)
#         else:
#             items.append(items2[index2])
#             index2 += 1
#             print('items2:%s' % items)

#     items += items1[index1:]
#     items += items2[index2:]
#     return items

# def main():

#     x = [0,2,1,6,9,8,3,7,5,4]
#     y = merge_sort(x)
#     print('bubble_sort:%s' % y)

# if __name__ == "__main__":
#     main()

# -------------------------------顺序查找------------------------------------

# def seq_search(items, key):
#     for index, item in enumerate(items):
#         if item = key:
#             return index

#     return -1


# -------------------------------折半查找------------------------------------

# def bin_search(items, key):

#     start, end = 0, len(items) - 1
#     while start <= end:
#         mid = (start + end) // 2
#         if key > items[mid]:
#             start = mid + 1
#         elif key < items[mid]:
#             end = mid - 1
#         else:
#             return mid

#     return -1

# def main():

#     x = [0,2,1,6,9,8,3,7,5,4]
#     y = bin_search(x,2)
#     print('bubble_sort:%s' % y)

# if __name__ == "__main__":
#     main()


# -------------------------------使用生成式（推导式）语法------------------------------------

# def main():
#     prices = {
#     'AAPL': 191.88,
#     'GOOG': 1186.96,
#     'IBM': 149.24,
#     'ORCL': 48.44,
#     'ACN': 166.89,
#     'FB': 208.09,
#     'SYMC': 21.29
#     }

#     # 用股票价格大于100元的股票构造一个新的字典
#     prices2 = {key: value for key , value in prices.items() if value > 100}
#     print ('price2:%s' % prices2)

# if __name__ == "__main__":
#     main()

# #-------------------------------套嵌的列表------------------------------------

# def main():
#     names = ['关羽', '张飞', '赵云', '马超', '黄忠']
#     courses = ['语文', '数学', '英语']
#     #录入五位学生三门课程的成绩
#     scores = [[None] * len(courses) for _ in range(len(names)]

#     for row, name in enumerate(names):
#         for col, courses in enumerate(courses):
#             scores[row][col] = float(input('请输入{name}的{course}的成绩:'))
#             print(scores)

# if __name__ == "__main__":
#     main()

# --------------------heapd, itertools用法-------------------
# 从列表中找出最大的或者最小的N个元素，堆结构（大根堆/小根堆）
# import heapq

# def main():
#     list1 = [34, 25, 12, 99, 87, 63, 58, 78, 88, 92]
#     list2 = [
#         {'name': 'IBM', 'shares': 100, 'price': 91.1},
#         {'name': 'AAPL', 'shares': 50, 'price': 543.22},
#         {'name': 'FB', 'shares': 200, 'price': 21.09},
#         {'name': 'HPQ', 'shares': 35, 'price': 31.75},
#         {'name': 'YHOO', 'shares': 45, 'price': 16.35},
#         {'name': 'ACME', 'shares': 75, 'price': 115.65}
#     ]

#     print('headpd.nlargest:%s' % heapq.nlargest(3,list1))#最大的3个数
#     print('headpd.nsmallest:%s' % heapq.nsmallest(3,list1))#最小的3个数
#     print('key-price:%s' % heapq.nlargest(2,list2,key=lambda x : x['price']))
#     print('key-sahre:%s' % heapq.nlargest(2,list2,key= lambda x : x['shares']))


# if __name__ == "__main__":
#     main()

# #------------迭代工具----排列 /组合 、 笛卡尔积

# import itertools

# def main():
#    x =  list(itertools.permutations('ABCD'))
#    y = list(itertools.combinations('ABCD',3))
#    z = list(itertools.product('ABCD',range(5)))

#    print('permutations:%s' % x)
#    print('combination:%s' % y)
#    print('product:%s' % z)

# if __name__ == "__main__":
#     main()

# --------------------------------------collection模块下的工具类---------------------------------------

# 找出序列中出现次数最多的元素

# from collections import Counter

# def main():
#     words = [
#     'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
#     'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around',
#     'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes',
#     'look', 'into', 'my', 'eyes', "you're", 'under'
#     ]

#     counter = Counter(words)
#     print('most_common:%s' % counter.most_common(3))

# if __name__ == "__main__":
#     main()

"""
常用算法：
    1、穷举法---又称为暴力破解法，对所有的可能性进行验证，知道找到正确的答案
    2、贪婪法---在对问题求解时，总是做出当前看来是最好的选择，不追求最优解，快速找到最优解
    3、分治法---把一个复杂的问题分成两个或者更过相似的子问题，再把子问题分成最小子问题，直到可以直接求解的程度，最后将子问题的解进行合并
    得到原问题的解
    4、回溯法----回溯法又称为试探法，按优选条件向前搜索，当搜索到某一步发现原先选择并不优或者达不到目的的时候，就退回一步重新选择
    5、动态规划--基本思想也是讲带求解问题分解成若干个子问题，先求解并保存这些子问题的解，避免产生大量的重复运算

"""
# 公鸡5元一只，母鸡3元1只，小鸡1元3只，用100元买100只鸡，个多少只

# def main():

#     for x  in range(20):
#         for y in range(33):
#             z = 100 - x - y
#             if 5 *x + y * 3 + z/3  == 100 and z%3 == 0:
#                 print('x = %d y = %d z = %d' % (x,y,z))


# if __name__ == "__main__":
#     main()

# A、B、C、D、E五人在某天夜里合伙捕鱼 最后疲惫不堪各自睡觉
# 第二天A第一个醒来 他将鱼分为5份 扔掉多余的1条 拿走自己的一份
# B第二个醒来 也将鱼分为5份 扔掉多余的1条 拿走自己的一份
# 然后C、D、E依次醒来也按同样的方式分鱼 问他们至少捕了多少条鱼

# def main():
#     fish = 1
#     while True:
#         total = fish
#         enough = True
#         for _ in range(5):
#             if (total -1) % 5 == 0:
#                 total = (total-1) // 5 * 4
#             else:
#                 enough = False
#                 break
#         if enough:
#             print ('最少捕鱼fish:%d'% fish)
#             break
#         fish += 1


# if __name__ == "__main__":
#     main()

# --------------------------------贪婪法---------------------------------------------
# 贪婪法求解时候，总是做出当前看来是最好的选择，不追求最优解，快速找到满意解
"""
贪婪法：在对问题求解时，总是做出在当前看来是最好的选择，不追求最优解，快速找到满意解。
输入：
20 6
电脑 200 20
收音机 20 4
钟 175 10
花瓶 50 2
书 10 1
油画 90 9
"""

# class Thing(object):
#     """物品"""

#     def __init__(self, name, price, weight):
#         self.name = name
#         self.price = price
#         self.weight = weight

#     @property
#     def value(self):
#         """价格重量比"""
#         return self.price / self.weight


# def input_thing():
#     """输入物品信息"""
#     name_str, price_str, weight_str = input().split()
#     return name_str, int(price_str), int(weight_str)


# def main():
#     """主函数"""
#     max_weight, num_of_things = map(int, input().split())
#     all_things = []
#     for _ in range(num_of_things):
#         all_things.append(Thing(*input_thing()))
#     all_things.sort(key=lambda x: x.value, reverse=True)
#     total_weight = 0
#     total_price = 0
#     for thing in all_things:
#         if total_weight + thing.weight <= max_weight:
#             print(f'小偷拿走了{thing.name}')
#             total_weight += thing.weight
#             total_price += thing.price
#     print(f'总价值: {total_price}美元')


# if __name__ == '__main__':
#     main()

# ------------------------------分治法（快速排序）------------------------------------
# 快速排序----选择枢轴对元素进行划分，左边都比枢轴小，右边都比枢轴大


#    def quick_sort(origin_items, comp=lambda x, y: x <= y):
#         items = origin_items[:]
#         _quick_sort(items, 0, len(items) - 1, comp)
#         print('item:%s' % items)
#         return items

#     def _quick_sort(items, start, end, comp):
#         if start < end:
#             pos = _partition(items, start, end, comp)
#             _quick_sort(items, start, pos - 1, comp)
#             _quick_sort(items, pos + 1, end, comp)

#     def _partition(items, start, end, comp):
#         pivot = items[end]
#         i = start - 1
#         for j in range(start, end):
#             if comp(items[j], pivot):
#                 i += 1
#                 items[i], items[j] = items[j], items[i]

#         items[i + 1], items[end] = items[end], items[i + 1]
#         return i + 1

#--------------------------------回溯法---------------------------------------------------
#骑士巡逻 地柜回溯法，又称为试探法，按优选条件向前搜索，当搜索到某一步，发现原先选择并不优或者达不到目的的时候
#就回退一步重新选择，比较经典的问题包括骑士巡逻，八皇后和迷宫寻路

# import sys
# import time

# SIZE = 5
# total = 0

# def print_board(board):
#     for row in board:
#         for col in row:
#             print(str(col).center(4),end='')

# def patrol(board, row, col, step = 1):
#     if row >= 0 and row < SIZE and \
#         col >= 0 and col < SIZE and \
#         board[row][col] == 0:

#         board[row][col] = step
#         if step == SIZE * SIZE:
#             global total
#             total += 1
#             print(f'第{total}种走法')
#             print_board(board)
        
#         patrol(board, row - 2, col - 1, step + 1)
#         patrol(board, row - 1, col - 2, step + 1)
#         patrol(board, row + 1, col - 2, step + 1)
#         patrol(board, row + 2, col - 1, step + 1)
#         patrol(board, row + 2, col + 1, step + 1)
#         patrol(board, row + 1, col + 2, step + 1)
#         patrol(board, row - 1, col + 2, step + 1)
#         patrol(board, row - 2, col + 1, step + 1)
#         board[row][col] =  0

# def main():
#     board = [[0] * SIZE for _ in range(SIZE)]
#     print('board=: %s' % board)
#     patrol(board, SIZE - 1, SIZE - 1)

# if __name__ == "__main__":
#     main()


#---------------------------------动态规划-------------------------------------
#动态规划---适用于有重叠问题和最优子结构性质的问题
#使用动态规划方法所消耗时间往往小于朴素解法（用空间换取时间）

def fib(num):
    #递归计算函数
    if num in (1,2):
        return 1
    
    try:
        return num
    except KeyError:
        num  = fib(num - 1) + fib(num - 2)
        return num

def main():


    y = []

    for i  in range(10):
        
        x =  fib(i)
        y.append(x)
        print(x)

if __name__ == "__main__":
    main()
