# -*- coding: utf-8 -*-

def factorial(n):
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    return num

if __name__ == "__main__":
	
	while True:
	    try:
	    	n ,m= map(int,input().split())
	    	print(factorial(n)+	factorial(m))
	    except EOFError:
	            break
