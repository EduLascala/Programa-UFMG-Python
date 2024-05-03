# -*- coding: utf-8 -*-

salario = float(input('Digite o valor do salário: '))

novo_salario = 0.0
if salario <= 280:
    novo_salario = salario * 1.2
elif salario > 280 and salario <= 700:
    novo_salario = salario * 1.15
elif salario > 700 and salario <= 1500:
    novo_salario = salario * 1.1
else:
    novo_salario = salario * 1.05

print('Valor do aumento: %.2f' % (novo_salario - salario))
print('Novo salário: %.2f' % novo_salario)