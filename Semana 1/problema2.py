# -*- coding: utf-8 -*-

velocidade = float(input('Digite o valor da velocidade: '))
aceleracao = float(input('Digite o valor da aceleração: '))
tempo = float(input('Digite o valor do tempo: '))

vel_final = velocidade + (aceleracao * tempo)
distancia = (velocidade * tempo) + ((aceleracao * tempo ** 2))/2

print('Velocidade final: %.2f' % vel_final)
print('Distância percorrida: %.2f' % distancia)