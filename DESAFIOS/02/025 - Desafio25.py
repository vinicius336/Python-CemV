'''
    Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
'''
print()
nome = input('\033[1;37;40m Digite seu nome: \033[m ').strip().upper()
print('\033[1;44m {:=^30} \033[m' .format(' Minha solução '))
vdd = nome.find('SILVA')

print('\033[1;34;40m Seu nome tem Silva? \033[m', end=' ')
print('\033[1;35;40m {} \033[m' .format(vdd >= 0)) if(vdd == nome.find('SILVA')) else print('{}' .format(vdd < 0))
print()
print('\033[1;46m {:=^30} \033[m' .format(' Solução do Professor '))
print('\033[1;36;40m Seu nome tem Silva? \033[m \033[1;33;40m {} \033[m' .format('SILVA' in nome.upper()))
print('\033[1;36;40m Seu nome tem Silva? \033[m \033[1;33;40m {} \033[m' .format('silva' in nome.lower()))

print()