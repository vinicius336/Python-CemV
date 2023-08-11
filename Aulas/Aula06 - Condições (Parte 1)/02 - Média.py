print()
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
print('Sua média é {:.1f}' .format(media))
if(media >= 6.0):
    print('Sua média foi boa! PARABÉNS!')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')
print('PARABÉNS! Você passou!') if(media >= 6) else print('REPROVADO! Estude mais!')
print()