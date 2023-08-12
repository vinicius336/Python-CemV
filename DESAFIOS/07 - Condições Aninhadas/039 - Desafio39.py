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
sexo = int(input('Informe o seu sexo:\n[1] - Masculino\n[2] - Feminino\n'))
if sexo == 1:
    if((date.today().year - ano) < 18):
        print('Você tem {} anos' .format(date.today().year - ano))
        print('Faltam {} anos para você se alistar ao serviço militar.' .format(date.today().year - ano))
    elif(date.today().year - ano == 18):
        print('Você tem {} anos' .format(date.today().year - ano))
        print('Está na hora de se alistar!')
    else:
        print('Você tem {} anos' .format(date.today().year - ano))
        print('Seu alistamento militar passou do prazo em {} ano(s).' .format((date.today().year - ano) - 18))
elif sexo == 2:
    print('Você não precisa se alistar!')
else:
    print('Opção inválida!')

print()
