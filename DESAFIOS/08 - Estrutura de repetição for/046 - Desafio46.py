'''
    Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
'''
from time import sleep
print()
for i in range(11, 0, -1):
    print('  \r{}  '.format(i - 1), end='')
    sleep(1)
print('\nFOGOS DE ARTIFÍCIO!')
print('\nPIIIUU!! BUM!! POW!!')

print()