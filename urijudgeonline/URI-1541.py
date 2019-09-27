# -*- coding: utf-8 -*-

import os
import math

while 1:
	try:
		A,B,C = input().split(' ')
		A = int(A) 
		B = int(B)
		C = int(C)
		y = A*B
		x = y*100/C
		print(int(math.sqrt(x)))
	except:
		break
