# -*- coding: utf-8 -*-
from operator import concat

l = input().split()
b = input().split()

l_ = []
b_ = []
for i in l:
    l_.append(int(i))

for i in b:
    b_.append(int(i))


if( len(concat(l,b)) - len(set(concat(l,b))) == 3):
    print("terno")
elif( len(concat(l,b)) - len(set(concat(l,b))) < 3):
    print("azar")
elif( len(concat(l,b)) - len(set(concat(l,b))) == 6):
    print("sena")
elif( len(concat(l,b)) - len(set(concat(l,b))) == 4):
    print("quadra")
elif( len(concat(l,b)) - len(set(concat(l,b))) == 5):
    print("quina")
