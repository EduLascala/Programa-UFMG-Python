import math

hi = int(input('Digite a hora de chegada: '))
mi = int(input('Digite o minuto de chegada: '))
hf = int(input('Digite a hora da partida: '))
mf = int(input('Digite o minuto da partida: '))

if hi > hf:
    hf = hf + 24
if mi > mf:
    mf = mf + 60
    hf = hf - 1

def estacionamento(hi, mi, hf, mf):
    x = (hi * 60) + mi
    y = (hf * 60) + mf
    z = y - x
    
    if z > 60 and z <= 120:
        return "Preço: R$ 2"
    elif z <= 60 and z <= 120:
        return "Preço: R$ 1"
    elif z > 120 and z <= 180:
        return "Preço: R$ 4.20"
    elif z > 180 and z <= 240:
        return "Preço: R$ 5.60"
    elif z > 240:
        p = (z / 60)
        p = math.ceil(p) * 2
        return ("Preço: R$ %.2f" % (p))



print('', estacionamento(hi, mi, hf, mf))
