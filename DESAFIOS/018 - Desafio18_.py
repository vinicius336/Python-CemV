'''
    Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo
'''
from math import sin, cos, tan
print()
ang = int(input('Digite o valor de um ângulo: '))
print('O ângulo é: {}' .format(ang))
print('Seu Seno é: {}' .format(sin(ang)))
print('Seu Cosseno é: {}' .format(cos(ang)))
print('Sua Tangente é: {}' .format(tan(ang)))

print()