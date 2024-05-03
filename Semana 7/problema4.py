# -*- coding: utf-8 -*-

def soma(n):
	if n == 1:
		return 1
	else:
		return n + soma(n - 1)

n = int(input())
print(soma(n))