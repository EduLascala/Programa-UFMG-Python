p = input("Digite a primeira palavra: ")
s = input("Digite a segunda palavra: ")

a = len(p)
b = len(s)
c = 0
d = 0
x = ""
while a > c or b > d:
    if a > c:
        y = p[c]
        x = x + y
        c = c + 1
    if b > d:
        z = s[d]
        x = x + z
        d = d + 1
print("Combinação: ", x)