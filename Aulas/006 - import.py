#   import math   -   IMPORTAR TODA A BIBLIOTECA
'''
    num = int(input('Digite um número: '))
    raiz = math.sqrt(num)
    print('A raiz de {} é: {}' .format(num, raiz))
    print('O arredondamento pra cima é {}' .format(math.ceil(raiz)))
    print('O arredondamento pra baixo é {}' .format(math.floor(raiz)))
    print('A raiz sem casas decimais é {}' .format(math.trunc(raiz)))
    print('Sem casas decimais também {:.0f}' .format(raiz))
'''
from math import sqrt, floor, ceil, trunc   #   IMPORTAR APENAS AS FUNÇÕES ESPECÍFICAS DA BIBLIOTECA
print()
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} é: {}' .format(num, raiz))
print('O arredondamento pra cima é {}' .format(ceil(raiz)))
print('O arredondamento pra baixo é {}' .format(floor(raiz)))
print('A raiz sem casas decimais é {}' .format(trunc(raiz)))
print('Sem casas decimais também {:.0f}' .format(raiz))

print()

# import Ctrl+espaço   -   Apertanto Ctrl + espaço aparecerá todas as bibliotecas instaladas na máquina