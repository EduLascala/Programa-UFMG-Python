# -*- coding: utf-8 -*-

x = 0
y = 0
z = 0
z = int(input('Digite um número: '))
y = z
x = z
while z >= 0:
    z = int(input('Digite um número: '))
    if z >= 0:
        if z > x:
            x = z
        elif z < y:
            y = z
            
print('Maior: ', x)
print('Menor: ', y)