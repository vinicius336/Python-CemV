'''
    Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira
'''
from math import trunc
print()
num = float(input('\033[1;40mDigite um número Real:\033[m '))
print('\033[1;40mA parte inteira de \033[4;35;40m{}\033[0;37;40m é \033[4;35;40m{}\033[m' .format(num, trunc(num)))
print()
print('\033[1;40mA parte inteira de \033[4;35;40m{}\033[0;37;40m é \033[4;35;40m{}\033[m' .format(num, int(num)))

print()