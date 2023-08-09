'''
    Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
    Calcule o preço a pagar, sabendo que o carro custa R$60,00 por dia e R$0,15 por Km rodado.
'''
print()
km = float(input('\033[1;34;40mQuantos quilômetros foram rodados?\033[m '))
dia = int(input('\033[1;34;40mQuantos dias foram o aluguel?\033[m '))
print('\033[1;36;40mO valor da diária é \033[1;33;40m R${:.2f} \033[m' .format(dia * 60))
print('\033[1;36;40mO valor por Km percorridos é \033[1;33;40m R${:.2f} \033[m' .format(km * 0.15))
print('\033[1;36;40mTotal a pagar: \033[1;33;40m R${:.2f} \033[m' .format(dia * 60 + km * 0.15))

print()