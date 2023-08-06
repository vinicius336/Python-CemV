'''
    Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
'''
print()
nome = input('Digite seu nome: ').strip().upper()
print('\n{:=^30}' .format(' Minha solução '))
vdd = nome.find('SILVA')
print('Seu nome tem Silva? {}' .format(vdd >= 0))

print('\n{:=^30}' .format(' Solução do Professor '))
print('Seu nome tem Silva? {}' .format('SILVA' in nome.upper()))
print('Seu nome tem Silva? {}' .format('silva' in nome.lower()))

print()