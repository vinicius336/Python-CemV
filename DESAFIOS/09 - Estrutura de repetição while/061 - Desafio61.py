'''
    Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da Progressão usando a estrutura While.
'''
termo1 = int(input('\nDigite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
termo10 = 10
termo = 0
i = 1

print('A PA tem como primeiro termo {} e razão {}' .format(termo, razao))
print('A sequência da PA é: ', end=' ')

while i < termo10:
    termo = termo1 + (i - 1) * razao
    print('{} ' .format(termo), end=' ')
    i += 1
    
print()
print()

'''
primeiroTermo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
termo = 10
termo = primeiroTermo + (termo - 1) * razao
print('A PA tem como primeiro termo {} e razão {}' .format(primeiroTermo, razao))
print('A sequência da PA é: ', end=' ')
for i in range(primeiroTermo, termo + 1, razao):
    print('{} ' .format(i), end=' ')
'''