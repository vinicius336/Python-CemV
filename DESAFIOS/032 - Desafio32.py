'''
    Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO (2024)
'''
print()
from datetime import date

ano = int(input('Digite o ano para analisar, ou 0 para o ano atual: '))
if(ano == 0):
    ano = date.today().year
if(ano % 4 == 0) and (ano % 100 != 0 or ano % 400 == 0):
    print('Ano Bissexto.')
else:
    print('Não é Bissexto.')

print()