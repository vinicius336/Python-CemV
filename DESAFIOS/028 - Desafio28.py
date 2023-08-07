'''
    Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
    O programa deverá escrever na tela se o usuário venceu (Parabéns!) ou perdeu.
'''
print()
from random import randint
from time import sleep

print('=-=' * 18)
print('| Vou pensar em um número do 0 ao 5. Tente advinhar! |')
print('=-=' * 18)

print('\rPENSANDO ', end=' !  '); sleep(.5)
print('\rPENSANDO ', end='    '); sleep(.5)
print('\rPENSANDO ', end=' !  '); sleep(.6)
print('\rPENSANDO ', end='    '); sleep(.6)
print('\rPENSANDO ', end=' !  '); sleep(.7)
print('\rPENSANDO ', end='    '); sleep(.7)
print('\rPENSANDO ', end=' !  '); sleep(.9)
print('\rPENSANDO ', end='    '); sleep(.9)
print('\rPENSANDO ', end=' !  '); sleep(1)
print('\rPENSANDO ', end='    '); sleep(1)
print('\rPENSANDO ', end=' !  '); sleep(1.1)
print('\rPENSANDO ', end='    '); sleep(1.2)
print('\rPENSANDO ', end=' !  '); sleep(1.3)
print('\rPENSANDO ', end='    '); sleep(1)

num = randint(0 , 5)
escolha = int(input('\nEm qual número eu pensei? '))

if(escolha == num):
    print('Parabéns! Você acertou!')
else:
    print('Erou!')
    print('Eu pensei em {}' .format(num))

print()