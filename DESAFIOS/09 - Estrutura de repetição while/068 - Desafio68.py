'''
    Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
'''
import random

while True:
    jogador = int(input('\nAdivinhe o número que pensei\n[1]ÍMPAR ou [2]PAR: '))
    computador = random.randint(1,10)
    print(f'Pensei em {computador}')
    if computador % 2 != 0 and jogador == 1:
        print('DE NOVO!')
        continue
    elif computador % 2 == 0 and jogador == 2:
        print('DE NOVO!')
        continue
    else:
        print()
        break