# -*- coding: utf-8 -*-
import os
import sys

A1 = int(input())
A2 = int(input())
A3 = int(input())

t3 = A2*2 + A1*4
t2 =  A3*2 + A1*2 
t1 = A3*4  + A2*2

p = [t3, t2, t1]
p.sort()

print(p[0])
