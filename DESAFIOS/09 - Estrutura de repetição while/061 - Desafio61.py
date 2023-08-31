'''
    Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da Progressão usando a estrutura While.
'''
termo1 = int(input('\nDigite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
termo10 = 10
termo = 0
i = 1

print('A PA tem como primeiro termo {} e razão {}' .format(termo1, razao))
print('-=' * 20, end='-\n')
print('A sequência da PA é: ')


while i <= termo10:
    termo = termo1 + (i - 1) * razao
    print(' {}' .format(termo), end=' ↦ ')
    i += 1
print(' FIM DA PROGRESSÃO\n')