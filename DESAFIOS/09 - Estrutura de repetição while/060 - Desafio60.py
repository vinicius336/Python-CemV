'''
    Faça um programa que leia um número qualquer e mostre o seu FATORIAL.
    Ex: 5! = 5x4x3x2x1 = 120
    Obs: Fazer com While e com for.
    ACRESCENTAR A ESCOLHA DE QUAL MODO CALCULAR O FATORIAL ATRAVÉS DE MENU COM IF
'''
fat = 1
num = int(input('\nDigite um número para calcular o seu fatorial: '))

print('\n{:=^20}' .format(' for '))
for i in range(num, 0, -1):
    fat = fat * i
    print('{} x ' .format(i), end='') if i > 1 else print('{}' .format(i))
print('O fatorial de {}! é {}\n' .format(num, fat))

fat = 1
print('{:=^20}' .format(' while '))
i = num
while i != 1:
    fat = fat * i
    i -= 1
    print('{} x' .format(i), end=' ') if i > 1 else print('{}' .format(num))
print('O fatorial de {}! é {}\n' .format(num, fat))

print('{:=^20}' .format(' Módulo math'))
from math import factorial
for i in range(num, 0, -1):
    print('{}' .format(i), end='')
    print(' x ' if i > 1 else '' .format(num), end='')
print('\nO fatorial de {}! é {}\n' .format(num, factorial(num)))