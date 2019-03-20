# -*- coding: utf-8 -*-


x  = int(input('x = '))
y = int(input('y = '))
if x > y:
    (x, y) = (y,x)
for factor in range(x, 0,-1):
    if x % factor == 0 and y % factor == 0:
        print('%d 和 %d max%d' % (x,y,factor))
        print('%d and %d mix %d' %(x,y,x*y // factor))
        break
        
