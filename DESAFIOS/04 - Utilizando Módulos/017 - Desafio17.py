'''
    Faça um programa que leia o comprimento do cateto oposto de do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa
'''
print()
from math import hypot
catOp = float(input('\033[1;37;40mDigite a medida do \033[4;31;40m Cateto Oposto: \033[m '))
catAd = float(input('\033[1;37;40mDigite a medida do \033[4;31;40m Cateto Adjacente: \033[m '))
hip = hypot(catOp, catAd)
print('\033[1;37;40mA \033[4;31;40m hipotenusa \033[m\033[1;37;40m vale \033[4;31;40m{:.2f}\033[m' .format(hip))
hip = (catOp ** 2 + catAd ** 2) ** (1/2)
print('\033[4;31;40m {:.2f} \033[m' .format(hip))

print()