'''
    Faça um programa que leia uma frase pelo teclado e moestre:
    >> Quantas vezes aparece a letras "A"
    >> Em que posição ela aparece a primeria vez.
    >> Em que posição ela aparece a última vez.
'''
print()
frase = input('Digite uma frase: ').strip().lower()
print('A letra {} aparece {} vezes na frase.' .format('a', frase.count('a')))
print('A primeria letra {} apareceu na posição {}.' .format('a', frase.find('a') + 1))
print('A última letra {} apareceu na posição {}.' .format('a', frase.rfind('a') + 1))

print()