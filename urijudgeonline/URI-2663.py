# -*- coding: utf-8 -*-
import os
import sys

N = int(input())
K = int(input())
pontos=[None]*N
count = K

for i in range(N):
	pontos[i] = int(input())
#print(pontos)

pontos.sort()
pontos.reverse()
for i in range(K,N):
	if(pontos[K-1] == pontos[i]):
		count = count +1

print(count)


