x = input("Frase embaralhada: ")

a = len(x)

if a%2 == 0:
    b = a//2
    e = -b -1
    f = -a -1
    c = x[-1:e:-1]
    d = x[e:f:-1]
    print("Frase correta: ",d + c)
    
else:
    b = a//2 + 1
    e = -b -1
    f = -a -1
    c = x[-1:e:-1]
    d = x[e:f:-1]
    print("Frase correta: ",d + c)