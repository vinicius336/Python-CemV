'''
    Faça um programa que leia um número inteiro e diga se ele é ou não um número primo
'''
print()
num = int(input('Digite um número: '))
cont = 0
for i in range(1, num + 1):
    if num % i == 0:
        cont += 1
        print('\033[32m', end=' ')
    else:
        print('\033[31m', end=' ')
    print('{}\033[m' .format(i), end=' ')
print('\033[m')
print('O número {} é primo!' .format(num)) if cont == 2 else print('O número {} não é primo!' .format(num))

print()