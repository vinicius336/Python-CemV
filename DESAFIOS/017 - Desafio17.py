'''
    Faça um programa que leia o comprimento do cateto oposto de do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa
'''
print()
from math import hypot
catOp = float(input('Digite a medida do Cateto Oposto: '))
catAd = float(input('Digite a medida do Cateto Adjacente: '))
hip = hypot(catOp, catAd)
print('A hipotenusa vale: {}' .format(hip))

print()