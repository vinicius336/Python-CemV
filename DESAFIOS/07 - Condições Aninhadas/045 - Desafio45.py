'''
    Crie um programa que faça o computador jogar JOKENPÔ com você.
'''
print()
from random import randint
pedra = 1
papel = 2
tesoura = 3
print('Vamos jogar pedra papel ou tesoura!')

print()
jogador = int(input('Faça sua escolha:\n1 - PEDRA\n2 - PAPEL\n3 - TESOURA\t'))
if jogador == 1:
    jogador = 'PEDRA'
elif jogador == 2:
    jogador = 'PAPEL'
elif jogador == 3:
    jogador = 'TESOURA'
else:
    print('EROU!')
    
computador = randint(1, 3)
if computador == 1:
    computador = 'PEDRA'
elif computador == 2:
    computador = 'PAPEL'
elif computador == 3:
    computador = 'TESOURA'
print()

if computador == 'PEDRA' and jogador == 'PEDRA' or computador == 'PAPEL' and jogador == 'PAPEL' or computador == 'TESOURA' and jogador == 'TESOURA':
    print('{} vs {}\n>> Empatou! <<' .format(computador, jogador))
elif computador == 'PEDRA' and jogador == 'PAPEL' or computador == 'PAPEL' and jogador == 'TESOURA' or computador == 'TESOURA' and jogador == 'PEDRA':
    print('{} vs {}\n>> você ganhou <<' .format(computador, jogador))
elif computador == 'PEDRA' and jogador == 'TESOURA' or computador == 'PAPEL' and jogador == 'PEDRA' or computador == 'TESOURA' and jogador == 'PAPEL':
    print('{} vs {}\n>> GANHEI! <<' .format(computador, jogador))

print()