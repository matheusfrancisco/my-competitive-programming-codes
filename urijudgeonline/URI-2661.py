# -*- coding: utf-8 -*-

n = int(input())
f = 2
factors = 0
while(f*f<n):
    if(n%f ==0):
        factors = factors + 1
        while(n%f==0):
            n =n/f
    f=f+1
if (n != 1):
    factors = factors+1
print((1<<factors)-factors-1)
