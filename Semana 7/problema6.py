# -*- coding: utf-8 -*-

def imprime_naturais_pares(n):
	if n == 0:
		print(n)
	elif n % 2 == 0:
		imprime_naturais_pares(n - 2)
		print(n)
	else:
		imprime_naturais_pares(n - 1)

n = int(input())
imprime_naturais_pares(n)

