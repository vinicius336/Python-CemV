'''
    Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
    Considere: US$ 1,00 = R$ 3,27
'''
print()

real = float(input('\033[1;33;40mDigite quanto você tem na carteira:\033[m \033[43mR$\033[m '))
dolar = real / 4.79
euro = real / 5.27
print('\033[1;33mCom\033[m \033[1;42m R$ {} \033[m \033[1;33mvocê pode comprar\033[m \033[1;44m US$ {:.2f} \033[m \033[1;33mou\033[m \033[1;46m €{:.2f} \033[m' .format(real, dolar, euro))

print()