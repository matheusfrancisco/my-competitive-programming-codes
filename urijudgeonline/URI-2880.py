# -*- coding: utf-8 -*-

import os

P = input()
M = input()

a = 0
countDif = 0

for i in range(0,len(P)):
	for j in range(0, len(M)):
		k= i+j
		if(k == len(P)):
			break	

		if(M[j]==P[j+i]):
			countDif = 0
			break
		countDif = countDif + 1
		if(countDif == len(M)):
			a = a + 1			
	
	
	countDif = 0
	
	
print(a)
	


