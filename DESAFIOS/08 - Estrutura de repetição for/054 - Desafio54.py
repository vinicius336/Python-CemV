'''
    Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
    Obs: Maioridade = 21 anos
'''
print()
from datetime import date
maiorIdade = 0
menorIdade = 0

for i in range(0, 7):
    ano = int(input('Digite o ano de nascimento: '))
    
    if date.today().year - ano >= 21:
        maiorIdade += 1
    else:
        menorIdade += 1
        
print('{} pessoas são menores de idade e {} pessoas são maiores de idade.' .format(menorIdade, maiorIdade))

print()