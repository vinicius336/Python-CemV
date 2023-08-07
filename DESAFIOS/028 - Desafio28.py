'''
    Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
    O programa deverá escrever na tela se o usuário venceu (Parabéns!) ou perdeu.
'''
print()
import random
print('Pensando...')
escolha = int(input('De 0 a 5, qual número eu pensei? '))
num = random.randint(0 , 5)
if(escolha == num):
    print('Parabéns! Você acertou!')
else:
    print('Erou!')
    print('Pensei em {}' .format(num))

print()