'''
    Escreva um código que leia um nome e dê as boas vindas
'''
print()
nome = input('\033[4;35mQual é o seu nome?\033[m ').strip()
print('\nOlá, \033[1;42m{}!\033[m Prazer e te conhecer. Seja bem vinda(o) ao Python!' .format(nome.title()))
print()