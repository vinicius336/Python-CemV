'''
    Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo
'''
from math import pi, sin, cos, tan, radians
print()
ang = float(input('\033[1;31;40mDigite o valor de um ângulo:\033[m '))
ang = ang * (180 / pi)
print('\033[1;35;40mO ângulo é: \033[4;33;40m {:.1f} \033[m' .format(radians(ang)))
print('\033[1;35;40mSeu Seno é: \033[4;33;40m {:.2f} \033[m' .format(sin(radians(ang))))
print('\033[1;35;40mSeu Cosseno é: \033[4;33;40m {:.2f} \033[m' .format(cos(radians(ang))))
print('\033[1;35;40mSua Tangente é: \033[4;33;40m {:.2f} \033[m' .format(tan(radians(ang))))

print()