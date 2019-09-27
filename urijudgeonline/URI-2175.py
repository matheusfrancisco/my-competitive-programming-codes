# -*- coding: utf-8 -*-
import os 
import sys

O,B,I= input().split(" ")
O = float(O)
B = float(B)
I = float(I)

d ={'Otavio':O,'Bruno':B,'Ian':I}
items = [(v,k) for k, v in d.items()]
items.sort()
items.reverse()
items= [(k,v) for v, k in items]

if(items[1][1] == items[2][1]):
	print('Empate')
else:
	print(items[2][0])
