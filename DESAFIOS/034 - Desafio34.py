'''
    Escreva um programa que pergunte o salário de um funcionério e calcule o valor do seu aumento.
    Para salários superiores a R$ 1.250,00, calcule um aumento de 10%.
    Para os inferiores ou iguais, o aumento será de 15%.
'''
print()
salario = float(input('\033[1;47m Digite seu salário: \033[33;40m R$ \033[m '))
if(salario > 1250):
    print('\033[1;40m Seu salário teve reajuste de \033[42m 10%. \033[m \033[36;40m Novo salário \033[33m R$ {:.2f} \033[m' .format(salario * 1.1))
else:
    print('\033[1;40m Seu salário teve reajuste de \033[42m 15%. \033[m \033[36;40m Novo salário \033[33m R$ {:.2f} \033[m' .format(salario * 1.15))

print()