'''
    Desenvolva um programa que leia o primeiro termo e a razão de uma Progressão Aritimética (PA). No final, mostre os 10 primeiros termos dessa progressão.
'''
print()
primeiroTermo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
termo = 10
termo = primeiroTermo + (termo - 1) * razao
print('A PA tem como primeiro termo {} e razão {}' .format(primeiroTermo, razao))
print('A sequência da PA é: ', end=' ')
for i in range(primeiroTermo, termo + 1, razao):
    print('{} ' .format(i), end=' ')

print('\n')