'''
    Crie um programa que faça o computador jogar JOKENPÔ com você.
'''
print()
from time import sleep
from random import randint
pedra = 1
papel = 2
tesoura = 3
print('Vamos jogar pedra papel ou tesoura!')

print()
jogador = int(input('''Faça sua escolha:
1 - PEDRA
2 - PAPEL
3 - TESOURA
>>> '''))
if jogador == 1:
    jogador = 'PEDRA'
elif jogador == 2:
    jogador = 'PAPEL'
elif jogador == 3:
    jogador = 'TESOURA'
else:
    print('EROU!')
    exit()
    
computador = randint(1, 3)
if computador == 1:
    computador = 'PEDRA'
elif computador == 2:
    computador = 'PAPEL'
elif computador == 3:
    computador = 'TESOURA'

print('{:=^20}' .format(''), end='\r'); sleep(1)
print('{:=^20}' .format(' JO      '), end='\r'); sleep(1)
print('{:=^20}' .format('   KEN   '), end='\r'); sleep(1)
print('{:=^20}' .format('      PÔ '), end='\r'); sleep(.5)
print('{:=^20}' .format(' JOKENPÔ ')); sleep(.2)


if computador == 'PEDRA' and jogador == 'PEDRA' or computador == 'PAPEL' and jogador == 'PAPEL' or computador == 'TESOURA' and jogador == 'TESOURA':
    print('{} vs {}\n>> Empatou! <<' .format(computador, jogador))
elif computador == 'PEDRA' and jogador == 'PAPEL' or computador == 'PAPEL' and jogador == 'TESOURA' or computador == 'TESOURA' and jogador == 'PEDRA':
    print('{} vs {}\n>> você ganhou <<' .format(computador, jogador))
elif computador == 'PEDRA' and jogador == 'TESOURA' or computador == 'PAPEL' and jogador == 'PEDRA' or computador == 'TESOURA' and jogador == 'PAPEL':
    print('{} vs {}\n>> GANHEI! <<' .format(computador, jogador))

print()