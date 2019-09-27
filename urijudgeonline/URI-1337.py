# -*- coding: utf-8 -*-

import os,sys

def main():
		while(1):
			a,b,c = input().split(' ')

			a = int(a)
			b = int(b)
			c = int(c)
			if(a == 0 and b== 0 and c ==0 ):
				break
			mao =[]
			mao.append(a)
			mao.append(b)
			mao.append(c)

			mao.sort()


			a = int(mao[0])
			b = int(mao[1])
			c = int(mao[2])
			
			s = p = False

			if(a == b and a == c): s = True
			if(a == b or b == c): p = True

			if(s):
				if(a == 13):
					print('*')
				else: 
					print(a + 1, a + 1, a + 1)
			elif(p):
				if(a == b):
					if(c == 13):
						print(1, a+1, a+1)
					else:
						print(a, a, c + 1)
				else:
					if(c == 13):
						if(a == 12):
							print('1 1 1')
						else:
							print(a + 1, b, b)
					else:
						if(a + 1 == b):
							print(b, b, a + 2)
						else:
							print(a + 1, b, b)
			else:
				print('1 1 2')
		





if __name__ == '__main__':
	
	main()

