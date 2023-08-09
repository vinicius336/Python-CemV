'''
    Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.
'''
print()

preco = float(input('\033[1;40mDigite o salário atual \033[1;33m R$ \033[m '))
print('\033[1;40mO salário com \033[1;37;42m 15% de aumento \033[1;40m é \033[1;33m R$ {:.2f} \033[m' .format(preco * 1.15))

print() 