# -*- coding: utf-8 -*-
#!/usr/bin/env python3

import sys
try: 

   a = float(input("Digite o comprimento do primeiro lado: "))
   b = float(input("Digite o comprimento do segundo lado: "))
   c = float(input("Digite o comprimento do terceiro lado: "))

except ValueError:

   sys.exit(1)

if a<=0 or b<=0 or c<=0 :
   print("Não é um triângulo")
   quit()

if a>=b+c or b>=c+a or c>=a+b :
   print("Não é um triângulo")
   quit()

if a==b and b==c :
   print("Triangulo Equilátero")

elif a==b or b==c or c==a :
   print("Triangulo Isósceles")

else:
   print("Triangulo Escaleno")
