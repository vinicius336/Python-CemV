'''
    Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
    >> Se ele ainda vai se alistar ao serviço militar.
    >> Se é a hora de se alistar.
    >> Se já passou do tempo do alistamento.
    Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''
from datetime import date
print()
ano = int(input('Digite o seu ano de nascimento: '))

if((date.today().year - ano) < 18):
    print('Faltam {} anos para você se alistar ao serviço militar.' .format(date.today().year - ano))
elif(date.today().year - ano == 18):
    print('Está na hora de se alistar!')
else:
    print('Seu alistamento militar passou do prazo em {} ano(s).' .format((date.today().year - ano) - 18))

print()
