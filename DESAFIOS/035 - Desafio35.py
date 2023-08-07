'''
    Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se ela podem ou não formar um triângulo.
'''
print()
from math import fabs
r1 = int(input('Digite o comprimento da primeira reta: '))
r2 = int(input('Digite o comprimento da segunda reta: '))
r3 = int(input('Digite o comprimento da tercerira reta: '))

if((fabs(r2 - r3) < r1) and (r1 < r2 + r3)
   or
   (fabs(r1 - r3) < r2) and (r2 < r1 + r3)
   or
   (fabs(r2 - r1) < r3) and (r3 < r1 + r2)):
    print('Existe triângulo.')
else:
    print('Não existe triângulo.')

print()