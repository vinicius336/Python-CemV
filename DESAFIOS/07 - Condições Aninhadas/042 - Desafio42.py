'''
    Refaça o DESAFIO035 dos triângulos, acrescentando o recurso de mostrar que tipo de triâgulo será formado:
    >> Equilátero: Todos os lados iguais
    >> Isósceles: Dois lados iguais
    >> Escaleno: Todos os lados diferentes
'''
print()
from math import fabs
r1 = int(input('\033[1;40m Digite o comprimento da \033[4;37m  primeira \033[0;40m reta:\033[m '))
r2 = int(input('\033[1;40m Digite o comprimento da \033[4;37m  segunda  \033[0;40m reta:\033[m '))
r3 = int(input('\033[1;40m Digite o comprimento da \033[4;37m tercerira \033[0;40m reta:\033[m '))

if fabs(r2 - r3) < r1 and r1 < r2 + r3 or fabs(r1 - r3) < r2 and r2 < r1 + r3 or fabs(r2 - r1) < r3 and r3 < r1 + r2:
    print('\033[1;32;40m ∃ triângulo. \033[m', end=' ')
    if r1 == r2 == r3:
        print('Equilátero: Todos os lados iguais')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Isósceles: Dois lados iguais')
    elif r1 != r2 != r3:
        print('Escaleno: Todos os lados diferentes')
else:
    print('\033[1;31;40m ∄ triângulo. \033[m')

print()