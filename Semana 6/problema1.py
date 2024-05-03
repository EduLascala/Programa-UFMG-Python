# -*- coding: utf-8 -*-

maior_linha = ''

arquivo = open('texto.txt')

for linha in arquivo:
    if len(maior_linha) < len(linha):
        maior_linha = linha

arquivo.close()
print(maior_linha, end='')
print(len(maior_linha))