'''
    Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.
'''
print()

preco = float(input('\033[1;37;40mDigite o preço do produto: \033[1;33m R$\033[m '))
print('\033[1;30;47mO produto custa \033[1;43m R${} \033[m' .format(preco))
print('\033[1;30;44mCom \033[1;41m 5% de desconto \033[1;44m fica por \033[1;43m R${:.2f} \033[m' .format(preco * 0.95))

print()