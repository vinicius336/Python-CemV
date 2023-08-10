'''
    Escreva um programa que leia a velocidade de um carro.
    Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
    A multa vai custar R$ 7,00 por cada Km acima do limite.
'''
print()
v = int(input('\033[3;40m Qual é a velocidade do carro?\033[m '))
if(v > 80):
    print('\033[1;31;40m MULTADO!! \033[47m O valor da multa é \033[33;40m R${:.2f} \033[m' .format((v - 80) * 7))
else:
    print('\033[1;32;40m PARABÉNS! \033[32;47m Você não tem multa! \033[m')

print()