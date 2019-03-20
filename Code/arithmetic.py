# -*- coding:utf-8 -*-

# 排序算法（选择，冒泡和归并） 和查找算法

#----------------------#简单的排序算法-------------------

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


#-------------------------------归并排序（分治法）------------------------------------

def merge_sort(items, comp = lambda x,y : x <= y):
    if len(items) < 2:
        return items[:]
    mid = len(items) // 2
    left = merge_sort(items[:mid],comp)
    print('left:%s' % left)
    right = merge_sort(items[mid:],comp)
    print('right:%s' % right)

    return merge(left, right, comp)

def merge(items1, items2, comp):
    #合并（将两个有序的列表合并成一个有序的列表）
    items = []
    index1, index2 = 0, 0
    while index1 < len(items1) and index2 < len(items2):
        if comp(items1[index1], items2[index2]):
            items.append(items1[index1])
            index1 +=  1
            print('items1:%s' % items)
        else:
            items.append(items2[index2])
            index2 += 1
            print('items2:%s' % items)
    
    items += items1[index1:]
    items += items2[index2:]
    return items

def main():

    x = [0,2,1,6,9,8,3,7,5,4]
    y = merge_sort(x)
    print('bubble_sort:%s' % y)

if __name__ == "__main__":
    main()
