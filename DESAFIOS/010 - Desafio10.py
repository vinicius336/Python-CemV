'''
    Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
    Considere: US$ 1,00 = R$ 3,27
'''
print()

real = float(input('Digite uma quantia em Real: '))
dolar = real / 3.27
print('Com R$ {} você pode comprar US$ {:.2f}' .format(real, dolar))

print()