'''
    Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO (2024)
'''
print()
from datetime import date

ano = int(input('\033[1;40m Digite o ano para analisar, \033[4m ou digite 0 para o ano atual:\033[m '))
if(ano == 0):
    ano = date.today().year
if(ano % 4 == 0) and (ano % 100 != 0 or ano % 400 == 0):
    print('\033[1;43m O ano é \033[4;45m Bissexto. \033[m')
else:
    print('\033[1;43m O ano \033[41m NÃO \033[43m é \033[4;45m Bissexto.\033[m')

print()