# -*- coding: utf-8 -*-

maior_palavra = ''

arquivo = open('texto.txt')

for linha in arquivo:
	for palavra in linha.split():
		if len(maior_palavra) < len(palavra):
			maior_palavra = palavra			

arquivo.close()
print(maior_palavra)
print(len(maior_palavra))