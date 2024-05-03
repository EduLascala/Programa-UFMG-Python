# -*- coding: utf-8 -*-

n = int(input('Digite n: '))
s = 0

for c in range(1, n+1):
    s += 1/c
print('Resultado: %.2f' % s)