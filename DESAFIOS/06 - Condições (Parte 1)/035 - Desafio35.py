'''
    Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se ela podem ou não formar um triângulo.
'''
print()
from math import fabs
r1 = int(input('\033[1;40m Digite o comprimento da \033[4;37m  primeira \033[0;40m reta:\033[m '))
r2 = int(input('\033[1;40m Digite o comprimento da \033[4;37m  segunda  \033[0;40m reta:\033[m '))
r3 = int(input('\033[1;40m Digite o comprimento da \033[4;37m tercerira \033[0;40m reta:\033[m '))

if((fabs(r2 - r3) < r1) and (r1 < r2 + r3)
   or
   (fabs(r1 - r3) < r2) and (r2 < r1 + r3)
   or
   (fabs(r2 - r1) < r3) and (r3 < r1 + r2)):
    print('\033[1;32;40m ∃ triângulo. \033[m')
else:
    print('\033[1;31;40m ∄ triângulo. \033[m')

print()