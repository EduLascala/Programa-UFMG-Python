# -*- coding: utf-8 -*-

idade = int(input('Digite a idade: '))
tempo_contribuicao = int(input('Digite o tempo de contribuição: '))
sexo = input('Digite o sexo (M/F): ')

sexo = sexo.lower()

if (sexo == 'm' and idade >= 60 and tempo_contribuicao >= 35) or (sexo == 'f' and idade >= 55 and tempo_contribuicao >= 30):
    print('Pode aposentar')
elif (sexo == 'm' and idade >= 65) or (sexo == 'f' and idade >= 60):
    print('Pode aposentar')
else:
    print('Não pode aposentar')