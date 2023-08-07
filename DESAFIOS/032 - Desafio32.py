'''
    Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO (2024)
'''
ano = int(input('Digite o ano: '))
if(ano % 4 == 0):
    print('É ano Bissexto.')
else:
    print('Não é ano Bissexto.')