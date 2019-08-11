
# -*- coding: utf-8 -*-

def ordenado(input_code):
    p = input_code[0]
    y =True
    for i in range(1,len(input_code)):
        if(input_code[i] < input_code[i-1] and y == True):
            y = False
    if(y):
        return True
    else:
        return False


def decrescente(input_code):
    p = input_code[0]
    y=True
    for i in range(1,len(input_code)):
        if(input_code[i] > input_code[i-1] and y == True):
            y = False
    if y:
        return True
    else:
        return False


card_list_ = input().split()
card_list = []
for i in card_list_:
	card_list.append(int(i))

if(ordenado(card_list)):
    print("C")
elif(decrescente(card_list)):
    print("D")
else:
    print("N")
