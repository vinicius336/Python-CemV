'''
    Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
    Ex: Ana Maria de Souza
    Primeiro: Ana
    Último: Souza
'''
print()
nome = input('Digite seu nome completo: ').strip().split()
print('Primeiro nome: {}' .format((nome[0])))
print('Último nome: {}' .format((nome[0-1])))

print()