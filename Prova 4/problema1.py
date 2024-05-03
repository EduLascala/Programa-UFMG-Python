# -*- coding: utf-8 -*-

n = int(input("Digite um número: "))

def soma_divisores(n):
    p = 0
    for i in range(1, n-1):
        if n % i == 0:
            p = p + i 
    return p

print('Resultado: ', soma_divisores(n))