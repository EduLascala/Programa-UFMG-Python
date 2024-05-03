c = float(input('Digite o salário do Carlos: '))
p = float(input('Digite o rendimento da poupança(%): '))
r = float(input('Digite o rendimento do fundo de renda fixa(%): '))

Sc = c
Sj = 1/3 * c
m = 0
while Sj < Sc:
    m = m+1
    Sc = Sc + (p/100 * Sc)
    Sj = Sj + (r/100 * Sj)

print('Meses: ', m)