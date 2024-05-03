import math

x = int(input('Digite o valor de x: '))
y = int(input('Digite o valor de y: '))

for i in range(x, y+1):
    for j in range(1, y):
        p = j*j
        if p == i:
            print(' ', p)
    
