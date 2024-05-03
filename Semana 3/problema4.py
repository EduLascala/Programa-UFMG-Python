# -*- coding: utf-8 -*-

def calcula_valor(preco_litro, quantidade_litros, tipo_combustivel):
	if tipo_combustivel == 'a':
		if quantidade_litros <= 20:
			preco_litro_desconto = preco_litro - (preco_litro * 0.03)			
		else:
			preco_litro_desconto = preco_litro - (preco_litro * 0.05)
		total = preco_litro_desconto * quantidade_litros
		return total			
	else:
		if quantidade_litros <= 20:
			preco_litro_desconto = preco_litro - (preco_litro * 0.04)			
		else:
			preco_litro_desconto = preco_litro - (preco_litro * 0.06)
		total = preco_litro_desconto * quantidade_litros
		return total