'''
    Melhore o jogo do DESAFIO 028 onde o computador vai "PENSAR" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no ginal quantos palpites foram necessaários para vencer.
'''
print()
from random import randint
from time import sleep
jogador = 0
computador = 1
cont = 0
while jogador != computador:
    jogador = int(input('Digite um número: '))
    cont += 1
    computador = randint(0, 1)
    for i in range(0, randint(1,4)):
        print('\rP        ', end=''); sleep(.1)
        print('\rPE       ', end=''); sleep(.1)
        print('\rPEN      ', end=''); sleep(.1)
        print('\rPENS     ', end=''); sleep(.1)
        print('\rPENSA    ', end=''); sleep(.1)
        print('\rPENSAN   ', end=''); sleep(.1)
        print('\rPENSAND  ', end=''); sleep(.1)
        print('\rPENSANDO ', end=''); sleep(.1)
        print('\rPENSANDO!', end=''); sleep(.3)
    if jogador != computador:
        print('\n\nErou! Eu pensei em {}.\nTente de novo!\n' .format(computador))
    else:
        if cont == 1:
            print('\n\nPARABÉNS!!!\nVOCÊ ACERTOU NA PRIMEIRA TENTATIVA!\nEu pensei no número {}\nAté a próxima! \o' .format(computador))
        else:
            print('\n\nVocê acertou na {}ª tentativa!\nEu pensei no número {}\nAté a próxima! \o' .format(cont, computador))


print()