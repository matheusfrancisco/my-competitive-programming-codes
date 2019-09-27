import math
v, n = input().split()
v = int(v)
n = int(n)

percent = []

for i in [1,2,3,4,5,6,7,8,9]:
    percent.append(math.ceil((i*10*n*v)/100))

str_to_print = ''
for i in percent[::-1]:
  str_to_print = '{} '.format(i) +str_to_print

print(str_to_print)
