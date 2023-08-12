'''
    A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
    >> Até 9 anos: Mirim
    >> Até 14 anos: Infantil
    >> Até 19 anos: Junior
    >> Até 20 anos: Sênior
    >> Acima: Master
'''
from datetime import date
print()
anoNasc = int(input('Digite o ano de nascimento do atleta: '))
if date.today().year - anoNasc <= 9:
    categoria = 'Mirim'
elif date.today().year - anoNasc > 9 and date.today().year - anoNasc <= 14:
    categoria = 'Infantil'
elif date.today().year - anoNasc > 14 and date.today().year - anoNasc <= 19:
    categoria = 'Junior'
elif date.today().year - anoNasc == 20:
    categoria = 'Sênior'
else:
    categoria = 'Master'
print('A categoria do atleta é {}' .format(categoria))

print()