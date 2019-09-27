# -*- coding: utf-8 -*-

a,b = [int(x) for x in input().split()]

for resto in range(abs(b)):
    if ((a - resto) %b) == 0:
        quociente = int((a-resto)/b)
        break

print(quociente,resto)
