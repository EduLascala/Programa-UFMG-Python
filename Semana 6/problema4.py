# -*- coding: utf-8 -*-

def maior_data(data1, data2):
	dia_data1 = int(data1[:2])
	dia_data2 = int(data2[:2])
	mes_data1 = int(data1[3:5])
	mes_data2 = int(data2[3:5])
	ano_data1 = int(data1[6:])
	ano_data2 = int(data2[6:])
	
	if ano_data1 > ano_data2:
		return data1
	elif ano_data1 < ano_data2:
		return data2
	elif mes_data1 > mes_data2:
		return data1
	elif mes_data1 < mes_data2:
		return data2
	elif dia_data1 > dia_data2:
		return data1
	else:
		return data2

arquivo = open('datas.txt')
mais_recente = '00/00/0000'

for data in arquivo:
	mais_recente = maior_data(mais_recente, data)

print(mais_recente, end='')
arquivo.close()