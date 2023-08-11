'''
    Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
    Ex: Ana Maria de Souza
    Primeiro: Ana
    Último: Souza
'''
print()
nome = input('\033[1;40m Digite seu nome completo:\033[m ').strip().split()
print('\033[1;37;40m Primeiro nome: \033[4;32m {} \033[m' .format((nome[0])))
print('\033[1;37;40m  Último  nome: \033[3;32m {}  \033[m' .format((nome[0-1])))

print()