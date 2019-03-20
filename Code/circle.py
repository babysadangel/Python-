
# -*- coding :utf-8 -*-
# -*- coding: cp936 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf8')

from math import sqrt

num = int(input("please input number"))
end = int(sqrt(num))

is_prime = True

for x in range(2,end+ 1):
	if num %x == 0:
		is_prime = False
		break
if is_prime and num != 1:
	print('%d yes' %num)

else:
	print('%d NO' %num)
	