'''
    Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raíz quadrada
'''

print()

num = int(input('\033[1;32;40mDigite um número:\033[m '))
print('\033[1;34mO {} de \033[1;40m {} \033[m \033[1;34mé: \033[1;32m{}' .format('Dobro ', num, num * 2))
print('\033[1;35mO {} de \033[1;40m {} \033[m \033[1;35mé: \033[1;32m{}' .format('Triplo', num, num * 3))
print('\033[1;36mA {} de \033[1;40m {} \033[m \033[1;36mé: \033[1;32m{:.2f}' .format('Raiz  ', num, num ** (1/2)))

print('\033[m')