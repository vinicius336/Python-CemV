'''
    Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.
'''
print()

n = int(input('\033[1;35;40mDigite um número:\033[m '))
print('\033[1;41m{:-^16}\033[m' .format('Sem--for'))
print('\033[41m \033[m \033[1;31m{}\033[m x {:2} = \033[1;35m{} \033[41m \033[m' .format(n, 1, n * 1))
print('\033[41m \033[m \033[1;31m{}\033[m x {:2} = \033[1;35m{} \033[41m \033[m' .format(n, 2, n * 2))
print('\033[41m \033[m \033[1;31m{}\033[m x {:2} = \033[1;35m{} \033[41m \033[m' .format(n, 3, n * 3))
print('\033[41m \033[m \033[1;31m{}\033[m x {:2} = \033[1;35m{} \033[41m \033[m' .format(n, 4, n * 4))
print('\033[41m \033[m \033[1;31m{}\033[m x {:2} = \033[1;35m{} \033[41m \033[m' .format(n, 5, n * 5))
print('\033[41m \033[m \033[1;31m{}\033[m x {:2} = \033[1;35m{} \033[41m \033[m' .format(n, 6, n * 6))
print('\033[41m \033[m \033[1;31m{}\033[m x {:2} = \033[1;35m{} \033[41m \033[m' .format(n, 7, n * 7))
print('\033[41m \033[m \033[1;31m{}\033[m x {:2} = \033[1;35m{} \033[41m \033[m' .format(n, 8, n * 8))
print('\033[41m \033[m \033[1;31m{}\033[m x {:2} = \033[1;35m{} \033[41m \033[m' .format(n, 9, n * 9))
print('\033[41m \033[m \033[1;31m{}\033[m x {:2} = \033[1;35m{} \033[41m \033[m' .format(n, 10, n * 10))
print('\033[41m-\033[m' * 16)
print('\033[1;42m{:-^16}\033[m' .format('Com--for'))
for i in range(1, 11):
    print('\033[42m \033[m \033[1;32m{}\033[m x {:2} = \033[1;35m{} \033[42m \033[m' .format(n, i, n * i))
print('\033[42m-\033[m' * 16)