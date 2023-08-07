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

print('\rPENSANDO ', end=' 1'); sleep(.5)
print('\rPENSANDO ', end=' 2'); sleep(.5)
print('\rPENSANDO ', end=' 3'); sleep(.5)
print('\rPENSANDO ', end=' 4'); sleep(.5)
print('\rPENSANDO ', end=' 5'); sleep(.5)
print('\rPENSANDO ', end=' 6'); sleep(.5)
print('\rPENSANDO ', end=' 7'); sleep(.5)
print('\rPENSANDO ', end=' 8'); sleep(.5)
print('\rPENSANDO ', end=' 9'); sleep(.5)
print('\rPENSANDO ', end=' 10'); sleep(.5)
print('\rPENSANDO ', end=' 11'); sleep(.5)
print('\rPENSANDO ', end=' 12'); sleep(.5)
print('\rPENSANDO ', end=' 13'); sleep(.5)
print('\rPENSANDO ', end=' 14'); sleep(.5)
print('\rPENSANDO ', end=' 15\n'); sleep(.5)

num = randint(0 , 5)
escolha = int(input('Em qual número eu pensei? '))

if(escolha == num):
    print('Parabéns! Você acertou!')
else:
    print('Erou!')
    print('Eu pensei em {}' .format(num))

print()