
nome = input()
l = []
while nome != '':
	nota1 = float(input())
	nota2 = float(input())
	media = (nota1 + nota2) / 2
	l.append((media, nome))
	nome = input()
l.sort(reverse=True)
for i in l:
	print('%s - %.2f' % (i[1], i[0]))