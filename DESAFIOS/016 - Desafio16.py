'''
    Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira
'''
from math import trunc
print()
num = float(input('Digite um número Real: '))
print('A parte inteira de {} é {}' .format(num, trunc(num)))
print()
print('A parte inteira de {} é {}' .format(num, int(num)))

print()