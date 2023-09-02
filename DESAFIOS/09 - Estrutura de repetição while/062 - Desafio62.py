'''
    Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.
'''
termo1 = int(input('\nDigite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
termo10 = 10; termo = 0; i = 1; termos = -1

print('A PA tem como primeiro termo {} e razão {}' .format(termo1, razao))
print('-=' * 20, end='-\n')
print('A sequência da PA é: ')

while termos != 0:
    while i <= termo10:
        termo = termo1 + (i - 1) * razao
        print('{}' .format(termo), end=' ↦  ')
        i += 1
        if i == termo10 + 1:
            print('FIM\n')
    termos = int(input('Quantos termos mais da P.A. você quer mostrar?\n'))
    termo10 += termos
print('\nFIM DA PROGRESSÃO')
print('A Progressão teve {} termos exibidos!\n' .format(i - 1))