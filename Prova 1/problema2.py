# -*- coding: utf-8 -*-

p = float(input('Digite o valor que o Pedro apostou: '))
j = float(input('Digite o valor que o João apostou: '))
m = float(input('Digite o valor que a Marcela apostou: '))
vp = float(input('Digite o valor do prêmio: '))

x = vp/(p+j+m)

pedro = (x * p)
joao = (x * j)
marcela = (x * m)

print('Prêmio do Pedro: %.2f' % pedro)
print('Prêmio do João: %.2f' % joao)
print('Prêmio do Marcela: %.2f' % marcela)