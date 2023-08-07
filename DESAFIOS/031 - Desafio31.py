'''
    Desenvolva um programa que pergunte a distância de uma viagem em Km.
    Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.
'''
print()
km = int(input('Digite a distância da viagem: '))
'''if(km <= 200):
    print('A passagem custa R${:.2f}' .format(km * .5))
else:
    print('A passagem custa R${:.2f}' .format(km * .45))'''

print('A passagem custa R${:.2f}' .format(km * .5)) if(km <= 200) else print('A passagem custa R${:.2f}' .format(km * .45))

print()