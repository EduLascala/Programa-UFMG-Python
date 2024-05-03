primeiro = int(input("Digite o primeiro número: "))
segundo = int(input("Digite o segundo número: "))

res = p + s
a = str(res)

b = a.find("0")

while b >= 0:
    inicio = a[:b]
    fim = a[b + 1:]
    a = inicio + fim
    b = a.find("0")
    res = a

print("Resultado: ", res)