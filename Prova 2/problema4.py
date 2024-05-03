# -*- coding: utf-8 -*-

a = int(input('Digite o valor de a: '))
b = int(input('Digite o valor de b: '))
c = int(input('Digite o valor de c: '))

if a>0 or 0>a:
    d = b*b - 4 * a * c
    if d == 0:
        print('Raiz única')
        r = -b / (2 * a)
        print('Raiz = %.2f' % r)
    elif d > 0:
        x1 = (-b + d** 0.5) / (2*a)
        x2 = (-b -d ** 0.5) / (2*a)
        print('Raiz 1 = %.2f' % x1)
        print('Raiz 2 = %.2f' % x2)
    elif d < 0:
        print('Não existe raiz real')
