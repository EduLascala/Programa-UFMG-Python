
v = float(input('Digite o valor da hora de trabalho: '))
h = int(input('Digite a quantidade de horas trabalhadas no mês: '))
b = v * h
print("Salário Bruto: %.2f" % b)

if b > 2500:
    r = 0.2 * b
    print("IR: R$ %.2f" % r)
elif b > 1500 and 2500 >= b:
    r = 0.1 * b
    print("IR: R$ %.2f" % r)
elif b > 900 and 1500 >= b:
    r = 0.05 * b
    print("IR: R$ %.2f" % r)
else:
    r = 0
    print("IR: R$ %.2f" % r)
INSS = 0.1 * b
print("INSS: R$ %.2f" % INSS)
FGTS = 0.11 * b
print("FGTS: R$ %.2f" % FGTS)
d = INSS + r
print("Total de descontos: R$ %.2f" % d)
l = b - d
print("Salário líquido: R$ %.2f" % l)