'''
    Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
    Considere: US$ 1,00 = R$ 3,27
'''
print()

real = float(input('Digite quanto você tem na carteira: R$'))
dolar = real / 4.79
euro = real / 5.27
print('Com R$ {} você pode comprar US$ {:.2f} ou €{:.2f}' .format(real, dolar, euro))

print()