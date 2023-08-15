'''
    Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500
'''
print()
soma = 0
cont = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        cont += 1
        soma = soma + i
print('A soma dos {} valores divisíveis por 3 de 1 até 500 é {}' .format(cont, soma))

print()