'''
    Desenvolva um programa que pergunte a distância de uma viagem em Km.
    Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.
'''
print()
km = int(input('\033[7;37;40m Digite a distância da viagem:\033[m '))
if(km <= 200):
    print('\033[4;40m A passagem custa \033[m \033[1;33;40m R${:.2f} \033[m' .format(km * .5))
else:
    print('\033[3;35;40 A passagem custa \033[m \033[33;40m R${:.2f} \033[m' .format(km * .45))

print('\033[4;40m A passagem custa \033[m \033[1;33;40m R${:.2f} \033[m' .format(km * .5)) if(km <= 200) else print('\033[3;35;40m A passagem custa \033[m \033[33;40m R${:.2f} \033[m' .format(km * .45))

print()