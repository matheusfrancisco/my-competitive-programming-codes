# -*- coding: utf-8 -*-
import os

N = int(input())
t1 = 0
t2 = 0
pt1 = 0
pt2 = 1
i = 0
s1 = 0
s2 = 0
golc1 = 0
golc2 = 0  
while(N != 0):

	M,x,V = input().split(' ')
	M = int(M)
	V = int(V)
	t1 = int(M)
	t2 = int(V)
	s1 = M
	s2 = V
	golc2 = V 
	if(t1 == t2 ):
		pt1 = 1
		pt2 = 1
	elif(t1 > t2):
		pt1 = 3
		pt2 = 0
	else:
		pt1 = 0
		pt2 = 3

	M,x,V = input().split(' ')
	M = int(M)
	V = int(V)
	t1 = t1 + V
	t2 = t2 + M
	golc1 = V
	s1 = s1 + V
	s2 = s2 + M
	
	if(t1 == t2):
		pt1 = 1
		pt2 = 1
	elif(t1 > t2):
		pt1 = pt1 +  3
		pt2 = 0
	else:
		pt1 = 0
		pt2 = pt2 +  3
	

	if(pt1 > pt2):

		print('Time 1')

	elif(pt2>pt1):

		print('Time 2')
	else:
		if(s1 > s2):
			print('Time 1')
		elif(s2 > s1):
			print('Time 2')
		else:
			if(golc1 > golc2 ):
				print('Time 1')
			elif(golc2 > golc1):
				print('Time 2')
			else:
				print('Penaltis')
	pt1 = 0
	pt2 = 0
	i = 0
	t1 = 0
	t2 = 0
	golc1 = 0
	golc2 = 0 
	N = N - 1
	s2 = 0
	s1 = 0

