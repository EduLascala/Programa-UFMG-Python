# -*- coding: utf-8 -*-

def soma(m, n):
	if m == n:
		return n
	else:
		return m + soma(m + 1, n)

m = int(input())
n = int(input())
print(soma(m, n))

