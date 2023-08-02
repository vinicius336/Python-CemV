'''
    Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
    Calcule o preço a pagar, sabendo que o carro custa R$60,00 por dia e R$0,15 por Km rodado.
'''
print()
km = float(input('Quantos quilômetros foram rodados? '))
dia = int(input('Quantos dias foram o aluguel? '))
print('O valor da diária é R${:.2f}\nO valor por Km percorridos é R${:.2f}\nTotal a pagar: R${:.2f}' .format(dia * 60, km * 0.15, dia * 60 + km * 0.15))

print()