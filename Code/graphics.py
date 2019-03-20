
# -*- coding: utf-8 -*-

# row = int(input('请输入行数')
# for i in range(row):
#     for  in range(i + 1):
#         print('*',end='')
#     print()
    
from __future__ import print_function

row = int(input('请输入行数: '))
for i in range(row):
    for _ in range(i + 1):
        print('*', end='')
    print()


for i in range(row):
    for j in range(row):
        if j < row - i - 1:
            print(' ', end='')
        else:
            print('*', end='')
    print()

for i in range(row):
    for _ in range(row - i - 1):
        print(' ', end='')
    for _ in range(2 * i + 1):
        print('*', end='')
    print()