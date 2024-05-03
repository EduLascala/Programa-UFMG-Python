# -*- coding: utf-8 -*-

vel_max = int(input('Digite o valor da velocidade máxima: '))
vel_reg = int(input('Digite o valor da velocidade registrada: '))

if vel_max <= 0 or vel_reg <= 0:
    print('Velocidades inválidas')
elif vel_reg <= vel_max:
    print('Sem Infração')
elif vel_reg > vel_max and vel_reg <= vel_max * 1.2:
    print('Infração Média')
elif vel_reg > vel_max * 1.2 and vel_reg <= vel_max * 1.5:
    print('Infração Grave')
elif vel_reg > vel_max * 1.5:
    print('Infração Gravíssima')