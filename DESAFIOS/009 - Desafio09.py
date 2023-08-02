'''
    Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.
'''
print()

n = int(input('Digite um número: '))
print('Sem for')
print('-' * 12)
print('{} x {:2} = {}' .format(n, 1, n * 1))
print('{} x {:2} = {}' .format(n, 2, n * 2))
print('{} x {:2} = {}' .format(n, 3, n * 3))
print('{} x {:2} = {}' .format(n, 4, n * 4))
print('{} x {:2} = {}' .format(n, 5, n * 5))
print('{} x {:2} = {}' .format(n, 6, n * 6))
print('{} x {:2} = {}' .format(n, 7, n * 7))
print('{} x {:2} = {}' .format(n, 8, n * 8))
print('{} x {:2} = {}' .format(n, 9, n * 9))
print('{} x {:2} = {}' .format(n, 10, n * 10))
print('-' * 12)
print('Com for')
print('-' * 12)
for i in range(1, 11):
    print('{} x {:2} = {}' .format(n, i, n * i))
print('-' * 12)
print()