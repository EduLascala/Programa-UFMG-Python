# -*- coding: utf-8 -*-

def imprime_naturais(n):
	if n == 0:
		print(n)
	else:
		imprime_naturais(n - 1)
		print(n)

n = int(input())
imprime_naturais(n)