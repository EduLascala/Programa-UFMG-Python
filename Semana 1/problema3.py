# -*- coding: utf-8 -*-

tempo_segundos = int(input('Digite o valor do tempo em segundos: '))

horas = int(tempo_segundos / 3600)
minutos = int((tempo_segundos % 3600 / 60))
segundos = int(tempo_segundos % 60)

print('Valor convertido:', horas, 'h', minutos, 'min', segundos, 's')
