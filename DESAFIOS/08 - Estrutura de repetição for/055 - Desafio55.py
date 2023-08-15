'''
    Faça um programa que leia o peso de 5 pessoas. No final, mostre qual foi o maior e o menor peso lidos.
'''
print()
maiorPeso = 0
menorPeso = 0
for i in range(0, 5):
    peso = float(input('Digite o peso da {}ª pessoa: ' .format(i+1)))
    if i == 0:
        maiorPeso = peso
        menorPeso = peso
    elif peso > maiorPeso:
        maiorPeso = peso
    elif peso < menorPeso:
        menorPeso = peso
print('O maior peso digitado foi {:.2f} e o menor peso foi {:.2f}' .format(maiorPeso, menorPeso))

print()