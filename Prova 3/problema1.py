# -*- coding: utf-8 -*-

f = "Fizz"
b = "Buzz"
fb = "FizzBuzz"
def fizz_buzz(n):
    if n % 3 == 0 and n % 5 == 0:
       return fb
    elif n % 5 == 0:
        return b
    elif n % 3 == 0:
        return f
    else:
        return n
n = int(input('Digite um número: '))
print(fizz_buzz(n))