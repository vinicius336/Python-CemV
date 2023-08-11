'''
    Escreva um código que leia o dia, mês e ano de nascimento e imprima na tela formatado com /
'''

print()
diaNasc = input('Que \033[43mdia\033[m você nasceu? ').strip()
mesNasc = input('De qual \033[43mmês\033[m? ').strip()
anoNasc = input('E o \033[43mano\033[m? ').strip()
print()
print('\033[4mVocê nasceu em\033[m \033[33m{}\033[1;31m/\033[33m{}\033[1;31m/\033[33m{}\033[m' .format(diaNasc, mesNasc, anoNasc))
print()