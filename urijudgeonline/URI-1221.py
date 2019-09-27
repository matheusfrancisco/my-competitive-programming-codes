# -*- coding: utf-8 -*-
from random import randrange

def modExp(base, exp, mod):
    if exp == 0:
        x = 1
    else:
        half = modExp(base, exp // 2, mod)
        x = half * half
        if exp % 2 == 1:
            x *= base
    return x % mod
    
def primality(numero, n_loops=8):
    if numero == 2:
        return True

    if numero < 2 or numero & 1 == 0:
        return False
        
    # numero -1  desloca para direta 1 vez, ou seja divide por 2
    rest = (numero - 1) >> 1
    # print(rest)
    # enquando rest and 1 for  == a zero desloca para direita
    while rest & 1 == 0:
        rest = rest >> 1

    for i in range(n_loops):
        if composto(rest, numero):
            #print('Debug')
            return False
    return True


def composto(rest, numero):
    a = randrange(1, numero)
    if modExp(a, rest, numero) == 1:
        #print('Debug')
        return False
    #r <- 0 to s-1 
    #a^(2^r * d) % n != -1
    exponent = rest
    while exponent < numero - 1:
        if modExp(a, exponent, numero) == numero - 1:
            #print('Debug')
            return False
        exponent = exponent << 1
    return True
    
if __name__ == '__main__':
    
    n = input()
    n = int(n)
    while(n!=0):
        n1 = input()
        n1 = int(n1)
        numero = primality(n1)
        if(numero==True):
        #print(numero)
            print('Prime')
        else:
            print('Not Prime')
        n = n-1
