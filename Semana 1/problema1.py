# -*- coding: utf-8 -*-

x = float(input('Digite o valor do raio da circunferência: '))
y = 3.1415

perimetro = 2 * y * x
area = y * x**2
volume = 4 * y * (x**3)/3

print('Perímetro: %.2f' % perimetro)
print('Área: %.2f' % area)
print('Volume: %.2f' % volume)