# -*- coding: utf-8 -*-

a = int(input('Digite o primeiro inteiro: '))
b = int(input('Digite o segundo inteiro: '))
c = int(input('Digite o terceiro inteiro: '))
d = int(input('Digite o quarto inteiro: '))
e = int(input('Digite o quinto inteiro: '))

maior = menor = a

if b > maior:
    maior = b
if c > maior:
    maior = c
if d > maior:
    maior = d
if e > maior:
    maior = e

if b < menor:
    menor = b
if c < menor:
    menor = c
if d < menor:
    menor = d
if e < menor:
    menor = e

divisores = 0

if a % 3 == 0: divisores = divisores + 1
if b % 3 == 0: divisores = divisores + 1
if c % 3 == 0: divisores = divisores + 1
if d % 3 == 0: divisores = divisores + 1
if e % 3 == 0: divisores = divisores + 1


print('Maior: ', maior)
print('Menor: ', menor)
print('Quantidade de divisíveis por 3: ', divisores)