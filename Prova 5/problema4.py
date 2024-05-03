x = input("Digite uma palavra: ")
y = int(input("Digite o valor da chave: "))

a = len(x)
b = 0
c = ""
while a > b:
    l = x[b]
    w = ord(l)
    z = w + y
    if z <= 122:
        d = chr(z)
        c = c + d
        b = b + 1
    else:
        z = z -26
        d = chr(z)
        c = c + d
        b = b + 1
print("Resultado: ",c)