'''
    Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo
'''
from math import sin, cos, tan, radians
print()
ang = int(input('Digite o valor de um ângulo: '))
print('O ângulo é: {:.1f}' .format(radians(ang)))
print('Seu Seno é: {:.4f}' .format(sin(radians(ang))))
print('Seu Cosseno é: {:.4f}' .format(cos(radians(ang))))
print('Sua Tangente é: {:.4f}' .format(tan(radians(ang))))

print()