'''
    Escreva um programa que leia a velocidade de um carro.
    Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
    A multa vai custar R$ 7,00 por cada Km acima do limite.
'''
print()
v = int(input('Qual é a velocidade do carro? '))
if(v > 80):
    print('VOCÊ FOI MULTADO! Valor: R${:.2f}' .format((v - 80) * 7))
else:
    print('Parabéns! Não tem multa!')

print()