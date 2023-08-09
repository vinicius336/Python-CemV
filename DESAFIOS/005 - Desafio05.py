'''
    Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.
'''

print()

num = int(input('\033[32;40mDigite um número:\033[m '))
print('\033[1;32mO Sucessor de   \033[35m{}\033[1;32m é:\033[7;30;42m {} \033[m\033[1;31m\nO Antecessor de \033[35m{}\033[1;31m é:\033[7;30;45m {} \033[m' .format(num, num + 1, num, num - 1))

print()