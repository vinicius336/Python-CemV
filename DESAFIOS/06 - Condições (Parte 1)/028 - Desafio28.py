'''
    Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
    O programa deverá escrever na tela se o usuário venceu (Parabéns-) ou perdeu.
'''
print()
from random import randint
from time import sleep

print('\033[1;35;45m=-=\033[m' * 18)
print('\033[35;45m| \033[1m\033[3;30;41mVou pensar em um número do 0 ao 5. Tente advinhar-\033[0;45m |\033[m')
print('\033[1;35;45m=-=\033[m' * 18)

for i in range(0, 1):
    print('\r\033[3;47m\033[1m ','PENSANDO \033[m',                        end='\033[1;37;47m | \033[m'); sleep(.2)
    print('\r\033[3;47m\033[1m ',         '\033[8mPEN\033[3mSANDO \033[m', end='\033[1;37;47m / \033[m'); sleep(.2)
    print('\r\033[3;47m\033[1m ',      'PEN\033[8mSAN\033[3mDO \033[m'   , end='\033[1;37;47m - \033[m'); sleep(.2)
    print('\r\033[3;47m\033[1m ',   'PENSAN\033[8mDO \033[m\033[m'       , end='\033[1;37;47m \ \033[m'); sleep(.2)
print('\r\033[3;47m\033[1m  PENSANDO\033[7m \033[m'                       , end='\033[1;37;47m ! \033[m'); sleep(.2)

print('\r\t\033[m') ; sleep(1)
num = randint(0 , 5)
escolha = int(input('\033[1;32;42m Em qual número eu pensei?\033[m '))

if(escolha == num):
    print('\033[1;32;42m PARABÉNS! \033[m\n\033[1;42m- \033[3mVocê acertou\033[1m -\033[m')
else:
    print('\033[1;31;41m- \033[3mErou\033[1m -\033[m')
    print('\033[3;41m Eu pensei em \033[1;42m {} \033[m' .format(num))

print()