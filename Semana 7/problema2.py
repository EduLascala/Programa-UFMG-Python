# -*- coding: utf-8 -*-

def power(k, n):
	if n == 0:
		return 1
	else:
		return k * power(k, n - 1)

k = int(input())
n = int(input())
print(power(k, n))

