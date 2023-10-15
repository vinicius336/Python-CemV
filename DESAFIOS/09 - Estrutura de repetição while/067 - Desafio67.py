'''
    Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuários. O programa será interrompido quando o número solicitado for negativo.
'''
while True:
    n = int(input('\nDigite um número: '))
    if n >= 0:
        for i in range(11):
            print(f'{n} x {i} = {n * i}')
    else:
        break