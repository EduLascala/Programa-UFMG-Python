# -*- coding: utf-8 -*-

def consumo(d, l):
    if d/l < 8:
        return "Venda o carro!"
    elif d/l >= 8 and d/l <= 12:
        return "Econômico!"
    elif d/l > 12:
        return "Super econômico!"

d = float(input('Digite a distância: '))
l = float(input('Digite a quantidade de gasolina consumida: '))
consumo(d, l)