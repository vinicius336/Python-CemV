'''
    Crie um programa que leia DOIS VALORES e mostre um MENU na tela:
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA
    Seu programa deverá realizar a operação solicitada em cada caso.
'''
from time import sleep
num1 = int(input('\nDigite um número: '))
num2 = int(input('Digite outro número: '))
opcao = 0
while opcao != 5:
    print('''\nEscolha uma opção:
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do Programa''')
    opcao = int(input('\nEscolha uma opção: '))
    
    if opcao == 1:
        print('{} + {} = {}' .format(num1, num2, num1 + num2))
    elif opcao == 2:
        print('{} x {} = {}' .format(num1, num2, num1 * num2))
    elif opcao == 3:
        if num1 > num2:
            print('{} > {}' .format(num1, num2))
        elif num2 > num1:
            print('{} > {}' .format(num2, num1))
        else:
            print('{} e {} são iguais.' .format(num1, num2))
    elif opcao == 4:
        print('\nDigite novos números:')
        num1 = int(input('Primeiro número: '))
        num2 = int(input('Segundo número: '))
    elif opcao == 5:
        print('Fim!\n')
        exit()
    else:
        print('Opção inválida. Tente novamente.')
    sleep(0) if opcao == 4 else sleep(2)
        