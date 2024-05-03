a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))

if a>c and a<b:
    mediana = a
if a<c and a>b:
    mediana = a

if b>c and b<a:
    mediana = b
if b<c and b>a:
    mediana = b    

if c>b and c<a:
    mediana = c
if c<b and c>a:
    mediana = c





if a==b and a<c:
    mediana = a
if a==c and a<b:
    mediana = a
    
if b==a and b<c:
    mediana = b
if b==c and b<a:
    mediana = b
    
if c==b and c<a:
    mediana = a
if c==a and c<b:
    mediana = a




if a==b and a>c:
    mediana = a
if a==c and a>b:
    mediana = a

if b==a and b>c:
    mediana = b
if b==c and b>a:
    mediana = b
    
if c==a and c>b:
    mediana = c
if c==b and c>a:
    mediana = c



print('Mediana: %i' % mediana)