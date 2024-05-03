# -*- coding: utf-8 -*-

x = int(input('Digite um inteiro de 4 algarismos: '))

soma = 0

while (x != 0):
    resto = x % 10
    x = (x - resto)//10
    soma = soma + resto
print('Resultado: %i' % soma)