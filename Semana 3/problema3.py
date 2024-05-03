# -*- coding: utf-8 -*-

def verifica_triangulo(a, b, c):
	return (a + b > c) and (a + c > b) and (b + c > a)

def tipo_triangulo(a, b, c):
	if a == b and a == c:
		return 'Equilátero'
	elif a == b or a == c or b == c:
		return 'Isósceles'
	else:
		return 'Escaleno'