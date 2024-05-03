# -*- coding: utf-8 -*-

# Existe uma solução mais simples.
# No entanto, ainda não estudamos listas.
arquivo = open('notas.txt')

for linha in arquivo:
	nome = linha[:3]
	notas = linha[4:]
	soma = 0
	for nota in notas.split():
		soma = soma + int(nota)
	media = soma / 4
	if media > 60:
		print('Nome: %s - Média: %.2f' % (nome, media))

arquivo.close()